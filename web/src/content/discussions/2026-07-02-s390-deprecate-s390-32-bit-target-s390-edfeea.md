---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- s390
- deprecation
- architecture
- mainframes
discussion_id: 6c8ebd42-d0af-43c0-add9-6e9dc906f771@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH v2 0/1] s390: Deprecate s390 32-bit target "s390-*"'
headline: 's390: Deprecate s390 32-bit target "s390-*"'
tldr: Deprecates the 32-bit s390 target in binutils, aligning with removal in Linux
  kernel, glibc, and GCC.
proposer: Andreas Krebbel <krebbel@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Removes legacy support, simplifying the codebase and build process.
- May impact users still relying on 32-bit s390, necessitating migration to 64-bit.
exchanges:
- author: Andreas Krebbel <krebbel@linux.ibm.com>
  role: maintainer
  position: Approves the patch for deprecating the 32-bit s390 target, agreeing with
    the proposed timeline for removal and finding backporting additional configure
    checks unnecessary.
  quote: null
- author: Jens Remus <jens.remus@ Gmail.com>
  role: proposer
  position: Proposes deprecating the 32-bit s390 target and format in binutils, providing
    an overview of the removal timeline across related projects and suggesting binutils
    2.47 for deprecation and 2.48 for removal.
  quote: null
primer_expert: 'This patch sequence deprecates the 32-bit s390 architecture support
  in binutils, specifically the targets named `s390-*` and the `elf32-s390` object
  file format. This action is driven by a broader ecosystem trend: the Linux kernel
  has removed 32-bit compatibility support, glibc has deprecated and will soon remove
  it, and GCC is also deprecating its `-m31` option. The binutils maintainers are
  aligning with these efforts, marking the 32-bit s390 support for future removal.
  The discussion confirms the acceptance of the deprecation and its planned removal
  in Binutils 2.48.'
primer_glossary:
- term: s390
  definition: IBM's 64-bit mainframe architecture, with earlier 32-bit variants.
- term: deprecation
  definition: The process of marking a feature or API as obsolete, indicating that
    it will be removed in a future version, allowing users to migrate away from it.
- term: ELF
  definition: Executable and Linkable Format, the standard file format for object
    files, executables, and shared libraries on many Unix-like systems.
- term: glibc
  definition: The GNU C Library, the standard C library used in GNU/Linux systems.
- term: GCC
  definition: The GNU Compiler Collection, a widely used compiler system.
series_id: 'binutils:s390: deprecate s390 32-bit target "s390-*"'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/6c8ebd42-d0af-43c0-add9-6e9dc906f771@linux.ibm.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

Andreas Krebbel approves a patch to deprecate the 32-bit s390 target (`s390-*`, `elf32-s390`) in binutils. This deprecation aligns with ongoing removal efforts in the Linux kernel, glibc, and GCC. The patch is considered acceptable, and the revision timeline for its removal (Binutils 2.48) is deemed appropriate, as users of deprecated features might be expected to use older binutils versions. Krebbel does not see a need to backport the configure-time checks from GCC to binutils, given the imminent removal.
