---
project: binutils
subsystem: glibc
patch_id: null
tags:
- glibc
- atanh
- rounding
- numerical stability
discussion_id: CAHt=NyP1bySRnwNQABx4K6ktyhUXR=BjXvWcP9342RQjtFNgvw@mail.gmail.com
source_type: public_inbox
title: GNU Tools Weekly News Week 34 (April 19, 2026)
headline: 'GNU Tools Weekly News: GLibc atanh correctly rounded'
tldr: The GNU Tools Weekly News reports the GNU libc atanh function is now correctly
  rounded.
stakes: Correctly rounded math functions in glibc ensure more accurate and reliable
  numerical computations for all applications using the library.
proposer: GNU Tools weekly <gnutoolsweekly@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges: []
primer_expert: This reports on a correctly rounded `atanh` implementation in glibc.
  Correct rounding is crucial for numerical stability and standards compliance, particularly
  in mathematical libraries. This matters for applications relying on precise floating-point
  computations. Also mentioned are GCC and sourceware infrastructure updates.
primer_general: This news item reports that the atanh (inverse hyperbolic tangent)
  function in the GNU C Library (glibc) has been updated to provide correctly rounded
  results. Glibc is a core library used by almost all programs on Linux systems. Correct
  rounding ensures that the function's output is as accurate as possible, which is
  important for applications that perform mathematical calculations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHt=NyP1bySRnwNQABx4K6ktyhUXR=BjXvWcP9342RQjtFNgvw@mail.gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This edition of GNU Tools Weekly News highlights that the GNU libc's atanh function is now correctly rounded. It also mentions updates to GCC, Valgrind, upcoming toolchain conferences, the gccrs project, and other general toolchain news.
