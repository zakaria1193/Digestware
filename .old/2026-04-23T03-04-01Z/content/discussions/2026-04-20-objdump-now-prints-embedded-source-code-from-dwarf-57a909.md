---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- objdump
- dwarf
- embedded source
- debugging
- binutils
discussion_id: 20260420143919.2721336-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] binutils/dwarf: Print embedded source, when available'
headline: Objdump now prints embedded source code from DWARF
tldr: Objdump can now extract and display embedded source code stored in DWARF debugging
  information.
stakes: Improves debugging experience by allowing developers to view source code directly
  from the executable, especially useful when source files are unavailable.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased binary size due to embedding source code in DWARF.
- Potential performance impact when extracting and displaying embedded source code.
- Requires compilers and build systems to generate DWARF with embedded source code.
exchanges:
- author: Will Hawkins
  role: proposer
  position: Proposes a patch to enable objdump to print embedded source code from
    DWARF, enhancing debugging when source files are unavailable.
  quote: 'I sincerely appreciate the first round of feedback and hope that I responded
    to all the feedback.


    I am clearly new to writing tests and hope that my cargo cult-ing is on

    the right track.'
primer_expert: This patch modifies `binutils/dwarf.c` to handle `DW_LNCT_source` and
  `DW_LNCT_LLVM_source` content types in DWARF line number tables. These content types
  indicate that source code is embedded directly within the DWARF information. The
  patch adds logic to extract and display this embedded source code when using objdump.
  This is particularly relevant for binaries built with link-time optimization (LTO)
  or when using build systems that embed source code for reproducibility.
primer_general: When you compile code, debugging information is often generated to
  help you understand the relationship between the compiled machine code and your
  original source code. This debugging information can be stored in a standard format
  called DWARF.  Sometimes, the actual source code itself is embedded within the DWARF
  information. This patch updates the `objdump` tool, which is used to inspect object
  files and executables, to extract and display this embedded source code. This is
  helpful when you no longer have access to the original source files, as you can
  still view the code directly from the compiled program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260420143919.2721336-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-20'
---

This patch enhances objdump to extract and print embedded source code stored within DWARF debugging information. This is particularly useful when the original source files are missing or inaccessible, as it allows developers to view the code directly from the executable or object file. This patch includes new tests and updates to the dwarf.c file to support this functionality.
