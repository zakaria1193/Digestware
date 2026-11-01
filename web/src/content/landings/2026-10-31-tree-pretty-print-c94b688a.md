---
project: gcc
subsystem: tree-pretty-print
patch_id: null
tags:
- lto
- c++
- debugging
commit_hash: c94b688a83fc84015c6fab8ab0ff142051598fc8
source_type: github
author: Stefan Schulze Frielinghaus
headline: Improve LTO type printing by handling NULLPTR_TYPE
tldr: GCC's LTO pretty-printer now correctly displays nullptr_t types, resolving obscure
  error messages.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In LTO builds, `lto1` relies on the generic tree pretty printer to
  serialize and display type information. This commit improves `dump_generic_node`
  in `tree-pretty-print.cc` by adding a case for `NULLPTR_TYPE`. Previously, this
  would hit `do_niy()`, leading to less informative output. The fix ensures that `nullptr_t`
  types are displayed more accurately, although perfect consistency with C++ front-end
  typedef rendering might still require further work.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization is a compiler optimization technique that performs
    optimizations across multiple object files during the linking phase, rather than
    solely within individual compilation units.
- term: lto1
  definition: The GCC driver program responsible for performing Link-Time Optimization.
    It reads intermediate representations from multiple object files and applies optimizations
    before final linking.
- term: generic tree
  definition: GCC's internal intermediate representation (IR). The generic tree describes
    the program's structure and semantics in a way that is largely independent of
    the source language and target architecture.
- term: pretty printer
  definition: A tool or function that formats data structures or code into a human-readable
    representation. In this context, it's used to display GCC's internal tree representation.
- term: NULLPTR_TYPE
  definition: GCC's internal representation for the C++ `nullptr_t` type, which represents
    a null pointer constant.
- term: do_niy
  definition: A GCC internal function that signifies 'Do Nothing Yet' or an unimplemented
    operation. Hitting this often indicates a missing case in the compiler's internal
    logic.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c94b688a83fc84015c6fab8ab0ff142051598fc8
date: '2026-10-31'
is_stub: true
stub_reason: low_score
---

The GCC Link-Time Optimization (LTO) process uses a generic tree pretty printer to display type information when front-end information is unavailable. Previously, it did not handle `NULLPTR_TYPE`, causing it to fall back to a generic 'unknown tree' message. This commit adds specific handling for `NULLPTR_TYPE`, similar to other `_TYPE` cases, resulting in more informative output like mentioning `nullptr_t`. Minor inconsistencies may remain compared to non-LTO builds due to typedef handling in the C++ front-end.
