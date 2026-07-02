---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
- optimization
commit_hash: ecfbd7d1b92886024ac6e94000425b3cd0bd0194
source_type: github
author: Zhongyao Chen
headline: 'RISC-V: Remove interleaved vector synthesis optimization [PR125215]'
tldr: The "hi/lo" optimization path for interleaved stepped constant vector synthesis
  in RISC-V has been removed due to performance concerns.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit removes `expand_const_vector_interleaved_stepped_npatterns`'s
  hi/lo optimization path in `riscv-v.cc`. The change simplifies vector synthesis
  and removes obsolete tests (`slp-interleave-[1-5].c`). The removed optimization
  aimed to improve the generation of interleaved stepped constant vectors, but proved
  less effective than the merge fallback.
primer_general: This commit concerns vectorization, which is an optimization technique
  where scalar operations are replaced with vector operations that process multiple
  data elements simultaneously.  This change specifically impacts the RISC-V architecture's
  vector extension.  The optimization attempted to generate efficient code for specific
  patterns of vector initialization, but was ultimately detrimental to performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ecfbd7d1b92886024ac6e94000425b3cd0bd0194
date: '2026-05-08'
is_stub: false
---

The commit removes the "hi/lo" optimization in interleaved stepped constant vector synthesis for RISC-V. This optimization was found to be less effective than the fallback merge version, especially after addressing overflow issues.  The associated tests have also been removed.
