---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gdb
- s390
- deprecation
- 32-bit
discussion_id: 20260423120006.3740571-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH v2 0/1] s390: Deprecate s390 32-bit target "s390-*"'
headline: 's390: Deprecate s390 32-bit target "s390-*"'
tldr: This patch deprecates the s390 32-bit target in binutils and GDB, aligning with
  similar deprecations in the Linux kernel, glibc, and GCC.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Removes support for an obsolete architecture, reducing maintenance burden.
- May impact users still using 32-bit s390 systems, requiring them to migrate.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Proposes deprecating the s390 32-bit target in binutils and GDB, citing
    similar actions in other projects and outlining a timeline for removal.
  quote: 'The s390 32-bit target (s390-*) is deprecated and planned for removal

    in a future release, along with the elf32-s390 target format.  Emit an

    error for this target during configure, which can be overridden using

    option --enable-obsolete.'
primer_expert: This patch series deprecates the s390 32-bit target in binutils and
  GDB. This means the `s390-*` target and `elf32-s390` format will be removed in a
  future release. The s390 architecture has largely moved to 64-bit, and other parts
  of the toolchain are dropping 32-bit support.
primer_general: This patch proposes removing support for 32-bit s390 systems from
  the binutils suite (which includes tools like the assembler and linker) and GDB
  (the debugger).  This is happening because the s390 architecture is migrating to
  64-bit, and other core components like the Linux kernel, the GNU C Library (glibc),
  and the GNU Compiler Collection (GCC) are also phasing out 32-bit support. This
  change simplifies the codebase and focuses development efforts on the more modern
  64-bit architecture.
series_id: 'binutils:s390: deprecate s390 32-bit target "s390-*"'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260423120006.3740571-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-04-23'
---

The s390 32-bit target (`s390-*` and format `elf32-s390`) is being deprecated in binutils and GDB, with a plan for removal in a future release. This change aligns with the removal of s390 32-bit compatibility support in Linux Kernel 6.19, deprecation in Glibc 2.43, and planned deprecation in GCC 16. The proposer notes that the deprecation error isn't issued during the top-level configure and asks whether this should be improved.
