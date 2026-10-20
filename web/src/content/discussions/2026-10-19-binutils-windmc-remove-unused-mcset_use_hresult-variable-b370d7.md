---
project: binutils
subsystem: binutils/windmc
patch_id: null
tags:
- cleanup
- build
- unimplemented
discussion_id: 20261019193231.1708375-8-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 07/18] binutils/windmc: remove unused mcset_use_hresult variable'
headline: 'binutils/windmc: remove unused mcset_use_hresult variable'
tldr: Remove unused `mcset_use_hresult` variable from binutils/windmc.c.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the codebase and resolving build warnings.
- No functional change is expected as the variable and its associated option were
  never implemented.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `mcset_use_hresult` variable from `windmc.c`,
    which causes build errors.
  quote: "Building binutils with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/binutils/windmc.c:116:12:\
    \ error: variable 'mcset_use_hresult' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe -o option that sets it was never implemented, it errors out right\nafter\
    \ setting the variable.  Remove the variable."
primer_expert: This patch removes an unused global variable `mcset_use_hresult` from
  `binutils/windmc.c`. This variable was intended to be set by the `-o` option, which
  is designed to generate an OLE2 header file using HRESULT definitions. However,
  the `-o` option itself is unimplemented and immediately exits via `fatal()`. Consequently,
  `mcset_use_hresult` is always set but never used, leading to a compiler warning.
primer_glossary:
- term: windmc.c
  definition: C source file for the Windows Message Compiler utility in binutils.
- term: mcset_use_hresult
  definition: A flag intended to control the generation of OLE2 header files using
    HRESULT definitions.
- term: OLE2
  definition: Object Linking and Embedding version 2, a Microsoft technology for inter-process
    communication and data sharing.
- term: HRESULT
  definition: A data type used in Windows for error codes, typically returned by COM
    (Component Object Model) interfaces.
series_id: 'binutils:binutils/windmc: remove unused mcset_use_hresult variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-8-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi proposes removing the `mcset_use_hresult` variable from `binutils/windmc.c`. This variable is set by the `-o` option, which is not implemented and immediately calls `fatal`. Therefore, the variable is never actually used and causes a build warning with recent Clang versions.
