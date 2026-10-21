---
project: gcc
subsystem: gimple-range-fold
patch_id: null
tags:
- c++
- optimization
- gimple
commit_hash: 04781c88dc80b5dd33264939b389090f6b6cc2bc
source_type: github
author: Jakub Jelinek
headline: C++ PMF types handled in gimple-range-fold
tldr: Fixes gimple-range-fold to correctly handle C++ pointer-to-member-function types.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adjusts the `accumulate_range_from_component_ref` function
  in `gimple-range-fold.cc` to accommodate C++'s handling of pointer-to-member-function
  (PMF) types. The C++ frontend may generate multiple `RECORD_TYPE`s for PMFs that
  are canonicalized to the same type. The original code relied on exact `FIELD_DECL`
  pointer equality, which failed when the frontend produced different `FIELD_DECL`s
  for canonically equivalent types. The fix introduces a fallback mechanism using
  bit offsets and sizes when `TYPE_CANONICAL` matches but `FIELD_DECL` pointers differ,
  preventing incorrect optimizat…
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation for code during optimization. It's a three-address
    code form that simplifies analysis and transformation.
- term: Pointer-to-Member-Function (PMF)
  definition: A C++ type that represents a pointer to a member function of a class.
    It's distinct from a regular function pointer as it needs to be associated with
    an object of the class.
- term: RECORD_TYPE
  definition: An internal GCC representation for C/C++ structs and classes.
- term: TYPE_CANONICAL
  definition: A GCC internal mechanism that identifies equivalent types, even if they
    are represented differently in the compiler's internal structures.
- term: FIELD_DECL
  definition: Represents a field (member) within a structure or class.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/04781c88dc80b5dd33264939b389090f6b6cc2bc
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

Recent changes to `gimple-range-fold.cc` caused issues with C++ pointer-to-member-function (PMF) types. The compiler's frontend can create distinct RECORD_TYPEs for these, even if they are canonically equivalent. This patch modifies `accumulate_range_from_component_ref` to fall back to bit offset and size comparisons when field declarations and constructors use canonically compatible but not identical aggregate types, resolving mismatches and a new test case.
