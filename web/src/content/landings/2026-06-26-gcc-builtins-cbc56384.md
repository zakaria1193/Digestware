---
project: gcc
subsystem: gcc/builtins
patch_id: null
tags:
- builtins
- optimization
- middle-end
commit_hash: cbc56384029c9224280b0a1018fb9502797f243d
source_type: github
author: H.J. Lu
headline: determine_block_size now sets len_rtx to minimum size for fixed-size blocks
tldr: GCC's `determine_block_size` function now ensures `len_rtx` is set to the minimum
  size when block sizes are fixed, improving accuracy for block operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `determine_block_size` function, located in `builtins.cc`, is crucial
  for assessing the size of memory blocks involved in built-in functions like `memcpy`
  and `memset`. This patch ensures that if `min_size == max_size` for a block (indicating
  a fixed size), `len_rtx` is explicitly set to this minimum size. This impacts `emit_block_move_via_pattern`
  and `set_storage_via_setmem` in `expr.cc`, which rely on `len_rtx` for pattern matching
  and code generation. By formalizing this representation, it eliminates ambiguity
  for fixed-size blocks, allowing for more precise instruction selection and…
primer_general: Compilers often recognize common operations, like copying chunks of
  memory (`memcpy`) or setting a region of memory to a specific value (`memset`),
  and replace them with highly optimized built-in functions. Before doing this, the
  compiler needs to determine the size of the memory block being operated on. This
  change improves how the compiler handles situations where the size of these memory
  blocks is fixed and known at compile time. Specifically, if the compiler knows a
  block will always be, for example, exactly 16 bytes, it will now explicitly record
  that fixed size more clearly internally. This helps the compiler generate slightly
  better and more accurate machine code for these common memory operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cbc56384029c9224280b0a1018fb9502797f243d
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

The `determine_block_size` function in GCC has been updated to set the `len_rtx` parameter to the minimum block size when the minimum and maximum block sizes are identical. This change clarifies the size of fixed-size blocks for built-in functions like `__builtin_memcpy` and `__builtin_memset`, improving the accuracy of how these sizes are represented in the internal representation. As a result, the compiler can make more precise decisions when optimizing memory block operations.
