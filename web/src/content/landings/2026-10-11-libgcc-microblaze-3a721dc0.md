---
project: gcc
subsystem: libgcc/microblaze
patch_id: null
tags:
- libgcc
- microblaze
- bugfix
- assembly
commit_hash: 3a721dc0238851e1d58d1cbf74c1164ca1aa21fa
source_type: github
author: Sam Price
headline: 'Microblaze: Fix hand-written 64-bit signed modulo implementation'
tldr: Corrects a long-standing bug in the Microblaze libgcc's 64-bit signed modulo
  function, fixing issues with negative divisors and LLONG_MIN.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `libgcc/config/microblaze/moddi3.S` file contains a hand-written
  assembly implementation for the 64-bit signed division remainder function (`__moddi3`).
  This function was found to be incorrect for various inputs, especially with `LLONG_MIN`
  and negative divisors, and did not account for both big-endian and little-endian
  Microblaze variants (which emerged in GCC 4.8). This patch, based on an existing
  OpenADK patch, rectifies several issues: register ordering based on endianness,
  correct sign handling for the remainder (which should match the dividend''s sign),
  proper clearing of return regi…'
primer_glossary:
- term: libgcc
  definition: The GCC runtime library, which provides essential functions such as
    integer arithmetic, floating-point operations, and exception handling that are
    not directly implemented by the target architecture's instruction set or are too
    complex to generate inline.
- term: Microblaze
  definition: A soft processor core from Xilinx, typically used in FPGAs. It is a
    32-bit RISC soft core with options for features like MMU, FPU, and cache.
- term: 64-bit signed modulo
  definition: The operation of finding the remainder of a division between two 64-bit
    signed integers. In C/C++, the sign of the remainder typically matches the sign
    of the dividend.
- term: Endianness
  definition: The order in which bytes of a multi-byte data word are stored in computer
    memory. Big-endian stores the most significant byte first, while little-endian
    stores the least significant byte first.
- term: LLONG_MIN
  definition: The smallest representable value for a signed long long integer type,
    typically defined in `<limits.h>`.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3a721dc0238851e1d58d1cbf74c1164ca1aa21fa
date: '2026-10-11'
is_stub: false
stub_reason: ''
---

This commit fixes a critical bug in the hand-written 64-bit signed modulo function (`moddi3.S`) for the Microblaze architecture, which had been present since 2010. The original implementation suffered from multiple defects, including incorrect handling of byte order (endianness), a negated high word for negative divisors, incorrect sign determination for the remainder, and a non-terminating loop for `LLONG_MIN` dividends. The fix addresses these issues by using endian-aware macros, correcting the sign logic, ensuring correct return registers, and preventing the infinite loop.
