---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
commit_hash: b627bfa76649bb65ccab8d9aad9c1b1f1d45cdde
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize complement masks for unsigned saturating truncation'
tldr: GCC's pattern matcher now recognizes an alternative way to express unsigned
  saturating truncation using bitwise complement.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` pattern matcher now handles a new variant of
  unsigned saturating truncation, specifically when the mask is derived via complement
  (`~X`) instead of negation (`-X`). This pattern is useful as it correctly handles
  edge cases and can be more efficiently mapped to hardware instructions. The change
  ensures that the unsigned range comparison is preserved, as a signed comparison
  would not correctly clamp negative inputs. This enhancement improves the patterns
  available for saturation and truncation operations within the compiler's arithmetic
  logic unit (ALU) matching.
primer_glossary:
- term: unsigned saturating truncation
  definition: A process that converts a value to a narrower unsigned integer type,
    clamping the result to the maximum value of the target type if the original value
    exceeds it. This prevents overflow by capping the result at the highest representable
    value for the unsigned type.
- term: bitwise complement (~X)
  definition: An operation that flips every bit in the binary representation of a
    number. For signed integers, it's equivalent to -X - 1.
- term: pattern matcher
  definition: A component within a compiler that identifies specific sequences of
    intermediate representation (IR) operations that can be replaced by more efficient
    instructions or simpler IR forms. This is crucial for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b627bfa76649bb65ccab8d9aad9c1b1f1d45cdde
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

The GCC pattern matcher in `match-sat-alu.pd` has been updated to recognize unsigned saturating truncation when the sign mask is formed using a bitwise complement (~X) instead of negation (-X). This optimization avoids potential issues with negating the minimum signed value and can lead to more efficient code generation, as demonstrated by an AArch64 example showing a reduction from multiple instructions to a single `smax` and `uqxtn` sequence.
