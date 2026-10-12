---
project: gcc
subsystem: cp/reflection
patch_id: null
tags:
- c++
- reflection
- template
- bugfix
commit_hash: 1b961bf9d7e76de9a36f93d8749dbe7fae302246
source_type: github
author: Marek Polacek
headline: 'c++/reflection: Fixed bogus error with dependent using declarations'
tldr: Fixes a compiler error when using dependent dependent typename declarations
  in reflection contexts.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `name-lookup.cc`, the `finish_nonmember_using_decl` function now
  accepts a `typename_p` boolean. This flag is propagated from `parser.cc`'s `finish_using_decl`
  and `pt.cc`'s `tsubst_stmt`. When set, it indicates that a `USING_DECL` should be
  treated as a type name, even when it refers to a dependent name in a non-class scope.
  This resolves an issue where the `USING_DECL_TYPENAME_P` flag was not being correctly
  propagated.
primer_glossary:
- term: reflection
  definition: A C++ feature (currently in study for standardization) that allows code
    to inspect and manipulate its own structure at compile time or runtime. This commit
    relates to compile-time reflection capabilities.
- term: using declaration
  definition: A C++ construct (`using namespace X;` or `using X::Y;`) that brings
    names from a namespace into the current scope or declares an alias for a specific
    name.
- term: dependent name
  definition: In C++ templates, a name whose meaning cannot be determined until the
    template is instantiated with specific arguments. This often involves names that
    depend on a template parameter.
- term: typename keyword
  definition: In C++, the `typename` keyword is used to explicitly state that a dependent
    name should be interpreted as a type name, disambiguating it from potential non-type
    names.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1b961bf9d7e76de9a36f93d8749dbe7fae302246
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

The C++ reflection mechanism now correctly handles dependent `using typename` declarations within templates. Previously, a bogus error occurred when trying to declare a type alias within a template where the namespace was a template parameter. This change ensures that such dependent declarations are properly recognized as types.
