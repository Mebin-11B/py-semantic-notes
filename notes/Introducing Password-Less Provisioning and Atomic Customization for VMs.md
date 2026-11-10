---
title: "Introducing Password-Less Provisioning and Atomic Customization for VMs"
source: "https://www.akamai.com/blog/cloud/password-less-provisioning-atomic-customization-vms"
author:
  - "[[Dan Sheppard]]"
published: 2026-05-26
created: 2026-06-05
description: "Akamai Cloud introduces password-less provisioning and atomic customization. Align with Zero Trust by eliminating root passwords and hardening VMs at creation."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-16
summary_status: done
concepts:
  - Computer Security
  - Cloud Infrastructure
  - Systems Programming
  - Zero Trust
  - Operating Systems
related:
  - "[[Diskless Linux boot using ZFS, iSCSI & PXE.md]]"
  - "[[Serving files over HTTP three ways synchronous, epoll, and io_uring.md]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Akamai Cloud introduces password-less provisioning and single-transaction atomic customization for virtual machines to eliminate root passwords and configuration drift, aligning with Zero Trust security.
>
> **Key points:**
> - Legacy VM provisioning models requiring root passwords are replaced with SSH key-only provisioning to reduce brute-force surfaces and cleartext secrets in IaC pipelines.
> - Password-less deployment automatically locks the root password hash and hardens SSH configuration (sshd_config) to reject password authentication and prohibit root logins.
> - Atomic customization allows engineers to define boot size, swap size, and kernel parameters in a single API POST request, reducing post-provisioning configuration steps and vulnerability windows.
> - Pinning specific kernels (such as distro-provided or custom grub2 kernels) prevents runtime drift and maintains driver compatibility, particularly for ephemeral GPU clusters.
> - The API-level improvements reduce script complexity, eliminate wait-for-ready loops, and boost deployment speeds by up to 30% for automated scaling.
>
> **Concept links:** [[Computer Security]], [[Cloud Infrastructure]], [[Systems Programming]], [[Zero Trust]], [[Operating Systems]]
>
> **Suggested connections:**
> - [[Diskless Linux boot using ZFS, iSCSI & PXE.md]] — both discuss operating system booting, configuration, and secure storage provisioning.
> - [[Serving files over HTTP three ways synchronous, epoll, and io_uring.md]] — connects infrastructure deployment with low-level systems programming concepts.
<!-- ai-summary:end -->
In the modern cloud landscape, security is more important than ever. AI-based, GPU-powered algorithms have made passwords a major weakness in security. Security is now being “baked in” from the very first API call.

Historically, the process of provisioning a virtual machine (VM) has relied on legacy patterns, including the mandatory root password. A practice that once ensured security now creates immediate security risks.

Akamai Cloud is introducing password-less provisioning and atomic customization as we move beyond simple convenience and align our infrastructure practices with Zero Trust principles. This approach gives developers the tools to build hardened, production-ready environments in a single, secure transaction.

## The death of the security anti-pattern: Mandatory root passwords

For years, the industry standard for cloud provisioning required a root\_password during creation. While functional, this created a significant security anti-pattern. Mandatory passwords often led to shared secrets being stored in cleartext within automation scripts, Terraform files, or CI/CD pipelines. They also provide an immediate, discoverable attack surface for brute-force attempts the moment that a VM gains a public IP.

### Transitioning to Zero Trust

Akamai Cloud’s new password-less provisioning changes the paradigm. You can now omit the root\_pass field entirely during the POST /linode/instances request, as long as you supply at least one secure shell (SSH) key.

When you choose this path, the system doesn't just leave the password blank. It actively hardens the instance by:

- **Locking the root hash**: Our console sets the root password to an unusable value and locks the hash. This makes it cryptographically impossible to log in via a password.
- **Automatically modifying the OS** sshd\_config to enforce PasswordAuthentication no and PermitRootLogin prohibit-password: In short, Akamai Cloud is hardening the SSH.
- **Restricting access to the authorized SSH key holders**: This creates a perfect alignment with Zero Trust identity frameworks.

## Atomic customization: Security through precision

Security is often a step in provisioning. When a developer has to create a VM, then resize a disk, swap a kernel, and reboot, there is a window of vulnerability, a period in which the VM is live but not yet in its intended, hardened state as the process has not yet reached that step.

We are introducing atomic customization to eliminate this “API chattiness” by defining your environment's physical and logical constraints at the point of creation. This change allows your VM to begin its life with a secure configuration by removing the during-provisioning risks.

### User-defined boot and swap sizes

In the past, disk layouts were largely dictated by the plan size. Now, you have granular control over the boot\_size and swap\_size parameters during the initial creation.

Why is this a security feature? The answer is simple; It allows minimalist provisioning. By defining a specific boot\_size (minimum 8,192 MB) and leaving the rest of the plan's storage as unallocated space, you reduce the data footprint of the OS and logically secure it separately from any data. This additional space can then be provisioned with a unique file system (e.g., raw, XFS, etc.) in a follow-up add disk space API.

### Kernel specification for specialized workloads

The kernel is the heart of your VM’s security. With this update, you can now explicitly define the kernel parameter during provisioning.

- Ensure you are running the exact, vendor-patched kernel provided by your distro (via linode/grub2).
- Engineers building ephemeral GPU clusters can ensure driver compatibility by pinning specific kernels immediately, preventing the drift that often occurs when a system updates to an incompatible version upon its first boot.
- Boot directly from the master boot record (MBR) of your primary disk, bypassing the cloud-provider kernel entirely for a truly custom, hardened stack.
- By pinning kernels during the first API call, developers can ensure that agentic AI nodes remain stable and compliant without the risk of runtime configuration drift during automated scaling.

## Reducing friction for infrastructure as code

Modern security is managed through code. Whether you use Terraform, Ansible, or custom Python scripts, these improvements are designed to make your automation more robust.

By allowing SSH keys, disk sizes, and kernel choices to be sent in a single POST request, we have significantly reduced the failure rate of complex deployments. No more wait-for-ready loops in your scripts to perform a resize or a kernel swap. Your infrastructure reaches its desired state faster, with fewer points of failure.

By eliminating the wait-for-ready loop through atomic provisioning, enterprises can achieve deployment speeds up to 30% faster overall — a critical requirement when scaling real-time inference capacity.

### The “break-glass” protocol

We recognize that in the real world, things go wrong. If an admin loses their SSH key, we maintain a secure “break-glass” procedure. The Reset Password functionality remains available via Cloud Manager and API.

However, we’ve designed this with security in mind: Resetting the password will unlock the root account for recovery, but it will *not* automatically revert your hardened SSH configurations, ensuring that your remote security posture remains intact.

## Available new improvements

No matter how you build or manage your Akamai Cloud infrastructure, our new improvements are available to support you.

1. **API**: POST /linode/instances calls
2. **Linode CLI**: Updated command-line tools for rapid, password-less deployment
3. **SDKs (Go and Python)**: Full support for the new parameters in our primary developer kits
4. **Infrastructure as code (IaC; Terraform and Packer)**: Updated providers to allow for "password-less by default" infrastructure definitions

## Conclusion: A new standard for the cloud

The shift to password-less provisioning and atomic customization represents more than just a list of new features. It is a commitment to a **security-first** philosophy. By removing the necessity of passwords and allowing for precise, one-step configurations, Akamai Cloud now provides a platform that is not just easier to use, but also fundamentally harder to compromise.

Take a look at your current deployment scripts and look for the root\_pass field and ask your team: “Do we really need this?” With this update to Akamai Cloud, the answer is likely “No.” It is time to enter the era of the hardened cloud. Experience a more secure, streamlined, and modern Akamai today.

## Get started now

Take a look at the [TechDocs](https://techdocs.akamai.com/cloud-computing/docs/create-a-compute-instance "Techdocs") or [API documents](https://techdocs.akamai.com/linode-api/reference/post-linode-instance "API Documents") for more information on how to add these new features to your deployment.

![Dan Sheppard](https://www.akamai.com/site/en/images/blog/userpics/dan-sheppard.png)

May 26, 2026

Tags