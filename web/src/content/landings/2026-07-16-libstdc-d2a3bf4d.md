---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- testing
- bugfix
commit_hash: d2a3bf4da621412d6fb574e117ff6046aaeaabb6
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Disable serialization test for piecewise_linear_distribution<double>
  on i686'
tldr: Serialization test for piecewise_linear_distribution<double> disabled on i686
  due to instability.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: ''
primer_glossary:
- term: piecewise_linear_distribution
  definition: A C++ standard library random number distribution that generates numbers
    following a piecewise linear function. It's used in statistical modeling and simulations.
- term: serialization
  definition: The process of converting an object's state into a format that can be
    stored (e.g., in a file or database) or transmitted (e.g., across a network) and
    reconstructed later.
- term: i686
  definition: A specific 32-bit IA-32 processor architecture. Code compiled for i686
    may exhibit different behavior or stability issues compared to other architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d2a3bf4da621412d6fb574e117ff6046aaeaabb6
date: '2026-07-16'
is_stub: false
stub_reason: ''
---

A test case for serialization of `piecewise_linear_distribution<double>` in libstdc++ has been disabled for the i686 architecture. Previously enabled for both double and float, testing revealed that the double version remains unstable on this architecture. This change aims to prevent test suite regressions while the underlying instability is investigated.
