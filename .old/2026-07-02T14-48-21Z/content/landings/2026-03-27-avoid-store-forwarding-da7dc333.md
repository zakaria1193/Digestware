---
project: gcc
subsystem: avoid-store-forwarding
patch_id: null
tags:
- optimization
- store-forwarding
- gcc
commit_hash: da7dc333c4a9ef997a9f3082fba73abf0380d684
source_type: github
author: Konstantinos Eleftheriou
headline: 'Avoid-store-forwarding: Continue BB analysis after complex memory ops'
tldr: The avoid-store-forwarding pass now continues analysis after encountering complex
  memory operations, potentially catching more optimization opportunities.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The avoid-store-forwarding pass optimizes memory operations within
  basic blocks. Previously, encountering a non-trivial store or load would halt analysis.
  This commit modifies `store_forwarding_analyzer::avoid_store_forwarding` to flush
  the pending store candidates and continue scanning, similar to the handling of throwing
  instructions and unknown-size memory operations. A toolchain developer outside this
  subsystem might not immediately realize the performance implications of prematurely
  terminating the analysis.
primer_general: Store forwarding is a compiler optimization technique where a load
  instruction retrieves data directly from a previous store instruction, instead of
  from memory.  This optimization improves performance by reducing memory accesses.
  This change enhances the compiler's ability to identify store-forwarding opportunities,
  even in the presence of complex memory operations within a basic block.  A basic
  block is a sequence of instructions with a single entry and exit point. By continuing
  analysis after complex memory operations, the compiler can potentially discover
  more opportunities for store forwarding and generate more efficient code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/da7dc333c4a9ef997a9f3082fba73abf0380d684
date: '2026-03-27'
is_stub: false
---

The avoid-store-forwarding pass in GCC previously stopped analyzing a basic block after encountering a complex memory operation. This change replaces the early return with a flush-and-continue, clearing pending store candidates and continuing the scan. This allows the pass to identify and exploit store-forwarding opportunities even after complex memory operations, potentially improving performance.
