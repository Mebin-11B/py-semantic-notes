---
title: "Tar Files Created on macOS Display Errors When Extracting on Linux (2024)"
url: https://aruljohn.com/blog/macos-created-tar-files-linux-errors/
clipped: 2026-06-17 01:08:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tar Files Created on macOS Display Errors When Extracting on Linux (2024)](https://aruljohn.com/blog/macos-created-tar-files-linux-errors/)

## Digest Summary
macOS’s default `bsdtar` includes Apple‑specific extended attributes (e.g., `LIBARCHIVE.xattr.com.apple.quarantine`, `...lastuseddate#PS`) and creates “._*” resource‑fork files. When such archives are extracted on Linux, GNU tar reports warnings like “Ignoring unknown extended header keyword …”.  

**Remediation options**

- **Suppress attributes at archive creation**: add `--no-xattrs` to the `tar` command, e.g. `tar -cvzf --no-xattrs pix.tar.gz pix`.  
- **Disable copy‑file metadata**: use `--disable-copyfile` similarly, e.g. `tar -cvzf --disable-copyfile pix.tar.gz pix`.  
- **Replace bsdtar with GNU tar**: install via Homebrew (`brew install gnu-tar`) and place its `gnubin` directory early in `$PATH` (`export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"` for Intel Macs or the Homebrew‑M1 path for Apple Silicon). Verify with `tar --version`; it should show GNU tar 1.35. Archives created with GNU tar omit the Apple‑specific headers, eliminating the Linux warnings.

These approaches produce clean tarballs that extract on Linux without extra “._” files or extended‑attribute warnings.

## Discussion Summary
The discussion outlines Apple’s approach to tar archives, emphasizing preservation of Finder, Gatekeeper, and other macOS metadata to avoid silent data loss and maintain consistency with system utilities. It notes that this focus on faithful filesystem representation can hinder portability, prompting workarounds such as disabling metadata inclusion, using specific tar options, or preferring zip when extended attributes are irrelevant. Compatibility differences among GNU tar, bsdtar, and libarchive are highlighted, and the comment questions why Linux lacks comparable metadata tracking while recognizing ongoing improvements in tar implementations.

---

## Full Article

I use my MacBook as my development machine and Debian / Ubuntu / Red Hat Linux at work and on this website. I occasionally create tarballs, or tar.gz and tgz files on Mac, which are then deployed on Linux servers. When I untar the tar.gz file on the Linux server, it may throw errors or warnings.

![How to exclude ._ files in tar.gz created on  macOS](https://aruljohn.com/blog/pix/macos-linux.jpg)

Creating tar files
------------------

I create tar.gz files the regular way. For example, if I want to create a tar.gz file of a directory `pix` containing pictures.

```
tar -cvzf pix.tar.gz pix
```

That command will create a tar gzipped file `pix.tar.gz`.

SCP to Linux server
-------------------

I will scp this tar.gz to **myserver.tld** as **user** and under the `/tmp` directory

```
scp pix.tar.gz user@myserver.tld:/tmp/
```

Now, I will extract this gzipped tar file on the Linux server.

```
cd /tmp
tar -xzvf pix.tar.gz
```

Output (snippet):

```
...
pix/TODO/._IMG_3110.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3110.jpeg
pix/TODO/._IMG_3113.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3113.jpeg
pix/TODO/._IMG_3115.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3115.jpeg
pix/TODO/._IMG_3114.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3114.jpeg
...
```

Warnings and errors when extracting tar.gz or tgz files
-------------------------------------------------------

As we can see, the tar file contained several new files starting with `._`. These appear to be duplicates of existing files.

You may or may not see errors and warnings when extracting files that were tarred on macOS.

On one occasion, I saw warnings like this:

```
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemTextContentLanguage'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseVersion'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseLabels'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseConfidences'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
```

Another time, I got these warnings:

```
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
```

And then, this:

```
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemTextContentLanguage'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseVersion'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseLabels'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseConfidences'
```

For some reason, the default BSD tar program on macOS seems to create and add these new files. There are two ways to get create a clean tar file.

Solution 1: Use `--no-xattrs` while creating the tar
----------------------------------------------------

While creating the tar file, you can add the attribute `--no-xattrs`. Doing this will prevent the extra files from getting added.

Previously, we did this:

```
tar -cvzf pix.tar.gz pix
```

Now, we will do this:

```
tar -cvzf --no-xattrs pix.tar.gz pix
```

This is the simplest way.

Now, SCP it to your Linux server and untar / gunzip it. You should not find the extra files or any errors or warnings.

```
tar -xzvf pix.tar.gz
```

Solution 2: Use `--disable-copyfile` while creating the tar
-----------------------------------------------------------

Similar to the previous solution, in this case, we will use the `--disable-copyfile` option.

```
tar -cvzf --disable-copyfile pix.tar.gz pix
```

Now, SCP the pix.tar.gz file to your Linux server and extract it. You should not find the extra files or any errors or warnings.

```
tar -xzvf pix.tar.gz
```

Solution 3: Install and use gnu-tar instead of bsdtar
-----------------------------------------------------

This is more of a permanent solution, in that you don't have to remember to type the extra optional arguments.

On your macOS, run this command to verify that you are using bsdtar. You should get something like this.

```
$ tar --version
bsdtar 3.5.3 - libarchive 3.5.3 zlib/1.2.12 liblzma/5.4.3 bz2lib/1.0.8
```

Check in which directory bsdtar is installed:

```
$ which tar
/usr/bin/tar
```

### Install gnu-tar

Now, install gnu-tar using Homebrew.

```
$ brew install gnu-tar
```

After a few minute, gnu-tar will be installed in your macOS. It will get installed in this location:

`/usr/local/opt/gnu-tar/libexec/gnubin/tar`

### Verify gnu-tar installation

You can verify gnu-tar by running this:

```
$ /usr/local/opt/gnu-tar/libexec/gnubin/tar --version
tar (GNU tar) 1.35
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by John Gilmore and Jay Fenlason.
```

### Make gnu-tar your default tar

Now, you can make that your default by setting the path to gnu-tar earlier than bsdtar in your `~/.bash_profile` file.

Edit your `~/.bash_profile` file.

If you are using a Mac with an Intel processor, add this line:

```
export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"
```

If you are using a Mac with an Apple Silicon M1, M2, M3 or M4 processor, add this line:

```
export PATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"
```

Save and quit your editor and restart your Terminal session.

### Check that gnu-tar is default tar, and tar again

Test and see if `tar --version` returns GNU tar instead of BSD tar.

```
$ tar --version
tar (GNU tar) 1.35
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by John Gilmore and Jay Fenlason.
```

If you get a similar response, then recreate the tar file the regular way.

```
tar -cvzf pix.tar.gz pix
```

SCP it to your Linux server and untar / gunzip it. You should not find the extra files or any errors or warnings.

Conclusion
----------

I hope the steps in this blog post worked for you. This post will be updated whenever there is anything relevant. Feel free to [contact me](https://aruljohn.com/about/) if you have any questions or suggestions.

Related Posts
-------------

If you have any questions, please contact me at arulbOsutkNiqlzziyties@gNqmaizl.bkcom. You can also post questions in our [Facebook group](https://www.facebook.com/groups/761643131624765). Thank you.

Disclaimer: Our website is supported by our users. We sometimes earn affiliate links when you click through the affiliate links on our website.

Last Updated: December 06, 2024.     This post was originally written on December 05, 2024.