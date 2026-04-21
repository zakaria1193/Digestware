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
tldr: This patch adds support to objdump to print embedded source code from DWARF
  debugging information, if available.
stakes: Allows developers to view the source code embedded within a binary using objdump,
  simplifying debugging and reverse engineering.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases the complexity of the objdump tool.
- Adds new dependencies on DWARF debugging information.
- May increase the size of the objdump executable.
exchanges: []
primer_expert: The patch modifies `binutils/dwarf.c` to enable `objdump` to display
  embedded source code stored in DWARF debugging information. This is achieved by
  handling the `DW_LNCT_source` and `DW_LNCT_LLVM_source` line table content types.
  The patch adds a new test file `dwarf-embedded-source.S` and updates `objdump.exp`
  to test the new functionality. Embedded source is a DWARF extension used to include
  source code directly in the binary.
primer_general: '`objdump` is a command-line tool for displaying various information
  about object files and executables, including disassembly, headers, and debugging
  information.  DWARF is a widely used debugging data format that provides mappings
  between machine code and source code.  This patch extends `objdump` to extract and
  display source code that has been embedded directly within the DWARF debugging information.  This
  can be useful when the original source files are unavailable, allowing developers
  to inspect the code directly from the compiled binary. DWARF line tables are used
  to map instruction offsets to source line numbers. This patch reads source code
  directly from the DWARF line table.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

This patch modifies objdump to print embedded source code directly from DWARF debugging information, assuming it exists. It adds new test cases and modifies the dwarf.c file to handle the new DWARF line content type DW_LNCT_source and DW_LNCT_LLVM_source.
