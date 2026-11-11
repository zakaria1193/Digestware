---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build
- ld
- plugins
discussion_id: avO5_3VDJyDnVkV8@squeak.grove.modra.org
source_type: public_inbox
title: PR 34985, ld fails to build on hosts without <dlfcn.h>
headline: ld fails to build on hosts without dlfcn.h
tldr: Fixes ld build failure on systems lacking dlfcn.h by conditionally compiling
  plugin support.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Conditional compilation adds minor complexity but ensures buildability on a wider
  range of systems.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes changes to conditionally compile plugin functionality in ld and
    improve test suite reporting for systems without dlfcn.h.
  quote: "ld/ * plugin.c: Wrap existing functions in #if BFD_SUPPORTS_PLUGINS.\n\t\
    Provide do-nothin stubs for !BFD_SUPPORTS_PLUGINS.\nbinutils/ * testsuite/binutils-all/x86-64/x86-64.exp\
    \ (run_pr33198_test):\n\tReturn \"untested\" rather than \"fail\" when no plugin\
    \ support.\n\tDifferentiate failure messages."
primer_expert: This change modifies `ld/plugin.c` to conditionally compile plugin-related
  functions based on `BFD_SUPPORTS_PLUGINS`. When the header is unavailable, it provides
  stub functions. The testsuite in `binutils/testsuite/binutils-all/x86-64/x86-64.exp`
  is also updated to differentiate between test failures and environments lacking
  plugin support, avoiding incorrect failure reports.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avO5_3VDJyDnVkV8@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses a build failure in ld on systems that do not provide the <dlfcn.h> header, which is necessary for plugin support. The changes conditionally compile existing functions related to plugins and provide no-operation stubs when plugin support is unavailable. Additionally, it updates a test case to report "untested" instead of "fail" when plugin support is absent, differentiating between actual failures and lack of support.
