---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- test
- typo
- IBM
- long double
discussion_id: 22c4ae3f7e5a80aa3ac118a909fe5a07c7808d03.1776882798.git.alx@kernel.org
source_type: public_inbox
title: '[PATCH 3/3]  sysdeps/ieee754/ldbl-128ibm-compat/test-printf-chk-ldbl-compat.c:
  Fix typo'
headline: Fix typo in test-printf-chk-ldbl-compat.c
tldr: Fixes a typo in a test file for IBM long double compatibility in glibc.
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Corrects a typo in a test file, improving code quality.
exchanges: []
primer_expert: This patch corrects a typo in a test file under `sysdeps/ieee754/ldbl-128ibm-compat/`.
  This directory contains code specific to the IBM 128-bit long double format, which
  is not universally supported. The test file verifies the correct behavior of `printf`
  when used with this format.  A typo in an error message was corrected, improving
  the accuracy of the test.
primer_general: Glibc is the standard C library for many systems. It provides functions
  for tasks like memory allocation, file I/O, and string manipulation. This patch
  modifies a test case for the `printf` function, which is used to format and print
  output.  The test case is specific to systems that use the IBM 128-bit floating-point
  format, ensuring that `printf` works correctly with this data type. A simple typo
  in the test's error message is corrected.
series_id: 'glibc:sysdeps/ieee754/ldbl-128ibm-compat/test-printf-chk-ldbl-compat.c:
  fix typo'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/22c4ae3f7e5a80aa3ac118a909fe5a07c7808d03.1776882798.git.alx@kernel.org
bugzilla_url: null
date: '2026-04-22'
---

This patch fixes a typo in `test-printf-chk-ldbl-128ibm-compat.c`, specifically changing "vasprintf" to "asprintf" in an error message. This test file is part of glibc's support for IBM's 128-bit long double format. The change improves the accuracy of the error message when `asprintf` fails.
