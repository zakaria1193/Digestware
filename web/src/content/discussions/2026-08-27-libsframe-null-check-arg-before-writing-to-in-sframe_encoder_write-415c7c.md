---
project: binutils
subsystem: libsframe
patch_id: null
tags:
- libsframe
- bugfix
- security
discussion_id: 20260827224146.3391610-2-ibhagatgnu@gmail.com
source_type: public_inbox
title: '[PATCH 01/10] libsframe: null check arg before writing to in sframe_encoder_write'
headline: 'libsframe: null check arg before writing to in sframe_encoder_write'
tldr: Add a null check for the encoded_size argument in sframe_encoder_write to prevent
  potential crashes.
proposer: Indu Bhagat <ibhagatgnu@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The `sframe_encoder_write` function in libsframe is responsible for
  encoding data into the SFrame format. This patch addresses a potential null pointer
  dereference when the `encoded_size` output parameter is NULL. The fix ensures that
  the assignment `*encoded_size = 0;` is guarded by a check, preventing a crash in
  cases where the caller does not provide a valid pointer for the encoded size.
primer_glossary:
- term: sframe_encoder_write
  definition: A function within the libsframe library responsible for writing encoded
    data. It takes an encoder context, a pointer to store the encoded size, and an
    error pointer.
- term: NULL pointer dereference
  definition: An error that occurs when a program attempts to access a memory address
    that has not been assigned a valid value (i.e., it points to NULL). This typically
    results in a program crash.
series_id: 'binutils:libsframe: null check arg before writing to in sframe_encoder_write'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827224146.3391610-2-ibhagatgnu@gmail.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch introduces a null check for the `encoded_size` argument in the `sframe_encoder_write` function. Previously, the function would dereference `encoded_size` unconditionally, which could lead to a crash if a NULL pointer was passed. This change adds a safeguard to prevent such an issue.
