---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- ctad
commit_hash: a2dab8f1d8ba2934e780f57c88bb6a513313e93f
source_type: github
author: Marek Polacek
headline: 'c++/reflection: Support splices with CTAD.'
tldr: Enables class template argument deduction (CTAD) with reflection splices in
  C++.
why_it_matters: Extends the functionality of C++ reflection, allows more flexible
  and expressive metaprogramming.
impact_score: 7
impact_rationale: Adds support for a new language feature (CTAD with reflection),
  significantly increasing metaprogramming capabilities.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies `parser.cc` and `pt.cc` to support CTAD with reflection
  splices. The issue was that the compiler didn't handle splice-type-specs designating
  deducible templates.  `cp_parser_splice_type_specifier` and `tsubst_splice_scope`
  are updated to call `make_template_placeholder` when `ctad_template_p` is true.
primer_general: This commit enhances C++'s reflection capabilities.  Reflection allows
  a program to inspect and manipulate its own structure at compile time.  Class Template
  Argument Deduction (CTAD) is a C++17 feature that allows the compiler to deduce
  the template arguments of a class from the constructor arguments.  This commit enables
  CTAD to work in conjunction with reflection, providing more flexibility in metaprogramming.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2dab8f1d8ba2934e780f57c88bb6a513313e93f
date: '2026-04-17'
---

This commit adds support for class template argument deduction (CTAD) when using reflection splices in C++. It addresses a case where a splice-type-spec designates a deducible template, which then serves as a placeholder for CTAD. The fix calls `make_template_placeholder` when a deducible template is encountered during splice processing.
