---
project: glibc
subsystem: glibc
patch_id: null
tags:
- THP
- performance
- memory
- linker
- properties
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: '[RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Propose Fine-Grained THP Control via GNU Properties
tldr: Adds GNU properties to allow per-application control of Transparent Huge Pages
  (THP) on read-only segments and in malloc.
stakes: THP can improve performance but also cause latency spikes and memory waste;
  this proposal gives developers more control.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: Some concern about the naming of the new properties.
technical_tradeoffs:
- Adding new GNU properties increases complexity but provides finer-grained control.
- Opting into THP can improve performance in some cases but may degrade it in others.
- The `NEEDED` suffix is questioned; alternatives are `OPTIONAL`, `DESIRED`, or no
  suffix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

H.J. Lu proposes adding `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` and `GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC` to allow applications to opt-in to THP usage. The goal is to give developers more control over THP, which has trade-offs, especially for databases.  The naming of the properties is under debate.
