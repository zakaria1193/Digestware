---
project: gcc
subsystem: avr/libgcc
patch_id: null
tags:
- avr
- libgcc
- code size
commit_hash: c033e4be4953b5924a67a2aad7fb3131704fa29c
source_type: github
author: Georg-Johann Lay
headline: 'AVR: Use more .branch_plus in lib1funcs.S'
tldr: Replaces some jump instructions with `.branch_plus` in AVR libgcc functions,
  potentially improving code density.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit targets two specific 64-bit multiplication routines in
  GCC''s AVR libgcc implementation: `__mulqihi3` (multiply quard-precision integer
  by half-precision) and `__mulsidi3` (multiply signed double-precision integer by
  signed integer). It replaces standard branch instructions with the `.branch_plus`
  pseudo-instruction. On AVR architectures, `.branch_plus` can sometimes generate
  more compact code than unconditional branches, especially when the target is close,
  potentially reducing code size for these multiplication functions.'
primer_glossary:
- term: AVR
  definition: A Reduced Instruction Set Computing (RISC) architecture developed by
    Atmel (now Microchip Technology) for microcontrollers. Common in embedded systems.
- term: libgcc
  definition: The GCC runtime library, which contains low-level functions (like software
    floating-point emulation, integer multiplication, exception handling) needed by
    compiled C/C++ code when hardware support is insufficient or unavailable.
- term: .branch_plus
  definition: A pseudo-instruction or assembler directive, likely specific to certain
    architectures or assemblers, that generates a relative branch instruction. It
    may offer advantages in code size or speed by encoding the branch displacement
    more efficiently than a standard jump.
- term: __mulqihi3
  definition: A GCC libgcc function name indicating a software implementation for
    multiplying a quard-precision integer (likely 64-bit) by a half-precision integer
    (likely 32-bit).
- term: __mulsidi3
  definition: A GCC libgcc function name indicating a software implementation for
    multiplying a signed 's' integer by a signed 'i' integer, resulting in a double-precision
    (likely 64-bit) product.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c033e4be4953b5924a67a2aad7fb3131704fa29c
date: '2026-07-22'
is_stub: true
stub_reason: low_score
---

The AVR `lib1funcs.S` file has been updated to use the `.branch_plus` pseudo-instruction in two additional functions: `__mulqihi3` and `__mulsidi3`. This change, along with minor comment adjustments, aims to optimize code generation for these multiplication functions on AVR microcontrollers by leveraging a more compact branching mechanism.
