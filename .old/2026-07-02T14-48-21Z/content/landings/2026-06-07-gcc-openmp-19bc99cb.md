---
project: gcc
subsystem: gcc/openmp
patch_id: null
tags:
- openmp
- compiler-internals
- refactoring
commit_hash: 19bc99cb9c0f85da79bee41fabf40461b64d2cd1
source_type: github
author: Kwok Cheung Yeung
headline: 'OpenMP: Add macros for iterator element access'
tldr: New macros and constructor functions simplify access and manipulation of OpenMP
  iterator elements across C, C++, and Fortran compilers.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces new macros (OMP_ITERATOR_VAR, OMP_ITERATOR_BEGIN,
  etc.) and constructors (make_omp_iterator) within tree.h to manage OMP_ITERATOR
  nodes uniformly. These changes impact various compiler passes including parsing
  in c-parser.cc and parser.cc, gimplification in gimplify.cc, and Fortran lowering
  in trans-openmp.cc. The goal is to abstract the direct manipulation of TREE_LIST
  structures representing OpenMP iterators, moving towards a more robust and type-safe
  access pattern. This refactoring does not alter the generated code or ABI, but rather
  the internal representation hand…
primer_general: When you write OpenMP code to parallelize loops, the compiler needs
  to understand how to break down and manage the loop iterations. This involves creating
  internal representations, called 'iterators,' that describe the start, end, and
  step of a loop. This change within the GCC compiler introduces new helper functions
  and macros that make it easier for different parts of the compiler (like the C,
  C++, and Fortran language frontends, or the internal code optimizer) to work with
  these iterators. Previously, each part might have handled iterator details slightly
  differently, leading to potential inconsistencies or harder-to-read code. By providing
  a unified way to access and create these iterators, the compiler becomes more robust
  and easier for developers to maintain and extend in the future, without changing
  how your OpenMP programs behave at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/19bc99cb9c0f85da79bee41fabf40461b64d2cd1
date: '2026-06-07'
is_stub: false
---

This update introduces a set of macros and constructors to standardize how OpenMP iterator elements are accessed and constructed within the GCC compiler. By centralizing these operations, the change improves code readability and maintainability for OpenMP-related features in C, C++, and Fortran frontends, as well as in the core GCC gimplifier and tree inliner. This refactoring streamlines future development and debugging of OpenMP support.
