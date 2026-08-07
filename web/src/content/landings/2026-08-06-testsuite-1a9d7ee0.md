---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- c++
- templates
- attributes
commit_hash: 1a9d7ee08ed49c637e94dad2695532d78909f24f
source_type: github
author: Jakub Jelinek
headline: New testcase for `[[clang::no_specializations]]` attribute.
tldr: Adds a test to verify GCC's handling of `[[clang::no_specializations]]` on template
  declarations, ensuring it correctly diagnoses specializations.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch adds a test case to `g++.dg/ext/attr-no_specializations13.C`
  to verify correct diagnostics for `[[clang::no_specializations]]` when applied to
  a template declaration. It specifically checks that GCC correctly rejects specializations
  even if the primary template definition omits the attribute, a behavior that Clang
  is also being updated to emulate.
primer_glossary:
- term: '[[clang::no_specializations]]'
  definition: A C++ attribute, primarily used with Clang, that is intended to prevent
    template specializations. This test ensures GCC adheres to this behavior, even
    when attributes are applied in specific patterns.
- term: template declaration
  definition: A declaration that introduces a template, which can be a function template
    or a class template. It specifies a blueprint for creating other entities.
- term: primary template definition
  definition: The actual definition of a template, as opposed to just a declaration.
    For class templates, this is where the class body is defined.
- term: explicit specialization
  definition: A user-defined definition for a specific template instantiation, overriding
    the compiler-generated one. For example, `template<> struct MyClass<int> { ...
    };`.
- term: partial specialization
  definition: A template definition that specifies some, but not all, of the template
    arguments. For example, `template<typename T> struct MyClass<T*> { ... };`.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1a9d7ee08ed49c637e94dad2695532d78909f24f
date: '2026-08-06'
is_stub: true
stub_reason: low_score
---

This commit introduces a new test case to the GCC test suite. The test verifies the compiler's behavior with the `[[clang::no_specializations]]` attribute when applied to a template declaration followed by a primary template definition without the attribute. It ensures that GCC, like Clang (which is being fixed), correctly diagnoses any subsequent explicit or partial specializations, preventing regressions in this area.
