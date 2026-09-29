---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- binutils
- testsuite
- debug
- compression
- dwarf
discussion_id: 20260928090146.4016188-4-tobias.deiminger@linutronix.de
source_type: public_inbox
title: '[PATCH 3/3] binutils/testsuite: test compress-debug-info round trip'
headline: 'binutils/testsuite: test compress-debug-info round trip'
tldr: Adds a test case to verify debug info compression and decompression in Binutils.
proposer: Tobias Deiminger <tobias.deiminger@linutronix.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Achieving broad test coverage requires generating object files for numerous target
  formats, which can increase test execution time.
- The test design relies on `objdump --dwarf=info` to validate debug information,
  assuming this tool accurately reflects the compressed/decompressed state.
exchanges:
- author: Tobias Deiminger
  role: proposer
  position: Adds a comprehensive test case to the binutils test suite to validate
    the compress/decompress round trip for debug information across multiple BFD targets.
  quote: "This adds a new test case that basically runs\n\n target_cc testprog.c testprog\n\
    \ for every enabled BFD target\n   objcopy -I <host> -O <target> testprog  # reformat\
    \ to target\n   objcopy --compress-debug-sections       # compress\n   objdump\
    \ --dwarf=info                    # main()/fn() info expected\n   objcopy --decompress-debug-sections\
    \     # decompress\n   objdump --dwarf=info                    # m…"
primer_expert: This patch adds a new test case to the binutils testsuite (`binutils-all/compress.exp`)
  that thoroughly exercises the debug section compression and decompression functionality
  for various BFD target formats. It involves generating test programs, reformatting
  them to different targets using `objcopy`, applying `--compress-debug-sections`,
  and then verifying the integrity of DWARF debug information using `objdump --dwarf=info`
  both pre- and post-decompression. This test is crucial for ensuring the reliability
  of debug information handling, especially when combined with the bug fixes in the
  acco…
primer_glossary:
- term: binutils testsuite
  definition: A collection of automated tests used to verify the correct functionality
    of the GNU Binutils suite of tools.
- term: compress-debug-info round trip
  definition: The process of compressing debug information within an executable, then
    decompressing it, and verifying that the original debug information is preserved.
- term: BFD target formats
  definition: The various executable and object file formats that the Binary File
    Descriptor (BFD) library supports, such as ELF, COFF, PE, etc.
- term: objdump
  definition: A GNU Binutils utility that displays information from object files,
    including symbol tables, section headers, and disassembly.
- term: DWARF
  definition: Debugging With Attributed Record Formats, a standardized, widely used
    format for debugging information embedded in executable files.
series_id: 'binutils:binutils/testsuite: test compress-debug-info round trip'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260928090146.4016188-4-tobias.deiminger@linutronix.de
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Tobias Deiminger introduces a new test case for the binutils test suite designed to verify the round-trip process of compressing and decompressing debug information. The test generates object files for various BFD target formats, compresses their debug sections, and then verifies the debug info using `objdump --dwarf=info` both before and after decompression, aiming for broad coverage across different targets.
