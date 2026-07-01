---
project: binutils
subsystem: cp-demangle.c
patch_id: null
tags:
- binutils
- gcc
- libiberty
- integer overflow
- c++ demangling
discussion_id: akRw-8BLQ-FkUM9O@squeak.grove.modra.org
source_type: public_inbox
title: libiberty d_compact_number signed integer overflow
headline: libiberty d_compact_number signed integer overflow
tldr: Fixes a signed integer overflow in libiberty's `d_compact_number` by using unsigned
  arithmetic for an addition.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: proposer
  position: Submits a patch to fix a signed integer overflow in `d_compact_number`
    by using unsigned arithmetic for an addition, applying it to binutils and gcc.
  quote: Fix this by doing the addition in unsigned arithmetic.
primer_expert: This patch in libiberty's C++ demangling code (cp-demangle.c) addresses
  a signed integer overflow in `d_compact_number`. The arithmetic `d_number(di) +
  1` can overflow if `d_number(di)` returns `INT_MAX`. The fix `d_number(di) + 1u`
  promotes the addition to unsigned arithmetic, preventing the overflow.
primer_general: This change corrects a potential bug in the code that processes C++
  function names. When decoding certain number formats, an arithmetic operation could
  lead to an overflow if the number was close to its maximum value. This could cause
  unexpected behavior or errors. The fix ensures that the calculation is performed
  in a way that prevents this overflow, making the C++ name decoding more robust.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akRw-8BLQ-FkUM9O@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Alan Modra identifies and fixes a signed integer overflow in the `d_compact_number` function within libiberty's C++ demangling code. The fix involves changing a standard addition to an unsigned addition to prevent potential overflow issues. The patch is being applied to both binutils and GCC.
