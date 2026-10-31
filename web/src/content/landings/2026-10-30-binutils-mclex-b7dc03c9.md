---
project: binutils
subsystem: binutils/mclex
patch_id: null
tags:
- mclex
- cleanup
- unused variable
commit_hash: b7dc03c969fd68b6a1970ae894af8c2ea5152335
source_type: public_inbox
author: Simon Marchi <simark@sourceware.org>
headline: 'Binutils mclex: Remove unused input_stream variable'
tldr: Binutils lexer for mc files removes an unused global variable.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `static unichar *input_stream` global variable
  from `binutils/mclex.c`. The variable was initialized in `mc_set_content` but is
  never read. The `windmc` tool, added in a prior commit, changed how input is handled,
  making `input_stream` obsolete. The lexer now correctly uses only `input_stream_pos`
  for its operations. This cleanup addresses a `-Wunused-but-set-global` compiler
  warning.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030140324.846524BA23F7@sourceware.org
date: '2026-10-30'
is_stub: true
stub_reason: low_score
---

The `input_stream` global variable in `binutils/mclex.c` has been removed. This variable was intended to hold the input stream for the lexer but has been unused since the `windmc` tool was added. The lexer now solely relies on `input_stream_pos` to process input, and removing the unused variable eliminates compiler warnings about unused variables.
