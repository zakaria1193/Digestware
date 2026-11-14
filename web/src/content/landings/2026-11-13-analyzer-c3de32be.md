---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- integer
- type safety
commit_hash: c3de32be053db1156e4e5fbc87143f93f5345e8d
source_type: github
author: David Malcolm
headline: Analyzer gains arbitrary-precision integer types
tldr: New integer classes for the analyzer's state tracking will improve type safety
  and support arbitrary precision.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC analyzer is introducing new C++ classes in `analyzer/integer.h`,
  `analyzer/integer-with-unit.h`, and `analyzer/concrete-ranges.h`. These leverage
  `libgmp` for arbitrary-precision arithmetic and aim to improve type safety and range
  tracking within the analyzer's state representation, particularly for upcoming rewrites
  targeting concretely-known endpoints.
primer_glossary:
- term: arbitrary-precision integer
  definition: An integer type that can store integers of any size, limited only by
    available memory, unlike fixed-size types (e.g., int32, int64).
- term: GCC analyzer
  definition: A static analysis component within GCC that inspects code without executing
    it, aiming to find bugs and provide information about program behavior.
- term: type safety
  definition: A property of programming languages where the type system prevents operations
    that are not well-defined for the given types, reducing runtime errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c3de32be053db1156e4e5fbc87143f93f5345e8d
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

The GCC analyzer has gained a new arbitrary-precision integer class that wraps libgmp's mpz_t. This forms the basis for a new unit-safe integer type that captures units like bits or bytes in the type system, preventing mismatches at compile time. Additionally, a concrete range class for these integers has been introduced. While not yet used, these foundational classes are intended to support an upcoming rewrite of the analyzer's state-tracking logic.
