---
project: gcc
subsystem: target, aarch64
patch_id: null
tags:
- target
- aarch64
- jump table
commit_hash: a0f92a2e71bfe49085d9a3a5fbc219a7efd7411b
source_type: github
author: Kyrylo Tkachov
headline: AArch64 adds hooks for shared jump tables
tldr: AArch64 gains new hooks to control shared jump table usage based on target options
  and assembly requirements.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch introduces `TARGET_CAN_SHARE_JUMP_TABLE_P` and `TARGET_ASM_JUMP_TABLE_BASE`
  hooks for targets that need fine-grained control over shared jump table usage. `TARGET_CAN_SHARE_JUMP_TABLE_P`
  is a boolean hook queried before table duplication, allowing targets to refuse sharing
  based on function options (e.g., code model). `TARGET_ASM_JUMP_TABLE_BASE` is an
  `asm_out` hook called once per shared table to emit a base label, which is necessary
  for targets like AArch64 where entries are relative to a synthetic label defined
  at the table's location. The AArch64 implementation uses ADRP and A…
primer_glossary:
- term: jump table
  definition: A data structure used to implement efficient multi-way branching. It
    typically contains addresses of target code blocks, allowing a program to jump
    to a specific block based on an index.
- term: AArch64
  definition: The 64-bit ARM architecture, known for its high performance and power
    efficiency.
- term: hook
  definition: A mechanism in GCC that allows target-specific code to be called at
    certain points during compilation, enabling customization for different architectures.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. Crucial for shared libraries.
- term: ADRP
  definition: A 64-bit ARM instruction that adds a 20-bit immediate to the PC, setting
    the upper 32 bits of the destination register. Used for PC-relative addressing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0f92a2e71bfe49085d9a3a5fbc219a7efd7411b
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This commit introduces two new target hooks for AArch64: `TARGET_CAN_SHARE_JUMP_TABLE_P` and `TARGET_ASM_JUMP_TABLE_BASE`. The former allows ports to refuse sharing for specific dispatches under current target options, defaulting to true. The latter allows specifying a base label for shared jump tables, which is needed when entries are relative to that base. These hooks are essential for correctly handling shared jump tables, especially on architectures like AArch64 where address calculation methods can vary and require careful management of base labels and offsets to avoid assembler symbol redefinition or incorrect address computations.
