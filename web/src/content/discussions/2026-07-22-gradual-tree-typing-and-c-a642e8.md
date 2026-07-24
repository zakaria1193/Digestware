---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler
- type system
- C++
- gradual typing
discussion_id: CAFiYyc0sHsvi71mqZo3yRKRA+q2OUPYEpL9n9Qh+t+xVvjOeWA@mail.gmail.com
source_type: public_inbox
title: 'Re: Gradual ''tree'' typing and C++'
headline: Gradual 'tree' typing and C++
tldr: Discussion on C++ syntax for gradual typing in GCC's tree representation, with
  concerns about ugliness and verbosity.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- 'Expressiveness vs. Verbosity: The proposed syntax might be more explicit but also
  more verbose and less flexible than current methods.'
- 'Maintainability: Debate over whether gradual typing, as implemented, improves or
  hinders code maintainability within the compiler''s internal code.'
- 'Idiomatic C++ vs. Compiler Internals: Balancing standard C++ practices with the
  specific needs and existing patterns of compiler internal representations.'
exchanges:
- author: Richard Biener
  role: proposer
  position: Critiques the proposed gradual 'tree' typing syntax as ugly, verbose,
    and less flexible than current methods like TREE_CODE.
  quote: 'All of it?

    Ugly syntax, having to type more than before (and thus having to deal with

    line wrapping more as well), having to introduce new vars for the dyn_cast

    way and being tied to if statements.

    With TREE_CODE/gimple_code/GET_CODE etc., one can choose coding style which

    is most appropriate for a particular case. If statement or several of

    those, switch case, tables indexed by the codes with ex…'
- author: Arsen Arsenović
  role: contributor
  position: Argues that gradual typing, particularly concerning checks and type narrowing,
    is an improvement, and that automatic runtime checks facilitate gradual adoption.
  quote: 'Interesting, I thought that this specific example was overly favourable

    to the idea of in-language gradual typing.


    It''s the trivial case where one check is replaced by another check whose

    result also gets encoded in the type system/current scope.


    Such a case - converting a check into a check + extra information in the

    variable type pretty much mechanically - seemed like strictly an

    improvement…'
- author: Jakub Jelinek
  role: contributor
  position: Counters that the proposed syntax is problematic due to its ugliness,
    verbosity, and inflexibility compared to existing C++ 'dyn_cast' and switch statements.
  quote: null
primer_expert: This discussion concerns proposals for introducing gradual typing features
  into GCC's internal C++ representation ('tree'). The goal is to allow C++ code within
  GCC to use type narrowing and runtime checks in a more integrated way, similar to
  dynamic languages. Participants debate the C++ syntax and idiomatic implementation
  for this, weighing expressiveness and maintainability against the flexibility of
  GCC's existing internal representation manipulation.
primer_glossary:
- term: tree
  definition: GCC's internal representation of abstract syntax trees, used to represent
    and manipulate code during compilation.
- term: gradual typing
  definition: A type system that allows a program to incorporate optional static type
    annotations within dynamically typed code, enabling a gradual transition and a
    mix of static and dynamic typing.
- term: TREE_CODE
  definition: An enumeration in GCC representing the type of a node in the 'tree'
    structure. It's used to classify and process different code constructs.
- term: dyn_cast
  definition: A C++ cast used for dynamic type checking, often employed in frameworks
    like LLVM and potentially in GCC's C++ internals to safely cast pointers between
    related classes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc0sHsvi71mqZo3yRKRA+q2OUPYEpL9n9Qh+t+xVvjOeWA@mail.gmail.com
bugzilla_url: null
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

Richard Biener critiques the proposed gradual 'tree' typing in C++ for GCC, citing concerns about ugly syntax, increased verbosity, and a less flexible approach compared to existing TREE_CODE mechanisms. The discussion highlights a preference for existing methods allowing varied coding styles over a rigid proposed syntax.
