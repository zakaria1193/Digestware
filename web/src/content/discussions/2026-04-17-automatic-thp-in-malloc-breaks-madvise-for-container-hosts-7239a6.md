---
project: glibc
subsystem: malloc
patch_id: null
tags:
- malloc
- THP
- containers
- performance
- madvise
discussion_id: 63944439-C902-4C74-8D6C-03631A610DCB@amazon.com
source_type: public_inbox
title: 'RFC: malloc automatic THP opt-in breaks madvise contract for container hosts'
headline: Automatic THP in malloc breaks madvise for container hosts
tldr: Glibc's automatic THP opt-in via madvise hurts container hosts by allocating
  huge pages to small management processes instead of actual workloads.
stakes: Unexpected THP usage can degrade performance in containerized environments,
  wasting memory on shims instead of benefiting the intended applications.
proposer: Sun, Yutong <yutongsu@amazon.com>
consensus: Proposed
outcome: proposed
sentiment_score: 4
sentiment_rationale: The RFC identifies a performance regression in a specific use
  case (container hosts), which can lead to contention.
  container environments.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/63944439-C902-4C74-8D6C-03631A610DCB@amazon.com
bugzilla_url: null
date: '2026-04-17'
---

Yutong Sun raises concerns about glibc's automatic Transparent Huge Pages (THP) opt-in behavior via `madvise(MADV_HUGEPAGE)` for heap allocations. This breaks the intended semantics of `madvise` mode where applications explicitly opt-in. On container hosts, this leads to small management processes (container shims) receiving huge page allocations, while actual container workloads do not, wasting memory. The author proposes either reverting the change or making THP usage opt-in.
