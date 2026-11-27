---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- testsuite
- fix
commit_hash: bc49f1e3701490e2293e8d3a363f30b0a2369274
source_type: github
author: mengqinggang
headline: LoongArch32 test failures fixed
tldr: Adjustments to LoongArch test suite resolve failures on LA32 and specify target
  requirements.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses testsuite failures on LoongArch32. It correctly
  marks an ICE for LA32 and adjusts test case configurations, including target requirements
  and file locations, to ensure correct execution and prevent misruns on incompatible
  architectures. Specifically, it modifies testsuite configurations for ICE reporting
  and architecture-specific test execution.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bc49f1e3701490e2293e8d3a363f30b0a2369274
date: '2026-11-24'
is_stub: true
stub_reason: low_score
---

Several test failures on LoongArch32 have been resolved. The `expand_expr_addr_expr_1` ICE is now correctly marked as expected to fail (XFAIL) for LA32. Additionally, the `loongarch_asx` target is now required for a specific LASX-only test, and two `bstrins` tests have been moved to prevent them from running on LA32.
