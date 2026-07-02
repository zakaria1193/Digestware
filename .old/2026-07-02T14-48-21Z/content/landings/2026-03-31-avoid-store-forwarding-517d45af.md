---
project: gcc
subsystem: avoid-store-forwarding
patch_id: null
tags:
- optimization
- rtl
- aarch64
- bugfix
commit_hash: 517d45af94f98f2c8c8bdf5231aa662c82b46c13
source_type: github
author: Konstantinos Eleftheriou
headline: Reapply extension after bit insert in store-forwarding
tldr: GCC's avoid-store-forwarding pass now correctly reapplies sign/zero extensions
  to values after bit-field insertions for non-eliminated loads.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `avoid-store-forwarding` pass in GCC optimizes memory accesses
  by trying to forward a value directly from a store to a subsequent load, bypassing
  memory. This optimization can interact with `SIGN_EXTEND` and `ZERO_EXTEND` operations
  that expand smaller data types to larger register widths. The issue arose when a
  bit-field insert, which manipulates specific bits within a register, followed an
  extending load that couldn't be fully eliminated. The fix in `process_store_forwarding`
  involves explicitly reasserting the extension (e.g., via `SIGN_EXTEND` or `ZERO_EXTEND`
  `RTL` operations) to ens…
primer_general: When a computer program runs, it often stores data in memory and then
  retrieves it later. A common optimization called 'store-forwarding' tries to make
  this faster by directly passing data from a 'store' (writing to memory) to a 'load'
  (reading from memory) if they happen close together, avoiding an unnecessary trip
  to main memory. This commit fixes a subtle problem in this optimization when dealing
  with 'extensions', which is when a small number (like an 8-bit number) is copied
  into a larger storage space (like a 32-bit register) and needs to be correctly 'padded'
  with zeros or ones. If a specific operation called a 'bit insert' happened, the
  compiler was sometimes forgetting to correctly re-apply this padding, leading to
  potentially wrong values. This fix ensures that the numbers are always correctly
  extended, maintaining the program's accuracy.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/517d45af94f98f2c8c8bdf5231aa662c82b46c13
date: '2026-03-31'
is_stub: false
---

This commit fixes a bug in the `avoid-store-forwarding` pass where `SIGN_EXTEND` or `ZERO_EXTEND` semantics were lost after a bit insert sequence. When an extending load was not fully eliminated, the bit-field insert operated on the full-width register but failed to reapply the extension, leading to stale upper bits. The fix ensures that the correct extension is re-applied, mirroring the behavior of fully eliminated loads, preventing incorrect values from propagating.
