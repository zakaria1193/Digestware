---
project: gcc
subsystem: gcc/ada
patch_id: null
tags:
- ada
- compiler-internals
- refactoring
commit_hash: f0ebef9e3cdbaf9dcef06515892e6c5573c1092b
source_type: github
author: Piotr Trojanek
headline: Use collective entity kinds for access-to-subprogram types
tldr: The Ada front end now consistently uses more general entity kinds for access-to-subprogram
  types, standardizing internal representations without altering progr…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc/ada` subsystem handles the Ada programming language front
  end for the GCC compiler. This commit refactors the internal representation of 'access-to-subprogram'
  types. In Ada, an access type is similar to a pointer or reference. Access-to-subprogram
  types are references to subroutines (procedures or functions). Previously, various
  specific 'entity kinds' might have been used to categorize these types. This change
  standardizes their representation to use `Access_Protected_Kind` and `Access_Subprogram_Kind`
  where appropriate. This is an internal code cleanup in `exp_ch4.adb`, `sem_attr.…
primer_general: 'The Ada front end within the GCC compiler is responsible for understanding
  and translating Ada code. In Ada, an ''access type'' is like a pointer in C or a
  reference in Java; it''s a way to refer to another part of the program''s data or
  code. An ''access-to-subprogram type'' specifically refers to a function or procedure.
  This commit changes how the compiler internally categorizes these types. Instead
  of using many very specific categories, it now uses broader, more general categories
  called `Access_Protected_Kind` and `Access_Subprogram_Kind`. This is like organizing
  a library: instead of having separate sections for ''fiction novels by author A,''
  ''fiction novels by author B,'' etc., you just have a section for ''fiction novels.''
  This change simplifies the compiler''s internal structure in files like `exp_ch4.adb`,
  `sem_attr.adb`, and `sem_ch3.adb`, making the compiler''s code cleaner and easier
  to manage, but it doesn''t change how your Ada programs behave.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f0ebef9e3cdbaf9dcef06515892e6c5573c1092b
date: '2025-04-25'
is_stub: false
---

The Ada front end now uses more collective entity kinds, `Access_Protected_Kind` and `Access_Subprogram_Kind`, when representing access-to-subprogram types. This change standardizes the internal representation within `exp_ch4.adb`, `sem_attr.adb`, and `sem_ch3.adb`, eliminating less specific kinds. While improving code consistency and maintainability, this internal refactoring does not affect the semantics or behavior of Ada programs.
