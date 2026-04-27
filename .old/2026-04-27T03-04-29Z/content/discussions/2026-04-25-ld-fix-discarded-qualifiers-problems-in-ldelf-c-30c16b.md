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
discussion_id: 3197a710e4b6bd87166a0dde13812259d09b452f.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 4/4] ld: Fix discarded-qualifiers problems in ldelf.c'
headline: 'ld: Fix discarded-qualifiers problems in ldelf.c'
tldr: Fixes discarded-qualifiers errors in ldelf.c, adapting to glibc 2.43's qualifier-preserving
  strchr().
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Correcting type errors to maintain compatibility with newer glibc versions.
- Potential for introducing subtle regressions if the fixes are not carefully implemented.
exchanges: []
primer_expert: This patch fixes build errors in `ldelf.c` within the binutils linker
  (`ld`) due to changes in glibc's `strchr()` function. The core problem is the `const`
  qualifier being preserved in the return type, leading to type mismatches.  The patch
  updates `ldelf_search_needed` and `ldelf_parse_ld_so_conf_include` to handle the
  new `strchr` behavior.
primer_general: This patch addresses compatibility issues between the binutils linker
  (`ld`) and a recent update to the glibc C standard library. The update involves
  a change in how the `strchr` function handles constant strings (`const char *`),
  leading to compilation errors in the linker's source code. This patch modifies the
  linker's code to accommodate this change, ensuring it continues to build and function
  correctly.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldelf.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/3197a710e4b6bd87166a0dde13812259d09b452f.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch addresses discarded-qualifiers errors in `ld/ldelf.c` caused by the change in glibc 2.43's `strchr()` function. It corrects type mismatches by either using a non-const pointer when calling `strrchr()` or declaring local variables as `const`.  This ensures that the linker builds correctly with the updated glibc.
