---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- optimization
- gcc
- memory usage
commit_hash: 0eeecd403f81fce28daca37cdeffce3534ff85c4
source_type: github
author: Andrea Pinski
headline: 'forwprop: Optimize enum types to unsigned char'
tldr: Reduces memory usage in the forward propagation pass by using unsigned char
  for enums.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-forwprop.cc`, the `long_mul_kind` and `long_mul_extract`
  enums are used to represent states and classifications related to scalar multiplication
  within the forward propagation pass. Previously, these enums likely defaulted to
  `int`. This change explicitly sets their underlying type to `unsigned char`, which
  is a smaller data type. This optimization is safe because the observed usage of
  these enums indicates their values will always fit within an `unsigned char`, thus
  reducing memory footprint for data structures that contain them.
primer_glossary:
- term: forwprop
  definition: Abbreviation for forward propagation, an optimization pass in compilers
    that replaces variables with their known values to simplify subsequent computations.
- term: tree-ssa-forwprop.cc
  definition: A source file in GCC that implements the forward propagation optimization
    pass using the Static Single Assignment (SSA) form of the intermediate representation.
- term: enum
  definition: An enumeration, a data type consisting of a set of named integer constants.
    In C++, enums can have different underlying types.
- term: unsigned char
  definition: An integer data type that is typically 8 bits wide and can represent
    values from 0 to 255. It is smaller than a standard 'int'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0eeecd403f81fce28daca37cdeffce3534ff85c4
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

This commit optimizes the storage for two enumerations, `long_mul_kind` and `long_mul_extract`, within the `tree-ssa-forwprop.cc` file. By changing their underlying type from the default `int` to `unsigned char`, the compiler can potentially save space, as these enums are used in contexts where their values are small. This change is considered obvious and has been verified by bootstrapping and testing.
