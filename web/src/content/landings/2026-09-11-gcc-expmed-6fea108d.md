---
project: gcc
subsystem: gcc/expmed
patch_id: null
tags:
- optimization
- compiler-error
commit_hash: 6fea108d4725f1aa79ce3acd9b6933da003d11a4
source_type: github
author: Robin Dapp
headline: Use store_bit_field for unsplittable targets
tldr: Fixes an ICE in extract_integral_bit_field by using store_bit_field for unsplittable
  targets, improving robustness.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `extract_integral_bit_field` function in `expmed.cc` previously
  assumed targets could always be split into subregisters. With recent `regmode_natural_size`
  changes, unsplittable targets like `reg:V2DF` can cause an ICE. This commit introduces
  a fallback to `store_bit_field` when `operand_subword` fails, ensuring correct handling
  of such targets and preventing the ICE.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A condition that prevents GCC from completing
    a compilation, often due to an unrecoverable state in the compiler's internal
    logic.
- term: regmode_natural_size
  definition: A GCC internal concept that defines the natural size of a machine mode
    for a register. Changes here can affect how subregisters are handled.
- term: store_bit_field
  definition: A GCC internal function or mechanism for storing a bit field into a
    target, likely handling cases where the field might not align perfectly or span
    register boundaries.
- term: operand_subword
  definition: Likely a GCC internal function related to accessing or manipulating
    sub-parts of a register operand, often used when dealing with bit fields or smaller
    data types within a larger register.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6fea108d4725f1aa79ce3acd9b6933da003d11a4
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

This change modifies extract_integral_bit_field to use store_bit_field when a target cannot be split into subregisters. This prevents an ICE that could occur after recent changes to regmode_natural_size. For RISC-V, this may introduce a spill per iteration, which is noted as a potential area for future mitigation.
