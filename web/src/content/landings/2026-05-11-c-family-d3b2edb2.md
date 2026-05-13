---
project: gcc
subsystem: c-family
patch_id: null
tags:
- c++
- typedef
- type resolution
- bugfix
commit_hash: d3b2edb2664893cc0deb3d8815effa27436b39f9
source_type: github
author: Jason Merrill
headline: 'C-family: Look through non-user-facing typedef'
tldr: The compiler now correctly identifies user-facing types even when going through
  non-user-facing typedefs.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The C family frontends (C, C++, Objective-C, Objective-C++) share
  a common infrastructure for type representation and manipulation.  The function
  ``user_facing_original_type_p`` is used to determine whether a type is user-facing,
  which affects how it''s displayed to the user.  This commit modifies ``c-common.cc``
  to recurse when encountering non-user-facing typedefs. Search terms: GCC c-family
  typedef user_facing_original_type_p.'
primer_general: 'In C and C++, ``typedef`` is used to create aliases for existing
  data types.  The compiler needs to be able to resolve these aliases to determine
  the underlying type.  This is especially important when displaying type information
  to the user, such as in error messages or debugging output. This commit ensures
  that the compiler can correctly resolve typedefs, even when they are nested or involve
  internal compiler types. Search terms: GCC c-family typedef user_facing_original_type_p.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d3b2edb2664893cc0deb3d8815effa27436b39f9
date: '2026-05-11'
is_stub: false
---

The compiler's 'aka' printing (used to display type information) could differ between in-tree and installed compilers, due to differences in how libstdc++ headers are treated. The issue was that the compiler would stop looking for the underlying user type when it encountered a non-user-facing typedef (e.g., ``__iter_type<T>``).  This commit fixes this by making the type resolution recurse through such typedefs.
