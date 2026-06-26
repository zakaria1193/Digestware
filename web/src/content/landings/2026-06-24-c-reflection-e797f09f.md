---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- parser
- bugfix
commit_hash: e797f09f8bdd680620da04d925ee429ed3201e07
source_type: github
author: Marek Polacek
headline: Prevent defining types within reflect expressions
tldr: The C++ reflection feature now correctly disallows type definitions within reflect
  expressions, enforcing language rules.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: C++ reflection, specifically the `reflect-expression` syntax using
  `^^ type-id`, is designed for querying type information, not for defining new types.
  The specification explicitly states that `type-id` in this context is not a `defining-type-id`.
  This commit fixes a long-standing oversight where the `cp_parser_reflect_expression`
  in `gcc/cp/parser.cc` was not enforcing this constraint, allowing type definitions
  within reflect expressions to pass through the parser. The change involves temporarily
  setting `parser->type_definition_forbidden_message` during the parsing of a reflect
  expression.…
primer_general: C++ is gaining powerful new features like 'reflection,' which allows
  programs to examine and manipulate their own structure (like asking what members
  a class has). One part of this, called a 'reflect expression' (using a syntax like
  `^^ something`), is meant for *querying* information about types, not for *creating*
  new types. This update fixes a bug in the GCC C++ compiler where it was accidentally
  letting you define new types inside these reflect expressions, even though the C++
  standard says this shouldn't be allowed. The fix makes sure the compiler catches
  these invalid definitions, stops them, and issues an error message, helping C++
  developers write correct and standard-compliant reflection code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e797f09f8bdd680620da04d925ee429ed3201e07
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

This commit addresses a compiler error where the C++ reflection feature could implicitly allow type definitions within `^^ type-id` reflect expressions, which is explicitly disallowed by the C++ standard. The fix, implemented in `cp_parser_reflect_expression`, temporarily sets a flag (`parser->type_definition_forbidden_message`) to prevent such definitions during parsing, ensuring that the compiler correctly rejects invalid code and adheres to the reflection specification.
