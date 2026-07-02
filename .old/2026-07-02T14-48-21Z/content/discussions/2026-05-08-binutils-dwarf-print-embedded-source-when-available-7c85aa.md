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
discussion_id: 20260508112818.47023-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v4] binutils/dwarf: Print embedded source, when available'
headline: 'Binutils/dwarf: Print embedded source, when available'
tldr: This patch adds support for printing embedded source code from DWARFv5 debugging
  information using objdump.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the size of the objdump binary due to added functionality.
- Relies on the availability of DWARFv5 debugging information with embedded source
  code.
exchanges: []
primer_expert: This patch adds support for the DW_LNCT_source line number entry type
  in DWARFv5, which allows embedding source code directly in the debugging information.  The
  patch modifies `binutils/dwarf.c` to handle this new entry type and adds a test
  case in `binutils/testsuite/binutils-all/dw5-embedded-source.S` and `.d` to verify
  the functionality. This is useful in environments where the original source files
  are not readily available.
primer_general: DWARF (Debugging With Attributed Records Format) is a debugging data
  format used by compilers and debuggers to provide information about the source code
  location of machine code instructions.  This patch extends the objdump utility to
  extract and display source code embedded within the DWARF debugging information,
  providing a more complete debugging experience.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260508112818.47023-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-08'
---

Will Hawkins proposes a patch to enhance objdump to print embedded source code directly from DWARFv5 debugging information. The patch modifies dwarf.c, adds a new test case, and updates the testsuite. This allows developers to view the original source code embedded within the binary, which can be helpful for debugging and analysis.
