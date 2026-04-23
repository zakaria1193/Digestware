---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- binutils
- dwarf
- objdump
- embedded source
- debugging
discussion_id: 20260420143919.2721336-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] binutils/dwarf: Print embedded source, when available'
headline: 'binutils/dwarf: Print embedded source, when available'
tldr: This patch enables objdump to display embedded source code from DWARF debug
  information, if present.
stakes: This feature allows developers to view source code directly from objdump output,
  simplifying debugging and reverse engineering.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in the `objdump` tool.
- Potential increase in the size of `objdump` output.
- Adds a dependency on the availability of embedded source code in the DWARF information.
exchanges:
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Submits version 2 of the patch, addressing feedback from the previous
    round and expressing uncertainty about the test writing approach.
  quote: 'I sincerely appreciate the first round of feedback and hope that I

    responded to all the feedback.


    I am clearly new to writing tests and hope that my cargo cult-ing is on

    the right track.'
primer_expert: This patch modifies `binutils/dwarf.c` to recognize and display embedded
  source code within DWARF line number tables. It handles the `DW_LNCT_source` and
  `DW_LNCT_LLVM_source` content types, which indicate the presence of embedded source.
  The changes affect how `objdump` interprets and presents DWARF information, specifically
  when dealing with binaries compiled with embedded source code.
primer_general: DWARF is a debugging data format used to describe the structure and
  contents of executables and shared libraries. It includes information such as source
  code locations, variable types, and function definitions.  `objdump` is a tool that
  displays various information from object files, including the contents of DWARF
  sections.  This patch extends `objdump` to extract and display source code that
  has been embedded directly within the DWARF information during compilation. This
  allows developers to see the original source code directly when examining the disassembled
  output of a program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

This patch enhances `objdump` to print embedded source code when available in DWARF debug information.  It adds support for the `DW_LNCT_source` and `DW_LNCT_LLVM_source` content types in DWARF line number tables. The patch introduces a new test case and updates the `objdump.exp` test suite to verify the new functionality.
