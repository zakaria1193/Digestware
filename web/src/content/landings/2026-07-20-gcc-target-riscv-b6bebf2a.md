---
project: gcc
subsystem: gcc/target/riscv
patch_id: null
tags:
- risc-v
- optimization
- atomic
commit_hash: b6bebf2a7326e6b5566f1aa2979233a60e5c8377
source_type: github
author: Shreya Munnangi
headline: RISC-V atomic load sequences improved
tldr: RISC-V atomic load sequences are optimized to remove redundant instructions
  and improve constraint handling.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch refactors RISC-V atomic load patterns in `constraints.md`
  and `sync-rvwmo.md`. It addresses PR target/124741 by removing redundant `sext.w`
  instructions after `lw` loads, and by combining address calculation into the load
  instruction itself. New constraints (`B1-B4`) and an iterator (`cond_extend`) are
  introduced to accurately model the interaction between memory ordering (`MEMMODEL_ACQUIRE`),
  the ZALASR/ZALRSC extensions, and the modes of atomic operations, ensuring correct
  generation of acquire semantics and preventing issues with zero-extension loads
  on ZALRSC-unsupported target…
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on Reduced
    Instruction Set Computing principles. It is modular and extensible, making it
    popular for embedded systems and high-performance computing.
- term: atomic operations
  definition: Operations that are guaranteed to be performed indivisibly, without
    interruption from other threads or processes. They are crucial for concurrent
    programming to ensure data consistency.
- term: RV64
  definition: The 64-bit version of the RISC-V instruction set architecture. It supports
    64-bit pointers and general-purpose registers.
- term: ZALRSC / ZALASR
  definition: RISC-V extensions related to atomic memory operations. ZALRSC (Atomic
    Loads and Reserved Store Conditional) and ZALASR (Atomic Loads and Reserved Store-Acquire)
    provide specific atomic primitives and memory ordering guarantees.
discussion_id_link: github:gcc-mirror/gcc#124741
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b6bebf2a7326e6b5566f1aa2979233a60e5c8377
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This commit optimizes atomic load sequences on RISC-V architectures, particularly for RV64. It eliminates redundant sign extensions and improves address arithmetic. New constraints and iterators are introduced to correctly handle memory model acquire semantics and target-specific features like ZALRSC, ensuring generated code is more efficient and correct across different configurations.
