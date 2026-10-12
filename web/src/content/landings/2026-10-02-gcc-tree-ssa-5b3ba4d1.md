---
project: gcc
subsystem: gcc/tree-ssa
patch_id: null
tags:
- optimization
- refactor
commit_hash: 5b3ba4d1832dd5b5879f98ae938a35fcb63110ff
source_type: github
author: Aldy Hernandez
headline: 'sccvn: Extract unwind state recording'
tldr: Separates recording of unwind state in sccvn pass for future reuse.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, the logic for recording the unwind state, previously
  embedded within `do_rpo_vn_1`, has been extracted into a new standalone function
  `record_unwind_state`. This function is now called by `do_rpo_vn_1`. This decomposition
  is intended to enable other passes or functions, such as `do_unwind`, to utilize
  the same unwind state recording mechanism, improving code sharing and maintainability
  within the SSA pass infrastructure.
primer_glossary:
- term: sccvn
  definition: Strongly Connected Components Value Numbering. A compiler optimization
    technique that uses value numbering within strongly connected components (typically
    loops) to identify and represent computations efficiently.
- term: unwind state
  definition: Information that the compiler generates to allow the runtime system
    to correctly unwind the call stack. This is crucial for exception handling and
    stack traces.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation in compilers
    where every variable is assigned exactly once. It simplifies many optimizations
    by making data flow explicit.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5b3ba4d1832dd5b5879f98ae938a35fcb63110ff
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

The GCC's sccvn (Strongly Connected Components Value Numbering) pass now explicitly records the unwind state in a separate function, `record_unwind_state`. Previously, this recording was inlined within the `do_rpo_vn_1` function. This refactoring allows the unwind state to be recorded by other functions in the future, promoting code reuse and modularity.

This change enhances the compiler's internal structure, enabling more flexible optimization strategies related to exception handling unwind information.
