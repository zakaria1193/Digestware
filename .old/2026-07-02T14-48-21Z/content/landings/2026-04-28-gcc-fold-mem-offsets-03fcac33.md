---
project: gcc
subsystem: gcc/fold-mem-offsets
patch_id: null
tags:
- RISC-V
- optimization
- code size
commit_hash: 03fcac336e04ba2cd57495a47534accc145e160e
source_type: github
author: Philipp Tomsich
headline: 'Fold-mem-offsets: Move RISC-V size-optimization workaround to the backend.'
tldr: A workaround for RISC-V size optimizations has been moved from the fold-mem-offsets
  pass to the RISC-V backend, improving performance for other targets.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses a RISC-V-specific interaction between the ``fold-mem-offsets``
  pass and the RISC-V ``shorten-memrefs`` pass.  The original workaround, which skipped
  size-optimized basic blocks in ``pass_fold_mem_offsets::execute`` in ``fold-mem-offsets.cc``,
  has been removed.  Instead, ``flag_fold_mem_offsets`` is now disabled via ``SET_OPTION_IF_UNSET``
  in ``riscv_option_override`` in ``config/riscv/riscv.cc`` when compiling for size
  with compressed instructions.
primer_general: This commit resolves an issue between two compiler optimization passes,
  `fold-mem-offsets` and `shorten-memrefs`, on the RISC-V architecture. `fold-mem-offsets`
  optimizes memory access by combining offsets, while `shorten-memrefs` reduces the
  size of memory access instructions. To avoid conflicts when optimizing for code
  size on RISC-V, the `fold-mem-offsets` pass was previously disabled. This commit
  moves the disablement logic to the RISC-V backend, allowing other architectures
  to benefit from `fold-mem-offsets` during size optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/03fcac336e04ba2cd57495a47534accc145e160e
date: '2026-04-28'
---

A target-specific workaround in the ``fold-mem-offsets`` pass, which skipped basic blocks optimized for size to avoid conflicts with RISC-V's ``shorten-memrefs`` pass, has been moved to the RISC-V backend. This change allows other targets to benefit from offset folding in size-optimized blocks, while preserving the original RISC-V behavior by disabling ``fold-mem-offsets`` when optimizing for size with compressed instructions enabled.
