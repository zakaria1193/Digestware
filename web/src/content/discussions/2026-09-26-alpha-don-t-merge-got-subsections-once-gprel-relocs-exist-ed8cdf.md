---
project: binutils
subsystem: alpha
patch_id: null
tags:
- binutils
- linker
- alpha
- relocation
- optimization
discussion_id: 20260926165132.1054779-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH] alpha: don''t merge .got subsections once GPREL relocs exist'
headline: 'alpha: don''t merge .got subsections once GPREL relocs exist'
tldr: Fixes binutils linker bug on alpha where merging .got subsections after GPREL
  relocs are created leads to relocation errors.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Prevents a relocation error by adding a new flag and conditional logic, ensuring
  correctness at the cost of slightly more complex linker state management.
exchanges:
- author: Matt Turner <mattst88@gmail.com>
  role: proposer
  position: Submits a patch to prevent merging .got subsections in the alpha ELF linker
    after GPREL relocations have been established, addressing a bug that arises when
    relaxation is re-evaluated.
  quote: "Remember that pass 1 has been reached and don't merge after that.\n\n\t\
    PR ld/5276\nbfd/\n\t* elf64-alpha.c (struct alpha_elf_link_hash_table): Add\n\t\
    no_got_merge.\n\t(elf64_alpha_relax_section): Set it once relax_pass is nonzero,\n\
    \tand don't merge .got subsections after that.\nld/\n\t* testsuite/ld-alpha/got-merge-gprel-a.s:\
    \ New.\n\t* testsuite/ld-alpha/got-merge-gprel-b.s: New.\n\t* testsuite/ld-alpha/got-merge-…"
primer_expert: This patch addresses a bug in the alpha ELF linker (bfd/elf64-alpha.c)
  where merging .got subsections can occur after GPREL16 relocations are in place.
  The linker's relaxation process can restart from pass 0, undoing an earlier prevention
  of merging. The fix introduces a `no_got_merge` flag to ensure subsections are not
  merged once GPREL relocs exist, resolving PR ld/5276.
primer_glossary:
- term: .got
  definition: 'Global Offset Table: a section used in ELF executables and shared libraries
    to store pointers to global or static variables, allowing for position-independent
    code.'
- term: GPREL
  definition: 'Global Pointer Relative: a type of relocation used in some architectures
    (like Alpha) where addresses are calculated relative to a global pointer register.'
- term: relaxation
  definition: A linker optimization process that adjusts addresses and sizes of code
    and data sections to potentially reduce their memory footprint or improve performance,
    often involving multiple passes.
- term: subsection
  definition: A smaller, contiguous part within a larger section (like .got) that
    can be manipulated or merged independently during linking.
- term: relocation
  definition: Information in an object file that tells the linker how to modify certain
    instructions or data in the code to refer to the correct memory addresses at runtime.
- term: pass
  definition: A single iteration of a process, such as the relaxation passes performed
    by the linker. Higher pass numbers usually indicate more significant or final
    adjustments.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260926165132.1054779-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-26'
is_stub: false
stub_reason: ''
---

This patch modifies the alpha ELF linker to prevent merging of .got subsections after Global Pointer Relative (GPREL) relocations are created. A previous change disabled merging after the first relaxation pass, but the linker's re-evaluation of layout can restart relaxation from pass zero, leading to incorrect merges and relocation truncation errors.
