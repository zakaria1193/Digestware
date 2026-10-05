---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- testsuite
- windows
- cross-platform
discussion_id: 20261004221717.235487-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] gas: testsuite: Fix gas/all/pr27381 test case on Windows/MSYS2.'
headline: 'gas: testsuite: Fix gas/all/pr27381 test case on Windows/MSYS2.'
tldr: Fixes a gas test case for the .incbin directive to correctly handle error messages
  on Windows.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Adjusting test case error messages for cross-platform compatibility versus maintaining
  strict POSIX-like error reporting.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Fixes the `gas/all/pr27381` test case by updating the expected error message
    regex and the directory used with the `.incbin` directive to accommodate Windows/MSYS2
    behavior.
  quote: null
primer_expert: This patch modifies a test case in `gas/testsuite/gas/all/pr27381`
  to ensure consistent behavior across different operating systems. The `.incbin`
  directive's handling of directories differs between POSIX and Windows due to `fopen()`
  behavior, resulting in distinct error messages. This change harmonizes the test's
  expected output on Windows/MSYS2.
primer_glossary:
- term: gas
  definition: The GNU Assembler, which translates assembly language code into machine
    code.
- term: .incbin
  definition: An assembler directive used to include the raw binary contents of a
    file into the assembled output.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
- term: MSYS2
  definition: A software distribution and building platform for Windows, providing
    a POSIX-like command-line environment.
- term: fopen()
  definition: A C standard library function used to open a file stream. Its behavior
    can differ slightly between operating systems, especially regarding permissions
    for directories.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261004221717.235487-1-jdx@o2.pl
bugzilla_url: null
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

This patch adjusts the error message regular expression and the target directory in a gas test case (`pr27381`) to ensure it passes on Windows/MSYS2. The change accounts for differing behavior in `fopen()` between POSIX systems and Windows when attempting to include a directory with the `.incbin` directive, harmonizing the expected error output.
