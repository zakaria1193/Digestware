---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- std::print
- c++23
- documentation
commit_hash: e2b1c3ea40727db805f8e062dbfff0bb93770004
source_type: github
author: Jonathan Wakely
headline: 'Libstdc++: Fix comment on std::print helper __open_terminal.'
tldr: Updates the comment for the `__open_terminal` function used by `std::print`
  to reflect its current behavior.
why_it_matters: Ensures that the comments accurately describe the code, improving
  maintainability.
impact_score: 2
impact_rationale: Comment update, low impact.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `__open_terminal` function is an internal helper function used
  by the `std::print` implementation in libstdc++. This function likely handles opening
  a connection to the terminal for output. This change is to bring the comments up
  to date with the implementation.
primer_general: The C++ standard library (libstdc++) provides various functions for
  input and output. The `std::print` function, introduced in C++23, provides a way
  to format and print output to the console. This commit updates a comment for a helper
  function used by `std::print` to ensure that the comments accurately reflect the
  code's behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2b1c3ea40727db805f8e062dbfff0bb93770004
date: '2026-04-21'
---

This commit updates the comment for the `__open_terminal` function in `src/c++23/print.cc`. The comment described an earlier version of the function, and this commit updates it to accurately reflect the current semantics of the function.
