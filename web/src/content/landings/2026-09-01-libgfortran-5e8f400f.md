---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- fortran
- bugfix
- pointer
commit_hash: 5e8f400f12c27a5c8c0bacc6ac5975c94274db1e
source_type: github
author: Jerry DeLisle
headline: libgfortran ASSOCIATED now compares element size for polymorphic pointers.
tldr: libgfortran's ASSOCIATED intrinsic now correctly handles polymorphic pointers
  by comparing element sizes.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Fortran `ASSOCIATED` intrinsic checks if two pointers refer to
  the same storage sequence. The existing implementation in `intrinsics/associated.c`
  compared descriptor spans and strides field-by-field. However, when a pointer is
  polymorphic or refers to a character section, its stride may be encoded differently
  (e.g., spacing folded into stride, element length as span). The fix modifies `associated`
  to compare the stride in bytes and requires agreement on either the element length
  (from `dtype`) or the span, rather than solely on the span, thus correctly handling
  these complex cases, parti…
primer_glossary:
- term: ASSOCIATED
  definition: A Fortran intrinsic function that returns `.TRUE.` if a given pointer
    is associated with a target, and `.FALSE.` otherwise. It can also check if two
    pointers refer to the same storage sequence.
- term: Descriptor
  definition: A data structure that describes an array or a scalar variable. For arrays,
    a descriptor typically holds information such as the base address, element size,
    shape (dimensions), and strides (the number of elements to skip to move to the
    next element along each dimension).
- term: Pointer
  definition: In Fortran, a variable that holds the memory address of another data
    item. Pointers are used for dynamic memory allocation and to refer to data indirectly.
- term: Storage sequence
  definition: A contiguous sequence of memory locations. Two pointers are associated
    with the same storage sequence if they point to the same block of memory.
- term: Stride
  definition: The number of elements to skip in memory to advance to the next element
    along a particular dimension of an array, as defined in its descriptor. It is
    often expressed in bytes or in number of elements.
- term: Polymorphic
  definition: In Fortran, a variable that can hold values of different data types
    during its lifetime. This is typically used with pointers and derived types.
- term: Character section
  definition: A contiguous part of a character string. When accessing a substring,
    a descriptor might represent it as a character section with specific span and
    stride information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e8f400f12c27a5c8c0bacc6ac5975c94274db1e
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

A bug in libgfortran's implementation of the `ASSOCIATED` intrinsic prevented it from correctly identifying associated polymorphic pointers, particularly character sections. The issue stemmed from comparing spans and strides directly, which could differ even when denoting the same storage. This fix introduces a `stride_in_bytes` helper and ensures `ASSOCIATED` now compares the stride in bytes and checks for agreement on element length or span, resolving PR126964.
