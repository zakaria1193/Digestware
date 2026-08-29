---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- compiler bug
- pr127105
commit_hash: 5fa2866f2674d274034de150f669aee611c2d9fe
source_type: github
author: Richard Biener
headline: Fix ICE with empty reduction in vectorization analysis
tldr: Corrects a bug in vectorization analysis that caused an ICE when encountering
  empty reduction chains.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes an ICE in `vect_analyze_slp_reduc_chain` within `tree-vect-slp.cc`
  where `scalar_stmts[0]` was accessed before verifying its existence. This corrects
  the analysis logic for reduction chains, preventing crashes when the chain is empty
  or malformed.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error, a crash within the compiler itself, usually
    indicating a bug in the compiler's logic.
- term: vectorization
  definition: An optimization process that transforms scalar code into vector code,
    allowing operations to be performed on multiple data elements simultaneously.
- term: SLP
  definition: Sliding Window Pattern, a vectorization technique that finds adjacent
    identical operations in the code and groups them into a single vector instruction.
- term: reduction chain
  definition: A sequence of operations where the result of one operation is used as
    an input to the next, typically accumulating a value (e.g., sum, product) across
    a set of data.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5fa2866f2674d274034de150f669aee611c2d9fe
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

This commit resolves an internal compiler error (ICE) in the vectorization analysis pass (`vect_analyze_slp_reduc_chain`). The bug occurred when the analysis attempted to access a non-existent statement after verifying its existence. The fix ensures that the statement is accessed only after its presence is confirmed, preventing the ICE and adding a new test case for this scenario.
