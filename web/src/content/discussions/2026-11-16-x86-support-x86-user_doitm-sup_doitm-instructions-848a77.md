---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- gas
- x86
- instructions
- patch
discussion_id: 20261116080006.1828333-1-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH] x86: Support x86 USER_DOITM/SUP_DOITM instructions'
headline: 'x86: Support x86 USER_DOITM/SUP_DOITM instructions'
tldr: Patch adds support for new Intel USER_DOITM/SUP_DOITM instructions to GNU assembler
  and disassembler.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Using a single `.doitm` switch for both user and supervisor modes simplifies the
  assembler/disassembler implementation but might require careful user awareness.
exchanges: []
primer_expert: This patch adds support for new x86 instructions (USER_DOITM/SUP_DOITM)
  to binutils. These instructions are part of recent Intel ISA disclosures. The key
  implementation detail is the use of a `.doitm` assembler directive to differentiate
  between user-mode and supervisor-mode execution of the same opcodes, simplifying
  gas and objdump.
primer_glossary:
- term: USER_DOITM
  definition: An Intel instruction extension operating in user mode.
- term: SUP_DOITM
  definition: An Intel instruction extension operating in supervisor mode.
- term: ISA
  definition: Instruction Set Architecture, defining the set of instructions a processor
    can execute.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: disassembler
  definition: A tool that translates machine code (binary) back into assembly language.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116080006.1828333-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch introduces support for Intel's new USER_DOITM and SUP_DOITM instructions to the GNU Assembler (gas) and disassembler. The author proposes using a `.doitm` switch to handle these instructions, as they share the same opcodes in both user and supervisor modes. The patch includes updates to NEWS, configuration, and testsuite files.
