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
discussion_id: 20260420143919.2721336-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] binutils/dwarf: Print embedded source, when available'
headline: 'Binutils/dwarf: Print embedded source, when available'
tldr: This patch enables objdump to print embedded source code from DWARF debugging
  information, if available.
stakes: Improves debugging experience by allowing developers to view source code directly
  from objdump output.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases the size of the DWARF debugging information.
- Adds complexity to objdump.
- Provides a more convenient way to view source code during debugging.
primer_expert: This patch modifies binutils' DWARF handling to support embedded source
  code, specifically by adding `DW_LNCT_source` and `DW_LNCT_LLVM_source` content
  types. This affects how `objdump` interprets and displays DWARF line number information.
  The patch likely requires changes to `dwarf.c` and related test infrastructure.
primer_general: DWARF is a debugging data format used to store information about a
  program's source code, variables, and other debugging-related information. `objdump`
  is a binutils tool that displays information from object files, including debugging
  information. This patch extends `objdump` to extract and display embedded source
  code directly from the DWARF information, which can be useful when the source code
  is not readily available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

This patch enables objdump to print embedded source code stored within DWARF debugging information. It adds new content types to DWARF and modifies objdump to handle them. The patch includes new test cases and has undergone initial review.
