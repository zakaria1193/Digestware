---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- lambdas
- bugfix
commit_hash: 4dc96a3ea00e6876bef3321288343c0abe78bd39
source_type: github
author: Marek Polacek
headline: Include lambda operator() in members_of
tldr: GCC's C++ reflection now correctly includes the call operator of lambda expressions
  when enumerating class members.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the GCC C++ front-end, within the reflection subsystem, the `members_of`
  intrinsic relies on the `class_members_of` function in `reflect.cc` to enumerate
  the members of a given type. This commit addresses a bug where `class_members_of`
  failed to include the call operator for closure types (lambdas) because it did not
  append the `LAMBDA_FUNCTION_P` from the implicitly-declared vector. By explicitly
  adding this, the reflection mechanism now correctly exposes the `operator()` of
  lambdas, crucial for tools that inspect or manipulate program structures.
primer_general: In C++, reflection is a powerful feature that allows a program to
  inspect its own structure at runtime, like listing all the functions or variables
  a class has. Lambda expressions are a convenient way to create small, anonymous
  functions. This commit fixes an issue in GCC where its reflection mechanism wasn't
  fully recognizing lambda expressions. Specifically, when you asked for a list of
  members of a class that was a lambda, it would sometimes omit the crucial 'call'
  operator (the part that actually executes the lambda's code). This fix ensures that
  GCC's reflection capabilities now correctly identify and report all parts of a lambda,
  making reflection-based tools more accurate when dealing with modern C++ features.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4dc96a3ea00e6876bef3321288343c0abe78bd39
date: '2026-06-18'
is_stub: false
---

This commit resolves a bug in GCC's C++ reflection capabilities where the `members_of` intrinsic failed to list the call operator (`operator()`) of lambda expressions. Previously, the `class_members_of` function did not append `LAMBDA_FUNCTION_P` from the implicitly-declared vector, leading to an incomplete reflection of lambda types. With this correction, `members_of` now accurately reflects the full set of members, ensuring that introspective code functions as expected for lambda expressions.
