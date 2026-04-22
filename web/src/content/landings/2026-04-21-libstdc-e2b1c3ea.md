---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- documentation
- std::print
- c++23
commit_hash: e2b1c3ea40727db805f8e062dbfff0bb93770004
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Correct comment on std::print helper function'
tldr: Updates the comment for the `__open_terminal` helper function in `std::print`
  to accurately describe its current behavior.
why_it_matters: Ensures that the documentation for the `std::print` feature is accurate
  and reflects the current implementation, improving code maintainability.
impact_score: 2
impact_rationale: Fixes a comment to accurately reflect the behavior of the __open_terminal
  function.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies a comment in `src/c++23/print.cc` within the `libstdc++`
  library. The comment pertains to the `__open_terminal` helper function used by the
  `std::print` feature. The change reflects the evolution of the function's implementation.
  The `search_context` tool will be used to give spotlight about 'C++ std::print'.
primer_general: This commit involves a minor documentation update in the C++ standard
  library (`libstdc++`). It corrects a comment associated with a helper function used
  in the `std::print` feature, a new way to print output in C++. The comment had become
  outdated as the implementation of the function evolved. This change ensures that
  the comment accurately reflects the function's current behavior. The `search_context`
  tool will be used to give spotlight about 'C++ standard library'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2b1c3ea40727db805f8e062dbfff0bb93770004
date: '2026-04-21'
---

The comment for the `__open_terminal` helper function in `src/c++23/print.cc` was outdated and described an earlier version of the function. This commit updates the comment to accurately reflect the current semantics of the function, which is used to open a terminal for `std::print` output.
