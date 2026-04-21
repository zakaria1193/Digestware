---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- binutils
- dwarf
- debugging
- objdump
- embedded source
discussion_id: 20260420143919.2721336-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] binutils/dwarf: Print embedded source, when available'
headline: 'Binutils/dwarf: Print embedded source, when available'
tldr: This patch enables objdump to print embedded source code from DWARF debugging
  information.
stakes: This feature enhances debugging capabilities by allowing developers to view
  the source code directly from the object file, improving the debugging workflow.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases the complexity of `objdump` by adding support for embedded source code.
- Improves debugging capabilities by allowing developers to view the source code directly
  from the object file.
- May increase the size of the object file if embedded source code is included in
  the DWARF information.
exchanges: []
primer_expert: DWARF debugging information can include embedded source code. This
  patch modifies `binutils/dwarf.c` to extract and display this embedded source when
  using `objdump`.  The changes involve adding new DWARF content types (DW_LNCT_source
  and DW_LNCT_LLVM_source) and updating the display logic in `display_formatted_table`.
primer_general: DWARF (Debugging With Arbitrary Record Format) is a widely used standard
  for representing debugging information in object files. This information maps executable
  code back to its original source code, enabling debuggers to set breakpoints, inspect
  variables, and step through the code. Sometimes, the source code itself is embedded
  within the DWARF information. This patch allows `objdump`, a tool for displaying
  information from object files, to extract and display this embedded source code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

This patch updates binutils to enable `objdump` to extract and print embedded source code stored within DWARF debugging information. The patch includes changes to `binutils/dwarf.c`, `include/dwarf2.h`, and adds new test files to verify the functionality.
