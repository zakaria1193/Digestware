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
tldr: The patch adds support to objdump to print embedded source code from DWARF debug
  information.
stakes: Allows developers to inspect embedded source code directly from the executable,
  which is useful for debugging and reverse engineering.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in `binutils/dwarf.c` to handle embedded source.
- Potential increase in `objdump` output size when embedded source is present.
exchanges: []
primer_expert: DWARF line tables can embed source code. This patch modifies `binutils/dwarf.c`
  to extract and print such embedded source when using `objdump`. The relevant DWARF
  line number table content types are `DW_LNCT_source` and `DW_LNCT_LLVM_source`.
primer_general: DWARF is a debugging data format used to describe the structure and
  contents of compiled programs.  It includes information like source file names,
  line numbers, and variable types.  This patch extends `objdump`, a tool for inspecting
  object files, to extract and display source code embedded directly within the DWARF
  debugging information. This allows developers to see the original source code that
  corresponds to the compiled machine code directly within `objdump`'s output.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

Will Hawkins proposes a patch to `binutils/dwarf.c` that enables `objdump` to print embedded source code when it's available in the DWARF debug information. The patch adds new tests and modifies the `dwarf.c` file to handle the `DW_LNCT_source` and `DW_LNCT_LLVM_source` content types.
