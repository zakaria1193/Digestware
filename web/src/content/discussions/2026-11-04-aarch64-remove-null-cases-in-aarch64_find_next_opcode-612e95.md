---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- cleanup
discussion_id: 6069cdef-afe0-9221-c934-948456e95c5b@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 12/28] aarch64: Remove NULL cases in aarch64_find_next_opcode'
headline: 'aarch64: Remove NULL cases in aarch64_find_next_opcode'
tldr: Cleans up the `aarch64_find_next_opcode` function by removing explicit NULL
  returns.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Slightly reduces code verbosity.
- Relies on implicit return behavior.
exchanges: []
primer_expert: The patch targets `aarch64-dis-2.c`, specifically the `aarch64_find_next_opcode`
  function. It removes redundant `return NULL;` statements, making the code slightly
  more concise by relying on the implicit return of `NULL` for functions returning
  pointers when the end of the function is reached without an explicit return.
primer_glossary: []
series_id: 'binutils:aarch64: remove null cases in aarch64_find_next_opcode'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6069cdef-afe0-9221-c934-948456e95c5b@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch simplifies the `aarch64_find_next_opcode` function in `aarch64-dis-2.c` by removing explicit `return NULL;` statements. The function will now implicitly return NULL at the end if no matching opcode is found, relying on the default behavior of functions that don't explicitly return a value.
