---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- compiler bugfix
commit_hash: 6a36a6dbe1379325f067fd90b237b1b78e211526
source_type: github
author: Richard Biener
headline: Fix insertion of early-break iteration count definition.
tldr: Correctly inserts loop iteration count definition after labels in vect_do_peeling.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR tree-optimization/128394 highlights a bug in `tree-vect-loop-manip.cc`'s
  `vect_do_peeling` where the iteration count definition for early-break conditions
  was inserted incorrectly. Because the function uses a `gsi_after_labels` iterator,
  insertions should logically occur after, but the `gsi_insert_after` operation was
  not correctly placing the definition relative to labels. The fix correctly uses
  `gsi_insert_before` in conjunction with the `gsi_after_labels` iterator to ensure
  proper placement of the niter definition, maintaining loop invariant correctness.
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler where the code is represented in an intermediate
    form called 'tree'. Optimizations are applied to this representation before further
    code generation.
- term: vect_do_peeling
  definition: A function within GCC's vectorizer that performs loop peeling, a technique
    where one or more iterations of a loop are duplicated outside the main loop to
    handle loop termination conditions or alignment requirements for vectorization.
- term: iteration count definition
  definition: In the context of loop optimization, this refers to the calculation
    or definition of how many times a loop will execute. This is crucial for optimizations
    like loop vectorization and software pipelining.
- term: early-break
  definition: A condition within a loop that causes it to terminate prematurely, before
    completing all intended iterations. This can complicate optimizations if not handled
    correctly.
- term: GSI
  definition: Generic Statement Iterator. An iterator used in GCC's intermediate representation
    (tree) to traverse and manipulate basic blocks and statements within functions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6a36a6dbe1379325f067fd90b237b1b78e211526
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the `vect_do_peeling` function within GCC's tree-vectorizer, specifically concerning the insertion of the early-break iteration count definition. The problem arose because the insertion was happening after labels using an iterator that required insertion before. The fix changes the insertion method to `gsi_insert_before` when using a `gsi_after_labels` iterator, ensuring the definition is placed correctly in the intermediate representation.
