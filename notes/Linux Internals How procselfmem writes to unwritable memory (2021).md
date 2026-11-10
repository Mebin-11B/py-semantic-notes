---
title: "Linux Internals: How /proc/self/mem writes to unwritable memory (2021)"
url: https://offlinemark.com/an-obscure-quirk-of-proc/
clipped: 2026-06-17 01:35:00
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Linux Internals: How /proc/self/mem writes to unwritable memory (2021)](https://offlinemark.com/an-obscure-quirk-of-proc/)

## Digest Summary
The article explains why writes to /proc/self/mem succeed on pages without write permission. User‑space code can open /proc/self/mem, seek to any virtual address, and write bytes; the kernel’s implementation bypasses normal MMU protection. When a write request arrives, the kernel’s mem_rw() calls access_remote_vm(), which uses get_user_pages_remote() with the FOLL_FORCE flag. This flag forces the page‑table walk to ignore the VM_WRITE flag, obtaining the backing physical frame even for read‑only mappings. The frame is then mapped into the kernel’s address space with kmap() (using PAGE_KERNEL RW permissions), and the data is copied via copy_to_user_page() (a simple memcpy). Because the kernel accesses the memory through its own writable mapping, the CPU’s Write‑Protect (CR0.WP) and SMAP settings are irrelevant. Thus, virtual‑address permissions apply only to accesses made through that address; the kernel can remap any physical page with arbitrary permissions, enabling the “punch‑through” semantics used by tools like the Julia JIT and rr debugger.

## Discussion Summary
The discussion expands the view of CPU mechanisms that limit kernel memory access beyond the two commonly cited settings, noting memory‑protection keys, virtualization page‑table structures (NPT/EPT), and hardware enclaves such as SEV, SGX, and TDX range registers. It emphasizes that the kernel retains ultimate control of page tables and can bypass hardware translation when handling /proc/self/mem, using software emulation to override existing protection. The tone is informative and highlights the complexity and flexibility of kernel memory handling.

---

## Full Article

Introduction
------------

An obscure quirk of the /proc/\*/mem pseudofile is its “punch through” semantics. **Writes performed through this file will succeed even if the destination virtual memory is marked unwritable**. In fact, this behavior is intentional and [actively used](https://lkml.org/lkml/2017/5/29/541) by projects such as the Julia JIT compiler and rr debugger.

This behavior raises some questions: Is privileged code subject to virtual memory permissions? In general, to what degree can the hardware inhibit kernel memory access?

By exploring these questions, this article will shed light on the nuanced relationship between an operating system and the hardware it runs on. We’ll examine the constraints the CPU can impose on the kernel, and how the kernel can bypass these constraints.

Patching libc with /proc/self/mem
---------------------------------

So what do these punch-through semantics look like?

Consider this code:

```
#include <fstream>
#include <iostream>
#include <sys/mman.h>

/* Write @len bytes at @ptr to @addr in this address space using
 * /proc/self/mem.
 */
void memwrite(void *addr, char *ptr, size_t len) {
  std::ofstream ff("/proc/self/mem");
  ff.seekp(reinterpret_cast<size_t>(addr));
  ff.write(ptr, len);
  ff.flush();
}

int main(int argc, char **argv) {
  // Map an unwritable page. (read-only)
  auto mymap =
      (int *)mmap(NULL, 0x9000,
                  PROT_READ, // <<<<<<<<<<<<<<<<<<<<< READ ONLY <<<<<<<<
                  MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

  if (mymap == MAP_FAILED) {
    std::cout << "FAILED\n";
    return 1;
  }

  std::cout << "Allocated PROT_READ only memory: " << mymap << "\n";
  getchar();

  // Try to write to the unwritable page.
  memwrite(mymap, "\x40\x41\x41\x41", 4);
  std::cout << "did mymap[0] = 0x41414140 via proc self mem..";
  getchar();
  std::cout << "mymap[0] = 0x" << std::hex << mymap[0] << "\n";
  getchar();

  // Try to write to the text segment (executable code) of libc.
  auto getchar_ptr = (char *)getchar;
  memwrite(getchar_ptr, "\xcc", 1);

  // Run the libc function whose code we modified. If the write worked,
  // we will get a SIGTRAP when the 0xcc executes.
  getchar();
}
```

This uses /proc/self/mem to write to two unwritable memory pages. The first is a read-only page that the code itself maps. The second is a code page belonging to libc itself (the `getchar` function).

The latter is the more interesting test — it writes a 0xcc byte (the x86-64 software breakpoint instruction) which will cause the kernel to deliver a SIGTRAP to our process if executed. This is literally changing the executable code of libc. So the next time we call `getchar`, if we get a SIGTRAP, we know that the write has succeeded.

Here’s what it looks like when I run the program:

![](https://i0.wp.com/offlinemark.com/wp-content/uploads/2021/05/image-1.png?resize=610%2C121&ssl=1)

It worked! The middle print statements prove that the value 0x41414140 was successfully written and read from memory. The last print shows that a SIGTRAP was delivered to our process when we called `getchar` after patching it.

Here’s a video demo:

Now that we’ve seen how this feature works from the perspective of userspace, let’s dive a bit deeper. To fully understand how this works, we must look at how the hardware enforces memory permissions.

To the hardware
---------------

On x86-64, there are two CPU settings which control the kernel’s ability to access memory. They are enforced by the memory management unit (MMU).

The first setting is the Write Protect bit (CR0.WP). From Volume 3, Section 2.5 of the Intel manual:

> Write Protect (bit 16 of CR0) — When set, inhibits supervisor-level procedures from writing into read- only pages; when clear, allows supervisor-level procedures to write into read-only pages (regardless of the U/S bit setting; see Section 4.1.3 and Section 4.6).

This inhibits the kernel’s ability to write to read-only pages, **which is notably allowed by default**.

The second setting is Supervisor Mode Access Prevention (SMAP) (CR4.SMAP). Its full description in Volume 3, Section 4.6 is verbose, but the executive summary is that SMAP disables the kernel’s ability to read or write userspace memory entirely. This hinders security exploits which populate userspace with malicious data to be read by the kernel during exploitation.

If the kernel code in question only uses approved channels for accessing userspace (copy\_to\_user, etc) SMAP can be safely ignored — these functions automatically toggle SMAP before and after accessing memory. But what about Write Protect?

With CR0.WP clear, the kernel implementation of /proc/\*/mem will indeed be able to unceremoniously write to unwritable userspace memory.

However, CR0.WP is [enabled at boot](https://elixir.bootlin.com/linux/v5.12/source/arch/x86/kernel/head_64.S#L240), and generally remains set for the life of a system. In this case, a page fault will be triggered in response to the write. As more of a tool to facilitate Copy-on-Write than a security boundary, this does not present any real restriction upon the kernel. That said, it does require the inconvenience of fault handling, which would not otherwise be necessary.

With this in mind, let’s examine the implementation.

How /proc/\*/mem works
----------------------

/proc/\*/mem is implemented in [fs/proc/base.c](https://elixir.bootlin.com/linux/v5.9-rc3/source/fs/proc/base.c).

A struct file\_operations is populated with handler functions, and the function [mem\_rw()](https://elixir.bootlin.com/linux/v5.9-rc3/source/fs/proc/base.c#L835) ultimately backs the write handler. mem\_rw() uses [access\_remote\_vm()](https://elixir.bootlin.com/linux/v5.9-rc3/source/mm/memory.c#L4805) for performing the actual writes. access\_remote\_vm() does the following:

* Calls get\_user\_pages\_remote() to lookup the physical frame corresponding to the destination virtual address.
* Calls kmap() to map that frame into the kernel’s virtual address space as writable.
* Calls copy\_to\_user\_page() to finally perform the writes.

**The implementation sidesteps the entire question of the kernel’s ability to write to unwritable userspace memory**! It exerts the kernel’s control over the virtual memory subsystem to bypass the MMU entirely, allowing the kernel to simply write to its own writable address space. This renders the CR0.WP discussion moot.

To elaborate on each of these steps:

**get\_user\_pages\_remote()**  
To bypass the MMU, the kernel needs to manually perform in software what the MMU accomplishes in hardware. The first step is translating the destination virtual address to a physical address.

This is exactly what the get\_user\_pages() family of functions provides. These functions lookup physical memory frames that back a given virtual address range by walking the page tables. They also handle access validation and non-present pages.  
   
The caller provides context and modifies the behavior of get\_user\_pages() via flags. Of particular interest is the FOLL\_FORCE flag, which mem\_rw() passes. This flag causes [check\_vma\_flags](https://elixir.bootlin.com/linux/v5.9-rc3/source/mm/gup.c#L930) (the access validation logic within get\_user\_pages()) to ignore writes to unwritable pages and allow the lookup to continue. The “punch through” semantics are attributed entirely to FOLL\_FORCE. (comments my own)

```
static int check_vma_flags(struct vm_area_struct *vma, unsigned long gup_flags)
{
        [...]
        if (write) { // If performing a write..
                if (!(vm_flags & VM_WRITE)) { // And the page is unwritable..
                        if (!(gup_flags & FOLL_FORCE)) // *Unless* FOLL_FORCE..
                                return -EFAULT; // Return an error
        [...]
        return 0; // Otherwise, proceed with lookup
}
```

get\_user\_pages() also honors copy-on-write (CoW) semantics. If a write is detected to a non-writable page table entry, an “page fault” is emulated by calling handle\_mm\_fault, the core page fault handler. This triggers the appropriate CoW handling routine via do\_wp\_page, which copies the page if necessary. This ensures that writes via /proc/\*/mem are only visible within the process if they occur to a privately shared mapping, such as libc.

**kmap()**  
Once the physical frame has been looked up, the next step is to map it into the kernel’s virtual address space with writable permissions. This is done through kmap().

On 64 bit x86, all of physical memory is mapped via the linear mapping region of the kernel’s virtual address space. kmap() is trivial in this case — it just needs to add the start address of the linear mapping to the frame’s physical address to compute the virtual address that frame is mapped at.

On 32 bit x86, the linear mapping contains a subset of physical memory, so kmap() may need to map the frame by allocating highmem memory and manipulating page tables.  
  
In both of these cases, the [linear mapping](https://elixir.bootlin.com/linux/v5.9-rc3/source/arch/x86/mm/init.c#L559) and [highmem](https://elixir.bootlin.com/linux/v5.9-rc3/source/include/linux/highmem.h#L44) mappings are allocated with [PAGE\_KERNEL](https://elixir.bootlin.com/linux/v5.9-rc3/source/arch/x86/include/asm/pgtable_types.h#L190) protection which is RW.

**copy\_to\_user\_page()**  
The last step is executing the writes. This is achieved through copy\_to\_user\_page(), which is essentially a memcpy. Since the destination is the writable mapping from kmap(), this just works.

Discussion
----------

To summarize, the kernel first translates the destination userspace virtual address to its backing physical frame via a software page table walk. Then it maps this frame into its own virtual address space as RW.  Finally, it performs the writes using a simple memcpy.

What is striking about this implementation is that it does not involve CR0.WP. **The implementation elegantly sidesteps this by exploiting the fact that it is under no obligation to access memory via the pointer it receives from userspace**. Since the kernel is in complete control of virtual memory, it can simply remap the physical frame into its own virtual address space, with arbitrary permissions, and operate on it as it wishes.

This gets at an important point: **the permissions guarding a page of memory are associated with the virtual address used to access that page, not the physical frame that backs the page**. Indeed the notion of memory permissions is purely a consideration of virtual memory and does not pertain to physical memory.

Conclusion
----------

Having thoroughly investigated the implementation details of /proc/\*/mem’s “punch through” semantics, we can reflect on the relationship between the kernel and the CPU.

At first glance, the ability of the kernel to write to unwritable userspace memory raises the question: to what degree can the CPU inhibit kernel memory access? The manual does indeed document control mechanisms that would seem to limit the kernel.

However, under inspection these prove to be superficial constraints at best — mere roadblocks that can be worked around, or sidestepped altogether.

---

This post was cited:

---

### Learn something new? Let me know!

Did you learn something from this post? I’d love to hear what it was — tweet me [@offlinemark](https://twitter.com/offlinemark)!

I also have a low-traffic mailing list if you’d like to hear about new writing. Sign up here:

---

Thanks to Jann Horn for explaining much of this to me. Thanks also to Peter Goodman and Ben Marks for reviewing earlier drafts of this post.