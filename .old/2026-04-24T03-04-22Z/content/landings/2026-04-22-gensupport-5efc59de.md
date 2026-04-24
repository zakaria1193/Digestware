---
project: gcc
subsystem: gensupport
patch_id: null
tags:
- gcc
- gensupport
- bugfix
commit_hash: 5efc59de33f0125fe02df9e03b15ad4307c1f53e
source_type: github
author: Jakub Jelinek
headline: Gensupport Fixes Comment Handling
tldr: Fixes an endless loop in gensupport.cc caused by an incorrect logical operator
  when handling comments.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ``convert_syntax`` function in ``gensupport.cc`` had an error in
  its comment-handling logic. The loop ``while (*templ != '\n' || *templ != '\0')
  ++templ;`` should have used ``&&`` instead of ``||``, leading to an infinite loop.
  This impacts the processing of *.md files during code generation.
primer_general: The gensupport subsystem in GCC helps automate the generation of code
  from descriptive files. This commit fixes a bug in the comment-handling logic within
  these descriptive files. Specifically, when the compiler processed files with a
  certain syntax, it would get stuck in an infinite loop trying to parse a comment.
  This fix ensures that gensupport correctly handles comments, allowing the compiler
  to proceed normally.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5efc59de33f0125fe02df9e03b15ad4307c1f53e
date: '2026-04-22'
---

The code in ``gensupport.cc`` used an incorrect logical operator in a loop designed to handle comments, causing it to enter an endless loop. This occurred in the context of new syntax *.md files.  This commit fixes the operator, resolving the infinite loop.
