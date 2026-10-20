---
project: binutils
subsystem: binutils/srconv
patch_id: null
tags:
- cleanup
- build
- obsolete
discussion_id: 20261019193231.1708375-7-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 06/18] binutils/srconv: remove unused quick variable'
headline: 'binutils/srconv: remove unused quick variable'
tldr: Remove unused `quick` variable from binutils/srconv.c.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the codebase and resolving build warnings.
- No functional change is expected as the variable was never used.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `quick` variable from `srconv.c`, which causes
    build errors.
  quote: "Building binutils with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/binutils/srconv.c:56:12:\
    \ error: variable 'quick' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe -q/--quick option is documented as obsolete and ignored, and the\nvariable\
    \ it sets has been unused since at least the initial sourceware\nimport.  Remove\
    \ the variable, keep accepting the option."
primer_expert: This patch removes an unused global variable `quick` from `binutils/srconv.c`.
  The `-q` or `--quick` option historically influenced `srconv`'s behavior but is
  now documented as obsolete and ignored. The variable `quick` that this option sets
  has not been used since the initial import to Sourceware. Removing this dead code
  cleans up the source file and resolves a compiler warning about an unused but set
  variable.
primer_glossary: []
series_id: 'binutils:binutils/srconv: remove unused quick variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-7-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi is removing the unused `quick` variable from `binutils/srconv.c`. The `-q/--quick` option, which sets this variable, is documented as obsolete and ignored. The variable has been unused since the initial Sourceware import, and its removal resolves a build warning.
