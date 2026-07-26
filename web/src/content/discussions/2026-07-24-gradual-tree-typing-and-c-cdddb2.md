---
project: gcc
subsystem: gcc
patch_id: null
tags:
- compiler
- gcc
- C++
- templates
- internal representation
discussion_id: 96e015e6-d0a2-320f-b4fe-49a0a8812dcd@redhat.com
source_type: public_inbox
title: 'Re: Gradual ''tree'' typing and C++'
headline: Gradual 'tree' typing and C++
tldr: Discussion on C++ template syntax for GCC's internal 'tree' types and its impact
  on code readability.
proposer: Joseph Myers <josmyers@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Using templates for 'tree' typing increases static analysis benefits and potentially
  catches errors earlier.
- Overuse of complex template syntax can decrease readability for developers unfamiliar
  with advanced C++ features.
- Explicitly typing 'tree' parameters might reveal poorly designed internal APIs that
  accept too wide a range of node types.
exchanges:
- author: Joseph Myers <josmyers@redhat.com>
  role: proposer
  position: Agrees that most code expecting 'tree' nodes likely has a specific type
    and supports static typing for clarity.
  quote: 'So I think we should aim for static typing in the cases where we expect

    that the code is already quite close to having exactly one static type for

    each place using "tree"'
- author: Martin Uecker <martinu@google.com>
  role: reviewer
  position: Critiques the proposed gradual typing syntax, arguing that functions working
    on disparate 'tree' codes are inherently suspect and that explicit types improve
    readability.
  quote: 'foo(tree< one_of<FUNCTION_DECL, PLUS_EXPR> > x)


    May be amazing technology, but just tells me the function should

    not exist in this form. So it only helps writing bad code.'
primer_expert: The conversation revolves around applying C++11 template metaprogramming
  features, specifically variadic templates and type traits, to GCC's internal compiler
  representation ('tree'). The proposal suggests using syntax like `tree<ExpectedCode1,
  ExpectedCode2>` to statically type function parameters that currently accept a generic
  `tree` type, replacing runtime assertions. The debate centers on whether this improves
  code clarity and maintainability or obscures the underlying AST/GIMPLE structure
  and signals poor API design.
primer_glossary:
- term: tree
  definition: GCC's internal representation for abstract syntax trees (AST) and intermediate
    representation (IR) during compilation. It represents code structure and constructs.
- term: tree codes
  definition: Specific identifiers within GCC's 'tree' structure that denote the type
    of construct, such as FUNCTION_DECL for function declarations or PLUS_EXPR for
    addition operations.
- term: GIMPLE
  definition: A three-address intermediate representation used by GCC, derived from
    the 'tree' representation, that simplifies optimization passes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/96e015e6-d0a2-320f-b4fe-49a0a8812dcd@redhat.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This discussion debates the merits of using C++ templates for GCC's internal 'tree' type, specifically proposing syntax like `foo(tree<one_of<FUNCTION_DECL, PLUS_EXPR>> x)`. While proponents see it as an improvement over assertions in function bodies, others argue it makes functions appear 'weird' and can lead to writing bad code. The core disagreement lies in whether explicit static typing of internal compiler data structures enhances or detracts from code clarity and design.
