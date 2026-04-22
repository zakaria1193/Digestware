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
tldr: objdump can now print embedded source code from DWARF debugging information,
  with aarch64 support.
stakes: Improves debugging experience by allowing developers to view source code directly
  from objdump output.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Under Review
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding embedded source increases the size of the debugging information.
- Displaying embedded source in objdump can increase the tool's complexity slightly.
- The patch improves debugging convenience, but requires compilers to embed the source
  code in the DWARF information.
exchanges:
- author: Will Hawkins
  role: proposer
  position: Announces v3 of the patch, which includes a fix for a failing test on
    aarch64.
  quote: v3 should contain a test that passes on aarch64 as well as x86_64. Sorry
    for the hassle!
- author: Jens Remus
  role: contributor
  position: Asks to keep the original commit message from v1.
  quote: 'Hello Will, it would be helpful if you could keep the original commit

    message from v1 of your patch (except for the last two paragraphs),

    including the description and motivation, and place any additional

    comments below the three dashes (as you did with the patch changelog).

    This should make it easier for everyone'
- author: Jan Beulich
  role: contributor
  position: Asks about testing on other targets, including 32-bit ones.
  quote: What about other targets, including 32-bit ones?
- author: Will Hawkins
  role: proposer
  position: Admits lack of testing on other targets and thanks for the feedback.
  quote: I, unfortunately, have not tested on that target, yet.
primer_expert: This patch modifies `binutils/dwarf.c` to extract and display embedded
  source code stored within DWARF debugging information. DWARF is a debugging data
  format used by compilers. The patch adds support for `DW_LNCT_LLVM_source` and `DW_LNCT_source`
  content types in DWARF line number tables. The changes also include a new test case
  (`binutils/testsuite/binutils-all/dwarf-embedded-source.S`) for verifying the functionality.
primer_general: When compiling code, debug information can be included in the executable
  or a separate file. DWARF is a standard format for this debug information, containing
  information like source file names, line numbers, and variable types. `objdump`
  is a command-line utility that displays information about object files, including
  executables and shared libraries. This patch extends `objdump` to extract and display
  the original source code embedded within the DWARF debugging information, making
  it easier to debug programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260421020204.2759264-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-21'
---

This patch enables `objdump` to print embedded source code directly from DWARF debugging information, when available. The patch includes a test case and fixes a failing test on aarch64. It introduces new DWARF line number content types for source code.
