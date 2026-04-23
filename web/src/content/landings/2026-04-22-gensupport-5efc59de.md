---
project: gcc
subsystem: gensupport
patch_id: null
tags:
- bugfix
- gensupport
- comments
commit_hash: 5efc59de33f0125fe02df9e03b15ad4307c1f53e
source_type: github
author: Jakub Jelinek
headline: 'Gensupport: Fix comment handling in syntax files.'
tldr: Fixes an infinite loop in gensupport.cc when handling // comments in the new
  syntax *.md files.
why_it_matters: This bug prevented proper processing of comments in syntax files,
  potentially leading to incorrect code generation or unexpected behavior. The fix
  ensures that comments are handled correctly during the generation process.
impact_score: 5
impact_rationale: Fixes a bug that caused an infinite loop, preventing proper processing
  of comments in syntax files.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gensupport` subsystem handles generation of diagnostic messages
  and other compiler artifacts from `.md` files. The `convert_syntax` function parses
  these files.  This patch fixes an infinite loop in the comment handling logic. Toolchain
  devs outside the subsystem might not immediately recognize the impact, as it's specific
  to the new syntax used in certain `.md` files.
primer_general: The `gensupport` component in GCC is responsible for automatically
  generating parts of the compiler from higher-level descriptions, often stored in
  `.md` files. This allows developers to define patterns and syntax rules that the
  compiler needs to understand. The `convert_syntax` function specifically deals with
  parsing and interpreting these syntax descriptions. A bug in comment handling could
  prevent the tool from correctly processing these syntax files, leading to errors
  in the generated compiler code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5efc59de33f0125fe02df9e03b15ad4307c1f53e
date: '2026-04-22'
---

The patch corrects a logical error in the `convert_syntax` function within `gensupport.cc`. The original code used an incorrect logical operator (`||` instead of `&&`) in a `while` loop, causing an infinite loop when encountering `//` comments.  The corrected code now uses `&&` to properly handle comments.
