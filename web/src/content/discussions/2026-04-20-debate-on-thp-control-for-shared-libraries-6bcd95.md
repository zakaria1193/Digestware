---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- THP
- shared libraries
- performance
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Debate on THP control for shared libraries
tldr: Jan Beulich questions H.J. Lu's proposal to use the main executable to control
  Transparent Huge Page (THP) behavior for shared libraries.
stakes: This discussion concerns the control and configuration of Transparent Huge
  Pages (THP), which can impact application performance and memory usage.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: Discussion involves disagreement and questioning of the proposed
  approach.
technical_tradeoffs:
- Centralized vs. decentralized control of THP behavior.
- Potential performance improvements vs. application compatibility issues with THP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

Jan Beulich is questioning H.J. Lu's proposal to add `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` to allow applications to opt-in to THP usage on read-only segments. Beulich argues that each binary, including shared libraries, should have its own control over THP behavior, rather than being dictated by the main executable. Lu counters that library developers often don't know how THP will affect application performance.
