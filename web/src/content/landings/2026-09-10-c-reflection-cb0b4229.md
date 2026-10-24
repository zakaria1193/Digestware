---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- namespace
commit_hash: cb0b42290642c021cab5f66075a38b15d5f2772d
source_type: github
author: Marek Polacek
headline: Fix C++ reflection to correctly handle spliced namespaces in using directives.
tldr: C++ reflection now correctly handles spliced namespaces in using directives,
  fixing a bug that prevented certain namespace usages.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The change in `gcc/cp/pt.cc` modifies `type_dependent_expression_p`
  to return false for `NAMESPACE_DECL`. This affects how C++ reflection handles namespace
  splicing in `using` directives, specifically for cases involving global or qualified
  namespaces. Previously, `global_namespace` was incorrectly treated as dependent
  due to its initial `void_type_node`, causing issues with constructs like `using
  namespace ::N;`. This commit ensures compliance with [namespace.udir]/1 and [namespace.alias]/2
  by correctly identifying dependent vs. non-dependent namespaces, particularly when
  `global_namespace`'…
primer_glossary:
- term: spliced namespace
  definition: A namespace that is merged with another namespace, typically for organizational
    purposes. In C++, this refers to using directives that incorporate namespaces,
    potentially leading to name clashes or ambiguities if not handled correctly by
    the compiler.
- term: using directive
  definition: A C++ construct (e.g., `using namespace ...;`) that brings all names
    from a namespace into the current scope, making them accessible without qualification.
- term: dependent expression
  definition: In the context of C++ templates, an expression whose evaluation depends
    on template parameters. Such expressions cannot be fully evaluated until the template
    is instantiated.
- term: namespace splicing
  definition: The C++ mechanism that allows the declaration of a namespace to be split
    across multiple definitions, effectively merging them into a single logical namespace.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb0b42290642c021cab5f66075a38b15d5f2772d
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in C++ reflection where spliced namespaces in using directives were not correctly detected or handled. Previously, the compiler would incorrectly consider the global namespace as dependent, leading to failures in using directives like 'using namespace ::' or 'using namespace std::'. The fix adjusts the `type_dependent_expression_p` function to correctly identify non-dependent namespaces, enabling these directives to work as expected and aligning with C++ standards regarding namespace splicing.
