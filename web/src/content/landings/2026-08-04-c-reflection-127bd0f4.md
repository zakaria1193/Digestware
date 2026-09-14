---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- standardization
commit_hash: 127bd0f40827d7472cebacd2093d3379ec25dbd7
source_type: github
author: Marek Polacek
headline: 'C++/reflection: Adapt to consteval-only values model for reflection.'
tldr: GCC's reflection implementation now supports the C++ P4101 paper's 'consteval-only
  values' model, requiring significant internal changes.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's C++ reflection infrastructure is updated to align with the C++
  proposal P4101 ('Consteval-only values'). This involves replacing `META_TYPE` with
  `LANG_TYPE` to accommodate null reflections within the Mid-level Expression (ME)
  representation, ensuring they map to DWARF's `DW_TAG_unspecified_type`. The handling
  of discarded-value expressions in `convert_to_void` is refactored; such expressions
  are now only discarded after checking for consteval-only values, and this discarding
  is moved to `cp_fold_r` to avoid interfering with subsequent processing like `maybe_save_constexpr_fundef`.
  `REF…
primer_glossary:
- term: reflection
  definition: A C++ feature (currently under development/proposal) that allows code
    to inspect and manipulate its own structure and metadata at compile time.
- term: consteval-only
  definition: A property indicating that a value or type can only be used in a constant
    evaluation context (i.e., at compile time).
- term: P4101
  definition: A C++ standards committee paper (P4101) that proposes changes to the
    consteval rules for reflection, moving from 'consteval-only types' to 'consteval-only
    values'.
- term: LANG_TYPE
  definition: GCC's internal representation for language types, used in various compiler
    passes.
- term: META_TYPE
  definition: An internal GCC type representation, likely specific to earlier reflection
    implementations.
- term: DW_TAG_unspecified_type
  definition: A DWARF debugging information tag used to represent a type that cannot
    be determined.
- term: ME
  definition: Mid-level Expression, an intermediate representation used within the
    GCC C++ frontend.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/127bd0f40827d7472cebacd2093d3379ec25dbd7
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This commit updates GCC's C++ reflection implementation to comply with the C++ standard paper P4101, which shifts the model from 'consteval-only types' to 'consteval-only values'. This change allows for more flexibility, such as null reflections no longer being restricted to consteval contexts.

Internally, this required substantial modifications, including using `LANG_TYPE` instead of `META_TYPE` for null reflections, ensuring `DW_TAG_unspecified_type` in debug info, and adjusting how discarded-value expressions are handled. The changes impact expression rewriting, consteval-only value checks, and code generation, particularly for debug information.
