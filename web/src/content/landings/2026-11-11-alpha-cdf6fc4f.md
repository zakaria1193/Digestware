---
project: gcc
subsystem: alpha
patch_id: null
tags:
- alpha
- performance
- latency
commit_hash: cdf6fc4fac85d7bee639346417dad0fc1d22dad2
source_type: github
author: Matt Turner
headline: 'alpha: Correct EV6 itof latency and model itof-to-ftoi penalty'
tldr: Fixes Alpha EV6 integer-to-float conversion latency and models the performance
  penalty when chaining itof to ftoi.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The Alpha EV6 `ev6_itof` instruction latency in `config/alpha/ev6.md`
  has been corrected from 3 to 4 cycles, matching the 21264/21364 Compiler Writer's
  Guide. Furthermore, a direct dependency from `ev6_itof` to `ev6_ftoi` is now modeled
  with an 8-cycle penalty, reflecting measured performance where routing through an
  intermediate FP operation mitigates this penalty. This adjustment is critical for
  accurate instruction scheduling and performance analysis, as the register-to-register
  path becomes only 1.20x faster than a memory-based alternative when this penalty
  is present.
primer_glossary:
- term: itof
  definition: Integer-to-float conversion instruction.
- term: ftoi
  definition: Float-to-integer conversion instruction.
- term: FP
  definition: Floating-Point. Refers to floating-point arithmetic operations and units.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cdf6fc4fac85d7bee639346417dad0fc1d22dad2
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This commit corrects the latency for the integer-to-float (itof) conversion on the Alpha EV6 processor to 4 cycles, aligning it with the official documentation. It also accurately models the performance penalty incurred when an itof result is directly consumed by a float-to-integer (ftoi) conversion. Measurements show this direct chaining costs 8 cycles, not the sum of individual latencies. Bypassing this penalty by routing through an FP operation improves code generation and makes the register path more competitive with memory-based conversions.
