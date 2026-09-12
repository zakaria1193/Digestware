---
project: gcc
subsystem: libgomp.texi
patch_id: null
tags:
- libgomp
- documentation
- openmp
- fortran
commit_hash: 9e55aa415ea90bcef8033892f6381402cb90b163
source_type: github
author: Tobias Burnus
headline: Libgomp documentation updated for omp_control_tool routine.
tldr: Libgomp documentation now includes a note and example for calling omp_control_tool
  with arguments from Fortran.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The libgomp documentation in `libgomp.texi` has been augmented with
  a note and example for the `omp_control_tool` function, specifically illustrating
  its invocation from Fortran with arguments. This aims to clarify the usage for Fortran
  developers interacting with OpenMP tools via `omp_control_tool`.
primer_glossary:
- term: libgomp
  definition: The OpenMP runtime library for GCC, providing support for parallel programming
    constructs defined by the OpenMP standard.
- term: omp_control_tool
  definition: An OpenMP routine that allows an application to control and communicate
    with attached tools, such as debuggers or performance analysis tools, during runtime.
- term: Fortran
  definition: A high-level programming language primarily used for scientific and
    engineering applications, known for its performance in numerical computation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9e55aa415ea90bcef8033892f6381402cb90b163
date: '2026-09-11'
is_stub: true
stub_reason: low_score
---

The documentation for the libgomp library has been updated to include a note regarding the `omp_control_tool` routine. Specifically, it now provides an example demonstrating how to call this routine with a passed argument from a Fortran program, improving usability for developers integrating libgomp with Fortran code.
