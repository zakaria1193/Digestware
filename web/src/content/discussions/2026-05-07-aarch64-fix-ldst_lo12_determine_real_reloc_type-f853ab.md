---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- relocation
- load/store
- code cleanup
discussion_id: 8d061c2f-909d-3c9f-19ab-1540666cb02a@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 12/23] aarch64: Fix ldst_lo12_determine_real_reloc_type'
headline: 'Aarch64: Fix ldst_lo12_determine_real_reloc_type'
tldr: Improve relocation type determination for load/store instructions and remove
  unused function `aarch64_get_expected_qualifier`.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves error handling in `ldst_lo12_determine_real_reloc_type`.
- Simplifies the code by inlining functionality and removing an unused function.
- May change the behavior of `ldst_lo12_determine_real_reloc_type` in edge cases.
exchanges: []
primer_expert: In the AArch64 backend, `ldst_lo12_determine_real_reloc_type` determines
  the relocation type for load/store instructions with a 12-bit offset.  This patch
  improves the function's robustness and removes the unused `aarch64_get_expected_qualifier`
  in `gas/config/tc-aarch64.c`, simplifying the relocation process.
primer_general: When code is compiled, the compiler sometimes needs to insert placeholders
  for memory addresses that will only be known later. These placeholders are called
  relocations. This patch improves how the assembler determines the correct type of
  relocation to use for certain load and store instructions, and it also removes a
  function that's no longer needed, making the assembler's code cleaner.
series_id: 'binutils:aarch64: fix ldst_lo12_determine_real_reloc_type'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8d061c2f-909d-3c9f-19ab-1540666cb02a@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch improves the `ldst_lo12_determine_real_reloc_type` function by adding fallback handling for invalid operand qualifiers, preventing assertions when encountering X registers in byte or half instructions. It also simplifies the code by inlining parts of `aarch64_get_expected_qualifer` and directly deducing the array index from qualifier enum values. As a result, the `aarch64_get_expected_qualifier` function becomes unused and is removed, simplifying the codebase.
