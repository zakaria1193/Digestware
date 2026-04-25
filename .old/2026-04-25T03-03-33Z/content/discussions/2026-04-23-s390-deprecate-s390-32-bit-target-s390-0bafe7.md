---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- s390
- deprecation
- 32-bit
- obsolete
discussion_id: 20260423120006.3740571-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH v2 0/1] s390: Deprecate s390 32-bit target "s390-*"'
headline: 's390: Deprecate s390 32-bit target "s390-*"'
tldr: Deprecates the s390 32-bit target in Binutils, aligning with similar changes
  in the kernel, glibc, and GCC.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Removes support for an obsolete architecture, reducing maintenance burden.
- May break build environments that still rely on the 32-bit s390 target, requiring
  them to migrate to 64-bit or use the `--enable-obsolete` flag.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Proposes deprecating the s390 32-bit target in Binutils and GDB, with
    a plan to remove it in a future release, and requests feedback on the timing of
    the configuration error.
  quote: The s390 32-bit target (s390-*) is deprecated and planned for removal in
    a future release, along with the elf32-s390 target format.  Emit an error for
    this target during configure, which can be overridden using option --enable-obsolete.
primer_expert: This patch deprecates the s390 32-bit target (`s390-*`) and `elf32-s390`
  format in binutils. This involves changes to `bfd/` to emit an error when configuring
  for this target. The deprecation mirrors similar efforts in the kernel, glibc, and
  gcc to remove support for the obsolete 32-bit s390 architecture. The patch also
  touches `gdb/` to ensure GDB also reflects the deprecation.
primer_general: Binutils is a collection of binary tools, including the assembler,
  linker, and other utilities for manipulating object and executable files.  The s390
  architecture is IBM's mainframe architecture.  This patch deprecates support for
  the 32-bit version of s390 in Binutils, meaning that the tools will issue a warning
  or error when attempting to build for this target. This is happening because the
  32-bit s390 architecture is becoming obsolete and is being removed from other parts
  of the toolchain, such as the Linux kernel and the glibc C library.
series_id: 'binutils:s390: deprecate s390 32-bit target "s390-*"'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260423120006.3740571-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-04-23'
---

This patch deprecates the s390 32-bit target ("s390-*" and format "elf32-s390") in Binutils and GDB. This change aligns with the removal of s390 32-bit compatibility support in Linux Kernel 6.19, the deprecation in Glibc 2.43, and the planned deprecation in GCC 16. The deprecation will introduce an error during configure, which can be overridden with `--enable-obsolete`. The author asks for feedback on whether the error should be issued earlier in the configuration process.
