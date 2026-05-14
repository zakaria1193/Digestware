---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- attributes
- error handling
commit_hash: 9d5c276dfb5f5812e0fa7b46e84beaca36295c6d
source_type: github
author: chzn@mail.ustc.edu.cn
headline: 'c++/reflection: Reject invalid annotation on class [PR123609]'
tldr: The C++ compiler now rejects invalid attributes on class declarations, improving
  error reporting.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies `cp_parser_class_head` in `gcc/cp/parser.cc` to
  re-parse attributes that caused a tentative parsing failure. This ensures that invalid
  attributes on class declarations are properly rejected instead of being ignored.
  This change is related to C++ reflection features. The commit also adjusts the expected
  errors in `g++.dg/cpp0x/attr-nodiscard1.C` and adds a new test case `g++.dg/reflect/annotations19.C`
  to verify the fix for PR c++/123609.
primer_general: C++ reflection is a feature that allows a program to inspect and modify
  its own structure and behavior at runtime. Attributes (using the `[[...]]` syntax)
  are annotations that can be added to various parts of the code, including class
  declarations. This commit ensures that the compiler correctly identifies and rejects
  invalid attributes applied to classes, which helps in preventing unexpected behavior
  and improving code quality by reporting errors early in the development process.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9d5c276dfb5f5812e0fa7b46e84beaca36295c6d
date: '2026-05-13'
is_stub: false
---

This commit fixes an issue where the C++ compiler ignored certain errors when parsing attributes on class declarations due to tentative parsing. Now the compiler re-parses attributes that previously caused a tentative parsing failure, ensuring that invalid attributes are rejected and appropriate errors are reported. This change improves the robustness of the compiler's error handling and provides more informative diagnostics to the user.
