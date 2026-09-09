---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- gcc
- middle-end
- cleanup
- internal
commit_hash: ba64a8e87c702788b0fdf9ecc6676f2c16b671a0
source_type: github
author: Kael Andrew Alonzo Franco
headline: Unused `pp_double_int` removed from GCC.
tldr: An unused pretty-printing function for double integers has been removed from
  GCC's middle-end.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `pp_double_int` function and its associated type definition have
  been deleted from GCC's tree pretty-printing utilities. This removal is justified
  by its lack of usage and is part of a broader initiative to deprecate and remove
  the `double-int` concept in favor of the more modern and general `fixed_wide_int`
  infrastructure, as discussed in broader GCC mailing list discussions.
primer_glossary:
- term: pp_double_int
  definition: A function or type related to pretty-printing, specifically for a 'double
    integer' representation, which has been removed as it was unused.
- term: tree-pretty-print.h/cc
  definition: Header and source files in GCC responsible for pretty-printing the compiler's
    internal tree structures.
- term: fixed_wide_int
  definition: GCC's internal data type for handling arbitrary-precision integers,
    which has superseded older representations like 'double-int'.
- term: middle-end
  definition: The part of a compiler that performs optimizations and transformations
    on an intermediate representation of the code, independent of the source language
    and target architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ba64a8e87c702788b0fdf9ecc6676f2c16b671a0
date: '2026-09-07'
is_stub: true
stub_reason: low_score
---

The `pp_double_int` function and related type from `tree-pretty-print.h` and `tree-pretty-print.cc` have been removed, as they are no longer used. This cleanup is part of a larger effort to remove `double-int` constructs now that `fixed_wide_int` provides similar functionality.
