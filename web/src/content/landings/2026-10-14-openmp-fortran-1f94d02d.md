---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- compiler
commit_hash: 1f94d02d9870ea5f1b511241d4d25bd39d54dcc8
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Support ''cgroup'' modifier to dyn_groupprivate clause'
tldr: Adds parsing support for the 'cgroup' modifier in OpenMP's dyn_groupprivate
  clause for Fortran.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Extends the Fortran front-end's OpenMP clause parsing to include the
  'cgroup' access-group modifier for `dyn_groupprivate`. This aligns the parser with
  the OpenMP specification's support for this modifier.
primer_glossary:
- term: OpenMP
  definition: A standardized API for shared-memory parallel programming that supports
    C, C++, and Fortran.
- term: dyn_groupprivate
  definition: An OpenMP clause that specifies data-private to a group of threads,
    where the group can dynamically change.
- term: cgroup
  definition: A modifier for OpenMP clauses that specifies the scope of data sharing
    or privacy, particularly related to dynamic thread groups.
- term: Fortran
  definition: A high-level programming language commonly used in scientific and numerical
    computing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1f94d02d9870ea5f1b511241d4d25bd39d54dcc8
date: '2026-10-14'
is_stub: false
stub_reason: ''
---

This commit enhances the Fortran OpenMP compiler to support the 'cgroup' modifier within the dyn_groupprivate clause. Previously, only the groupprivate clause parsing was added, and this change ensures the 'cgroup' modifier, which is also the default, is correctly parsed. New test cases are included to verify this functionality.
