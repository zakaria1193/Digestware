---
project: glibc
subsystem: elf
patch_id: null
tags:
- tunables
- ld.so.cache
- dynamic configuration
- performance
discussion_id: f2c3955f106f9ce2401a97c392d3bb3575b10b0b.1776449736.git.dj@redhat.com
source_type: public_inbox
title: '[PATCH v7 3/4] Add system-wide tunables: Apply tunables part'
headline: 'Add system-wide tunables: Apply tunables part'
tldr: Loads ld.so.cache, fetches the tunables extension, and applies those tunables
  to the current program, deferring security policy enforcement.
stakes: Enables dynamic configuration of glibc behavior via tunables, potentially
  affecting performance and functionality.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: stalled
sentiment_score: 5
sentiment_rationale: This patch implements a significant part of the tunables feature,
  but the deferral of security policies warrants a neutral score in the absence of
  further discussion.
series_id: 'glibc:add system-wide tunables: apply tunables part'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f2c3955f106f9ce2401a97c392d3bb3575b10b0b.1776449736.git.dj@redhat.com
bugzilla_url: null
date: '2024-02-21'
---

This patch loads the ld.so.cache, retrieves the tunables extension, and applies the tunables to the current program. Security policies are not yet applied in this patch.
