---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- memcmp
- optimization
- sve
- kunpeng 950
discussion_id: 20260424035025.574-1-yeweihong@huawei.com
source_type: public_inbox
title: 'Ping:[PATCH v2] aarch64: Optimize memcmp for Kunpeng 950 with SVE'
headline: 'Ping:[PATCH v2] Aarch64: Optimize memcmp for Kunpeng 950 with SVE'
tldr: Pings the list for feedback on a patch optimizing memcmp for Kunpeng 950 with
  SVE.
proposer: Weihong Ye <yeweihong@huawei.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased code complexity vs. potential performance gains on specific hardware.
- May require compiler support for SVE instructions.
exchanges: []
primer_expert: This patch optimizes `memcmp` for the aarch64 architecture, specifically
  the Kunpeng 950 processor, by utilizing SVE instructions. SVE allows for vectorization
  of the comparison, potentially improving performance when comparing large memory
  regions.
primer_general: '`memcmp` is a standard C library function used to compare two blocks
  of memory. This patch aims to improve the performance of `memcmp` on a specific
  ARM-based processor (Kunpeng 950) by using advanced CPU instructions (SVE) that
  can process multiple data elements simultaneously.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260424035025.574-1-yeweihong@huawei.com
bugzilla_url: null
date: '2026-04-24'
---

Weihong Ye is requesting feedback on a patch that optimizes the `memcmp` function for the Kunpeng 950 processor using Scalable Vector Extension (SVE) instructions. The patch was originally posted on April 17th, and the author is seeking reviews and comments.
