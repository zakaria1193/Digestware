---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
commit_hash: 4edc3eedf0d2e91865272c1e693264ae6bbb3c6d
source_type: github
author: Marek Polacek
headline: 'c++/reflection: splicing null reflection'
tldr: The compiler now detects splicing a null reflection and avoids printing an error
  message.
why_it_matters: This commit improves the usability of the C++ reflection feature by
  preventing confusing error messages when dealing with null reflections.
impact_score: 4
impact_rationale: A quality-of-life improvement relating to C++ reflection, preventing
  spurious warnings. Limited user impact.
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

The compiler was representing a null reflection with `unknown_type_node`, leading to an error message when splicing. This commit now detects splicing of a null reflection, preventing the error message from being printed. A new test case has also been added.
