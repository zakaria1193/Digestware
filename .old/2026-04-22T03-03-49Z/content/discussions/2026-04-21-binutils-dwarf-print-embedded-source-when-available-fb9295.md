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
tldr: This patch enables objdump to print embedded source code from DWARF debug information,
  and includes a test case.
stakes: This feature enhances debugging capabilities by allowing developers to view
  the original source code directly within objdump, particularly useful when source
  files are unavailable or when analyzing stripped binaries with embedded debug information.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch is in its third version, suggesting ongoing improvements
  and addressing issues. The reviewer's request for the original commit message indicates
  a desire for better understanding and integration.
technical_tradeoffs:
- Adding support for embedded source increases the complexity of `objdump`.
- Extracting and printing embedded source might increase the execution time of `objdump`.
- The size of the binary might increase if it includes embedded source code.
exchanges:
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Submits version 3 of the patch, including a fix for a failing test on
    aarch64 and apologizing for the inconvenience.
  quote: 'v3 should contain a test that passes on aarch64 as well as x86_64. Sorry

    for the hassle!'
- author: Jens Remus <jremus@linux.ibm.com>
  role: reviewer
  position: Requests that the original commit message from v1 be included for better
    context and understanding.
  quote: 'it would be helpful if you could keep the original commit

    message from v1 of your patch (except for the last two paragraphs),

    including the description and motivation, and place any additional

    comments below the three dashes (as you did with the patch changelog).'
primer_expert: This patch modifies `binutils/dwarf.c` to enable printing of embedded
  source code from DWARF debug information, specifically from the `.debug_line` section
  where line number information is stored. The patch adds support for `DW_LNCT_source`
  and `DW_LNCT_LLVM_source` content types. Embedded source code allows debuggers to
  display source even when the original source files are not present. A new test case,
  `dwarf-embedded-source.S`, is added to verify the functionality.
primer_general: DWARF is a debugging format used to store information about a program's
  source code, variables, and functions within the compiled binary or in a separate
  debug file. `objdump` is a command-line utility that displays various information
  about object files, including disassembled code and debugging information. This
  patch enhances `objdump` to be able to extract and display source code that is embedded
  directly within the DWARF debugging information. This is useful in situations where
  the original source code files are not available, allowing developers to still see
  the source code corresponding to the disassembled instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260421020204.2759264-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-04-21'
---

Will Hawkins proposes a patch to add the ability for `objdump` to print embedded source code directly from DWARF debug information. The patch includes a new test case and fixes a failing test on aarch64. The author also apologizes for the inconvenience caused by the failing test in previous versions.
