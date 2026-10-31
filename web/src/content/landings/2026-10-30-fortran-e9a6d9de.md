---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- bugfix
commit_hash: e9a6d9dee3098bc32d7b5da750a65755fea7a734
source_type: github
author: Mikael Morin
headline: 'fortran: Fix copy from polymorphic pointer source in ALLOCATE [PR128033]'
tldr: Fortran ALLOCATE statement now correctly handles polymorphic pointer sources.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit resolves PR128033 by correcting the handling of polymorphic
  pointer array sources in Fortran's `ALLOCATE` statement. A previous change (r14-9160)
  introduced automatic parenthesized wrapping of the source expression to create a
  temporary, which inadvertently broke polymorphic array handling. The generated temporary's
  array reference missed the 'class container' parent, leading to incorrect array
  indexing via the non-polymorphic fallback. This patch reverts that temporary solution.
  It also fixes an assertion failure in `gfc_find_array_ref` that incorrectly expected
  single-element re…
primer_glossary:
- term: ALLOCATE statement
  definition: A Fortran statement used to dynamically allocate memory for variables,
    such as pointers or allocatable arrays.
- term: polymorphic pointer
  definition: In Fortran, a pointer that can point to objects of different, but related,
    dynamic types. These types are usually organized in an inheritance hierarchy.
- term: class container
  definition: In Fortran, a derived type that holds polymorphic components. It represents
    an object whose dynamic type can change.
- term: array subreference
  definition: A part of an array reference, potentially involving indexing or slicing,
    that itself refers to an array.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e9a6d9dee3098bc32d7b5da750a65755fea7a734
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

A regression in the Fortran ALLOCATE statement that caused incorrect copying from polymorphic pointer sources has been fixed. The issue arose from a temporary fix for another bug, which inadvertently introduced a temporary array that lacked the necessary 'class container' information. This caused indexing errors when copying data. This commit reverts the problematic temporary fix and addresses the root cause by correctly identifying and using array references within the source expression, resolving the bug for users with polymorphic pointer arrays.
