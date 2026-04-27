---
project: binutils
subsystem: gprof
patch_id: null
tags:
- binutils
- gprof
- glibc
- strchr
- const qualifier
discussion_id: 2f5264b0-9152-4085-8936-e476512557f9@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 1/4] gprof: Fix discarded-qualifiers problems in source.c'
headline: 'gprof: Fix discarded-qualifiers problems in source.c'
tldr: Suggests removing a redundant cast and identifies another variable needing a
  const qualifier fix in gprof/source.c for glibc 2.43 compatibility.
proposer: Simon Marchi <simon.marchi@polymtl.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Ensuring compatibility with newer glibc versions.
- Potential for introducing subtle regressions if the fixes are not carefully implemented.
exchanges:
- author: Calvin Owens
  role: proposer
  position: Proposes a patch to fix discarded-qualifiers problems in gprof/source.c
    related to the changed strchr() in glibc.
  quote: null
- author: Simon Marchi
  role: other
  position: Suggests removing a redundant cast and identifies another spot to change,
    variable `bslash` at line 187.
  quote: 'I think that you can just remove this cast to `const char *`, since

    `sf->name` is already a `const char *`.


    There is another spot to change, variable `bslash` at line 187 of the

    same file.  I found this by inverting all #if conditions just to

    build-test.'
primer_expert: This patch series addresses `const` qualifier issues in gprof due to
  glibc 2.43's new `strchr` behavior. This specific patch modifies `gprof/source.c`.  The
  discussion centers around ensuring correct type handling when assigning the result
  of `strchr`.  Gprof is the GNU profiler.
primer_general: This patch is part of a series to ensure the GNU profiler (`gprof`)
  remains compatible with changes in the glibc C standard library. The core issue
  stems from how the `strchr` function now handles the `const` qualifier, leading
  to type mismatches in the profiler's source code. This change is necessary to avoid
  build errors and ensure the profiler functions correctly with newer versions of
  glibc.
series_id: 'binutils:gprof: fix discarded-qualifiers problems in source.c'
series_role: reply
series_parts:
- title: 'gprof: Fix discarded-qualifiers problems in source.c'
  url: https://inbox.sourceware.org/binutils/003fed7e07f6f9ed6a8c365e31325162a840fa03.1777074100.git.calvin@wbinvd.org
  n: 1
  total: 4
url: https://inbox.sourceware.org/binutils/2f5264b0-9152-4085-8936-e476512557f9@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

Simon Marchi reviews a patch addressing `const` qualifier issues in `gprof/source.c` due to glibc 2.43's `strchr()` changes. Marchi suggests removing an unnecessary cast and identifies another variable (`bslash` at line 187) that requires a similar `const` qualifier fix.  This is part of an effort to maintain compatibility with the updated glibc.
