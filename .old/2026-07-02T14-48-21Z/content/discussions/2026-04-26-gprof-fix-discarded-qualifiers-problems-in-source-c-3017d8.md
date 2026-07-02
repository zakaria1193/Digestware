---
project: binutils
subsystem: gprof
patch_id: null
tags:
- gprof
- profiler
- const
- strchr
- build error
discussion_id: 2f5264b0-9152-4085-8936-e476512557f9@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 1/4] gprof: Fix discarded-qualifiers problems in source.c'
headline: 'gprof: Fix discarded-qualifiers problems in source.c'
tldr: Fixes discarded-qualifiers errors in gprof's source.c due to qualifier-preserving
  strchr().
proposer: Simon Marchi <simon.marchi@polymtl.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Simon Marchi <simon.marchi@polymtl.ca>
  role: contributor
  position: Suggests removing the cast to `const char *` and points out variable `bslash`
    at line 187 also needs to be changed.
  quote: 'I think that you can just remove this cast to `const char *`, since `sf->name`
    is already a `const char *`.


    There is another spot to change, variable `bslash` at line 187 of the same file.'
primer_expert: '`gprof` is a performance analysis tool. This patch updates `gprof`
  to accommodate changes in how `strchr()` handles `const` qualifiers, specifically
  in `source.c` where source file names are manipulated.'
primer_general: '`gprof` is a tool for profiling program execution, helping developers
  identify performance bottlenecks.  This patch fixes compile errors caused by stricter
  type checking in newer compiler versions when processing source file names.'
series_id: 'binutils:gprof: fix discarded-qualifiers problems in source.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2f5264b0-9152-4085-8936-e476512557f9@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

This patch addresses `-Wdiscarded-qualifiers` errors in `source.c` within the `gprof` profiler. The errors are caused by the qualifier-preserving behavior of `strchr()`. The patch declares local pointer variables as `const` to avoid discarding the `const` qualifier. Simon Marchi notes that the cast to `const char *` is unnecessary, and variable `bslash` at line 187 also needs to be changed.
