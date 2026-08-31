---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- documentation
- parallel programming
commit_hash: a5ad8aa6077b1e68d93b41517da5f1c450133df3
source_type: github
author: Gerald Pfeifer
headline: 'libstdc++: Update reference to openDPL Parallel API'
tldr: Documentation updated to reflect changes in the openDPL Parallel API.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the status documentation for C++17 and C++20 in
  libstdc++, specifically concerning references to the openDPL Parallel API. This
  likely involves aligning the library's documentation with the latest API specifications
  or changes in the openDPL library.
primer_glossary:
- term: libstdc++
  definition: The C++ Standard Library implementation used by GCC. It provides core
    language features like containers, algorithms, and I/O streams.
- term: openDPL Parallel API
  definition: Likely refers to an API for parallel programming provided by the Open
    Deep Programming Language (openDPL) or a similar framework, integrated or referenced
    within the C++ standard library documentation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a5ad8aa6077b1e68d93b41517da5f1c450133df3
date: '2026-08-30'
is_stub: true
stub_reason: low_score
---

This commit updates documentation within `libstdc++` to reflect recent changes or clarifications regarding the openDPL Parallel API. The updates affect the C++17 and C++20 status documents and require regeneration of the HTML status page.
