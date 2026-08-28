---
project: gcc
subsystem: c++/contracts
patch_id: null
tags:
- c++
- contracts
- templates
commit_hash: 4d26b4cc14c1db94062240a69bffdbe3e2aa5904
source_type: github
author: Wang Jinghao
headline: C++ contracts regeneration from templates is now always performed.
tldr: C++ contracts are now always regenerated from the current code pattern in templates,
  resolving issues with explicit instantiations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `regenerate_decl_from_template` function in `gcc/cp/pt.cc` is responsible
  for creating a specialized declaration from a template. When dealing with C++ contracts,
  it previously associated uninstantiated contracts with template instantiations.
  If an explicit instantiation of a template occurred before a subsequent redeclaration
  that redefined the function or its contracts, the contracts might still reference
  parameter declarations (`PARM_DECL`) from the older version. This change modifies
  `regenerate_decl_from_template` to unconditionally regenerate contracts from the
  `code_pattern` if con…
primer_glossary:
- term: C++ contracts
  definition: A C++ language feature (tentatively C++26) that allows developers to
    specify contract conditions (preconditions, postconditions, assertions) directly
    in the code. These contracts can be used for static analysis, runtime checking,
    and documentation.
- term: template instantiation
  definition: The process by which a function template or class template is converted
    into a concrete function or class by substituting template arguments for template
    parameters.
- term: explicit instantiation
  definition: A C++ construct that forces the instantiation of a template for a specific
    set of arguments, even if it's not directly used in the code.
- term: PARM_DECL
  definition: A GCC internal representation for a function parameter declaration.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4d26b4cc14c1db94062240a69bffdbe3e2aa5904
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit ensures that C++ contracts are always regenerated from the current code pattern within `regenerate_decl_from_template()` when either the declaration or the pattern has contracts. This addresses an issue where uninstantiated contracts associated with a function template instantiation could incorrectly refer to parameter declarations from an earlier definition if an explicit instantiation was encountered before a later redeclaration. By always regenerating from the current pattern, the compiler ensures that contracts accurately reflect the latest definition, preventing potential errors related to stale parameter references.
