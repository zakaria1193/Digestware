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
discussion_id: CAHktk4jfh9qqipNs2V9_5fU7vK11_g-c_tUCafUG+yv7ZQL1CQ@mail.gmail.com
source_type: public_inbox
title: 'Re: Request for feedback on WG14 proposal N3849 (alloc_at_least)'
headline: Request for feedback on WG14 proposal N3849 (alloc_at_least)
tldr: Florian Weimer provides feedback on WG14 proposal N3849 (alloc_at_least), questioning
  its utility with glibc's malloc implementation.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 5
technical_tradeoffs:
- Increased allocator complexity vs. potential performance gains in specific scenarios.
- Standardization of new allocator APIs vs. reliance on existing `realloc` optimization.
exchanges:
- author: Florian Weimer <fweimer@redhat.com>
  role: other
  position: Provides feedback on the proposal, questioning the utility of `alloc_at_least`
    with glibc's malloc implementation.
  quote: 'These new functions are not very meaningful with glibc malloc, except

    maybe the initial switch from the small string optimization in

    std::string to the heap-allocated size, where they could make the full

    40 bytes available instead of the requested 31 (with the libstdc++

    implementation), avoiding a future resize.'
- author: Charles Munger <clm@google.com>
  role: proposer
  position: Thanks Florian Weimer for his response.
  quote: null
- author: Florian Weimer <fweimer@redhat.com>
  role: other
  position: Clarifies free_sized and free_aligned_sized were added in C23.
  quote: null
primer_expert: This discussion revolves around WG14 proposal N3849, which introduces
  new allocator APIs like `alloc_at_least`. The functions aim to give allocators more
  flexibility in providing slightly larger allocations than requested. The feedback
  concerns the potential benefits and complexities within the context of glibc's malloc
  implementation.
primer_general: Memory allocation is a fundamental aspect of programming, where programs
  request chunks of memory from the operating system to store data.  The C standard
  library provides functions like `malloc` and `free` for managing memory. This discussion
  concerns a proposal to add new memory allocation functions to the C standard, and
  whether these functions would be beneficial for implementations like glibc.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhu8qadc49x.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-23'
---

Charles Munger requested feedback on WG14 proposal N3849, which introduces a new allocator API `alloc_at_least`. Florian Weimer responded, noting that the `free_sized` description is incomplete and questioning the usefulness of these new functions with glibc's current malloc implementation, except in specific cases like small string optimization or large aligned allocations. He concludes that the potential benefits may not outweigh the added complexity.
