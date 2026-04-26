---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- glibc
- strchr
- const qualifier
- build error
discussion_id: f666177e-aaf6-42c0-b5f3-0222c632d7e9@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 0/4] Fix build errors due to qualifier preserving strchr()'
headline: Fix build errors due to qualifier preserving strchr()
tldr: Responds to a patch series fixing build errors caused by glibc 2.43's qualifier-preserving
  `strchr()`, suggesting an additional fix in bucomm.c.
proposer: Simon Marchi <simon.marchi@polymtl.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Correcting type errors to maintain compatibility with newer glibc versions.
- Potential for introducing subtle regressions if the fixes are not carefully implemented.
exchanges:
- author: Calvin Owens
  role: proposer
  position: Proposes a patch series to fix build errors due to the new qualifier preserving
    strchr() in glibc 2.43.
  quote: 'Building binutils with glibc 2.43 and GCC 15.2 fails due to the new

    qualifier preserving strchr() and strrchr(), which now return a const

    pointer when passed one as their first argument.'
- author: Simon Marchi
  role: other
  position: Identifies another error in `binutils/bucomm.c` and suggests a fix.
  quote: 'In addition to those I pointed out in my other messages, I found one

    more error by changing `#ifdef HAVE_DOS_BASED_FILE_SYSTEM` to `#ifndef

    HAVE_DOS_BASED_FILE_SYSTEM` throughout.  At binutils/bucomm.c:505,

    variable `bslash` should be made const.'
primer_expert: This thread discusses fixing build errors in binutils due to glibc
  2.43's changed `strchr()` behavior. The core issue involves the `const` qualifier
  being preserved in the return type of `strchr()`, leading to type mismatches in
  binutils code.  The discussion centers around specific locations in the source code
  that need adjustments, specifically mentioning `bucomm.c` and conditional compilation
  via `HAVE_DOS_BASED_FILE_SYSTEM`.
primer_general: This discussion revolves around adapting binutils to a change in the
  C standard library (glibc).  Specifically, the `strchr()` function now preserves
  the `const` qualifier of its input, which can cause compilation errors in code not
  expecting this behavior.  The patch series aims to fix these errors by adjusting
  binutils' source code. The errors occur because `strchr` is used to search for a
  character within a string, and the new `strchr` might return a "constant" pointer,
  where previously it returned a modifiable pointer.
series_id: binutils:fix build errors due to qualifier preserving strchr()
series_role: cover
series_parts:
- title: Fix build errors due to qualifier preserving strchr()
  url: https://inbox.sourceware.org/binutils/cover.1777074100.git.calvin@wbinvd.org
  n: 0
  total: 4
url: https://inbox.sourceware.org/binutils/f666177e-aaf6-42c0-b5f3-0222c632d7e9@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

Simon Marchi responds to a patch series that addresses build errors in binutils caused by changes in glibc 2.43's `strchr()` function, which now preserves qualifiers. He points out an additional error in `binutils/bucomm.c` related to the use of `strchr()` and suggests making the `bslash` variable const, discovered by temporarily inverting `#ifdef HAVE_DOS_BASED_FILE_SYSTEM`.
