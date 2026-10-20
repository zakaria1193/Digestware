---
project: binutils
subsystem: ld/ticoff
patch_id: null
tags:
- cleanup
- build
- linker
- ticoff
discussion_id: 20261019193231.1708375-16-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 15/18] ld/ticoff: remove unused coff_version variable'
headline: 'ld/ticoff: remove unused coff_version variable'
tldr: Remove unused `coff_version` variable from ld/ticoff emulation.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving code clarity and resolving build warnings.
- No change in linker behavior as the variable was never used.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `coff_version` variable from `ld/ticoff`
    which causes build errors.
  quote: "Building ld with a recent clang fails with:\n\n    etic3xcoff.c:46:12: error:\
    \ variable 'coff_version' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe same happens for the other emulations generated from ticoff.em.  The\nvariable\
    \ has been unused since it was added in commit 74459f0e3ead\n(\"tic54x/ibmc54xdsp\
    \ target for ld.\", 2000-06-20).  The --format option\nselects the output format\
    \ directly.…"
primer_expert: This patch removes an unused global variable `coff_version` from `ld/emultempl/ticoff.em`.
  This variable was intended to control the COFF version for specific TI emulations
  but has been obsolete since 2000. The `--format` option directly handles output
  format selection, rendering `coff_version` unnecessary and causing build warnings
  with modern compilers.
primer_glossary: []
series_id: 'binutils:ld/ticoff: remove unused coff_version variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-16-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi is removing the `coff_version` variable from the `ld/ticoff` emulation. This variable has been unused since 2000 and causes build failures with recent Clang versions due to the `-Wunused-but-set-global` warning. The `--format` option directly selects the output format, making this variable redundant.
