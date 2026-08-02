---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- vector
- testing
commit_hash: a6ceb8bca802db02edddbebfe2dbf589e5710fc5
source_type: github
author: Pan Li
headline: 'RISC-V: Add test cases for vwadd.vv with register overlap'
tldr: Adds test cases for RISC-V vwadd.vv instruction to ensure correct handling of
  register group overlap.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds test coverage for register overlap in RISC-V Vector
  extension instructions, specifically `vwadd.vv`. The tests target scenarios where
  the destination register group for the `vwadd.vv` instruction might overlap with
  source register groups, particularly when `csrr` is used and overlap is enabled.
primer_glossary:
- term: RISC-V Vector extension
  definition: An extension to the RISC-V instruction set architecture that provides
    single instruction, multiple data (SIMD) capabilities for efficient vector processing.
- term: vwadd.vv
  definition: A RISC-V vector instruction that performs a widened addition of two
    vector registers into a destination vector register, with both source and destination
    registers being vector registers.
- term: register overlap
  definition: A condition in vector processing where the destination registers for
    an instruction's results may overlap with the source registers being read in the
    same instruction. This requires careful handling to avoid data corruption.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a6ceb8bca802db02edddbebfe2dbf589e5710fc5
date: '2026-07-31'
is_stub: true
stub_reason: low_score
---

This commit introduces a new test case for the RISC-V vwadd.vv instruction, specifically addressing scenarios where register groups overlap. The test ensures proper functionality when the `csrr` instruction is used without assembly and overlap is enabled. This complements existing tests for register overlap in related vector operations.
