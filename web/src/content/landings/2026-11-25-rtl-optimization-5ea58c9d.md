---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- optimization
- CSE
- RISC-V
- bugfix
commit_hash: 5ea58c9d725146c20854720dba46175add86bac6
source_type: github
author: Jeff Law
headline: Clear SUBREG_PROMOTED state after copy propagation into SUBREGs
tldr: Fixes a bug where copy propagation into SUBREGs incorrectly preserved promotion
  state, leading to incorrect code generation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR128997 by correcting `canon_reg` in `cse.cc`.
  When Common Subexpression Elimination (CSE) propagates a copy into a `SUBREG` that
  has `SUBREG_PROMOTED_VAR_P` set, the promotion state was being incorrectly retained.
  This state signifies that the `reg` operand within the `SUBREG` is assumed to be
  properly extended, impacting subsequent analyses like `nonzero_bits`. The fix involves
  clearing the `SUBREG_PROMOTED_VAR_P` flag when such a substitution occurs, ensuring
  that the promotion assumption is invalidated when the transformation breaks it.
  A new test case `pr128997.c`…
primer_glossary:
- term: SUBREG
  definition: A machine-dependent construct in GCC's RTL (Register Transfer Language)
    that represents a sub-register, i.e., a portion of a larger register.
- term: copy propagation
  definition: An optimization pass that replaces uses of a variable with its definition
    if the variable is assigned directly from another variable.
- term: CSE
  definition: Common Subexpression Elimination. An optimization that identifies and
    eliminates redundant computations of the same expression.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used internally
    by GCC to represent code before it is translated into machine code.
- term: promotion state
  definition: A state associated with a SUBREG that indicates the underlying register
    is assumed to be correctly sign or zero-extended, influencing subsequent optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5ea58c9d725146c20854720dba46175add86bac6
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

A bug related to Common Subexpression Elimination (CSE) has been fixed, where copy propagation into a SUBREG marked with promotion state was incorrectly allowing that state to persist. This state implies that the underlying register is always properly extended, an assumption baked into various subsequent optimizations. The fix ensures that when a copy is propagated into such a SUBREG, the promotion state is cleared or the SUBREG is adjusted to reflect that the assumption no longer holds. This resolves issues seen on RISC-V and potentially other architectures.
