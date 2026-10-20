---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- clz
- ctz
commit_hash: 44eaf4ae9e1d26c120a92540abfc225ec634243c
source_type: github
author: Kyrylo Tkachov
headline: 'testsuite: Add clzsi and ctzsi effective targets'
tldr: Introduces new testsuite procedures to verify CLZ and CTZ operations on 32-bit
  integers.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change adds `clzsi` and `ctzsi` effective target checks. These
  are necessary because GIMPLE builtins for CLZ/CTZ (e.g., `__builtin_clz`) lack a
  fallback expansion and require specific instruction patterns for the operand mode.
  The new checks verify that the `niter` analysis correctly identifies opportunities
  to replace counting loops on 32-bit unsigned integers with .CLZ or .CTZ calls, which
  only occurs if the target has the appropriate pattern, even if it's an expander.
primer_glossary:
- term: clzsi
  definition: Effective target for count leading zeros on a 32-bit signed integer
    (si mode).
- term: ctzsi
  definition: Effective target for count trailing zeros on a 32-bit signed integer
    (si mode).
- term: GIMPLE
  definition: GCC's Internal Multiple Expression Representation, an intermediate representation
    used for optimization passes.
- term: effective target
  definition: A testsuite concept that verifies if a specific hardware instruction
    or optimization is available and correctly handled by the compiler for a given
    code pattern.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/44eaf4ae9e1d26c120a92540abfc225ec634243c
date: '2026-10-09'
is_stub: true
stub_reason: low_score
---

This commit adds two new procedures, `check_effective_target_clzsi` and `check_effective_target_ctzsi`, to the GCC testsuite. These procedures are designed to verify that the compiler correctly recognizes and optimizes count leading zeros (`clzsi`) and count trailing zeros (`ctzsi`) operations on 32-bit unsigned integers, ensuring they are expanded to native instructions rather than falling back to library calls.
