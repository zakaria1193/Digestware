---
project: gcc
subsystem: gensupport
patch_id: null
tags:
- gensupport
- bugfix
- comments
commit_hash: 5efc59de33f0125fe02df9e03b15ad4307c1f53e
source_type: github
author: Jakub Jelinek
headline: 'Gensupport: Fixed handling of // comments.'
tldr: The gensupport tool now correctly handles `//` comments in syntax files, fixing
  an infinite loop.
why_it_matters: Fixing the comment handling in gensupport ensures that syntax files
  are processed correctly, avoiding errors during compiler builds.
impact_score: 5
impact_rationale: Fixes a bug that could prevent gensupport from processing syntax
  files correctly, impacting compiler builds.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '`gensupport` is a tool used to generate support code for GCC, often
  from `.md` files that describe instruction syntax or other language features. The
  `convert_syntax` function parses these files. This commit fixes an error in how
  `convert_syntax` handles `//` comments, specifically the loop condition used to
  skip over comments. Compiler developers working on new architectures or language
  extensions that require modifications to the syntax files will benefit from this
  fix.'
primer_general: The GCC compiler uses a special tool called `gensupport` to automatically
  generate parts of its code. This tool reads special files describing things like
  the syntax of the programming languages it supports. This commit fixes a bug in
  `gensupport` that caused it to get stuck in an endless loop when it encountered
  comments (`//`) in those syntax files.  Fixing this bug ensures that `gensupport`
  can correctly process the syntax files and that the compiler can be built correctly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5efc59de33f0125fe02df9e03b15ad4307c1f53e
date: '2026-04-22'
---

The `convert_syntax` function in `gensupport.cc` had a bug in its handling of `//` comments, causing an infinite loop. The loop condition `while (*templ != '\n' || *templ != '\0')` used an incorrect logical operator. This commit fixes the condition to use `&&` instead, ensuring correct comment handling.
