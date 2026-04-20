---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- thp
- gnu properties
- elf
- memory management
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]
tldr: Proposes adding GNU properties to allow per-application control over THP usage
  in read-only segments and malloc.
stakes: Allows developers to fine-tune THP usage, potentially improving performance
  and avoiding compatibility issues.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Requires modifications to binutils to support the new GNU properties.
- Adds complexity to the ELF format.
- Provides finer-grained control over THP usage.
primer_expert: This proposal involves changes to binutils to support new GNU properties
  in the ELF header related to THP. This likely affects the linker and other tools
  that process ELF files.  The discussion involves the rationale for executable-wide
  control.
primer_general: Transparent Huge Pages (THP) is a memory optimization technique in
  which larger memory pages are used. Binutils is a collection of tools for working
  with binary files, including the assembler, linker, and other utilities.  GNU properties
  in ELF headers are used to convey metadata about executables and shared libraries.
  This change would enable developers to specify THP usage through ELF headers, requiring
  binutils to understand and process this new information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This RFC proposes adding new GNU properties that would allow developers to control THP usage on read-only segments and in malloc on a per-application basis. This is intended to address issues where THP can negatively impact application performance. The discussion raises concerns about whether the main executable should control behavior for shared libraries.
