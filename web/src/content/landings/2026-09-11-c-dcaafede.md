---
project: gcc
subsystem: c++
patch_id: null
tags:
- c++
- templates
- compiler bug
commit_hash: dcaafedee8a34f9ad60ac4d47ffe7529959028d2
source_type: github
author: Jakub Jelinek
headline: C++ compiler fixes tsubst_splice_expr for PR127276.
tldr: Corrects the C++ compiler's handling of splice expressions in templates to properly
  convert references.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Within GCC's C++ frontend (`pt.cc`), the `tsubst_splice_expr` function
  handles template argument substitution for splice expressions. When parsing splice
  expressions outside of templates, the `finish_id_expression` path correctly invokes
  `convert_from_reference`. However, within `tsubst_splice_expr`, this conversion
  was omitted for `PARM_DECL`s of `REFERENCE_TYPE`, causing `build_x_array_ref` to
  be called with incorrect types instead of indirect references. This patch inserts
  the missing `convert_from_reference` call, aligning the template substitution logic
  with the non-template path.
primer_glossary:
- term: tsubst_splice_expr
  definition: A function within GCC's C++ frontend that handles the substitution of
    template arguments for splice expressions.
- term: template argument substitution
  definition: The process by which a compiler replaces placeholder template parameters
    with actual types or values provided when a template is instantiated.
- term: PARM_DECL
  definition: A GCC internal representation node (declaration) for a function parameter.
- term: REFERENCE_TYPE
  definition: An internal GCC type representing a C++ reference (e.g., 'int&').
- term: INDIRECT_REF
  definition: An internal GCC representation for dereferencing a pointer or reference.
- term: build_x_array_ref
  definition: A GCC internal function used to construct an expression representing
    an array reference (e.g., 'arr[index]').
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcaafedee8a34f9ad60ac4d47ffe7529959028d2
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's C++ frontend where splice expressions used within templates were not being correctly processed. Specifically, the compiler failed to call `convert_from_reference` for PARM_DECLs of REFERENCE_TYPE, leading to incorrect calls to `build_x_array_ref`. The fix ensures `convert_from_reference` is called, resolving the issue and allowing a new test case to pass.
