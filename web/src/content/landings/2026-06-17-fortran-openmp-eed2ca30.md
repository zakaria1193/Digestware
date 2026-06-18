---
project: gcc
subsystem: fortran/openmp
patch_id: null
tags:
- fortran
- openmp
- refactoring
- readability
commit_hash: eed2ca30e49d8177921e8c01cdd4af69ac5e9892
source_type: github
author: Tobias Burnus
headline: Fortran OpenMP module clarifies declare mapper struct member names
tldr: GCC Fortran's OpenMP implementation renames internal struct members for `declare
  mapper` to improve clarity and reduce confusion in user-defined mapper handlin…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gfc_omp_udm` and `gfc_omp_namelist_udm` structs are central to
  GCC's Fortran frontend for managing OpenMP user-defined mappers. The renaming of
  `mapper_id` to `requested_mapper_id` and `usm` to `resolved_usm` within `gfc_omp_namelist_udm`
  addresses a clarity issue where `usm->mapper_id` was conflated with `usm->usm->mapper_id`.
  This is a common pattern for managing distinct "request" and "resolve" states for
  entities found-by-name, ensuring that `requested_mapper_id` stores the identifier
  provided in a `map` clause (e.g., `mapper(my_name)`) and `resolved_usm` points to
  the object created…
primer_general: In scientific and high-performance computing, OpenMP is a popular
  way to make Fortran programs run faster by using parallel processing. A feature
  called `declare mapper` allows programmers to define how complex data structures
  should be handled when moved between different parts of a parallel system, especially
  in GPU computing. Inside the GCC compiler's Fortran part, there are internal data
  structures that manage these user-defined mappers. This update clarifies the names
  of certain fields within these internal structures. Previously, some fields like
  `mapper_id` and `usm` had names that could be confusing, especially when one pointed
  to another with a similar name. By renaming them to `requested_mapper_id` and `resolved_usm`,
  the compiler's code becomes easier to understand and maintain, making it clearer
  which field holds the name specified by the programmer and which holds the actual,
  fully-resolved mapper definition.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eed2ca30e49d8177921e8c01cdd4af69ac5e9892
date: '2026-06-17'
is_stub: false
---

The GCC Fortran frontend's handling of OpenMP `declare mapper` constructs has been refactored for improved code clarity. Previously, internal `gfc_omp_udm` struct members for managing user-defined mappers, such as `mapper_id` and `usm`, caused confusion due to ambiguous naming and nesting. This change renames these to `requested_mapper_id` and `resolved_usm`, with the actual `mapper_id` now clearly residing within `resolved_usm`, making the intent of each member more explicit in the context of OpenMP user-defined mappers.
