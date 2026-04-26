---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- malloc
- WG14
- performance
- standards
discussion_id: 9eda20a2-2b4b-431b-a41f-5a1a6233066f@cs.ucla.edu
source_type: public_inbox
title: 'Re: Request for feedback on WG14 proposal N3849 (alloc_at_least)'
headline: Request for feedback on WG14 proposal N3849 (alloc_at_least)
tldr: Questions whether the proposed alloc_at_least API has realistic performance
  measurements to support its adoption.
proposer: Paul Eggert <eggert@cs.ucla.edu>
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Paul Eggert
  role: other
  position: Raises concerns regarding the lack of performance figures supporting the
    adoption of alloc_at_least.
  quote: Since the main motivation for the proposal is performance, it would be helpful
    to have realistic measurements to see what the performance effects are in practice.
    Otherwise we're kinda in the dark about the proposal's costs and benefits.
primer_expert: This discussion is about the `alloc_at_least` proposal to the C standard
  and its potential performance impact on glibc. The core of the issue is whether
  the proposed API provides measurable benefits in realistic applications versus microbenchmarks,
  and whether it might negatively impact existing applications. The discussion revolves
  around the performance tradeoffs of different malloc implementations.
primer_general: The `alloc_at_least` proposal is a suggestion to add a new function
  to the C standard library for allocating memory. Paul raises a point about whether
  it actually makes programs faster in real-world scenarios. He cautions that changes
  to core functions like memory allocation should be carefully evaluated to ensure
  they truly improve performance and don't negatively impact existing software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/9eda20a2-2b4b-431b-a41f-5a1a6233066f@cs.ucla.edu
bugzilla_url: null
date: '2026-04-24'
---

Paul Eggert questions the performance claims of the WG14 proposal N3849 (`alloc_at_least`), noting the lack of realistic performance measurements from real-world C applications.  He raises concerns that the change might optimize rewritten applications but worsen performance for unmodified applications due to increased complexity in memory allocation.
