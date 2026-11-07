---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- linker
- PE/COFF
- relocation
- BFD
discussion_id: 0e0d165a-3190-467e-a921-17eebfa73437@suse.com
source_type: public_inbox
title: '[PATCH 0/3] PE/COFF: R_*_ABS / R_*_NONE handling'
headline: 'PE/COFF: R_*_ABS / R_*_NONE handling'
tldr: Series of patches to improve handling of R_*_ABS and R_*_NONE relocations in
  PE/COFF files.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves handling of non-altering relocations in PE/COFF files.
- Consolidates relocation checking logic across different backends.
- Requires adding new test cases to ensure correctness.
exchanges: []
primer_expert: This is the cover letter for a series of three patches intended to
  improve the binutils support for PE/COFF files concerning relocations of type `R_*_ABS`
  and `R_*_NONE`. These relocations, analogous to ELF's `R_*_NONE`, do not modify
  the binary's content. The series introduces support for `R_AMD64_ABS` in `bfd/coff-x86_64.c`,
  modifies the PE linker (`ld/pe-dll.c`) to ignore these types of relocations, and
  refactors relocation checking using `in_reloc_p()`. A new test case is also added.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the executable file format
    used by Windows operating systems. Binutils' ld supports this format for Windows
    targets.
- term: relocation
  definition: A modification of a program or its data in the executable or library
    by the linker or loader to resolve symbolic references and make it runnable at
    its final address. Relocation types specify how the address or value should be
    calculated.
- term: R_*_ABS / R_*_NONE
  definition: Relocation types that do not alter the binary's content. R_*_ABS typically
    refers to absolute symbol relocations, while R_*_NONE indicates no relocation
    is needed. These are analogous to ELF's R_X86_64_NONE.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries in Unix-like operating systems. Binutils
    fully supports ELF.
series_id: 'binutils:pe/coff: r_*_abs / r_*_none handling'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/0e0d165a-3190-467e-a921-17eebfa73437@suse.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This is the cover letter for a series of patches addressing the handling of R_*_ABS and R_*_NONE relocation types within the PE/COFF file format support in binutils. These relocations are similar to ELF's R_*_NONE and can be used for various purposes without altering the binary. The series aims to improve their processing and introduces necessary test cases.
