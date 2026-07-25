---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- c++
- cleanup
commit_hash: b37ace0e98ded690b4392e65487f3a9d2120e76e
source_type: github
author: Kael Andrew Alonzo Franco
headline: Remove ENUM_BITFIELD uses.
tldr: GCC removes deprecated macro ENUM_BITFIELD, aligning with C++14 enum support.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit removes redundant uses of the ENUM_BITFIELD macro, which
  was a pre-C++14 mechanism for defining bitfields for enums. Modern C++ handles this
  directly. The macro was used in various internal structs like `c_common_resword`,
  `cp_declspecs`, `cgraph_node`, and `rtx_def`. This cleanup simplifies internal compiler
  data structures and removes dead code.
primer_glossary:
- term: ENUM_BITFIELD
  definition: A deprecated GCC macro used to enable bit-field storage for C++ enumeration
    types before C++14 support was complete. Modern C++ handles this directly.
- term: C++14
  definition: A revision of the C++ programming language standard, published in 2014.
    It introduced features like generic lambdas, digit separators, auto lambda parameters,
    and improved support for constexpr.
- term: middle-end
  definition: The part of the compiler that performs optimizations and transformations
    on an intermediate representation (IR) of the code, after the frontend has parsed
    the source code and before the backend generates machine code.
- term: struct cgraph_node
  definition: An internal GCC data structure representing a node in the call graph,
    used for analyzing function call relationships and performing inter-procedural
    optimizations.
- term: rtx_def
  definition: The fundamental data structure in GCC's internal representation (RTL
    - Register Transfer Language), representing an expression or instruction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b37ace0e98ded690b4392e65487f3a9d2120e76e
date: '2026-07-25'
is_stub: true
stub_reason: low_score
---

GCC consolidates its internal representation by removing the use of the deprecated ENUM_BITFIELD macro. This change aligns the compiler with C++14 standards, which fully support enum bitfields. The removal affects various internal structures across the middle-end and core compiler components, simplifying the codebase.
