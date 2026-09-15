---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- optimization
- gsoc
- ipa
- icf
discussion_id: 20260914192200.56210-1-kapellirohith@gmail.com
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: IPA-ICF project direction explored for PRs'
tldr: GSoC student investigates IPA-ICF project direction for specific GCC PRs.
proposer: Rohith Kapelli <kapellirohith@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Balancing the benefits of IPA-ICF optimizations against potential complexities and
  correctness issues with out-of-line bodies and C++ specific features.
- Investigating the interaction between ICF, IPA-cloning, and GNU extern inline semantics
  to ensure correct code generation.
exchanges:
- author: Rohith Kapelli <kapellirohith@gmail.com>
  role: proposer
  position: Investigates IPA-ICF project direction using reduced test cases for GCC
    PRs 119006 and 123227, observing different behaviors with separate-body approaches.
  quote: 'I looked into the separate-body idea using reduced testcases for PR119006
    and PR123227, using trunk from 3 September, before the PR119006 and PR123227 fixes.


    For PR119006, the current merge is safe when the leader''s out-of-line body is
    not inlined, but inlining the leader into the other caller produces the wrong
    code. Defining the two structs in the opposite order swaps the leader and makes
    the…'
primer_expert: This discussion concerns the exploration of an Interprocedural Analysis
  (IPA) pass combined with Identical Code Folding (ICF) for GCC, within the context
  of a Google Summer of Code project. The author is investigating how to handle issues
  arising from IPA-cloning and ICF merging when functions have out-of-line bodies,
  specifically for C++ member functions with potential null 'this' pointers and GNU
  extern inline semantics. The goal is to improve the correctness and robustness of
  these optimizations.
primer_glossary:
- term: IPA
  definition: Interprocedural Analysis is a compiler optimization technique that analyzes
    the entire program's call graph to optimize function calls and data flow across
    function boundaries.
- term: ICF
  definition: Identical Code Folding is a compiler optimization that detects identical
    functions or code sections and replaces duplicates with references to a single
    copy, saving space and potentially improving cache usage.
- term: GSoC
  definition: Google Summer of Code is an annual program that awards stipends to contributors
    who successfully complete short-term programming projects on open-source platforms.
- term: PR
  definition: Problem Report, typically referring to a bug report filed in a project's
    issue tracking system.
- term: out-of-line body
  definition: In C++, a function defined outside its class declaration, often used
    for non-inlined member functions.
- term: GNU extern inline
  definition: A GCC-specific extension to C's inline function semantics, affecting
    how inline functions are treated in separate compilation units.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260914192200.56210-1-kapellirohith@gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

A GSoC student is exploring a new direction for an IPA-ICF project, focusing on issues raised in GCC PR119006 and PR123227. Initial tests indicate that while a separate-body approach might be safe for PR119006 under certain conditions, it exposes problems with PR123227 due to differing non-null promises. The student plans to further investigate ICF's handling of losing bodies and the applicability of the separate-body scheme.
