---
project: binutils
subsystem: ld/pe
patch_id: null
tags:
- linker
- PE/COFF
- relocation
discussion_id: 2ef36e60-0501-42f0-9def-0b302f666e33@suse.com
source_type: public_inbox
title: '[PATCH 2/3] ld/PE: ignore R_*_ABS / R_*_NONE'
headline: 'ld/PE: ignore R_*_ABS / R_*_NONE'
tldr: The PE linker will now ignore R_*_ABS and R_*_NONE relocations instead of erroring
  on them.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Allows for more flexible use of ABS/NONE relocations in PE/COFF files.
- Introduces a new test case to cover the expected behavior.
exchanges: []
primer_expert: This patch modifies `ld/pe-dll.c` to skip relocations where `BITS_AND_SHIFT(relocs[i]->howto->bitsize,
  relocs[i]->howto->rightshift)` results in `BITS_AND_SHIFT(0, 0)`, effectively ignoring
  ABS/NONE type relocations. This change is accompanied by a new test case (`ld/testsuite/ld-pe/reloc-none.*`)
  and associated test runner configuration (`pe.exp`) to validate that these previously
  problematic relocations are now handled correctly without erroring out, aligning
  with their potential use cases.
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
- term: BITS_AND_SHIFT
  definition: A macro used within binutils to extract the bitsize and rightshift parameters
    from a relocation howto structure.
series_id: 'binutils:ld/pe: ignore r_*_abs / r_*_none'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2ef36e60-0501-42f0-9def-0b302f666e33@suse.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch modifies the PE linker to gracefully ignore relocation types designated as R_*_ABS or R_*_NONE. Previously, these might have caused errors. The change allows these relocations to be used for 'interesting purposes' without halting the linking process, and introduces a new test case to verify this behavior.
