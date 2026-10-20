---
project: binutils
subsystem: opcodes/cr16
patch_id: null
tags:
- cleanup
- build
- disassembler
- cr16
discussion_id: 20261019193231.1708375-6-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 05/18] opcodes/cr16: remove unused processing_argument_number and imm4flag
  variables'
headline: 'opcodes/cr16: remove unused processing_argument_number and imm4flag variables'
tldr: Remove unused variables `processing_argument_number` and `imm4flag` from cr16
  disassembler.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the codebase and resolving build warnings.
- No functional change is expected as the variables were never used.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `processing_argument_number` and `imm4flag`
    variables from `cr16-dis.c`, which cause build errors.
  quote: "Building opcodes with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/opcodes/cr16-dis.c:83:12:\
    \ error: variable 'processing_argument_number' set but not used [-Werror,-Wunused-but-set-global]\n\
    \    /home/smarchi/src/binutils-gdb/opcodes/cr16-dis.c:85:12: error: variable\
    \ 'imm4flag' set but not used [-Werror,-Wunused-but-set-global]\n\nThese variables\
    \ have been unused since the cr16 port…"
primer_expert: This patch removes two unused global variables, `processing_argument_number`
  and `imm4flag`, from `opcodes/cr16-dis.c`. The `processing_argument_number` variable
  was intended to track the current argument being processed in an instruction, and
  `imm4flag` indicated if an instruction used a 4-bit immediate value. Both have been
  obsolete since the CR16 port's introduction in 2007, as they are never set or used,
  leading to compiler warnings.
primer_glossary: []
series_id: 'binutils:opcodes/cr16: remove unused processing_argument_number and imm4flag
  variables'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-6-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi is removing two unused variables, `processing_argument_number` and `imm4flag`, from the CR16 disassembler code. These variables have been unused since the CR16 port was added in 2007 and are now flagged by the compiler's unused variable warnings, causing build failures.
