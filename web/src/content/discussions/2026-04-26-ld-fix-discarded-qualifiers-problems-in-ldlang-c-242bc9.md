---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- glibc
- strchr
- const qualifier
discussion_id: 4c9f78f3-4d42-48ac-ae83-89d5b955cd5d@polymtl.ca
source_type: public_inbox
title: 'Re: [PATCH 3/4] ld: Fix discarded-qualifiers problems in ldlang.c'
headline: 'ld: Fix discarded-qualifiers problems in ldlang.c'
tldr: Points out another location in ldlang.c (variable `bslash` at line 10957) needing
  const qualifier fix for glibc 2.43 compatibility.
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
  position: Proposes a patch to fix discarded-qualifiers problems in ldlang.c due
    to the change in strchr().
  quote: null
- author: Simon Marchi
  role: other
  position: Points out another variable in the same file that needs a similar fix
    (bslash at line 10957).
  quote: There is one more to change in this file, variable `bslash` at line 10957.
primer_expert: This patch addresses `const` qualifier issues in `ldlang.c` related
  to the new `strchr` behavior in glibc 2.43. The focus is on ensuring type compatibility
  when assigning the result of `strchr` to variables. The specific location mentioned
  is variable `bslash` at line 10957.  `ldlang.c` handles the ld linker's input language
  processing.
primer_general: This patch is part of a series to ensure the binutils linker (`ld`)
  remains compatible with changes in the glibc C standard library. The core issue
  stems from how the `strchr` function now handles the `const` qualifier, leading
  to type mismatches in the linker's source code. This change is necessary to avoid
  build errors and ensure the linker functions correctly with newer versions of glibc.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldlang.c'
series_role: reply
series_parts:
- title: 'ld: Fix discarded-qualifiers problems in ldlang.c'
  url: https://inbox.sourceware.org/binutils/33f90399c05753a483d91cc801953714bb7b83d9.1777074100.git.calvin@wbinvd.org
  n: 3
  total: 4
url: https://inbox.sourceware.org/binutils/4c9f78f3-4d42-48ac-ae83-89d5b955cd5d@polymtl.ca
bugzilla_url: null
date: '2026-04-26'
---

Simon Marchi identifies an additional location in `ld/ldlang.c` that needs to be updated to address the `const` qualifier issue arising from glibc 2.43's `strchr()` change. Specifically, the variable `bslash` at line 10957 should also be declared as const. This is in response to a patch that fixes other discarded-qualifiers problems in the same file.
