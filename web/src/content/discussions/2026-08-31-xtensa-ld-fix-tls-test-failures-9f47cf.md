---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- binutils
- xtensa
- linker
- TLS
- testsuite
discussion_id: 20260831155556.1721973-1-jcmvbkbc@gmail.com
source_type: public_inbox
title: '[COMMITTED] xtensa: ld: fix TLS test failures'
headline: 'xtensa: ld: fix TLS test failures'
tldr: 'Committed: Fixes to TLS test cases in ld for Xtensa target.'
proposer: Max Filippov <jcmvbkbc@gmail.com>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This commit fixes discrepancies in the linker test suite for Xtensa's
  TLS implementation. Specifically, it updates the expected addresses of the `.xtensa.info`
  section in `ld/testsuite/ld-xtensa/*.rd` files. These files are used to verify the
  linker's output against expected ELF section headers, and the addresses were no
  longer matching due to changes in section layout or linker behavior.
primer_glossary:
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows each thread in a multi-threaded
    program to have its own private copy of a variable.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: Xtensa
  definition: A configurable processor architecture widely used in embedded systems.
- term: .xtensa.info
  definition: A specific section in Xtensa executables that likely contains information
    related to the Xtensa architecture's features, possibly including TLS-related
    metadata.
- term: PROGBITS
  definition: An ELF section type indicating that the section contains data and should
    be included in the output file.
- term: NOTE
  definition: An ELF section type used to store arbitrary data, often used for platform-specific
    information or metadata.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260831155556.1721973-1-jcmvbkbc@gmail.com
bugzilla_url: null
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit addresses test failures in the linker (ld) for the Xtensa target related to Thread-Local Storage (TLS). The failures were due to incorrect addresses for the '.xtensa.info' section in the test output files. The patch updates the expected addresses in the `.rd` test files to match the actual output, resolving the discrepancies.
