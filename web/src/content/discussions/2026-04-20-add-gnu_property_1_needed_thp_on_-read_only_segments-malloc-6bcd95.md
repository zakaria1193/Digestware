---
project: binutils
subsystem: binutils
patch_id: null
tags:
- glibc
- thp
- memory management
- performance
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]
tldr: Proposes adding a GNU property to allow per-application control of Transparent
  Huge Page (THP) usage on read-only segments and in malloc.
stakes: THP can improve performance but also cause latency spikes, memory waste, and
  database incompatibility, so per-app control is valuable.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
sentiment_score: 5
sentiment_rationale: The discussion is neutral, with a question about the scope of
  the proposed change.
technical_tradeoffs:
- Adding a new GNU property increases complexity in the loader.
- Application developers need to understand THP implications.
- Potential for ABI breakage if the property is not handled correctly.
- The approach might not be flexible enough if different shared libraries require
  different THP settings.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes adding  `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` to
    allow applications to opt-in to THP usage on read-only segments.  When the bit
    is set, the run-time loader should call madvise with MADV_HUGEPAGE on all THP-eligible
    RO segments.
  quote: 'To enable developers per-application control over THP usage under madvise
    THP mode, add the following bits to GNU_PROPERTY_1_NEEDED:


    1. GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions why the main executable should control THP behavior for shared
    libraries, suggesting each binary should have its own control.
  quote: 'Why would one (the main) executable control behavior for all involved

    shared libraries? Shouldn''t each binary get its own say?'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Claims library developers usually don't know if THP usage in their libraries
    will improve or hurt application performance.
  quote: 'Normally library developers don''t know if THP usage in the library will

    improve or hurt application performance.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks for clarification on what 'normally' means.
  quote: '"Normally" as in what exactly? An enti'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Has not yet responded to the question about 'normally'.
  quote: ''
primer_expert: This RFC proposes adding a new `GNU_PROPERTY_1_NEEDED` bit to control
  THP usage in glibc.  THP, when enabled with `madvise`, requires explicit opt-in
  via `madvise(MADV_HUGEPAGE)`. The RFC aims to allow application developers to control
  this behavior for both the main executable and its shared libraries, due to the
  performance trade-offs of THP. The discussion centers on the scope of control (executable
  vs. individual shared libraries).
primer_general: Transparent Huge Pages (THP) is a memory management feature in Linux
  kernels that attempts to use larger memory pages (2MB) to improve performance. However,
  THP can sometimes degrade performance due to latency spikes, memory waste, and compatibility
  issues with certain databases. This proposal suggests adding a mechanism to glibc,
  the standard C library, that allows applications to control whether THP is used
  for read-only memory segments and memory allocations. This would provide developers
  with more fine-grained control over memory management and potentially improve application
  performance or stability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

H.J. Lu proposes adding a new GNU property to allow developers to control THP usage on read-only segments and in malloc. This would allow applications to opt-in to THP usage, potentially improving performance while avoiding the common issues associated with THP. Jan Beulich questions whether the main executable should control THP behavior for all involved shared libraries.
