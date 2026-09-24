---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- gas
- refactoring
- instruction encoding
discussion_id: 20260924015023.36799-3-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3 4/4] microblaze: use md_number_to_chars in md_assemble too'
headline: 'microblaze: use md_number_to_chars in md_assemble too'
tldr: Replaces raw byte assignments with `md_number_to_chars` in MicroBlaze's `md_assemble`
  for cleaner instruction encoding.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves code readability and maintainability by using a standard function (`md_number_to_chars`)
  instead of manual byte manipulation.
- Removes unused macros, simplifying the codebase.
exchanges: []
primer_expert: This patch, the fourth in a series, refactors `md_assemble` in `gas/config/tc-microblaze.c`
  by replacing manual byte-by-byte instruction word assembly with calls to `md_number_to_chars`.
  This follows the approach taken in the previous patch for `md_apply_fix`. The six
  remaining hardcoded instruction word assembly sites are converted, and the `INST_BYTE`
  macros are deleted. The `INST_IMM_OFFSET` macro is retained as `md_number_to_chars`
  doesn't handle immediate field offsets correctly on its own. Testing confirms no
  functional change across both MicroBlaze endiannesses.
primer_glossary:
- term: md_assemble
  definition: A function within the MicroBlaze backend that handles the assembly of
    instructions into machine code.
- term: md_number_to_chars
  definition: A generic BFD function that converts a numerical value into a sequence
    of bytes in the target's endianness, suitable for writing to an object file.
- term: INST_BYTE0
  definition: A macro that extracts the most significant byte (or least significant,
    depending on endianness) of a 32-bit instruction word.
- term: INST_IMM_OFFSET
  definition: A macro or constant that specifies the offset within an instruction
    word where the immediate field is located. This is important for relocations that
    modify immediate values.
- term: Endianness
  definition: The order in which bytes of a multi-byte data word are stored in computer
    memory. Little-endian stores the least significant byte first, while big-endian
    stores the most significant byte first.
series_id: 'binutils:microblaze: use md_number_to_chars in md_assemble too'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924015023.36799-3-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch continues the cleanup of MicroBlaze instruction encoding by replacing six instances of direct byte assignments within the `md_assemble` function with calls to `md_number_to_chars`. These direct assignments were effectively equivalent to a four-byte store in the target's byte order. By using `md_number_to_chars`, the code becomes more concise and consistent with other backends. The associated macros for individual bytes (`INST_BYTE0` through `INST_BYTE3`) are removed as they are no longer used. This change is intended to have no functional impact and has been verified across test suites for both big-endian and little-endian MicroBlaze configurations.
