---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- ssa
- bugfix
commit_hash: 2686ecea4f63daf463ab8674c657b2d7f30de737
source_type: github
author: Richard Biener
headline: Fix Value Numbering to avoid stale optimistic expressions in SSA
tldr: Corrects GCC's Value Numbering to prevent stale optimistic expressions from
  causing incorrect SSA name reuse, fixing a bug in SSA SCCVN.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch targets `tree-ssa-sccvn.cc` to resolve PR tree-optimization/128651.
  The core issue was in `vn_nary_build_or_lookup_1`, where expressions built with
  optimistic operand value numbers were inserted into `valid_info->nary`. This could
  lead to stale entries if the operands later varied. The fix introduces `vn_tables_s::inserted_exprs`,
  a separate table keyed by the expression's operands (not value numbers), to manage
  re-usable SSA names across iterations. Expressions are now correctly linked into
  the undo chain via `valid_info->nary` but re-use is managed through `inserted_exprs`,
  ensur…
primer_glossary:
- term: Value Numbering (VN)
  definition: A compiler optimization technique that identifies equivalent expressions
    by assigning them a unique 'value number'. This allows the compiler to avoid recomputing
    values that have already been computed and are known to be equivalent.
- term: SSA (Static Single Assignment)
  definition: An intermediate representation form used in compilers where every variable
    is assigned a value exactly once. This simplifies many optimization passes by
    making data flow explicit.
- term: SSA SCCVN
  definition: A specific optimization pass in GCC that combines Static Single Assignment
    (SSA) form with Value Numbering, particularly focusing on strongly connected components
    (SCCs) in the control flow graph.
- term: optimistic expression
  definition: An expression in a compiler's intermediate representation that is created
    based on tentative or assumed values of its operands. These assumptions might
    later prove to be incorrect.
- term: SSA name
  definition: In the SSA form, a unique identifier assigned to each version of a variable.
    When a variable is redefined, a new SSA name is created.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2686ecea4f63daf463ab8674c657b2d7f30de737
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's SSA-based Value Numbering (VN) optimization pass. The issue occurred when optimistic expressions, derived from value numbers that might change later, were inserted into the Value Numbering hash table. This led to stale entries persisting, causing incorrect SSA name reuse. The fix introduces a new `inserted_exprs` table to track expressions based on their operands rather than optimistically-keyed value numbers, ensuring correct SSA name generation.
