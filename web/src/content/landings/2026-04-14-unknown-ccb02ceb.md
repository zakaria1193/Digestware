---
project: gcc
subsystem: unknown
patch_id: null
commit_hash: ccb02ceb86c5b9d4f2139f6c73a6660bda4a5b1f
source_type: github
author: H.J. Lu
impact_score: 5
performance_win: false
breaking_change: false
discussion_id_link: null
bugzilla_pr: null
url: https://github.com/gcc-mirror/gcc/commit/ccb02ceb86c5b9d4f2139f6c73a6660bda4a5b1f
date: '2026-04-14'
---

x86: Zero ZMM16-31 when zeroing all call used registers

When zeroing all call used registers with AVX512F enabled, zero ZMM16-31
explicitly since vzeroall doesn't touch ZMM16-31.  Also add a test for
