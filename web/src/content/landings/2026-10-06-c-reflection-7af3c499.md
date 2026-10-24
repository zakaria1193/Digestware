---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler error
commit_hash: 7af3c499e0006fa7087b677dc635be2c2c6da299
source_type: github
author: Marek Polacek
headline: Fix C++ reflection ICE with splice member access on uninstantiated classes.
tldr: C++ reflection now handles splice member access on uninstantiated classes, preventing
  an ICE and ensuring correct instantiation.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The fix in `gcc/cp/pt.cc` modifies `tsubst_expr`'s handling of `COMPONENT_REF`
  when `COMPONENT_REF_SPLICE_P` is set. Previously, it would call `finish_non_static_data_member`,
  leading to an ICE when the `object_type` was not yet complete. The change now directs
  these splice expressions to the `finish_class_member_access_expr` path. This path
  includes a call to `complete_type_or_maybe_complain`, ensuring the class is instantiated
  and a `TREE_BINFO` is created before proceeding, thus preventing the ICE and removing
  the unreachable `dependent_splice_p` assertion.
primer_glossary:
- term: splice member access
  definition: A C++ reflection feature allowing access to members of a class specified
    within a splice expression, often used in template metaprogramming.
- term: uninstantiated class
  definition: A class definition within a template that has not yet been concretely
    defined with specific template arguments.
- term: Internal Compiler Error (ICE)
  definition: A severe error encountered by the compiler during translation that prevents
    it from continuing, usually indicating a bug in the compiler itself.
- term: TREE_BINFO
  definition: A GCC internal tree node structure that holds information about a class,
    used for representing class members and their attributes.
- term: tsubst_expr
  definition: A GCC internal function responsible for template substitution of expressions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7af3c499e0006fa7087b677dc635be2c2c6da299
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This commit resolves an Internal Compiler Error (ICE) in C++ reflection that occurred when performing splice member access (e.g., `o->[:^^A::m:]`) on an uninstantiated class. The issue arose because `tsubst_expr` would incorrectly call `finish_non_static_data_member` on a `FIELD_DECL` from a splice expression before the object's type was fully instantiated. The fix routes these cases through `finish_class_member_access_expr`, which correctly instantiates the class and creates the necessary `TREE_BINFO`, thereby avoiding the ICE and ensuring the dependent_splice_p check is not reached erroneously.
