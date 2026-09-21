---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
commit_hash: 49e640dc4675de1f48166906a11950cb6698e77f
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize signed saturating truncation after a shift'
tldr: GCC now optimizes signed saturating truncation that follows an arithmetic right
  shift, simplifying code.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` pattern matcher has gained the ability to recognize
  signed saturating truncation (`.SAT_TRUNC`) following an arithmetic right shift.
  This pattern is applicable when the input sign is preserved by the shift, allowing
  the saturation logic to use the original input value while the shift operates on
  it. The commit requires the data shift to be a constant less than the input precision
  and the range type to be at least as wide as the shifted value and output type.
  This enables a significant simplification for a specific sequence, demonstrated
  by an AArch64 example reducing to…
primer_glossary:
- term: signed saturating truncation
  definition: A conversion to a narrower signed integer type where the result is clamped
    to the minimum or maximum representable value of the target type if the original
    value falls outside that range. This prevents overflow by capping the result.
- term: arithmetic right shift
  definition: A bitwise operation that shifts the bits of a number to the right. For
    signed numbers, the sign bit is propagated to preserve the sign of the number.
- term: pattern matcher
  definition: A component within a compiler that identifies specific sequences of
    intermediate representation (IR) operations that can be replaced by more efficient
    instructions or simpler IR forms. This is crucial for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/49e640dc4675de1f48166906a11950cb6698e77f
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

GCC's `match-sat-alu.pd` pattern matcher can now recognize and optimize signed saturating truncation that occurs after an arithmetic right shift. This optimization allows the saturation value to use the original input while the shift operates on the already shifted value. This can simplify complex code sequences, such as an AArch64 example that reduces to a single `SQSHRN` instruction.
