---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- rs6000
- powerpc
- mma
commit_hash: 6098abe39da8573bb1412f1e1a7ffde6ecebbe4d
source_type: github
author: Avinash Jayakar
headline: Split rs6000 mma tests by dense math version
tldr: Granularizes rs6000 mma test cases into dense vs. non-dense math configurations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The testsuite for GCC''s rs6000 target has been refactored to explicitly
  separate test cases exercising MMA instructions into two groups: those that rely
  on dense math capabilities and those that do not. This involves renaming and segregating
  tests which previously might have been conflated, using specific compiler flags
  like `-mno-dense-math` and specific `*_compile_ok` macros to establish the desired
  test environment for each subset. This aims to improve the clarity and accuracy
  of the test suite''s coverage of MMA features across different Power ISA profiles.'
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6098abe39da8573bb1412f1e1a7ffde6ecebbe4d
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

Test cases for the rs6000 architecture's MMA (Matrix Multiply Accumulate) functionality have been split to specifically target dense math (dmf) and non-dense math (nodmf) compiler options. This change separates tests, using `-mno-dense-math` for nodmf and `powerpc_future_compile_ok` for dmf, to ensure more precise testing of MMA behavior under different floating-point instruction set configurations.
