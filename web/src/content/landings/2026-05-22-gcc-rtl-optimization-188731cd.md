---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- bugfix
- rtl-optimization
- architecture-specific
- bit-fields
commit_hash: 188731cde7a5b36df6aea08eec035ceece150ce9
source_type: github
author: Konstantinos Eleftheriou
headline: Storing integral bit fields no longer asserts on SUBREG narrowing failures
tldr: GCC now gracefully falls back to a different method when `SUBREG` narrowing
  of multi-word integral bit fields fails, preventing assertions and improving robust…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `store_integral_bit_field` function in `expmed.cc` handles storing
  values into bit fields that span multiple words. Previously, the `simplify_gen_subreg`
  call to narrow a `SUBREG` (Sub-register) for multi-word fields could fail, particularly
  when dealing with vector types (e.g., `V8SI` on big-endian AArch64 where `validate_subreg`
  rejects word-aligned subregs). This failure would lead to a `gcc_assert(op0)` firing.
  Unlike `extract_integral_bit_field` which migrated to `force_subreg`, the store
  side couldn't due to `op0` being an lvalue. This patch now directs such failures
  to `store_split…
primer_general: Compilers optimize your code by working with an internal representation
  called Register Transfer Language (RTL). This commit addresses an issue within GCC's
  RTL optimization pass related to how it handles storing data into "bit fields."
  Bit fields are small chunks of memory within a larger data type (like a few bits
  within an integer). When these bit fields span across multiple memory "words" (the
  natural size of data that your computer's processor handles at one time), the compiler
  needs to combine or split operations to store the data correctly. Previously, in
  certain complex scenarios, especially when dealing with vector data types on specific
  architectures (like AArch64 in big-endian mode), the compiler would encounter an
  internal error and crash if it couldn't perfectly narrow down the memory location
  using a `SUBREG` (sub-register) operation. This fix teaches the compiler to handle
  these tricky situations more gracefully by switching to a different, more general
  method (`store_s…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/188731cde7a5b36df6aea08eec035ceece150ce9
date: '2026-05-22'
is_stub: false
---

When trying to store multi-word integral bit fields, GCC's `store_integral_bit_field` function previously asserted if `SUBREG` narrowing failed, especially with vector operations. This commit replaces the assertion with a graceful fallback to `store_split_bit_field`, mirroring the behavior of other code paths. This change fixes an issue triggered by the avoid-store-forwarding pass, preventing unexpected crashes and improving compiler stability for specific architectures like AArch64 within big-endian contexts.
