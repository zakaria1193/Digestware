---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- parser
- error handling
- memory leak
commit_hash: ab3c778a2530b25713002ba78af65334174deb3d
source_type: github
author: Harald Anlauf
headline: Fortran parser recovers from invalid inquiry references
tldr: Fortran parser handles invalid inquiry references more gracefully and fixes
  memory leaks.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gfc_match_varspec` function in `primary.cc` previously had an
  assertion that could trigger on invalid inquiry references. This commit replaces
  the assertion with a failure return and fixes memory leaks on error paths. The changes
  in `symbol.cc` ensure `gfc_find_derived_types` returns a null symbol pointer when
  an associated symbol is null, preventing a potential dereference of a null pointer.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab3c778a2530b25713002ba78af65334174deb3d
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

The Fortran compiler now replaces an assertion with a failure return value when encountering invalid inquiry references during parsing. This change improves error recovery and also addresses minor memory leaks in the frontend's error return path. A new test case is included to verify the fix.
