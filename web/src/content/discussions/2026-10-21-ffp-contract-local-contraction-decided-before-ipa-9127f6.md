---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- floating-point
- attributes
- intrinsics
discussion_id: CAKa7H4oQe_5wBRc_VhFdee6qyJRLJ3h9QjbpG3o9rD19TBWjxQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] -ffp-contract=local: contraction decided before IPA'
headline: 'ffp-contract=local: contraction decided before IPA'
tldr: Proposes function attributes to enable floating-point contraction across calls
  to intrinsics and wrapper types when -ffp-contract=on is used.
proposer: Paavan Indela <indela.paavankumar@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Relying on function attributes as a promise, which could lead to incorrect results
  if the attribute is misapplied.
- Increased complexity in the compiler's optimization logic for handling these attributes.
- 'Limited scope: currently only covers add, sub, and mul, and specific argument types.'
exchanges: []
primer_expert: This proposal introduces function attributes to extend the scope of
  the `-ffp-contract=on` optimization. Currently, this flag only enables contraction
  (e.g., FMA) for operations within a single source expression. The new attributes
  (`fp_contractable_add`, `fp_contractable_sub`, `fp_contractable_mul`) would allow
  contraction to occur across calls to functions (like intrinsics or methods of wrapper
  types) that are declared to perform these operations. This requires the compiler
  to trust the attribute declaration as a promise, similar to `const`, and the compiler
  verifies the function signature…
primer_glossary:
- term: -ffp-contract=on
  definition: A GCC optimization flag that enables floating-point contraction, allowing
    certain operations like multiply-add to be combined into a single FMA instruction
    for performance.
- term: IPA
  definition: Interprocedural Analysis. A compiler optimization technique that analyzes
    code across function calls, not just within a single function, to find optimization
    opportunities.
- term: intrinsic
  definition: A function or operation that is recognized by the compiler and may have
    a special, optimized implementation, often corresponding to a specific machine
    instruction.
- term: floating-point wrapper type
  definition: A user-defined type (e.g., a class or struct) that encapsulates a floating-point
    number and overloads operators to mimic built-in floating-point arithmetic, potentially
    adding features or enabling specific optimizations.
- term: FMA
  definition: Fused Multiply-Add. A single machine instruction that performs both
    a multiplication and an addition, often with higher precision and performance
    than separate multiply and add operations.
- term: function attribute
  definition: A GCC extension that allows specifying special properties or behaviors
    for functions, such as `const`, `nothrow`, or the proposed `fp_contractable_*`
    attributes.
- term: cv-qualifiers
  definition: Const (const) and volatile (volatile) qualifiers applied to types in
    C++. They indicate whether a variable can be modified or if its value might change
    unexpectedly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAKa7H4oQe_5wBRc_VhFdee6qyJRLJ3h9QjbpG3o9rD19TBWjxQ@mail.gmail.com
bugzilla_url: null
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

Paavan Indela proposes three new function attributes (`fp_contractable_add`, `fp_contractable_sub`, `fp_contractable_mul`) to enable floating-point contraction for expressions involving calls to intrinsics or operators of floating-point wrapper types. This proposal extends the behavior of -ffp-contract=on to scenarios where operations are not direct source-level expressions but function calls, allowing for fused multiply-add (FMA) optimizations. The attributes imply `const` and `nothrow` and have specific requirements regarding function signature and argument types.
