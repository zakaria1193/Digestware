---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- gas
- x86
- instruction set
discussion_id: bc8f6005-f586-4808-ab24-b608647421a5@suse.com
source_type: public_inbox
title: '[PATCH v2] x86: Support x86 USER_DOITM/SUP_DOITM instructions'
headline: 'x86: Support x86 USER_DOITM/SUP_DOITM instructions'
tldr: Binutils gas assembler is updated to support the new USER_DOITM and SUP_DOITM
  instructions.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Adding new instruction support increases assembler complexity but enables use of
  new hardware features.
- Unified `.doitm` switch simplifies assembly syntax but requires clear distinction
  between user/supervisor modes.
exchanges:
- author: Haochen Jiang <haochen.jiang@intel.com>
  role: proposer
  position: Submits a patch to add support for USER_DOITM/SUP_DOITM instructions to
    gas, stating it will be committed after minor adjustments.
  quote: 'This will be the patch I am going to commit after adjusting tabs and

    blanks near slashes if no objection.


    Thx,

    Haochen'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Grants approval for the patch, confirming that the author should proceed
    with the commit after the mentioned adjustments.
  quote: Just to confirm - please go ahead.
primer_expert: This patch adds support for the USER_DOITM and SUP_DOITM instructions
  to the GNU Assembler (gas). These instructions appear to be new extensions, with
  `USER_DOITM` for user-mode and `SUP_DOITM` for supervisor-mode. The patch involves
  modifications to `gas/ChangeLog`, `gas/config/tc-i386.c`, `gas/doc/c-i386.texi`,
  and various test suite files, as well as updates to `opcodes/` files for instruction
  decoding and encoding. A common `.doitm` switch is used to access both.
primer_glossary:
- term: USER_DOITM
  definition: Likely a new x86 instruction extension related to operations performed
    in user mode.
- term: SUP_DOITM
  definition: Likely a new x86 instruction extension related to operations performed
    in supervisor (kernel) mode.
- term: .doitm
  definition: An assembler directive or switch used to invoke the USER_DOITM and SUP_DOITM
    instructions.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    translating assembly language code into machine code.
- term: x86
  definition: The dominant instruction set architecture for desktop and server processors.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261118022848.2989863-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch adds support for the USER_DOITM and SUP_DOITM instructions to the GNU Assembler (gas). These instructions are related to user-mode and supervisor-mode operations, respectively, and are accessed via the `.doitm` switch. The patch includes updates to gas's configuration, documentation, and test suite, along with modifications to opcode definitions.
