---
project: gcc
subsystem: gensupport
patch_id: null
tags:
- gensupport
- bugfix
- parsing
commit_hash: 5efc59de33f0125fe02df9e03b15ad4307c1f53e
source_type: github
author: Jakub Jelinek
headline: 'Gensupport: Fix handling of // comments.'
tldr: Fixes an infinite loop in gensupport.cc that prevented proper handling of //
  comments in certain syntax files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `convert_syntax` function in `gensupport.cc` failed to correctly
  parse // comments due to an infinite loop caused by an incorrect logical operator.  Specifically,
  the `while (*templ != '\n' || *templ != '\0') ++templ;` loop never terminated because
  it required *both* conditions to be false. The fix replaces `||` with `&&`.
primer_general: The "gensupport" subsystem in GCC helps automate the generation of
  code from templates.  This involves parsing specially formatted files that describe
  the syntax of various programming languages and hardware architectures. This commit
  fixes a bug in the comment handling logic, ensuring that the parser correctly identifies
  and ignores comments, preventing errors during code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5efc59de33f0125fe02df9e03b15ad4307c1f53e
date: '2026-04-22'
---

A faulty logical operator in the convert_syntax function caused an infinite loop when processing // comments in new syntax *.md files. Replacing `||` with `&&` in the while loop condition resolves the issue, ensuring correct parsing and handling of comments.
