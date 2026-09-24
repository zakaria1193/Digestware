---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- gas
- refactoring
- relocation
discussion_id: 20260924015023.36799-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3 2/4] microblaze: use md_number_to_chars in md_apply_fix'
headline: 'microblaze: use md_number_to_chars in md_apply_fix'
tldr: Refactors MicroBlaze's `md_apply_fix` to use `md_number_to_chars` for more consistent
  and cleaner relocation handling.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaces architecture-specific byte manipulation with a generic BFD function for
  improved portability and maintainability.
- Introduces a new macro to handle instruction immediate offsets, maintaining functional
  correctness.
- No functional change, but improves code structure and consistency.
exchanges: []
primer_expert: This patch replaces manual, open-coded byte writes within MicroBlaze's
  `md_apply_fix` (in `gas/config/tc-microblaze.c`) with calls to `md_number_to_chars`.
  This function is the standard BFD way to write numerical values as bytes according
  to the target's endianness. For data relocations (`BFD_RELOC_32`, etc.), this removes
  endianness checks. For instruction relocations, the immediate field's offset within
  the 32-bit word requires special handling, hence the introduction of `INST_IMM_OFFSET`.
  The 64-bit instruction cases are adjusted accordingly. The series' test results
  show identical outcome…
primer_glossary:
- term: md_apply_fix
  definition: A BFD function responsible for applying relocation fixups to data or
    code during the assembly process for a specific target architecture.
- term: md_number_to_chars
  definition: A generic BFD utility function that converts a number into a sequence
    of bytes respecting the target's endianness.
- term: BFD_RELOC_32
  definition: A relocation type indicating a 32-bit value needs to be adjusted.
- term: INST_IMM_OFFSET
  definition: A MicroBlaze-specific macro defining the byte offset of the immediate
    field within a 32-bit instruction word.
- term: Relocation
  definition: The process of updating symbolic references in object code to their
    final memory addresses. Relocations are instructions for the linker or dynamic
    loader on how to modify addresses.
series_id: 'binutils:microblaze: use md_number_to_chars in md_apply_fix'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924015023.36799-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch refactors the `md_apply_fix` function in the MicroBlaze backend to utilize the generic `md_number_to_chars` function for writing relocation data. This approach is consistent with how other backends like AArch64, MIPS, and SPARC handle relocations. For data relocations, this simplifies the code by removing endianness-specific branches. For instruction relocations, a new macro `INST_IMM_OFFSET` is introduced to handle the immediate field's offset within the instruction word, as `md_number_to_chars` only addresses byte ordering. The change aims to have no functional impact and has been validated by the test suite, showing no unexpected failures on either MicroBlaze endianness.
