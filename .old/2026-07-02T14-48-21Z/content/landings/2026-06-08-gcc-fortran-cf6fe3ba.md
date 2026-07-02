---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- optimization
- memory-management
- pdt
commit_hash: cf6fe3baf828c3e6cbb4b1898ff702030ae06d5c
source_type: github
author: Paul Thomas
headline: 'Fortran: Prevent unnecessary mallocs and frees for parameterized derived
  types'
tldr: GCC's Fortran front end now avoids unnecessary memory allocations and deallocations
  for parameterized derived types.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In GCC's Fortran front end, handling Parameterized Derived Types (PDTs)
  involves tracking characteristics like array bounds or string lengths. This commit
  (`decl.cc`, specifically `gfc_get_pdt_instance`) optimizes the management of these
  types. Previously, attributes like `pdt_array` and `pdt_string` might have been
  set even when the relevant expressions (bounds for arrays, length for characters)
  simplified to a constant. Setting these attributes unnecessarily could trigger dynamic
  memory allocations (`malloc`) and subsequent deallocations (`free`). By avoiding
  setting these attributes when c…
primer_general: Fortran, a programming language often used in scientific computing,
  allows programmers to define their own complex data structures, called 'derived
  types'. These can be further customized with 'parameters', such as specifying the
  size of an array within the structure, leading to 'parameterized derived types'
  (PDT). When a Fortran program uses these PDTs, the compiler (GCC, in this case)
  needs to determine their exact layout and properties. This commit introduces an
  optimization where, if the size of an array or the length of a character string
  within a PDT can be figured out as a fixed number during compilation, the compiler
  will be smarter about how it handles that information. Instead of treating it as
  something that might change (which would require it to allocate and free memory
  repeatedly at runtime), it recognizes it as constant. This subtle change means the
  program will perform fewer memory management operations (like asking the operating
  system for new memory or giving it back…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cf6fe3baf828c3e6cbb4b1898ff702030ae06d5c
date: '2026-06-08'
is_stub: false
---

The Fortran front end in GCC has been optimized to reduce unnecessary memory allocations and deallocations when handling parameterized derived types (PDT). Specifically, if the bound expressions for array components or length expressions for character components simplify to a constant, the compiler will no longer set the `pdt_array` or `pdt_string` attributes respectively. This change prevents redundant heap operations, leading to improved performance for programs heavily using PDTs.
