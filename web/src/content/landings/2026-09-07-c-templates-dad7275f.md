---
project: gcc
subsystem: c++/templates
patch_id: null
tags:
- c++
- templates
- compiler bug
commit_hash: dad7275f7cc570fe222777285d8e8dbf274bb772
source_type: github
author: Iain Sandoe
headline: 'C++: Fix folding of CONSTRUCTOR in templates to avoid invalid expressions.'
tldr: C++ template instantiation now correctly avoids folding CONSTRUCTORs that have
  already been processed, fixing an issue with template expression substitution.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's C++ frontend, the `store_init_value` function in `typeck2.cc`
  is modified to prevent re-folding of `CONSTRUCTOR` expressions within template instantiations,
  particularly when an NSDMI has already been folded. This prevents the generation
  of malformed intermediate expressions that would fail during template substitution
  (`tsubst`). The change ensures that the handling of initializers in templates remains
  consistent with previously folded constructs.
primer_glossary:
- term: CONSTRUCTOR
  definition: In C++, a special member function called automatically when an object
    of a class is created. It is used to initialize the object's members.
- term: template
  definition: A C++ feature that allows for generic programming, enabling functions
    and classes to operate on values of any type without needing to be rewritten for
    each type.
- term: NSDMI
  definition: Non-Type Template Parameter Declaration with Initializer. This allows
    template parameters to be initialized with values directly within the template
    declaration.
- term: fold expression
  definition: A C++17 feature that allows applying a binary operator over a pack of
    parameters in a variadic template expansion.
- term: tsubst
  definition: Template substitution, the process by which C++ template code is instantiated
    with specific types or values to generate actual code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dad7275f7cc570fe222777285d8e8dbf274bb772
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in C++ template instantiation where the compiler attempted to re-fold a CONSTRUCTOR expression within a template. This occurred after the Non-Type Template Parameter Declaration (NSDMI) had already been folded, leading to invalid expressions that the template substitution machinery could not handle.

The fix, implemented in `typeck2.cc`, prevents the folding of CONSTRUCTORs in such scenarios, resolving the issue and ensuring correct template instantiation. A new test case is added to verify the fix.
