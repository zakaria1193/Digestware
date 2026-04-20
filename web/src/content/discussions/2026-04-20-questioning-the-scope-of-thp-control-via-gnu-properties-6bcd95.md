---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- THP
- memory management
- performance
- linker
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Questioning the scope of THP control via GNU properties
tldr: Jan Beulich questions H.J. Lu's proposal to control THP usage in shared libraries
  from the main executable, suggesting each binary should have its own control.
stakes: Transparent Huge Pages (THP) can improve performance but also cause issues;
  proper control over THP usage is crucial for application stability and performance.
  Impacts how binaries are built and linked.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: under_review
sentiment_score: 5
sentiment_rationale: An RFC under discussion, with concerns raised.
technical_tradeoffs:
- The proposal aims to give developers more control over THP usage, but it's unclear
  if controlling THP from the main executable is the right approach.
- Enabling THP can improve performance in some applications, but it can also degrade
  performance in others due to latency spikes and memory waste.
primer: Binutils are a set of binary utilities used in software development, including
  tools for linking and manipulating object files.  Transparent Huge Pages (THP) are
  a memory management feature. This discussion concerns how binutils might be modified
  to allow programs to control THP usage.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

Jan Beulich responds to H.J. Lu's RFC for adding `GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]` to control THP usage. Beulich questions why the main executable would control THP behavior for shared libraries, arguing that each binary should have its own say. H.J. Lu claims library developers normally don't know if THP usage will improve or hurt application performance.
