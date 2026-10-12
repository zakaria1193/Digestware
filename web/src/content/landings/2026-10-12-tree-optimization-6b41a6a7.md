---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- ICE
commit_hash: 6b41a6a73ef8f39ac913c0224a2c23b67f2a0665
source_type: github
author: Richard Biener
headline: Fix ICE in SLP vectorizer when scheduling extern vector defs.
tldr: Prevent compiler crash when scheduling vector definitions from control statements.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp_node` function in `tree-vect-slp.cc` handles
  the scheduling of nodes for the Superword Level Parallelism (SLP) vectorizer. When
  an external vector definition, created by a control statement, is scheduled, the
  subsequent transformation pass incorrectly asserts due to an outdated view of the
  vector definition's status. This commit adjusts the assertion to treat these 'extern'
  definitions similarly to non-last-statement definitions, allowing the transformation
  to proceed correctly without an ICE.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. An ICE signifies a bug within the compiler
    itself, causing it to crash during compilation rather than producing an error
    message about the source code.
- term: SLP vectorizer
  definition: Superword Level Parallelism vectorizer. This part of the compiler identifies
    opportunities to perform the same operation on multiple data elements simultaneously
    using vector instructions.
- term: External vector definition
  definition: A vector variable or definition whose storage or properties are determined
    externally, often originating from a control flow statement or other non-local
    context within the code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6b41a6a73ef8f39ac913c0224a2c23b67f2a0665
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

An internal compiler error (ICE) that occurred when scheduling vector definitions created by control statements has been fixed. The issue arose because the vectorizer's re-scheduling logic asserted incorrectly on external vector definitions.

This change modifies the SLP vectorizer to correctly handle these external definitions, preventing the ICE and improving robustness. A new test case has been added to verify the fix.
