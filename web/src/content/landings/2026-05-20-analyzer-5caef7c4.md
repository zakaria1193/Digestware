---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- static analysis
- pointer arithmetic
- optimization
commit_hash: 5caef7c4a904a065706ad375691f3b9d9bf525cb
source_type: github
author: David Malcolm
headline: 'analyzer: Add Pointer Difference Folding'
tldr: The static analyzer now folds pointer subtraction expressions, allowing it to
  better handle `std::string::size()` on non-empty strings.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `region-model-manager.cc` by adding pointer difference
  folding to the `-fanalyzer`. The `maybe_fold_binop` function now folds expressions
  of the form `(X POINTER_PLUS Y) POINTER_DIFF_EXPR X` to `Y`. This enables the analyzer
  to handle `std::string size()` calls on non-empty strings by simplifying the pointer
  arithmetic involved.
primer_general: The `-fanalyzer` is a tool that attempts to find bugs in code by reasoning
  about what values variables might hold during program execution, without actually
  running the program. This commit improves the analyzer's ability to understand pointer
  arithmetic, specifically pointer subtraction (`(X + Y) - X`). This allows the analyzer
  to better understand how standard library components like `std::string` work and
  find potential issues in code that uses them.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5caef7c4a904a065706ad375691f3b9d9bf525cb
date: '2026-05-20'
is_stub: false
---

The static analyzer can now simplify expressions involving pointer subtraction. Specifically, it can fold `(X + Y) - X` to `Y`. This allows `-fanalyzer` to reason about `std::string::size()` when called on non-empty strings. This improvement enhances the analyzer's ability to detect potential issues in code that uses pointer arithmetic.
