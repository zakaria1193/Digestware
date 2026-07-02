---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- c
- type-system
- compiler-internals
- refactoring
discussion_id: 9a0c6c9e-fe13-64cf-a444-5b5f4130f58c@redhat.com
source_type: public_inbox
title: 'Re: [RFC TREE-WIDE] gcc: stop using ''int'' to represent sets of qualifiers'
headline: 'gcc: stop using ''int'' to represent sets of qualifiers'
tldr: Discussion on appropriately representing qualifier sets in GCC, moving away
  from 'int' to handle complexities like TYPE_QUAL_ATOMIC and address spaces.
proposer: Joseph Myers <josmyers@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Moving from `int` bitfields to a more robust representation for qualifier sets improves
  accuracy but complicates internal compiler logic and may require significant code
  changes.
- Handling `TYPE_QUAL_ATOMIC` explicitly ensures correctness for atomic operations
  but requires careful integration with existing qualifier logic.
- Decoupling bug fixes from refactoring ensures the refactoring itself can proceed
  more smoothly, but may delay the resolution of existing issues.
exchanges:
- author: Arsen Arsenović
  role: contributor
  position: Suggests renaming a predicate function to 'usable_as_p' and handling complexities
    like TYPE_QUAL_ATOMIC differences.
  quote: 'Then, maybe, making ''includes_p'' (the predicate that was checking

    whether QS1 includes all qualifiers of QS2) actually be called

    usable_as_p or such, and having it reject TYPE_QUAL_ATOMIC differences

    makes sense?'
- author: Joseph Myers
  role: maintainer
  position: Concurs that qualifier predicates should consider complexities like TYPE_QUAL_ATOMIC
    and address spaces, advocating for separate bug fixing from the refactoring effort.
  quote: "I'd expect cases for C that check such a predicate generally to be \nconcerned\
    \ with access qualifiers (and thus already exclude \nTYPE_QUAL_ATOMIC), but the\
    \ question is what the code currently does (if \nthe refactoring shows up bugs,\
    \ fixing those bugs would best be done \nseparately from the refactoring)."
primer_expert: This discussion concerns the internal representation of C type qualifiers
  within GCC. Currently, sets of qualifiers are often represented using `int` bitfields.
  The proposal aims to move away from this simplistic approach to better handle nuanced
  qualifiers like `TYPE_QUAL_ATOMIC` and considerations related to different memory
  address spaces. The participants are debating the semantics of predicates that compare
  qualifier sets and how to ensure correctness and clarity during this refactoring,
  suggesting that bug fixes should be decoupled from the core refactoring effort.
primer_glossary:
- term: Type qualifiers
  definition: Keywords in C (like `const`, `volatile`, `restrict`, `atomic`) that
    specify additional properties of a type.
- term: TYPE_QUAL_ATOMIC
  definition: An internal GCC representation flag indicating that a type has atomic
    properties, relevant for concurrent access.
- term: Address spaces
  definition: Different regions of memory a processor can access, which may have different
    properties (e.g., coherence, access speed). C supports this through extensions
    and the `_Atomic` keyword in C11.
- term: Predicate
  definition: In programming, a function that returns a boolean value (true or false)
    based on certain conditions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/9a0c6c9e-fe13-64cf-a444-5b5f4130f58c@redhat.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

In a continuation of a discussion about refactoring GCC's internal representation of qualifier sets, Joseph Myers addresses Arsen Arsenović's suggestion to rename `includes_p` to `usable_as_p`. Myers agrees that qualifier sets, particularly `TYPE_QUAL_ATOMIC`, involve complexities beyond simple inclusion, especially concerning address spaces. He emphasizes that while the refactoring itself is ongoing, any bugs found during this process should be addressed separately to maintain clarity.
