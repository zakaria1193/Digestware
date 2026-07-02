---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build error
- strchr
- const
- glibc
- gcc
discussion_id: f666177e-aaf6-42c0-b5f3-0222c632d7e9@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 0/4] Fix build errors due to qualifier preserving strchr()'
headline: Fix build errors due to qualifier preserving strchr()
tldr: Qualifer-preserving `strchr()` causes build errors in binutils; this patch series
  fixes them.
proposer: Simon Marchi <simon.marchi@polymtl.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Refactoring is required in one patch.
exchanges:
- author: Simon Marchi <simon.marchi@polymtl.ca>
  role: contributor
  position: Reports finding an additional error in `binutils/bucomm.c` related to
    the same issue, where variable `bslash` should be made const.
  quote: In addition to those I pointed out in my other messages, I found one more
    error by changing `#ifdef HAVE_DOS_BASED_FILE_SYSTEM` to `#ifndef HAVE_DOS_BASED_FILE_SYSTEM`
    throughout.  At binutils/bucomm.c:505, variable `bslash` should be made const.
primer_expert: '`strchr()` is a standard C library function for finding a character
  in a string.  The qualifier-preserving change means that `strchr()` now returns
  a `const char*` if the input is a `const char*`, which exposes latent type errors
  in older code.  This series fixes those errors in binutils.'
primer_general: Binutils is a suite of tools used in the software development process,
  including the linker and assembler. Recent updates to the C standard library functions
  like `strchr()` cause stricter type checking, exposing errors in existing code that
  must be fixed for compatibility.
series_id: binutils:fix build errors due to qualifier preserving strchr()
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/f666177e-aaf6-42c0-b5f3-0222c632d7e9@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

This thread discusses a patch series addressing build errors in binutils caused by the qualifier-preserving behavior of `strchr()` in newer glibc versions and GCC. The updated `strchr()` returns a `const` pointer when passed a `const` argument, leading to type mismatches in binutils code.  The series aims to resolve these errors, with one patch requiring refactoring.
