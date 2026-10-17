---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- relaxation
- bfd
- elf
- testing
discussion_id: 20261016123644.1429854-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 2/8] bfd: check relaxation delete ranges in simple ELF backends'
headline: 'bfd: check relaxation delete ranges in simple ELF backends'
tldr: Adds unified range checking for ELF relaxation byte deletion to 13 backends
  and introduces shared test helpers.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Standardizes safety checks across multiple ELF backends, reducing code duplication.
- Increases robustness by preventing potential heap corruption issues.
- Introduces new testing infrastructure and specific regression tests.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Introduces `_bfd_elf_relax_delete_range_ok` and applies it to 13 ELF backends,
    adding shared test infrastructure.
  quote: 'Validate relaxation deletion bounds in 13 ELF backends using

    _bfd_elf_relax_delete_range_ok before memmove: CR16, CRX, FT32,

    H8/300, IP2K, M10200, M10300, M32C, MIPS, MSP430, PRU, SH, and V850.


    Add shared relaxation test helpers to ld/testsuite/lib/ld-lib.exp

    (ld_write_hex_object, ld_relax_run_capture, ld_test_relax_valid,

    ld_test_relax_underflow), and add DejaGnu regression tests for

    CRX and H8…'
primer_expert: This patch introduces a common safety mechanism, `_bfd_elf_relax_delete_range_ok`,
  into the BFD library's ELF support. This function validates the parameters for byte
  deletion during linker relaxation, preventing underflows that could lead to heap
  corruption. It is applied to a significant number of ELF backends, standardizing
  this safety check. Furthermore, it establishes shared testing utilities in `ld/testsuite/lib/ld-lib.exp`
  and adds specific regression tests for CRX and H8/300 relaxation underflows.
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: memmove
  definition: A C standard library function that copies a block of memory from a source
    location to a destination location. It handles overlapping memory regions safely.
- term: regression test
  definition: A test designed to detect whether a recent change to a program has adversely
    affected existing functionality, often by re-running tests that previously passed.
series_id: 'binutils:bfd: check relaxation delete ranges in simple elf backends'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch introduces a shared helper function, `_bfd_elf_relax_delete_range_ok`, to validate bounds before deleting bytes during linker relaxation. This check is applied to 13 ELF backends including CR16, CRX, FT32, H8/300, IP2K, M10200, M10300, M32C, MIPS, MSP430, PRU, SH, and V850. Additionally, new shared relaxation test helpers are added to `ld/testsuite/lib/ld-lib.exp`, and specific regression tests for CRX and H8/300 are included.
