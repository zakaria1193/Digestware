---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
commit_hash: 7cdbbbdecb09e518e28c5116b05e0018b9460b95
source_type: github
author: Robin Dapp
headline: 'RISC-V: Fix single-step expansion.'
tldr: Corrects RISC-V single-step instruction expansion by using the correct pattern
  count.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In RISC-V vector extension support, `expand_const_vector_single_step_npatterns`
  in `riscv-v.cc` builds an intermediate vector using a secondary builder. This patch
  corrects the use of `npatterns` from this secondary builder, which could differ
  from the primary one, potentially leading to incorrect intermediate operations.
  It now correctly uses the `npatterns` from the primary builder.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7cdbbbdecb09e518e28c5116b05e0018b9460b95
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This change fixes an issue in the RISC-V vector constant synthesis where an incorrect number of patterns was used for creating intermediate operations. The fix ensures that the 'npatterns' from the original vector builder are used, aligning the expansion logic with the intended behavior and resolving a problem reported in PR126550.
