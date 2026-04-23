---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- test case
- typo
- printf
- long double
discussion_id: 22c4ae3f7e5a80aa3ac118a909fe5a07c7808d03.1776882798.git.alx@kernel.org
source_type: public_inbox
title: '[PATCH 3/3]  sysdeps/ieee754/ldbl-128ibm-compat/test-printf-chk-ldbl-compat.c:
  Fix typo'
headline: 'Sysdeps/ieee754/ldbl-128ibm-compat/test-printf-chk-ldbl-compat.c: Fix typo'
tldr: A patch fixes a typo in a glibc test file.
stakes: Correcting errors in test code ensures the reliability and accuracy of the
  test suite, preventing false positives or negatives and improving the overall quality
  of glibc.
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses a minor error in a glibc test file related to
  `printf` and long double compatibility on IBM systems.  The `test-printf-chk-ldbl-compat.c`
  file specifically tests the `printf` family of functions with the `_chk` suffix,
  which are security-enhanced versions with buffer overflow protection. 'ldbl-128ibm-compat'
  refers to 128bit long double implementation on IBM systems.
primer_general: Glibc is the standard C library. This patch fixes a small error in
  a test case for glibc. Test cases are code that is used to automatically verify
  that a library is working correctly. The specific test case involves printing floating-point
  numbers with high precision on particular systems. The typo caused the wrong error
  message to appear when the test failed.
series_id: 'glibc:sysdeps/ieee754/ldbl-128ibm-compat/test-printf-chk-ldbl-compat.c:
  fix typo'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/22c4ae3f7e5a80aa3ac118a909fe5a07c7808d03.1776882798.git.alx@kernel.org
bugzilla_url: null
date: '2026-04-22'
---

This patch corrects a typo in the `test-printf-chk-ldbl-compat.c` file within the glibc test suite. The typo caused an incorrect error message to be printed when `asprintf` failed. It changes `vasprintf` to `asprintf`.
