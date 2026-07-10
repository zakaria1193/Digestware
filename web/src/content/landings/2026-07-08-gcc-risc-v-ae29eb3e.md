---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- testsuite
- vector extension
commit_hash: ae29eb3e2d4efeb4175060582d9eb665ff1813d2
source_type: github
author: Pan Li
headline: RISC-V test case adjusted for vf[sz]ext.vf4 overlap
tldr: RISC-V test cases removed XFAIL markers due to changes in vf[sz]ext.vf4 behavior.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Test cases `gcc.target/riscv/rvv/base/pr112431-16.c` and `pr112431-17.c`
  no longer require xfail markers. This adjustment reflects changes in the RISC-V
  Vector extension handling of `vf4` instructions, specifically related to register
  overlap scenarios for `vfsext.vf4` and `vzext.vf4`.
primer_glossary:
- term: vf[sz]ext.vf4
  definition: RISC-V Vector extension instructions for type-widening vector element
    extraction. '.vf4' indicates the operation affects four vector elements.
- term: xfail
  definition: A marker in test suites indicating that a test is expected to fail due
    to a known bug or limitation. Removing it signifies the underlying issue has been
    addressed or the test condition has changed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ae29eb3e2d4efeb4175060582d9eb665ff1813d2
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit removes the 'xfail' markers from two RISC-V test cases, `pr112431-16.c` and `pr112431-17.c`. The removal is a consequence of adjustments made to handle potential overlaps in the `vf[sz]ext.vf4` instructions.
