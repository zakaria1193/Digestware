---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- template
- instantiation
- bug fix
commit_hash: c9a23dde6888a96c87e1aea5dd02d9d3bacc7d64
source_type: github
author: David Malcolm
headline: 'analyzer: add template instantiation [PR128712]'
tldr: Adds explicit template instantiation for a specific type in the analyzer.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/analyzer/symbolic-scalars.cc`, this commit adds an explicit
  template instantiation for `scalar<integer_with_unit<units::bit>>::is_unknown_p`
  for the specific type `scalar<integer_with_unit<units::bit>>`. This resolves PR
  analyzer/128712 by ensuring that this particular template instantiation, which is
  used for checking unknown scalar values within the analyzer, is generated when needed,
  preventing potential link-time errors or incomplete analysis.
primer_glossary:
- term: GCC analyzer
  definition: A component of GCC that performs static analysis to find bugs, particularly
    related to memory safety and array bounds.
- term: template instantiation
  definition: The process in C++ where a template is compiled to produce a concrete
    class or function for a specific set of template arguments.
- term: explicit instantiation
  definition: A C++ mechanism to force the instantiation of a template for a particular
    set of arguments, often used to control which instantiations are generated or
    to resolve ambiguities.
- term: scalar
  definition: In programming, a value of a primitive type (like an integer or float)
    as opposed to a composite type (like an array or struct).
- term: integer_with_unit
  definition: A C++ template likely used in the analyzer to represent integer values
    that are associated with specific units, such as bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c9a23dde6888a96c87e1aea5dd02d9d3bacc7d64
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This commit explicitly instantiates a template for the `scalar<integer_with_unit<units::bit>>::is_unknown_p` type within the GCC analyzer. This resolves a reported issue (PR128712) where this specific instantiation was missing, potentially leading to compilation or runtime errors for certain analysis paths involving integral types with bit units.
