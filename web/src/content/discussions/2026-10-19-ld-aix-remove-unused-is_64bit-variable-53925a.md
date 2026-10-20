---
project: binutils
subsystem: ld/aix
patch_id: null
tags:
- cleanup
- build
- linker
- aix
discussion_id: 20261019193231.1708375-15-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 14/18] ld/aix: remove unused is_64bit variable'
headline: 'ld/aix: remove unused is_64bit variable'
tldr: Remove unused `is_64bit` variable from AIX linker emulation.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, cleaning up the codebase and resolving build warnings.
- No functional change is expected as the variable was never used.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `is_64bit` variable from AIX linker emulation,
    which causes build errors.
  quote: "Building ld with a recent clang fails with:\n\n    eaix5ppc.c:128:12: error:\
    \ variable 'is_64bit' set but not used [-Werror,-Wunused-but-set-global]\n\nThe\
    \ same happens for the other emulations generated from aix.em.  The\nvariable\
    \ has been unused since it was added in commit 742aeb63e9f0\n(\"Pass argc and\
    \ argv to ldemul_choose_target. Support -b64 in AIX\",\n2001-12-03).  Remove it."
primer_expert: This patch removes an unused global variable `is_64bit` from `ld/emultempl/aix.em`.
  This variable was intended to track whether a 64-bit link was being performed but
  has been obsolete since 2001. The logic for selecting 32-bit or 64-bit modes is
  handled by `syscall_mask` and `symbol_mode_mask`, making `is_64bit` redundant and
  a source of build warnings.
primer_glossary: []
series_id: 'binutils:ld/aix: remove unused is_64bit variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-15-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi proposes removing the `is_64bit` variable from the AIX linker emulation. This variable, introduced in 2001, has been unused and now causes build failures with recent Clang versions due to `-Wunused-but-set-global`. The linker logic for 32-bit and 64-bit modes is handled by other mechanisms.
