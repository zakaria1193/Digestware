---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- OpenACC
- compiler
- runtime
commit_hash: 0dbe46aeaf5c06cbd3deaa833e5ae2150fe67c56
source_type: github
author: Sebastian Galindo
headline: 'Fortran: Add OpenACC init, set, shutdown directives support.'
tldr: Fortran front-end now supports OpenACC init, set, and shutdown directives with
  device clause handling.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch integrates OpenACC's `init`, `set`, and `shutdown` directives
  into the Gfortran compiler. It introduces new built-ins (`BUILT_IN_GOACC_INIT`,
  `_SET_DEVICE`, `_SHUTDOWN`) mapped via `omp-builtins.def` and `builtin-types.def`.
  The Fortran front-end (`gfc_statement`, `gfc_omp_clauses`, `match.h`, etc.) is updated
  to parse these directives and associated clauses, particularly `DEVICE_TYPE` and
  `DEVICE_NUM`, translating them into `libgomp` calls. The `device_type` clause's
  scoping for subsequent directives is noted as a future refactoring target, and `default_async`
  for `set` is deferre…
primer_glossary:
- term: OpenACC
  definition: A directive-based programming model designed to make it easier to specify
    parallel computing tasks, particularly for accelerators like GPUs, using compiler
    directives embedded in source code.
- term: Fortran
  definition: A high-level programming language commonly used for numerical computation
    and scientific computing, known for its performance and suitability for array
    manipulation.
- term: libgomp
  definition: The GNU implementation of the OpenMP runtime library, which provides
    support for parallel programming constructs and management of threads and execution
    environments.
- term: device_type
  definition: An OpenACC clause that specifies the type of accelerator device (e.g.,
    'nvidia', 'amd') to be used for computation.
- term: device_num
  definition: An OpenACC clause that specifies the index of the accelerator device
    to be used when multiple devices of the same type are available.
- term: runtime API
  definition: A set of functions and interfaces provided by a library or system that
    allows a program to interact with the underlying runtime environment, controlling
    aspects like device management, memory allocation, and execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0dbe46aeaf5c06cbd3deaa833e5ae2150fe67c56
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

This extensive commit adds support for OpenACC `init`, `set`, and `shutdown` directives to the Fortran front-end. It includes parsing these directives and generating calls to the `libgomp` runtime library, mirroring existing implementations for other runtime API calls. The change also incorporates support for `device_type` and `device_num` clauses, although `device_type` is currently limited to a single clause per directive.
