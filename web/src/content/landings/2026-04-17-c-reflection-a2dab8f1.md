---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- CTAD
- templates
commit_hash: a2dab8f1d8ba2934e780f57c88bb6a513313e93f
source_type: github
author: Marek Polacek
headline: 'C++: Support class template argument deduction (CTAD) with reflection splices.'
tldr: The C++ reflection implementation now handles class template argument deduction
  (CTAD) when used with splice-type-specifiers.
why_it_matters: Enables more flexible and concise code when using reflection to generate
  types, as CTAD reduces the verbosity of template instantiations.
impact_score: 7
impact_rationale: Implements a user-visible feature, enhancing the capabilities of
  C++ reflection.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The C++ reflection implementation in GCC's `parser.cc` and `pt.cc`
  now supports CTAD with splices. When `cp_parser_splice_type_specifier` or `tsubst_splice_scope`
  encounters a deducible template, `make_template_placeholder` is called. This resolves
  PR c++/124706, enabling reflection on types deduced via CTAD.
primer_general: C++ reflection allows programs to inspect and manipulate their own
  structure at compile time. Template argument deduction (CTAD) simplifies template
  usage by automatically inferring template arguments. This commit extends the C++
  reflection capabilities to work seamlessly with CTAD. Now, when reflective code
  generates types that rely on CTAD, the compiler can correctly deduce the template
  arguments, leading to more concise and expressive code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2dab8f1d8ba2934e780f57c88bb6a513313e93f
date: '2026-04-17'
---

The C++ reflection implementation was missing support for splice-type-specifiers that designate deducible templates, which are used as placeholders for CTAD. This commit adds the necessary logic to handle these cases by calling `make_template_placeholder` when a deducible template is encountered during parsing and template substitution. This allows CTAD to be used with reflection splices.
