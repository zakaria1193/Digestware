---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- bugfix
commit_hash: b3763e32ea4b0bf9e68bb89eac9bf2d7ab92680c
source_type: github
author: Richard Biener
headline: Optimization pass avoids rewriting multi-use statements.
tldr: GCC's `tree-ssa-reassoc` pass now always creates new statements for associative
  operands, preventing incorrect rewriting of multi-use definitions.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `optimize_vec_cond_expr` function within `tree-ssa-reassoc.cc`
  is part of GCC's reassociation pass, which aims to optimize expression trees. Prior
  to this change, the optimization could directly rewrite definition statements of
  associative operands. This is problematic if such statements have multiple use sites,
  as rewriting them would affect all those uses unintendedly. The fix introduces a
  new statement creation mechanism, ensuring that alterations are localized and do
  not cause wider, incorrect side effects when optimizing vector conditional expressions,
  which could include scalar repl…
primer_general: Compilers like GCC transform your source code into a lower-level representation,
  then perform various optimizations to make the compiled program run faster. One
  such optimization is called "reassociation," which rearranges operations in your
  code (e.g., `(A + B) + C` becoming `A + (B + C)`) to expose more opportunities for
  other optimizations. This commit addresses a bug in how GCC's reassociation pass
  handled certain expressions. Previously, when optimizing 'vector conditional expressions'
  (which are like `if-else` statements but operate on multiple data items simultaneously),
  the compiler might directly modify an existing calculation that was used in several
  places. This could lead to incorrect program behavior if other parts of the code
  relied on the original calculation. The fix ensures that the compiler now creates
  a brand-new calculation for these optimized operations, preventing unintended side
  effects and making the compiled code more robust.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3763e32ea4b0bf9e68bb89eac9bf2d7ab92680c
date: '2026-06-15'
is_stub: false
---

GCC's `tree-ssa-reassoc` optimization pass previously risked rewriting statements that had multiple uses, leading to incorrect code generation. This commit modifies the `optimize_vec_cond_expr` function to instead create a new statement for associative operands. This change ensures that existing definitions are not inadvertently altered, preserving program correctness and improving the reliability of the optimization pass.
