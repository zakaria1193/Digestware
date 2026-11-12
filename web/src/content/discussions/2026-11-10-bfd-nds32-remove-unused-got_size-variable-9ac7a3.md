---
project: binutils
subsystem: bfd/nds32
patch_id: null
tags:
- cleanup
- bfd
- nds32
- compiler warnings
- linker script
discussion_id: 19f9a47f-e23a-4867-bc58-8c423af91b60@efficios.com
source_type: public_inbox
title: 'Re: [PATCH] bfd/nds32: remove unused got_size variable'
headline: 'bfd/nds32: remove unused got_size variable'
tldr: Removes an unused variable `got_size` from the BFD NDS32 backend after it was
  identified as unused and flagged by a compiler warning.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code and simplifies linker logic.
- Addresses compiler warnings.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the `got_size` variable as it's unused and causing compiler
    warnings, also simplifying related code.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-nds32.c:154:13:\
    \ error: variable 'got_size' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since it was introduced by commit\n35c081572f32\
    \ (\"Add support for Andes NDS32:\", 2013-12-13).  Remove it,\nalong with the\
    \ comment that describes it.  The branches handling the\n.got and .…"
- author: Alan Modra
  role: reviewer
  position: Approves the removal of the unused variable and associated code simplification.
  quote: OK.
- author: Simon Marchi
  role: proposer
  position: Confirms the patch has been applied.
  quote: null
primer_expert: This patch is a code cleanup for the BFD backend supporting the NDS32
  architecture. It targets the `elf32-nds32.c` file to remove a global variable `got_size`,
  which has been unused since the initial NDS32 support was added. The compiler (Clang)
  flagged this variable with `-Werror=unused-but-set-global`. The removal also leads
  to a simplification of the `nds32_elf_late_size_sections` function, as the code
  blocks specifically handling `.got` and `.got.plt` sections, which were empty due
  to the unused variable, are merged into the handling for the `.plt` section.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to abstract over various object file formats (like ELF, a.out, COFF).
- term: NDS32
  definition: A 32-bit processor architecture developed by Andes Technology Corporation.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: GOT
  definition: Global Offset Table. A table used by position-independent executable
    code to locate global variables and functions at runtime.
- term: .got
  definition: The Global Offset Table section in an ELF object file.
- term: .got.plt
  definition: A specific section within the GOT used for lazy binding of Procedure
    Linkage Table (PLT) entries.
- term: .plt
  definition: The Procedure Linkage Table section in an ELF object file, used for
    dynamic linking.
- term: unused-but-set-global
  definition: A compiler warning indicating that a global variable has been assigned
    a value but is never subsequently read or used.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/19f9a47f-e23a-4867-bc58-8c423af91b60@efficios.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch removes the `got_size` variable from the BFD NDS32 backend code. The variable was found to be unused since its introduction in 2013, triggering a compiler warning with `-Werror,-Wunused-but-set-global`. The removal also simplifies the `nds32_elf_late_size_sections` function by merging empty branches related to `.got` and `.got.plt` handling with the `.plt` handling.
