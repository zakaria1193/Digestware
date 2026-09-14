---
project: gcc
subsystem: gcc
patch_id: null
tags:
- C++
- compiler
- GCC
- lambda
- templates
discussion_id: V3AUSQ3beDn7dZBzc5IPO2qaZHlrhvp5-8jwpFVpx0iIYglKIhFeqzTUuNZFRO1R11rRYdO8o1b84cf-It_jG80adLlX7xsupBh0HE3QSCM=@protonmail.com
source_type: public_inbox
title: 'Re: Requires clauses in pfn conversions for generic lambdas'
headline: Requires clauses in pfn conversions for generic lambdas
tldr: Discussion on C++ standard's handling of requires clauses in generic lambda
  pfn conversions, suggesting a CWG issue and a GCC PR for an ICE.
proposer: Waffl3x <waffl3x@protonmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Strict adherence to the current standard (even if ambiguous) vs. adopting compiler-specific
  extensions that offer more flexibility.
- Clarifying the standard via CWG is slow but provides a definitive answer; compiler-specific
  bug fixes are faster but may lead to inconsistencies.
- The interaction between generic lambdas, PFN conversion, and requires clauses is
  complex, requiring careful analysis to ensure correct and consistent behavior.
exchanges:
- author: Waffl3x <waffl3x@protonmail.com>
  role: proposer
  position: Agrees that the C++ standard may need clarification regarding requires
    clauses in generic lambda pfn conversions and advises filing a CWG issue and GCC
    PR.
  quote: Yes I think you should open a CWG issue. And at minimum open a PR for the
    ICE in your first message. (Please do check if it is a duplicate first, I haven't
    done so yet.)
- author: Ivan Sokolov
  role: contributor
  position: Observes that both Clang and GCC deviate from the standard regarding trailing
    return types in generic lambdas, allowing template parameter deduction.
  quote: The standard [expr.prim.lambda.closure#12] seems silent on the matter, and
    the above examples make me think this paragraph was simply forgotten when wording
    was modified to account for constraints.
primer_expert: 'This thread discusses a subtle C++ language feature: the conversion
  of generic lambdas to function pointers (PFN). Specifically, it examines how `requires`
  clauses, introduced for C++20 concepts, interact with this conversion when a trailing
  return type is used. The participants note that current C++ standards (as of C++20)
  might not fully specify or might have overlooked the behavior in this specific scenario,
  leading to potential ambiguities or deviations between compilers like GCC and Clang.
  The discussion points towards a need for clarification from the C++ Core Working
  Group (CWG) and a…'
primer_glossary:
- term: Generic lambda
  definition: A C++ lambda expression that uses `auto` for its parameter types, allowing
    it to accept arguments of different types, similar to a function template.
- term: Pointer-to-function (PFN)
  definition: A pointer that stores the address of a function.
- term: Requires clause
  definition: A C++20 language feature used to specify constraints on template parameters,
    often associated with concepts.
- term: Trailing return type
  definition: A C++11 feature allowing the return type of a function or lambda to
    be specified after the parameter list, using `-> type`.
- term: CWG
  definition: C++ Core Working Group. The committee responsible for maintaining and
    evolving the C++ programming language standard.
- term: ICE
  definition: Internal Compiler Error. An error condition within the compiler itself,
    indicating a bug in the compiler's implementation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/V3AUSQ3beDn7dZBzc5IPO2qaZHlrhvp5-8jwpFVpx0iIYglKIhFeqzTUuNZFRO1R11rRYdO8o1b84cf-It_jG80adLlX7xsupBh0HE3QSCM=@protonmail.com
bugzilla_url: null
date: '2026-09-12'
is_stub: false
stub_reason: ''
---

Following up on a discussion about C++ lambda conversion operators, Alex (Waffl3x) agrees that the standard might be lacking in its description of requires clauses for pointer-to-function conversions of generic lambdas. He suggests opening a Core Working Group (CWG) issue to clarify the standard and advises the original poster to file a bug report for an Internal Compiler Error (ICE) observed in GCC, after checking for duplicates.
