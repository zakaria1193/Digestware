---
project: glibc
subsystem: glibc
patch_id: null
tags:
- memory allocation
- glibc
- c standard
- malloc
- wg14
discussion_id: PAWPR08MB898228E093C2022B8DFEE96B832A2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: Request for feedback on WG14 proposal N3849 (alloc_at_least)
headline: Request for feedback on WG14 proposal N3849 (alloc_at_least)
tldr: Wilco Dijkstra argues that the alloc_at_least proposal adds complexity without
  significant benefit, as realloc already handles similar optimizations.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: 4
technical_tradeoffs:
- Increased allocator complexity vs. potential performance gains in specific scenarios.
- Standardization of new allocator APIs vs. reliance on existing `realloc` optimization.
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: other
  position: Argues that the `alloc_at_least` proposal adds unnecessary complexity
    because realloc already handles similar optimizations.
  quote: All it does is avoid a call to realloc when it fits in the allocated size.
    However realloc already does this optimization, so I don't see how it helps.
- author: Paul Eggert <eggert@cs.ucla.edu>
  role: other
  position: Suggests that the proposal lacks clear evidence of practical efficiency
    improvements, making the cost/benefit ratio questionable.
  quote: "Although the proposal's main motivation is runtime efficiency, it \ndoesn't\
    \ say what sort of efficiency improvements are likely in practice, \nso I can\
    \ see an argument that it's not worth the complexity."
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: other
  position: States he didn't find any clear motivation about performance in the proposal.
  quote: "I didn't find a clear motivation about performance in the proposal.\nHowever\
    \ realloc is *fast* if the size fits or is a little smaller: it takes \nless than\
    \ 5 cycles on a mod"
- author: Florian Weimer <fweimer@redhat.com>
  role: other
  position: Points out that without knowing the allocator's internals, it's difficult
    to determine which realloc arguments are fast or which malloc arguments result
    in unused slack.
  quote: 'If you don''t know the allocator internals, you can''t tell which realloc

    arguments are actually fast (or which arguments to malloc produce zero

    unused slack).'
- author: Paul Eggert <eggert@cs.ucla.edu>
  role: other
  position: Argues about the need for realistic applications.
  quote: "Clearly the main motivation for the proposal is performance, as realloc\
    \ \nalready provides the functionality needed for correctness. So, "
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: other
  position: Suggests to write nano benchmarks/tests to find out more.
  quote: 'You can write nano benchmarks/tests like I did to get the above stat. It''s
    easy

    to figure out m'
primer_expert: This discussion concerns WG14 proposal N3849, which introduces new
  allocator APIs like `alloc_at_least`. Arguments revolve around whether these additions
  provide tangible benefits over existing features of glibc's malloc, specifically
  realloc's ability to efficiently manage memory resizing.
primer_general: Memory allocation in programming is managed by functions like malloc
  and realloc. This discussion centers around a proposal to add a new function, alloc_at_least,
  to the C standard library for memory allocation. The core question is whether this
  new function offers advantages over the existing realloc function, which already
  optimizes memory resizing operations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB898228E093C2022B8DFEE96B832A2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-23'
---

Charles Munger requested feedback on WG14 proposal N3849, which introduces a new allocator API `alloc_at_least`. Wilco Dijkstra argues that the proposal's benefits are minimal because `realloc` already incorporates optimizations that achieve similar results. He questions the value of requesting slightly larger blocks when `realloc` can efficiently handle resizing.
