---
project: gcc
subsystem: avoid-store-forwarding
patch_id: null
tags:
- optimization
- store-forwarding
- register allocation
- gcc
commit_hash: ba0d75df9c02da51f212f6fe50d96b18265c7181
source_type: github
author: Konstantinos Eleftheriou
headline: 'Avoid-store-forwarding: Reject bit-inserts that clobber live hard regs'
tldr: The avoid-store-forwarding pass now avoids generating bit-insert sequences that
  would corrupt live hardware registers.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's `store_bit_field` can generate bit-insert sequences with side
  effects on hard registers.  This commit adds a liveness check to `store_forwarding_analyzer::process_store_forwarding`,
  using `df_simulate_one_insn_backwards` to compute live-out hard-register sets cached
  in `store_forwarding_analyzer::m_bb_live_after`.  The cache is populated lazily.
  A toolchain developer might not immediately realize the interaction with the flag
  register on x86.
primer_general: Store forwarding is an optimization where a load instruction obtains
  data directly from a prior store, avoiding a memory access. This commit improves
  the correctness of the store-forwarding optimization in GCC. It addresses a potential
  issue where bit-insert instructions generated during store forwarding could overwrite
  hardware registers that are still in use, leading to incorrect program behavior.
  A hardware register is a storage location within the CPU itself. The compiler now
  checks if any hardware registers are "live" (still holding needed values) before
  performing the optimization, preventing corruption of those registers and ensuring
  the program works as expected.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ba0d75df9c02da51f212f6fe50d96b18265c7181
date: '2026-03-27'
is_stub: false
---

The avoid-store-forwarding optimization in GCC can generate bit-insert sequences that inadvertently clobber hardware registers, such as the flags register on x86, potentially corrupting flag-dependent sequences. To prevent this, the pass now performs a liveness check before applying the transformation. It identifies the hard registers clobbered by the bit-insert sequences and rejects the transformation if any of them are live at the insertion point, ensuring correctness.
