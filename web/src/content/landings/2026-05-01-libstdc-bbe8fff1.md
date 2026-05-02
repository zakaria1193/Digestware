---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- documentation
- simd
commit_hash: bbe8fff16e366976bd95b981c138e5f12caf9010
source_type: github
author: Jonathan Wakely
headline: Tweak Doxygen Comments for Experimental SIMD
tldr: This commit improves Doxygen documentation generation for the experimental SIMD
  features in libstdc++ by adjusting macro definitions and comment placement.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The libstdc++ uses Doxygen to generate API documentation. The `<experimental/simd>`
  header defines the `_GLIBCXX_SIMD_BEGIN_NAMESPACE` and `_GLIBCXX_SIMD_END_NAMESPACE`
  macros to encapsulate the `std::experimental::parallelism_v2` namespace. This commit
  adjusts the Doxygen configuration and the placement of these macros to ensure correct
  documentation generation, working around a potential Doxygen issue.
primer_general: Doxygen is a tool used to automatically generate documentation from
  source code. SIMD (Single Instruction, Multiple Data) is a technique that allows
  processors to perform the same operation on multiple data points simultaneously,
  improving performance for certain types of calculations. This commit improves the
  documentation generated for the SIMD features in the C++ standard library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbe8fff16e366976bd95b981c138e5f12caf9010
date: '2026-05-01'
---

This commit improves the Doxygen documentation for the experimental SIMD (Single Instruction, Multiple Data) features in libstdc++. It defines Doxygen macros for the SIMD namespace and adjusts the placement of these macros and Doxygen comments in the `<experimental/simd>` header. This ensures that the SIMD components are correctly documented within the `std::experimental::parallelism_v2` namespace.
