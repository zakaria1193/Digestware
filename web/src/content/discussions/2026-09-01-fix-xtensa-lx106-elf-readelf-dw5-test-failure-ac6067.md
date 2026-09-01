---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- xtensa
- debugging
- testsuite
discussion_id: apY0z2sDv2rkuK6U@squeak.grove.modra.org
source_type: public_inbox
title: binutils dw5 test
headline: Fix xtensa-lx106-elf readelf dw5 test failure
tldr: Allow for uleb128 padding in binutils dw5 test for xtensa-lx106-elf.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: null
primer_glossary:
- term: uleb128
  definition: Unsigned Little Endian Base 128. A variable-length encoding used in
    DWARF for unsigned integers.
- term: readelf
  definition: A utility that displays information about ELF files, including debugging
    information.
- term: DW_AT_location
  definition: DWARF attribute indicating the location of a variable or expression.
- term: .debug_info
  definition: DWARF section containing debugging information, such as variables, types,
    and functions.
- term: .debug_loclists
  definition: DWARF section containing location lists, which specify the address ranges
    where a variable is valid.
- term: .debug_rnglists
  definition: DWARF section containing range lists, used for various debugging information
    ranges.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/apY0z2sDv2rkuK6U@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch addresses a test failure in binutils for the xtensa-lx106-elf target when running `readelf -wiaoRlL dw5`. The failure is due to unexpected padding in uleb128 encoding within the debug information. The fix modifies the testsuite to accommodate this padding, ensuring the test passes.
