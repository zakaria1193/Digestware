---
project: binutils
subsystem: binutils
patch_id: null
tags:
- THP
- memory management
- performance
- GNU properties
- binutils
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]
tldr: Proposes adding GNU properties to allow per-application control over THP usage
  for read-only segments and malloc.
stakes: Allows developers to optimize THP usage per-application, mitigating potential
  performance issues or memory waste associated with THP.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in ELF binary metadata.
- Potential for inconsistent THP behavior across applications.
- Overhead of checking GNU properties at runtime.
primer_expert: This thread proposes adding `GNU_PROPERTY_1_NEEDED` bits for THP control,
  impacting binutils via changes to how it handles ELF properties. The core question
  is whether the main executable should control THP behavior for all involved shared
  libraries. Binutils (specifically `ld`) needs to propagate these ELF properties
  to the dynamic linker.
primer_general: Transparent Huge Pages (THP) are large memory pages intended to improve
  performance but sometimes cause regressions.  Binutils is a suite of tools including
  the linker (`ld`) that processes object files and libraries to create executables.
  GNU properties are metadata in ELF files that guide runtime behavior. This proposal
  aims to add new GNU properties to allow developers to control THP usage on a per-application
  basis. This requires changes to binutils to handle these new properties during linking
  and pass them to the dynamic linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This RFC proposes adding new GNU properties to enable per-application control over Transparent Huge Pages (THP) usage for read-only segments and malloc. The goal is to address issues where THP can negatively impact performance due to latency spikes, memory waste, or database incompatibility. The discussion questions whether the main executable should control THP behavior for all shared libraries.
