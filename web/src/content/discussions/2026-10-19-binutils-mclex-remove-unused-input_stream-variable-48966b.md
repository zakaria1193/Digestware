---
project: binutils
subsystem: binutils/mclex
patch_id: null
tags:
- cleanup
- build
- lexer
discussion_id: 20261019193231.1708375-9-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 08/18] binutils/mclex: remove unused input_stream variable'
headline: 'binutils/mclex: remove unused input_stream variable'
tldr: Remove unused `input_stream` variable from binutils/mclex.c.
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
  position: Proposes removing the unused `input_stream` variable from `mclex.c`, which
    causes build warnings.
  quote: "Building binutils with a recent clang gives:\n\n    /home/smarchi/src/binutils-gdb/binutils/mclex.c:42:17:\
    \ warning: variable 'input_stream' set but not used [-Wunused-but-set-global]\n\
    \nThe variable has been unused since windmc was added.  Only\ninput_stream_pos\
    \ is used to read the input.  Remove it."
primer_expert: This patch removes an unused global variable `input_stream` from `binutils/mclex.c`.
  This variable was intended to hold the input character stream for the lexer but
  has been obsolete since the `windmc` tool was introduced. The `input_stream_pos`
  variable is used instead for tracking the current position in the stream. Removing
  `input_stream` cleans up the code and resolves a compiler warning related to unused
  variables.
primer_glossary:
- term: mclex.c
  definition: A C source file containing a lexer for parsing message compiler directives.
- term: windmc
  definition: A tool likely related to the Windows Message Compiler, used in the binutils
    project.
- term: input_stream_pos
  definition: A pointer likely used to track the current position within an input
    stream of characters.
series_id: 'binutils:binutils/mclex: remove unused input_stream variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-9-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi proposes removing the unused `input_stream` variable from `binutils/mclex.c`. This variable has been obsolete since the addition of `windmc`, and only `input_stream_pos` is used for reading input. This change aims to clean up the code and resolve build warnings.
