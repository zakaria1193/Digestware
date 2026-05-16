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
discussion_id: 20260516001043.422461-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v5] binutils/dwarf: Print embedded source, when available'
headline: 'binutils/dwarf: Print embedded source, when available'
tldr: Extends objdump to print embedded source code from DWARFv5 debug information,
  if present.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased objdump complexity to support a new DWARFv5 feature.
- Potential performance impact due to additional data processing in objdump.
exchanges: []
primer_expert: DWARFv5 allows embedding source code directly within the debugging
  information.  This patch modifies `binutils/dwarf.c` to recognize and display the
  `DW_LNCT_source` and `DW_LNCT_LLVM_source` content types in the line number program
  tables.  The primary file is `binutils/dwarf.c`, with test cases in `binutils/testsuite/binutils-all/`.
  This feature is useful when the original source files are unavailable.
primer_general: DWARF (Debugging With Attributed Record Formats) is a standard used
  by debuggers to locate variables, functions, and source code lines within a compiled
  binary.  It bridges the gap between compiled code and the original source code,
  making debugging possible.  The objdump utility displays various information from
  object files, including disassembled code and debugging information. This patch
  enhances objdump to extract and display source code embedded directly within the
  DWARF debugging information, which can be useful when the original source files
  are not readily accessible.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260516001043.422461-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This patch modifies objdump to extract and print embedded source code stored in DWARFv5 debugging information. The patch iterates on previous versions by fixing issues such as incorrect bitwise operations, formatting problems, scoping issues, and test case compatibility. This enhancement allows developers to view the original source code directly from the disassembled object file, which simplifies debugging and reverse engineering, especially when source files are missing.
