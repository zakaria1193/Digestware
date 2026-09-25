---
project: binutils
subsystem: binutils/microblaze
patch_id: null
tags:
- microblaze
- assembler
- code-refactor
commit_hash: 0dabe1eeb6d85e5081b5014d8c1b98edba74251a
source_type: public_inbox
author: Michael Eager <eager@sourceware.org>
headline: MicroBlaze assembler uses md_number_to_chars for instruction assembly
tldr: MicroBlaze assembler simplifies instruction word generation, improving consistency
  and potentially performance.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gas/config/tc-microblaze.c`, the explicit byte-by-byte assembly
  of instruction words using `INST_BYTE0` through `INST_BYTE3` macros has been replaced
  with calls to `md_number_to_chars`. This function handles writing integer values
  to memory in the target's byte order. The change removes dead macros and simplifies
  the `md_assemble` function, which is called for every instruction, ensuring consistency
  with other backends that use similar helpers.
primer_glossary:
- term: md_assemble
  definition: A function within an assembler's backend that is responsible for converting
    an instruction mnemonic and its operands into the machine code representation.
- term: md_number_to_chars
  definition: A utility function, common in assembler backends, that converts an integer
    value into a sequence of bytes according to the target's endianness and desired
    word size.
- term: endianness
  definition: The order in which a machine's memory stores the bytes of a multi-byte
    word. Big-endian stores the most significant byte first, while little-endian stores
    the least significant byte first.
- term: gas
  definition: GNU Assembler. The assembler component of the GNU Binutils package.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260924153107.EF5B348727FE@sourceware.org
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

The MicroBlaze assembler now uses the `md_number_to_chars` function to assemble instruction words, replacing manual byte assignments. This change simplifies the code by consolidating logic for writing instruction bytes in the target's native endianness and removes unused macros. It aims for a functional no-op but enhances code clarity and maintainability.
