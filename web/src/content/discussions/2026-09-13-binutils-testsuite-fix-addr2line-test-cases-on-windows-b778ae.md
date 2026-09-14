---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- testing
- Windows
- cross-platform
- patch
discussion_id: 20260913163802.130948-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] binutils: testsuite: Fix add2line test cases on Windows.'
headline: 'binutils: testsuite: Fix addr2line test cases on Windows'
tldr: Patch fixes addr2line test cases on Windows by addressing path format differences
  and GCC's symbol naming conventions.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adapting tests for Windows compatibility adds complexity but ensures broader test
  suite coverage and reliability.
- Handling platform-specific behaviors (like path formats or symbol mangling) is necessary
  for robust cross-platform development.
- The choice of test scripting language (e.g., Tcl for `exp` files) affects how platform
  differences can be programmatically managed.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Submits a patch to correct `addr2line` test cases on Windows by handling
    path formats and GCC symbol naming.
  quote: 'The following two test cases fail on Windows:

    [...] FAIL: addr2line

    FAIL: addr2line -f option

    ...'
primer_expert: 'This patch addresses cross-platform testing issues within the Binutils
  test suite, specifically for the `addr2line` utility when run on Windows. The core
  problems are: 1) Path canonicalization differences between native Windows paths
  (drive letters) and the UNIX-like paths often used in build environments like MSYS/MinGW,
  and 2) Target-specific symbol mangling, exemplified by the `h8300-*-elf` target
  which prepends an underscore to symbols. The patch modifies the `addr2line.exp`
  test script to dynamically adjust for these variations, ensuring test reliability
  across different environments.'
primer_glossary:
- term: addr2line
  definition: A command-line utility that translates addresses into line numbers and
    function names, useful for debugging.
- term: Test suite
  definition: A collection of tests designed to verify the correctness of a software
    program.
- term: Windows
  definition: Microsoft's proprietary graphical operating system.
- term: MSYS/MinGW
  definition: Environments providing a POSIX-like shell and development tools on Windows,
    often used for compiling software originally developed for Unix-like systems.
- term: Symbol naming
  definition: The process by which compilers and linkers generate names for functions,
    variables, and other entities. Different targets or compiler versions may use
    different naming conventions (mangling).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913163802.130948-1-jdx@o2.pl
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

Jan Dubiec submits a patch to fix failing `addr2line` test cases on Windows within the Binutils test suite. The failures stem from two main issues: 1) `nm` on Windows uses DOS-style paths (e.g., `C:/`), while the test suite expects UNIX-style paths, and 2) certain GCC targets (like `h8300-*-elf`) prepend an underscore to symbol names, which the tests did not account for. The patch modifies the `addr2line.exp` test script to handle these platform-specific differences.
