---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ld
- const
- strchr
- build error
discussion_id: 4c9f78f3-4d42-48ac-ae83-89d5b955cd5d@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 3/4] ld: Fix discarded-qualifiers problems in ldlang.c'
headline: 'ld: Fix discarded-qualifiers problems in ldlang.c'
tldr: The patch fixes discarded-qualifiers errors in ldlang.c due to qualifier-preserving
  strchr().
proposer: Simon Marchi <simon.marchi@polymtl.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Simon Marchi <simon.marchi@polymtl.ca>
  role: contributor
  position: Points out that variable `bslash` at line 10957 also needs to be changed.
  quote: There is one more to change in this file, variable `bslash` at line 10957.
primer_expert: This patch modifies the binutils linker (`ld`) to accommodate changes
  in how `strchr()` handles const qualifiers. The specific file modified, `ldlang.c`,
  handles language-specific aspects of linking.
primer_general: The linker is a program that combines compiled object files into a
  single executable.  This patch fixes errors in the linker's source code that arise
  due to more strict type checking in newer compiler versions.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldlang.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4c9f78f3-4d42-48ac-ae83-89d5b955cd5d@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

This patch addresses `-Wdiscarded-qualifiers` errors in `ldlang.c` within the binutils linker (`ld`). The errors arise because of the new qualifier-preserving `strchr()` function.  The patch makes the return type of `archive_path()` const and fixes up its callers. Simon Marchi notes one more variable, `bslash` at line 10957, needs to be changed in the same file.
