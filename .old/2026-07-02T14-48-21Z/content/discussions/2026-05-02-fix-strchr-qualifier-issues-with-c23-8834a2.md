---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- C23
- const
- strchr
- gcc
discussion_id: 20260502170132.3303884-1-mark@klomp.org
source_type: public_inbox
title: Fix some strchr (discarded) qualifier issues with C23
headline: Fix strchr qualifier issues with C23.
tldr: The patch series fixes build errors due to implicit const conversions when compiling
  binutils with GCC 16.1 in C23 mode.
proposer: Mark Wielaard <mark@klomp.org>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Code changes needed to accommodate the new constness may introduce subtle bugs if
  not handled carefully.
- Ignoring the warnings could lead to undefined behavior if the code attempts to modify
  a const string.
- The fix might require casting away constness in some cases, which should be done
  with caution.
exchanges:
- author: Mark Wielaard <mark@klomp.org>
  role: proposer
  position: Proposes to fix discarded qualifier errors when compiling binutils with
    GCC 16.1 in C23 mode due to stricter constness of functions like strchr.
  quote: 'GCC 16.1 defaults to C23 and glibc 2.43 added const qualifiers to

    serveral functions. In particular strchr will now return a const char

    * when a const char * is given as input (and a char * when given a

    char * as input).'
- author: H.J. Lu
  role: reviewer
  position: Acknowledges the first patch and points out a similar error in `gprof/source.c`.
  quote: null
- author: Alan Modra
  role: reviewer
  position: Confirms one patch has been checked in, and provides another patch for
    a similar error related to DOS-based filesystems.
  quote: 'Well, one of them was.


    > Fix the strrchr error like:

    >

    > gprof/source.c:130:28: error: initialization discards ‘const’

    > qualifier from pointer target type [-Werror=discarded-qualifiers]

    >   130 |             char *bslash = strrchr (sf->name, ''\'');'
primer_expert: Binutils uses `strchr` and related functions to manipulate strings.
  With C23 and newer glibc versions, these functions now return `const char *` when
  passed a `const char *`. This requires changes in binutils code to avoid discarding
  the `const` qualifier, which is enforced by `-Werror`.
primer_general: '`binutils` is a collection of tools used for working with binary
  files, including the linker (`ld`), assembler (`as`), and other utilities.  The
  C standard library provides functions like `strchr` for string manipulation.  C23
  adds stricter `const` rules; code that used to compile cleanly may now produce errors
  if it implicitly discards `const` qualifiers.  This change ensures that code adheres
  to const-correctness, preventing accidental modification of immutable data.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260502170132.3303884-1-mark@klomp.org
bugzilla_url: null
date: '2026-05-02'
---

With GCC 16.1 defaulting to C23, the stricter constness of functions like `strchr` in glibc 2.43 trigger `-Werror=discarded-qualifiers` errors in binutils. This patch series updates calls to `strchr` and similar functions to handle the `const char *` return type when given a `const char *` argument. This resolves build failures and ensures compatibility with the updated C standard and glibc.
