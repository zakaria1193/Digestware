---
project: gcc
subsystem: c++/modules+reflection
patch_id: null
tags:
- c++
- modules
- reflection
- bugfix
commit_hash: 7802275c29d3c301c6f168ef1098a38494a0e836
source_type: github
author: Patrick Palka
headline: 'C++ Modules: Handle typedef struct { } A with reflection'
tldr: Fixes module merging for typedefs to unnamed types when reflection is enabled.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC C++ frontend's module implementation (``module.cc``) now correctly
  merges typedefs to unnamed types when the ``-freflection`` option is used, addressing
  a regression introduced by r16-7903. The patch specifically handles the case where
  the unnamed type declaration exists but is not visible to name lookup, ensuring
  that the merge proceeds correctly.
primer_general: C++ modules are a way to organize code into reusable units, improving
  dependency management. Reflection is a feature that allows a program to inspect
  and modify its own structure and behavior at runtime.  When modules and reflection
  are combined, the compiler needs to handle the interaction between these features
  correctly, including the merging of type declarations across module boundaries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7802275c29d3c301c6f168ef1098a38494a0e836
date: '2026-04-29'
---

GCC's C++ module merging had issues with typedefs to unnamed types (e.g., ``typedef struct { } A``) when reflection was enabled.  A recent change modified the representation of such typedefs, and this patch updates the module merging logic to handle this new representation correctly. This ensures that the unnamed decl is properly handled, even though it isn't visible to name lookup, resolving a merge failure. New test cases are added.
