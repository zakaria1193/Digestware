---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- risc-v
- x86
- pattern matching
commit_hash: c05164c348242b00b33cdf2988cc5e93d29b0478
source_type: github
author: Milan Tripkovic
headline: Improves sign-extension optimization for mask/subtract idiom
tldr: GCC now better optimizes a specific sign-extension pattern, resulting in more
  compact and efficient generated code for RISC-V and x86.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change enhances GCC's pattern matching capabilities within `match.pd`,
  specifically targeting the canonicalization of a sign-extension idiom. `match.pd`
  is a declarative language used in GCC to define target-independent and target-dependent
  instruction patterns, enabling the generator of RTL (Register Transfer Language)
  to match complex operations and optimize them into simpler, more efficient instruction
  sequences. The new pattern recognizes `(bitwise AND with low bits) - (bitwise AND
  with sign bit)`, allowing the compiler to convert this composite operation into
  a single-instruction si…
primer_general: Compilers like GCC work by translating high-level programming language
  code into machine code that a computer's processor can understand and execute. An
  important part of this process is 'optimization,' where the compiler tries to make
  the generated machine code as efficient as possible—meaning it runs faster and takes
  up less space. This commit improves how GCC optimizes a common operation called
  'sign extension.' Sign extension is used when converting a smaller number type (like
  an 8-bit integer) to a larger one (like a 32-bit integer) while preserving its signed
  value. Previously, GCC would generate a few instructions to perform this. Now, the
  compiler recognizes a specific way this operation is sometimes written as a combination
  of 'masking' and 'subtracting' bits. By recognizing this pattern, GCC can replace
  those multiple instructions with a single, dedicated sign-extension instruction
  provided by modern processors, making the resulting programs smaller and faster,
  particularly…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c05164c348242b00b33cdf2988cc5e93d29b0478
date: '2026-06-18'
is_stub: false
---

This commit introduces a new pattern to GCC's `match.pd` to recognize and optimize the sign-extension idiom `(x & low_bits) - (x & sign_bit)`. By canonicalizing this pattern, GCC can now generate significantly more efficient code for both RISC-V and x86 architectures, reducing three-instruction sequences to single instructions for common sign-extension operations. This leads to smaller and faster binaries.
