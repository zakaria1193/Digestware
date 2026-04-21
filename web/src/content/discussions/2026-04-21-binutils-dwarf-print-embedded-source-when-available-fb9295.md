---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- binutils
- dwarf
- objdump
- debugging
- embedded source
discussion_id: 20260421020204.2759264-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v3] binutils/dwarf: Print embedded source, when available'
headline: 'binutils/dwarf: Print embedded source, when available'
tldr: This patch enables objdump to print embedded source code from DWARF debugging
  information, and fixes a test failure on aarch64.
stakes: This feature would improve the debugging experience by allowing developers
  to view source code directly from objdump output.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding support for embedded source increases the complexity of the objdump utility.
- Displaying embedded source can significantly increase the size of objdump output.
exchanges:
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Proposes a patch to enable objdump to print embedded source code from
    DWARF and notes a fix for a failing test on aarch64.
  quote: 'v3 should contain a test that passes on aarch64 as well as x86_64. Sorry

    for the hassle!'
- author: Jens Remus <jremus@linux.ibm.com>
  role: contributor
  position: Requests the author to include the original commit message from v1 of
    the patch.
  quote: 'Hello Will, it would be helpful if you could keep the original commit

    message from v1 of your patch (except for the last two paragraphs),

    including the description and motivation, and place any additional

    comments below the three dashes (as you did with the patch changelog).'
primer_expert: This patch modifies `binutils/dwarf.c` to handle `DW_LNCT_source` and
  `DW_LNCT_LLVM_source` DWARF attributes, allowing `objdump` to display embedded source
  code.  This is relevant to developers working with DWARF debugging information and
  compiler extensions that embed source. A binutils dev would know DWARF line tables,
  but might not know the details of source embedding.
primer_general: DWARF is a debugging data format used to describe the structure of
  compiled programs, which helps debuggers like GDB map machine code back to the original
  source code. This patch extends the `objdump` utility, which disassembles object
  files, to be able to extract and display source code embedded directly within the
  DWARF debugging information. This can be useful for debugging stripped binaries
  where the source code is not readily available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260421020204.2759264-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies objdump to print embedded source code when available in DWARF debugging information. It adds support for the `DW_LNCT_source` and `DW_LNCT_LLVM_source` line number content types, which store the source code directly within the DWARF information.  A test failure on aarch64 was also fixed.
