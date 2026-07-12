---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- gfortran
- bugfix
commit_hash: 69a2daacba6353d1aab3118415b89afd479c4c76
source_type: github
author: Jerry DeLisle
headline: Restrict host association symbol skipping to derived types.
tldr: Fixes PR126210 by ensuring host association symbol skipping only applies to
  derived types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `read_module` function in `gcc/fortran/module.cc` was modified
  to ensure that symbols already visible via host association from the same module
  are only skipped for re-import if they are derived types. This change rectifies
  an overzealous application of PR126170's fix, which had incorrectly broadened the
  scope of symbol skipping beyond its intended target.
primer_glossary:
- term: host association
  definition: A Fortran feature where entities declared in a host program unit (e.g.,
    a main program or module) are accessible within a contained subprogram or derived
    type definition without requiring explicit argument passing or procedure calls.
- term: derived type
  definition: A user-defined composite data type in Fortran, analogous to a struct
    or class in other languages. It can contain components of various intrinsic or
    other derived types.
- term: PR126170
  definition: A bug report identifier. These are used internally by the GCC project
    to track specific issues, bugs, or feature requests. This commit addresses a related
    issue, PR126210.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/69a2daacba6353d1aab3118415b89afd479c4c76
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

The recent fix for PR126170 in `read_module()` incorrectly skipped re-importing any symbol already visible via host association from the same module, if matched by name. This commit refines that behavior, ensuring that symbol skipping now only occurs when the matched symbol is specifically a derived type, thus resolving PR126210 and preventing unintended omissions of other symbol types.
