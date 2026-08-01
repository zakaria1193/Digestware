---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- compiler
- optimization
- bit-int
- aarch64
commit_hash: b61bb45f622b94dd2a2ebafb4a7e815b6bdf5dad
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Fix miscompilation with unsigned add/subtract operations'
tldr: Fixes incorrect handling of unsigned add/subtract operations for bit-integers,
  resolving miscompilations on certain architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bitintlower` pass optimizes bit-integer operations. This change
  corrects the use of `IFN_UADDC`/`IFN_USUBC` vs. `.SUB_OVERFLOW` based on target
  `optabs`. Targets without specific optabs incorrectly used general `.SUB_OVERFLOW`
  for bit-integer arithmetic, leading to incorrect results when overflow/underflow
  semantics differ from standard integer types.
primer_glossary:
- term: bitintlower
  definition: A GCC compiler pass that lowers operations on variable-width integers
    (bit-integers) into more primitive operations understandable by the target architecture.
- term: optabs
  definition: Optimization tables in GCC that define machine-specific operations,
    allowing the compiler to select the most efficient instructions for a given target.
- term: IFN_UADDC/IFN_USUBC
  definition: Specific instructions or patterns used for unsigned addition with carry
    and unsigned subtraction with borrow, often optimized for bit-integer operations.
- term: aarch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and servers,
    with its own set of instructions and calling conventions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b61bb45f622b94dd2a2ebafb4a7e815b6bdf5dad
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This commit addresses a miscompilation issue on aarch64 related to unsigned add/subtract operations on bit-integers. The problem arose when specific target architectures used different instruction sets for these operations, leading to incorrect results. The fix ensures correct handling by properly utilizing the appropriate instructions or fallbacks, thus resolving the miscompilation.
