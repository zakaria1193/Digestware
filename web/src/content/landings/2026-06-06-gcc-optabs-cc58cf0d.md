---
project: gcc
subsystem: gcc/optabs
patch_id: null
tags:
- optimization
- gimple
- risc-v
- code generation
commit_hash: cc58cf0d2f9b255e29d9b7a409c5ab31542604d1
source_type: github
author: Richard Sandiford
headline: Extend can_open_code_p to handle bswap operations for store merging
tldr: GCC now uses `can_open_code_p` to determine if `bswap` operations can be open-coded
  during store merging, improving scalar optimization and fixing a RISC-V tes…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: GCC's `gimple-ssa-store-merging` pass attempts to coalesce multiple
  small stores into larger, more efficient ones, particularly when dealing with vector
  constructors or byte-swapping operations. The `can_open_code_p` function in `optabs-query.cc`
  serves as a centralized mechanism for determining if an operation can be expressed
  using direct machine instructions rather than a library call. This change integrates
  `bswap` operation checks into `can_open_code_p`, moving logic previously scattered
  across `maybe_optimize_vector_constructor`, `pass_optimize_bswap::execute`, and
  `imm_store_chain_info…
primer_general: When a computer program stores data in memory, it often does so in
  small pieces. Compilers like GCC try to optimize this by combining several small
  storage operations into one larger, more efficient operation, a process called "store
  merging." One specific operation that can benefit from this is "byte swapping" (`bswap`),
  which reorders the bytes within a word of data. This commit improves how GCC handles
  byte swapping during store merging. Previously, the compiler had separate, somewhat
  redundant checks to see if it could generate direct machine instructions for byte
  swaps. This change centralizes that decision-making into a single function, `can_open_code_p`,
  which is responsible for determining if an operation can be directly translated
  into machine code. This makes the compiler more efficient and fixes a specific problem
  that caused incorrect code generation for byte-swapping operations on RISC-V processors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cc58cf0d2f9b255e29d9b7a409c5ab31542604d1
date: '2026-06-06'
is_stub: false
---

This commit refactors GCC's store merging pass to rely on `can_open_code_p` for determining if `bswap` (byte swap) operations can be generated as inline code. Previously, this logic was duplicated and less efficient within `gimple-ssa-store-merging.cc`. By centralizing this check in `can_open_code_p` and extending it to handle various `bswap` cases, the compiler can more effectively optimize scalar code and resolve a bug in `gcc.dg/optimize-bswapsi-6.c` on RISC-V architectures.
