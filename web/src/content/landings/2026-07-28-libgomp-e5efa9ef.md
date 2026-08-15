---
project: gcc
subsystem: libgomp
patch_id: null
tags:
- libgomp
- fortran
- gfortran
- configure
commit_hash: e5efa9eff99da897f0bbd69455d8f7856985b2db
source_type: github
author: Thomas Schwinge
headline: 'Libgomp: Revise Fortran support conditionals'
tldr: Correctly enables libgomp/Fortran support when Gfortran is pre-installed.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Previous commits (r152931, r156232, r156264) correctly disabled libgomp/Fortran
  support when `--enable-languages=fortran` was not specified. However, these changes
  broke detection for a pre-installed Gfortran, causing support to remain disabled.
  This patch revises the `libgomp/Fortran` support conditionals to correctly handle
  both scenarios: building Gfortran internally and using an externally provided Gfortran.
  It addresses issues where the `test -x` check in `configure.ac` failed for Gfortran
  found via `PATH` and ensures that libgomp/Fortran support is only disabled when
  Fortran is definiti…'
primer_glossary:
- term: libgomp
  definition: The GCC runtime library for OpenMP. It provides the necessary functions
    to support parallel execution directives in C, C++, and Fortran programs.
- term: OpenMP
  definition: An API that supports multi-platform shared-memory parallel programming
    in C, C++, and Fortran. It consists of compiler directives, library routines,
    and environment variables.
- term: pre-installed
  definition: In the context of GCC builds, this refers to a situation where a component,
    such as the Gfortran compiler, is already installed on the system and is being
    used by the current GCC build process, rather than being built from source as
    part of the GCC tree.
- term: configure.ac
  definition: A file used by the Autoconf tool to generate a `configure` script. This
    script checks the system environment and available tools to prepare the source
    code for compilation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e5efa9eff99da897f0bbd69455d8f7856985b2db
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

This commit revises the conditional logic for building libgomp's Fortran support. Previous changes correctly disabled this support when Fortran was not enabled during GCC configuration. However, these changes inadvertently prevented support from being enabled when Gfortran was pre-installed (provided externally). This update ensures that libgomp's Fortran support is correctly enabled in configurations with a pre-installed Gfortran, aligning with the expected behavior and fixing issues discussed in related bug reports and patches.
