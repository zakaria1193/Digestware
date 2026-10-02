---
project: gcc
subsystem: gcc/ranger
patch_id: null
tags:
- optimization
- compiler pass
- refactor
commit_hash: 7cca1da5cca6521a389cceb6032125346b30bd90
source_type: github
author: Aldy Hernandez
headline: 'ranger: Refactor range_from_readonly_load into a class.'
tldr: The ranger pass's `range_from_readonly_load` function is refactored into a class
  for better maintainability and future enhancements.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ranger` pass's `range_from_readonly_load` function, which recursively
  determined the range of values loaded from read-only memory, has been converted
  into a class `ctor_ref_range`. This addresses issues with threading invariant parameters
  and new information through recursive calls. The class now holds the invariant data
  and provides methods for accumulating ranges from different types of references
  (scalar, component, array), improving modularity and extensibility for future analysis,
  such as DOM parity checks.
primer_glossary:
- term: ranger pass
  definition: A GCC optimization pass that analyzes and optimizes memory access patterns,
    particularly for read-only data, to improve code efficiency.
- term: DOM parity
  definition: Ensuring that the compiler's analysis of data access patterns (Data
    Object Model) accurately reflects the actual runtime behavior, especially concerning
    aliasing and aliasing-related optimizations.
- term: SSA_NAME
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned a value exactly once. SSA_NAME refers to a variable
    in this form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7cca1da5cca6521a389cceb6032125346b30bd90
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

The `range_from_readonly_load` function in the ranger pass has been refactored into a class to better manage its state. This change encapsulates invariant data as class members, making the function easier to enhance, particularly for tasks like improving DOM parity in the ranger threader. The original recursive function is split into methods of the new class.
