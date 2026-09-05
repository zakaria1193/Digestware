---
project: gcc
subsystem: c++/modules
patch_id: null
tags:
- c++
- modules
- templates
- bugfix
commit_hash: dad0fca70f5a35b1016189eb544ea729b0144417
source_type: github
author: Patrick Palka
headline: 'c++/modules: Improve handling of friend template specializations in modules.'
tldr: 'c++/modules: Fixes module handling for friend template specializations without
  prior declarations.'
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'c++/modules: handle tinfo with identifier as template [PR127207]


  This commit relaxes two sanity checks in `cp/module.cc` (`trees_out::decl_value`
  and `get_originating_module_decl`) to accept `IDENTIFIER_NODE` as the `TI_TEMPLATE`
  for `TEMPLATE_INFO` structures. This is necessary to correctly handle friend template
  specializations like `createFoo<T>()` when `createFoo` itself has not yet been declared.
  Such cases are represented internally with `IDENTIFIER_NODE` for the template argument,
  which the previous checks did not anticipate, leading to errors when processing
  modules containing these…'
primer_glossary:
- term: TEMPLATE_INFO
  definition: An internal GCC data structure representing information about a C++
    template.
- term: IDENTIFIER_NODE
  definition: A GCC internal representation for an identifier, such as a variable
    or function name.
- term: TI_TEMPLATE
  definition: A field within the TEMPLATE_INFO structure that points to the template
    itself.
- term: friend template specialization
  definition: A declaration that makes a template a friend of a class or another template,
    allowing access to private members. A specialization occurs when a template is
    instantiated for a specific type or value.
- term: PR127207
  definition: A problem report number in GCC's bug tracking system, indicating a specific
    issue that has been addressed by this commit.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dad0fca70f5a35b1016189eb544ea729b0144417
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This change enhances C++ module support by correctly handling template information that uses an identifier as a template, specifically for friend template specializations that lack a prior declaration. This resolves an issue where certain sanity checks were too strict, preventing these cases from being processed correctly. New test cases are included to verify the fix.
