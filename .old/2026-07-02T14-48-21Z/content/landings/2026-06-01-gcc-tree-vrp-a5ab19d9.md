---
project: gcc
subsystem: gcc/tree-vrp
patch_id: null
tags:
- optimization
- pointers
- gimple
- value-range-analysis
commit_hash: a5ab19d9db2d13db3ea21d0b2a0e3e5e02766bc8
source_type: github
author: Andrew MacLeod
headline: Switch VRP to use prange
tldr: GCC's Value Range Propagation (VRP) now utilizes the new `prange` system for
  points-to information, replacing an older side table and requiring test case adjus…
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's Value Range Propagation (VRP) is an important optimization pass
  that analyzes the possible values of variables, represented at the GIMPLE intermediate
  representation level. This commit fundamentally alters how VRP handles pointer analysis.
  Previously, VRP might have used a `value-range-equiv` side table to establish points-to
  information. This has been deprecated in favor of the more comprehensive `prange`
  system, which now directly incorporates points-to data through mechanisms like `prange::set_pt`
  and `prange::union_`. The integration of `prange` into VRP's `rvrp_folder::value_of_exp…
primer_general: 'Compilers like GCC try to make your code run faster by understanding
  what values your variables might hold. This process is called "Value Range Propagation"
  (VRP). When your code uses pointers (variables that store memory addresses), the
  compiler also needs to figure out what those pointers might be pointing to. This
  is called "points-to information." This commit updates how GCC''s VRP does this:
  it now uses a new, more advanced system called `prange` (pointer range) which directly
  incorporates points-to analysis. This is a significant internal change that makes
  the compiler''s understanding of pointers more accurate. As a consequence, some
  of the compiler''s self-tests needed updating because the new analysis changes the
  generated code, sometimes leading to fewer runtime checks for memory operations
  (`mem*_chk routines`). Other tests were temporarily marked to ''expect failure''
  (`XFAIL`) due to newly uncovered issues related to how the compiler handles arithmetic
  on pointers during an in…'
discussion_id_link: github:gcc-mirror/gcc#123160
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a5ab19d9db2d13db3ea21d0b2a0e3e5e02766bc8
date: '2026-06-01'
is_stub: false
---

The Value Range Propagation (VRP) pass in GCC has been refactored to use the newly introduced `prange` (pointer range) system for its points-to analysis, moving away from a previous value-range-equivalence side table. This change affects how VRP determines what memory locations pointers can access. As a result of this modification, several test cases were adjusted, with some (like `memcpy-chk.c`) needing updates due to changes in generated `mem*_chk` routines, and others (like `builtin-object-size-4.c`) being `XFAIL`ed due to ongoing issues with `pointer_plus` handling in GIMPLE folding.
