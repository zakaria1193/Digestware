---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- malloc
- WG14
- N3849
- alloc_at_least
discussion_id: lhuwlxw7ilg.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Request for feedback on WG14 proposal N3849 (alloc_at_least)'
headline: Request for feedback on WG14 proposal N3849 (alloc_at_least)
tldr: Discusses the implications of the WG14 proposal N3849 (alloc_at_least) for glibc
  malloc and its interaction with libstdc++.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Florian Weimer
  role: other
  position: Discusses the implications of the WG14 proposal N3849 (alloc_at_least)
    for glibc malloc and its interaction with libstdc++.
  quote: We can split chunks and use the remaining part for something else.  I think
    this is how glibc malloc differs from most other implementations, which is why
    we keep this behavior.
primer_expert: This discussion revolves around the `alloc_at_least` proposal for the
  C standard and its interaction with glibc's `malloc`. Glibc's `malloc` implementation
  has unique behaviors like chunk splitting. The `std::string` implementation in `libstdc++`
  might benefit from this new proposal. This is relevant to ABI stability and performance
  considerations within glibc.
primer_general: '`malloc` is a function in the C standard library (glibc) that allocates
  memory. The `alloc_at_least` proposal suggests a new standard function for allocating
  memory that guarantees a minimum size. The discussion centers on how this proposal
  would affect glibc''s internal memory management and whether it would improve performance
  or introduce compatibility issues with other C++ libraries like `libstdc++`. This
  involves understanding how glibc manages memory chunks and how it interacts with
  higher-level language features.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuwlxw7ilg.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-24'
---

This email thread discusses WG14 proposal N3849 (`alloc_at_least`) and its potential impact on glibc's `malloc` implementation.  The discussion covers scenarios where applications store capacity in terms of allocation size instead of element count, the limitations of using non-system `malloc` implementations with `libstdc++`, and glibc's chunk splitting behavior. The potential benefits and drawbacks of the proposal for different use cases and `malloc` implementations are examined.
