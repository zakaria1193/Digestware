---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- middle-end
- avr
- bugfix
- compiler
commit_hash: b7fbc9e1a4ebb2f7f52dff4b8a57309847aaa90d
source_type: github
author: Philipp Tomsich
headline: Fix buffer overflow in synth_mult for AVR multiplication.
tldr: Corrects a buffer overflow in `synth_mult` when generating code for AVR constant
  multiplication.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `synth_mult` function, when processing a sub-algorithm exceeding
  `MAX_BITS_PER_WORD`, writes to `op[MAX_BITS_PER_WORD]` and `log[MAX_BITS_PER_WORD]`.
  This causes an alias to `log`'s shift counts and an out-of-bounds write for `log`.
  This patch resizes both `op` and `log` arrays within `struct algorithm` to prevent
  this overflow, which is triggered on AVR at `-O1/-O2` for `uint32_t` multiplication
  by dense constants like `0xaaab`.
primer_glossary:
- term: synth_mult
  definition: A function within GCC's middle-end that synthesizes multiplication operations,
    likely for optimizing constant multiplications.
- term: AVR
  definition: A family of microcontrollers manufactured by Atmel (now Microchip Technology).
    GCC supports targeting these microcontrollers.
- term: buffer overflow
  definition: A condition where a program attempts to write data beyond the allocated
    buffer boundaries, potentially corrupting adjacent memory and causing crashes
    or security vulnerabilities.
- term: MAX_BITS_PER_WORD
  definition: A constant likely defining the maximum number of bits or operations
    handled within a single 'word' or intermediate step during the synthesis of multiplication.
- term: struct algorithm
  definition: A data structure used internally by GCC to represent a sequence of operations
    or an algorithmic step, likely related to optimization passes.
- term: dense constant
  definition: A constant value that is used in a multiplication, where the constant
    itself has many bits set, requiring complex operations to represent.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b7fbc9e1a4ebb2f7f52dff4b8a57309847aaa90d
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

This commit addresses a buffer overflow vulnerability in the `synth_mult` function, which is used for generating code for constant multiplication on the AVR target. The overflow occurred when transient arrays `op` and `log` were written beyond their allocated bounds. This patch resizes these arrays to accommodate the appended operation, preventing data corruption and ensuring correct compilation for specific AVR multiplications.
