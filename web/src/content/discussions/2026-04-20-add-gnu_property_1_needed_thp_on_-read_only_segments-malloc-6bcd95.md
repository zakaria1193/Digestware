---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- thp
- elf
- memory management
- performance
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]
tldr: Proposes adding a GNU property to control THP usage on read-only segments and
  malloc to allow per-application control under madvise THP mode.
stakes: This proposal aims to give developers more control over THP usage, potentially
  improving performance and reducing memory waste, but also adding complexity to application
  deployment.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a new ELF property increases the complexity of the ELF format and dynamic
  linking process.
- Allowing per-application control over THP provides flexibility but requires developers
  to understand the performance implications of THP.
- The proposal needs to address the question of whether THP control should be per-executable
  or per-shared library.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes adding `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` to allow
    per-application control over THP usage on read-only segments under madvise THP
    mode.
  quote: 'To enable developers per-application control over THP usage under madvise

    THP mode, add the following bits to GNU_PROPERTY_1_NEEDED:


    1. GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions why the main executable should control THP behavior for all
    involved shared libraries, suggesting each binary should have its own control.
  quote: 'Why would one (the main) executable control behavior for all involved

    shared libraries? Shouldn''t each binary get its own say?'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Claims that library developers typically don't know if THP usage will
    improve or hurt application performance.
  quote: 'Normally library developers don''t know if THP usage in the library will

    improve or hurt application performance.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks for clarification on the meaning of "normally".
  quote: '"Normally" as in what exactly? An enti'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Acknowledges the need to control THP behavior per shared library.
  quote: null
primer_expert: This RFC proposes adding a new ELF property to control THP usage on
  read-only segments and in malloc. The discussion revolves around whether a main
  executable should control the THP behavior for its shared libraries or whether each
  shared library should have its own control. This impacts how the dynamic linker
  (`ld-linux.so`) handles THP enablement via `madvise` for different program segments.
  Binutils is involved because the proposal requires changes to the ELF format.
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that attempts
  to improve performance by using larger memory pages. This proposal discusses adding
  a mechanism to control THP usage on a per-application basis. The core idea is to
  introduce a new property in the ELF (Executable and Linkable Format) file format
  that allows developers to specify whether THP should be enabled for read-only segments
  and malloc allocations.  Binutils, the binary utilities, is involved because it
  is responsible for handling and manipulating ELF files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

H.J. Lu proposes adding new bits to `GNU_PROPERTY_1_NEEDED` to allow developers to opt-in to THP usage on read-only segments and in malloc. This is intended to provide per-application control over THP usage as THP may improve or hurt application performance. Jan Beulich questions whether the main executable should control THP behavior for all shared libraries, suggesting each binary should have its own control.
