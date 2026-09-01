---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- dwarf
- testing
- xtensa
commit_hash: 6bbfbcceb8bd97a6c15da630578f20f9a86d5961
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: binutils dw5 test
tldr: Fixes a test case for binutils' handling of DWARF 5 debug information.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates the `dw5.W` test case in binutils to pass for the
  xtensa-lx106-elf target. The failure was due to the `readelf -wiaoRlL dw5` command
  expecting specific `uleb128` padding that was not being accounted for. The fix adjusts
  the test's expected output to accommodate this padding, improving test coverage
  for DWARF 5 location list parsing.
primer_glossary:
- term: DWARF 5
  definition: The fifth version of the DWARF debugging data format, used by compilers
    and debuggers to represent program information for debugging.
- term: xtensa-lx106-elf
  definition: A specific target triple for the Xtensa LX6 microcontroller, often used
    in ESP8266 Wi-Fi modules, configured for bare-metal development (ELF).
- term: readelf
  definition: A utility that displays information about ELF files, including details
    about symbols, sections, and debugging information.
- term: uleb128
  definition: Unsigned LEB128 (Little-Endian Base 128) is a variable-length encoding
    format used in DWARF for representing unsigned integers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260901021356.8CD3A4BA23FE@sourceware.org
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

This commit corrects a test case for binutils, specifically for the xtensa-lx106-elf target, that was failing when running `readelf -wiaoRlL dw5`. The fix allows for `uleb128` padding in the `dw5.W` test file, ensuring more robust testing of DWARF 5 debug information processing.
