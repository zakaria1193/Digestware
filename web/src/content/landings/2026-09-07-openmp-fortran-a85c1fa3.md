---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- fortran
- OpenMP
- directives
- parser
commit_hash: a85c1fa3d82221748329b7f7dda329ba8fa22d04
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Support underscore variants of directive names'
tldr: Fortran now supports multi-word OpenMP directive names with underscores.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Fortran parser in `gcc/fortran/parse.cc` has been updated to decode
  underscore variants of multi-word OpenMP directive names. This complements existing
  support for space-separated variants. The changes ensure compliance with newer OpenMP
  standards that introduced these alternative spellings for directives like `declare_mapper`,
  `declare_reduction`, `target_data`, etc. Libgomp's implementation status documentation
  is also updated.
primer_glossary:
- term: OpenMP
  definition: A standard API for supporting shared-memory parallel programming on
    architectures like multicore processors and GPUs.
- term: Fortran
  definition: A high-level programming language commonly used for scientific and numerical
    computation.
- term: directive
  definition: A special command or instruction in OpenMP that controls the behavior
    of parallel execution, such as creating threads or distributing work.
- term: libgomp
  definition: The GNU implementation of OpenMP, providing runtime support for parallel
    programming constructs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a85c1fa3d82221748329b7f7dda329ba8fa22d04
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

Fortran support for OpenMP has been extended to recognize multi-word directive names that use underscores, aligning with the OpenMP specification. This includes directives such as `declare_mapper`, `target_data`, and `cancellation_point`. The changes involve updates to the Fortran parser and libgomp documentation, with new test cases added to verify the functionality.
