---
project: glibc
subsystem: glibc
patch_id: null
tags:
- tunables
- configuration
- ldconfig
- performance
discussion_id: cover.1776449736.git.dj@redhat.com
source_type: public_inbox
title: '[PATCH v7 0/4] Add system-wide tunables'
headline: Add system-wide tunables
tldr: This series introduces system-wide tunables configurable via /etc/tunables.conf,
  allowing administrators to adjust glibc behavior per-process.
stakes: This feature could impact application performance and resource utilization
  by allowing administrators to fine-tune glibc's behavior without recompilation.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch series has gone through several revisions, indicating
  active development and refinement.
  but may constrain the design.
series_id: glibc:add system-wide tunables
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/cover.1776449736.git.dj@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

This patch series implements system-wide tunables for glibc. It reads tunable configurations from /etc/tunables.conf using ldconfig, stores them in /etc/ld.so.cache, and applies them to running applications. The configuration supports per-process overrides. This is version 7 of the patch.
