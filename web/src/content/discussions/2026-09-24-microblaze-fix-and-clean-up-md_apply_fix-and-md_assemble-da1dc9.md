---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- gas
- refactoring
- relocation
- testsuite
discussion_id: 20260924014435.30185-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3 0/4] microblaze: fix and clean up md_apply_fix and md_assemble'
headline: 'microblaze: fix and clean up md_apply_fix and md_assemble'
tldr: A series of patches cleaning up and fixing MicroBlaze assembly code related
  to relocations and instruction encoding.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Consolidates instruction encoding logic by using `md_number_to_chars` across `md_apply_fix`
  and `md_assemble`.
- Fixes test suite issues related to MicroBlaze endianness.
- Improves code maintainability and reduces potential for errors in manual byte manipulation.
exchanges: []
primer_expert: This series of patches targets the MicroBlaze backend in binutils.
  The primary goal is to refactor and fix issues in `md_apply_fix` and `md_assemble`.
  Patch 1/4 adds `BFD_RELOC_8` and `BFD_RELOC_16` support to `md_apply_fix`, using
  `md_number_to_chars`. Patch 2/4 converts the rest of `md_apply_fix` to use `md_number_to_chars`.
  Patch 4/4 does a similar conversion for `md_assemble`, replacing manual byte writes
  with `md_number_to_chars` and removing dead macros. Patch 3/4 is a testsuite fix
  for `gas.exp` that ensures MicroBlaze test exclusions apply to both endiannesses
  (`microblaze*-*-*`). The…
primer_glossary:
- term: md_apply_fix
  definition: A BFD function responsible for applying relocation fixups to data or
    code during the assembly process for a specific target architecture.
- term: md_assemble
  definition: A function within the MicroBlaze backend that handles the assembly of
    instructions into machine code.
- term: Relocation
  definition: The process of updating symbolic references in object code to their
    final memory addresses. Relocations are instructions for the linker or dynamic
    loader on how to modify addresses.
- term: md_number_to_chars
  definition: A generic BFD utility function that converts a number into a sequence
    of bytes respecting the target's endianness.
- term: Endianness
  definition: The order in which bytes of a multi-byte data word are stored in computer
    memory. Little-endian stores the least significant byte first, while big-endian
    stores the most significant byte first.
series_id: 'binutils:microblaze: fix and clean up md_apply_fix and md_assemble'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924014435.30185-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This is the cover letter for a four-patch series aimed at fixing and cleaning up the MicroBlaze backend's handling of relocations and instruction assembly. Patch 1/4 adds support for 8-bit and 16-bit relocations in `md_apply_fix` using `md_number_to_chars`. Patch 2/4 extends this refactoring to the remaining parts of `md_apply_fix`. Patch 4/4 cleans up `md_assemble` by replacing manual byte assignments with `md_number_to_chars` and removing unused macros. Patch 3/4, a testsuite-only change, corrects MicroBlaze test exclusions in `gas.exp` to work for both endiannesses. The series results in code simplification and resolves test failures, with no functional changes and identical test suite results before and after.
