---
project: binutils
subsystem: binutils/microblaze
patch_id: null
tags:
- microblaze
- assembler
- relocation
- code-refactor
commit_hash: 5047dd4a3a208ff158bb48b5343ed7d392d76fba
source_type: public_inbox
author: Michael Eager <eager@sourceware.org>
headline: MicroBlaze assembler uses md_number_to_chars for apply_fix
tldr: MicroBlaze assembler simplifies relocation fixup handling using a standard utility
  function.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gas/config/tc-microblaze.c`, the manual construction of relocation
  fixups using bitwise OR operations (`|=`) and direct byte assignments has been replaced
  by calls to `md_number_to_chars`. For data relocations, this simplifies the code
  to a single call. For instruction relocations, where immediate fields have specific
  offsets within the instruction word, `md_number_to_chars` is used in conjunction
  with an `INST_IMM_OFFSET` macro to correctly handle both byte ordering and the immediate
  field's position, similar to how Mips handles it.
primer_glossary:
- term: md_apply_fix
  definition: A function in an assembler's backend responsible for applying relocation
    information to an object file, adjusting values based on symbol addresses and
    relocation types.
- term: md_number_to_chars
  definition: A utility function, common in assembler backends, that converts an integer
    value into a sequence of bytes according to the target's endianness and desired
    word size.
- term: relocation
  definition: A process performed by the linker or assembler to adjust memory addresses
    in code or data. It resolves references to symbols that are not yet known at compile
    or assembly time.
- term: endianness
  definition: The order in which a machine's memory stores the bytes of a multi-byte
    word. Big-endian stores the most significant byte first, while little-endian stores
    the least significant byte first.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260924153057.B790B48A0832@sourceware.org
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

The MicroBlaze assembler's relocation handling has been refactored to use the `md_number_to_chars` function, replacing manual bitwise operations for writing data and instruction relocations. This change unifies the implementation with other backends and simplifies code for handling byte order and immediate field placement, aiming for code clarity without functional changes.
