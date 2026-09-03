---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- risc-v
- compiler
commit_hash: da3b0463f66312c9e93a027bae73bf17c24a8833
source_type: github
author: Kyrylo Tkachov
headline: Canonicalize conditional signed narrow clips to fix RISC-V saturation patterns.
tldr: Canonicalizes conditional signed narrow clips to ensure correct saturation behavior
  for RISC-V targets.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Canonicalizes conditional signed narrow clips in tree-ssa, specifically
  `(NT) ((UT) x > NT_MAX ? (-x) >> (PREC - 1) : x)`, to `(NT) MIN ((UT) MAX (x, 0),
  NT_MAX)`. This is done before loop if-conversion to preserve the original overflow
  semantics, especially for RISC-V targets where certain negations might otherwise
  be misinterpetered as saturating truncations. This ensures correct handling of signed
  minimums and avoids issues with unsigned conversions or negations.'
primer_glossary:
- term: tree-ssa
  definition: Static Single Assignment form applied to GCC's Gimple intermediate representation.
    It simplifies many optimizations by ensuring each variable is assigned exactly
    once.
- term: loop if-conversion
  definition: An optimization that replaces conditional branches within a loop with
    conditional move instructions, enabling better instruction-level parallelism.
- term: saturation
  definition: In arithmetic operations, saturation means clamping the result to the
    maximum or minimum representable value if an overflow or underflow occurs, rather
    than wrapping around.
- term: RISC-V
  definition: An open-standard instruction set architecture based on open RISC principles,
    known for its modularity and extensibility.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/da3b0463f66312c9e93a027bae73bf17c24a8833
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This change canonicalizes conditional signed narrow clip operations before loop if-conversion. The original form could lead to undefined behavior with signed minimum values and was being incorrectly transformed into saturating truncations. The new form ensures that the original overflow semantics are preserved when specific conditions like -fwrapv or sanitization are in effect, restoring correct saturation patterns for RISC-V tests.
