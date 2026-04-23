---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- c++23
- std::print
- documentation
commit_hash: e2b1c3ea40727db805f8e062dbfff0bb93770004
source_type: github
author: Jonathan Wakely
headline: Update comment on std::print helper __open_terminal in libstdc++.
tldr: This commit updates a comment for the `__open_terminal` helper function in `std::print`
  to reflect its current behavior.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '`std::print` is a new feature in C++23, and `__open_terminal` is an
  internal helper function within its implementation in libstdc++. The comment for
  `__open_terminal` was outdated and no longer accurately described its function.
  This change affects the readability and maintainability of the `std::print` implementation.'
primer_general: '`std::print` is a new C++23 feature designed to provide a simpler
  and more consistent way to output formatted text. This commit addresses an outdated
  comment within the internal implementation of `std::print` in libstdc++.  Specifically,
  the comment for the helper function `__open_terminal` was inaccurate and has been
  updated. While not directly impacting users, this improves the clarity and maintainability
  of the libstdc++ library itself.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2b1c3ea40727db805f8e062dbfff0bb93770004
date: '2026-04-21'
---

The commit fixes a comment in `src/c++23/print.cc` for the `__open_terminal` helper function used by `std::print`.  The comment described an earlier version of the function, so it has been updated to reflect the current semantics. This enhances code maintainability and understanding.
