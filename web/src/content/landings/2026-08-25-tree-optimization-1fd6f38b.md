---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- compiler
commit_hash: 1fd6f38b133f7c4c2b87840dae93b68e2dc03b24
source_type: github
author: Richard Biener
headline: Fix ICE with partly populated vectors in SLP scheduling.
tldr: Corrects an ICE by ensuring vector scheduling fails gracefully when constraints
  are not met.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses an ICE in `vect_schedule_slp_node` related to
  SLP scheduling of vector code. When the scheduler encounters a situation where it
  cannot place statements due to constraints (potentially trapping), it previously
  triggered an assertion. This commit changes the behavior to emit a scheduling failure,
  which is a more robust way to handle such cases and is now covered by a new testcase.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. An unrecoverable error that occurs within the
    compiler itself, usually due to a bug in the compiler's logic.
- term: SLP
  definition: Superword Level Parallelism. A type of instruction-level parallelism
    where multiple independent data elements within a vector are processed in parallel
    by a single instruction.
- term: scheduling
  definition: The process of ordering instructions to maximize performance, often
    by minimizing dependencies and utilizing available execution units on the CPU.
- term: trapping statements
  definition: Statements that may cause an exception or trap if certain conditions
    are met (e.g., division by zero, accessing invalid memory). Scheduling these requires
    careful consideration of their potential side effects.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1fd6f38b133f7c4c2b87840dae93b68e2dc03b24
date: '2026-08-25'
is_stub: false
stub_reason: ''
---

This commit fixes an ICE (Internal Compiler Error) that occurred during SLP (Superword Level Parallelism) scheduling. The issue arose when constraints for potentially trapping statements could not be met. The fix modifies `vect_schedule_slp_node` to treat such unmet constraints as a scheduling failure instead of an assertion failure, thereby preventing the ICE and ensuring test coverage.
