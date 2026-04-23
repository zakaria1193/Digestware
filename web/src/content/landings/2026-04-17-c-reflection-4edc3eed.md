---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- C++
- reflection
- bugfix
commit_hash: 4edc3eedf0d2e91865272c1e693264ae6bbb3c6d
source_type: github
author: Marek Polacek
headline: 'c++/reflection: splicing null reflection'
tldr: The compiler now detects and handles splicing of null reflections in C++ reflection.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4edc3eedf0d2e91865272c1e693264ae6bbb3c6d
date: '2026-04-17'
---

When splicing a null reflection, the compiler was printing a note indicating that the `lang_type` was not supported. This patch detects the splicing of a null reflection, which is represented by `unknown_type_node`, and handles it appropriately. A new test case has been added to verify the fix.
