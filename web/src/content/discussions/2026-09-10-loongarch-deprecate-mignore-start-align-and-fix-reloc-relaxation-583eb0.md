---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- assembler
- linker
- relocation
- deprecated
discussion_id: 20260910092253.526336-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 0/3] LoongArch: Deprecate -mignore-start-align and fix .reloc for relaxtion'
headline: 'LoongArch: Deprecate -mignore-start-align and fix .reloc relaxation'
tldr: Deprecates an old alignment option and fixes linker relaxation issues related
  to .reloc directives on LoongArch.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removes a deprecated option, simplifying the assembler's interface.
- Fixes correctness issues in linker relaxation handling.
- Introduces new test cases to verify the fixes.
exchanges: []
primer_expert: This is the cover letter for a three-patch series affecting the LoongArch
  toolchain. Patch 1 deprecates the `-mignore-start-align` option in GAS, as alignment
  optimization is now standard. Patches 2 and 3 address problems with linker relaxation
  on LoongArch, specifically concerning how GAS handles `.reloc *, R_LARCH_RELAX`
  directives. These directives mark code fragments as linker-relaxable, but GAS previously
  failed to properly record and act on this state, leading to incorrect relocations
  and DWARF output. The series ensures correct processing of these relaxable fragments.
primer_glossary:
- term: linker relaxation
  definition: A process where the linker adjusts code and data locations to optimize
    for size or performance, often by replacing instructions with smaller variants
    or using different addressing modes.
- term: GAS
  definition: The GNU Assembler, a component of the GNU Binutils package that translates
    assembly language code into machine code.
- term: R_LARCH_RELAX
  definition: A LoongArch relocation type that signals to the linker that the associated
    instruction or fragment is subject to relaxation.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about variables, types, and source code locations.
- term: relocation
  definition: A process performed by the linker or dynamic loader to resolve symbolic
    references between different object files or libraries. It involves adjusting
    addresses based on the final memory layout.
series_id: 'binutils:loongarch: deprecate -mignore-start-align and fix .reloc for
  relaxtion'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910092253.526336-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch series addresses two main areas for the LoongArch toolchain. The first patch deprecates the `-mignore-start-align` option in GAS, as its functionality is now handled by default optimizations. The subsequent two patches fix critical issues related to linker relaxation when `.reloc *, R_LARCH_RELAX` directives are used. These fixes ensure that fragments marked as linker-relaxable are correctly identified and handled, preventing incorrect relocation generation and DWARF information.
