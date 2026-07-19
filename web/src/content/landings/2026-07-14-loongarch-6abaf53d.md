---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- vector
- bugfix
commit_hash: 6abaf53d84db86bd917d18cac5aac3c3bf37929c
source_type: github
author: Xi Ruoyao
headline: Fix conditional vector shuffle operand handling for LoongArch.
tldr: Corrected predicate logic for LoongArch's vector shuffle instructions to handle
  operand modes properly.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `par_const_vector_shf_set_operand` predicate in LoongArch's `predicates.md`
  was designed to check if a constant vector shuffle's selector operand matched the
  mode of the shuffled vector. However, due to the underlying `lsx_vshuf4i_<lsxfmt_f>`
  definitions using `VOIDmode` for the selector's `mode` field, the predicate would
  accept any mode. This commit refactors the predicate into a special predicate and
  ensures `VIMODE` is passed to it when processing `lsx_vshuf4i`, aligning the mode
  checking with the expected behavior and resolving issues arising from recent improvements
  in folding `vec_…
primer_glossary:
- term: LoongArch
  definition: A family of RISC-based computer architectures developed in China.
- term: VIMODE
  definition: Likely refers to a specific GCC internal mode representing a vector
    integer type, used for operations on vector data.
- term: VOIDmode
  definition: A GCC internal mode representing an undefined or unused type, often
    used as a placeholder.
- term: predicate
  definition: In GCC's machine description files (like `.md`), a predicate is a condition
    that must be true for a particular instruction pattern to match.
- term: lsx_vshuf4i
  definition: A LoongArch specific instruction for performing a 4-element vector shuffle
    operation.
discussion_id_link: github:gcc-mirror/gcc#126200
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6abaf53d84db86bd917d18cac5aac3c3bf37929c
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in the LoongArch backend concerning the predicate `par_const_vector_shf_set_operand`, which was used to validate operands for constant vector shuffle instructions like `lsx_vshuf4i`. The predicate incorrectly accepted any mode for the selector operand because it was declared as `VOIDmode`. The fix modifies this predicate to be a special predicate and specifies `VIMODE` for the selector, ensuring it matches the expected mode and preventing incorrect folding of vector select operations.
