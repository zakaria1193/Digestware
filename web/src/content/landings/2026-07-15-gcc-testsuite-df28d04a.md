---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- risc-v
- vector extension
- testing
commit_hash: df28d04aa00224116c23c8ba4f2b43350532de68
source_type: github
author: Pan Li
headline: 'RISC-V: Add tests for vwcvt.x.x.v register overlap'
tldr: New RISC-V test cases verify vwcvt.x.x.v instruction behavior with register
  overlap.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds autovectorization test cases for the RISC-V Vector
  extension, specifically targeting the `vwcvt.x.x.v` instruction. These tests exercise
  the instruction's behavior when the destination vector register `vd` overlaps with
  the source vector register `vs2`, a scenario that can be tricky for instruction
  schedulers and register allocators. The tests cover various element widths and vector
  lengths.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/df28d04aa00224116c23c8ba4f2b43350532de68
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

Adds a suite of new test cases to the RISC-V testsuite specifically for the vwcvt.x.x.v instruction. These tests focus on scenarios involving register group overlap, ensuring correct functionality when source and destination registers might coincide.
