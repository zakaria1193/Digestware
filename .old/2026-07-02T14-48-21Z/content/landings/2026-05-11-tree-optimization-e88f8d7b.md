---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- loop optimization
commit_hash: e88f8d7bfc811f6d152c42ba009255506f5beba1
source_type: github
author: Richard Biener
headline: Loop idiom recognition avoids speculating no-op load/store.
tldr: GCC's loop idiom recognition avoids speculating load/store pairs for modes that
  cannot transfer bits, preventing undefined behavior.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's loop idiom recognition (LIM) pass attempts to identify common
  loop patterns and transform them into more efficient code. This change addresses
  a bug where LIM would speculate on memory accesses even when the data type couldn't
  be meaningfully loaded or stored, or when a bitfield access would result in undefined
  behavior. The fix involves modifying the `execute_sm` function in `tree-ssa-loop-im.cc`
  to account for these cases.
primer_general: Modern compilers use many optimization passes to improve code performance.  One
  such pass is loop idiom recognition, which identifies common patterns in loops and
  replaces them with faster equivalents. This commit fixes a bug in GCC where the
  compiler would introduce potentially invalid load/store operations during loop optimization,
  especially when dealing with bitfields or boolean types.  The fix ensures that the
  compiler only speculates on valid memory transfers, preventing undefined behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e88f8d7bfc811f6d152c42ba009255506f5beba1
date: '2026-05-11'
is_stub: false
---

The loop idiom recognition pass in GCC was speculating load/store pairs for modes where bit transfer is impossible. This commit prevents the speculation for such modes, including boolean types and bitfield accesses.  It also avoids undefined behavior when bitfield loads are out-of-bounds.
