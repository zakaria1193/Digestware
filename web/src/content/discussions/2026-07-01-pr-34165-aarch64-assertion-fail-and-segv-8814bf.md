---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- aarch64
- linker
- TLS
- bugfix
discussion_id: akTVYb32aOjEDV8W@squeak.grove.modra.org
source_type: public_inbox
title: PR 34165 aarch64 assertion fail and segv
headline: PR 34165 aarch64 assertion fail and segv
tldr: Fixes aarch64 TLS segfault by removing assertion and returning 0 for undefined
  sections.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Removes a strict assertion to improve robustness.
- Aligns aarch64 TLS handling with x86 behavior for weak undefined symbols.
- Acknowledges potential underlying issues with weak undefined TLS symbols.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Applies a fix for PR 34165 that resolves a segfault on aarch64 by removing
    an assertion and returning 0 for undefined TLS sections.
  quote: 'I''m going to apply this as a fix for pr34165.  It fixes the segv and results
    in a zero .got entry for the weak undefined tls syms, the same as x86.


    It seems to me that weak undefined and tls don''t work together very well, as
    the address of such a sym includes the thread pointer.  So I don''t think there
    is a reliable machine independent way to test whether the sym is defined.'
primer_expert: This change modifies the aarch64 ELF backend in binutils' BFD library.
  It removes an assertion in `dtpoff_base` and `tpoff_base` that previously required
  `tls_sec` to be non-NULL. The fix replaces this assertion with a check that returns
  0 if `tls_sec` is NULL, resolving a segfault observed in PR 34165 when dealing with
  weak undefined TLS symbols. The author notes potential issues with the interaction
  of weak undefined symbols and TLS on aarch64.
primer_general: This is a fix for a bug in the binutils software, specifically affecting
  the AArch64 (a 64-bit ARM architecture) version. The bug caused the linker to crash
  (segmentation fault) and display an error message (assertion failure) when compiling
  certain types of code that use Thread-Local Storage (TLS). TLS is a way for each
  thread in a program to have its own private copy of a variable. The fix prevents
  the crash by adjusting how the linker handles situations where TLS-related information
  is missing, making the process more robust.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akTVYb32aOjEDV8W@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch addresses a segmentation fault and assertion failure in binutils' aarch64 ELF linker related to Thread-Local Storage (TLS). It modifies the linker to return 0 instead of asserting when a TLS section is not found, aligning its behavior with x86 for weak undefined TLS symbols. The author notes that weak undefined and TLS symbols may not work reliably together due to thread pointer inclusion.
