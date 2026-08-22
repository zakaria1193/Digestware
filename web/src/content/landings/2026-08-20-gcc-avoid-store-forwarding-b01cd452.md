---
project: gcc
subsystem: gcc/avoid-store-forwarding
patch_id: null
tags:
- optimization
- compiler bug
commit_hash: b01cd452a6c7ba2a2f95a77f62f0727cbbe9d6a5
source_type: github
author: Konstantinos Eleftheriou
headline: Reject BLKmode memory operands for store forwarding.
tldr: Avoids compiler assertion by rejecting BLKmode memory operands in store forwarding.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The store_forwarding_analyzer::avoid_store_forwarding pass collects
  forwarding candidates. BLKmode, representing bitfields, lacks a direct integer mode
  equivalent. Building bit insert sequences for BLKmode memory operands caused an
  assertion in store_bit_field. This commit modifies the candidate collection to reject
  BLKmode memory operands, preventing the assertion.
primer_glossary:
- term: store forwarding
  definition: An optimization where a load instruction can read directly from the
    store buffer of a preceding store instruction, rather than waiting for the store
    to be committed to memory. This can improve performance by reducing memory latency.
- term: BLKmode
  definition: A GCC internal mode representing bitfields. It does not have a direct
    mapping to standard integer types, which can cause issues in operations that expect
    specific integer modes.
- term: assertion failure
  definition: A condition detected by the compiler during compilation that indicates
    a programming error or an unexpected state, causing the compilation to stop.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b01cd452a6c7ba2a2f95a77f62f0727cbbe9d6a5
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

The store forwarding optimization pass now rejects BLKmode memory operands when collecting candidates. Previously, it only rejected operands with unknown or non-constant sizes, leading to an assertion failure when building bit insert sequences for BLKmode stores. This change prevents such assertions and improves robustness.
