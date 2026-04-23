---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- memcmp
- SVE
- optimization
- kunpeng950
discussion_id: 20260417082427.118-1-yeweihong@huawei.com
source_type: public_inbox
title: '[PATCH v2] aarch64: Optimize memcmp for Kunpeng 950 with SVE'
headline: Optimize memcmp for Kunpeng 950 with SVE
tldr: This patch optimizes memcmp for the Kunpeng 950 using SVE, resulting in 15%
  - 50% speedups for small to large inputs.
stakes: This improves the performance of memcmp on AArch64 systems using the Kunpeng
  950 processor, benefiting applications that rely heavily on memory comparison operations.
proposer: Weihong Ye <yeweihong@huawei.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: Positive benchmark results and addressed review comments indicate
  a good direction.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417082427.118-1-yeweihong@huawei.com
bugzilla_url: null
date: '2026-04-17'
---

The patch optimizes memcmp for the Kunpeng 950 by using SVE predication, 4-way loop unrolling, and optimized mismatch detection. It uses cntb instead of rdvl and mul vl addressing based on review feedback. Benchmarks show significant speedups, but regressions may occur near 4K boundaries.
