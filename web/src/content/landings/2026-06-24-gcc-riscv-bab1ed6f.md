---
project: gcc
subsystem: gcc/riscv
patch_id: null
tags:
- risc-v
- compiler
- extension
- concurrency
- atomics
commit_hash: bab1ed6f96a90398ad55eb73978a0ea2b97adec7
source_type: github
author: Jiawei
headline: 'RISC-V: Add minimal Ziccamoc extension support'
tldr: GCC compiler now supports the RISC-V Ziccamoc extension for compare-and-swap
  atomics.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The incorporation of the RISC-V Ziccamoc extension into GCC requires
  updates to \`riscv-ext.def\`, \`riscv-ext.opt\`, and \`doc/riscv-ext.texi\`. Ziccamoc
  provides atomic CAS instructions, essential for lock-free data structures and concurrent
  programming. By recognizing this extension, GCC can generate correct and potentially
  optimized code for multi-threaded applications relying on atomic memory operations,
  improving correctness and performance in concurrent scenarios. A version test is
  included.
primer_glossary:
- term: RISC-V Ziccamoc
  definition: The RISC-V Ziccamoc extension adds support for atomic compare-and-swap
    (CAS) operations on main memory. These operations are crucial for implementing
    lock-free algorithms and ensuring data integrity in concurrent programming.
- term: atomic operations
  definition: Atomic operations are indivisible and uninterruptible sequences of operations.
    In the context of memory, they guarantee that a read-modify-write sequence on
    a memory location completes as a single, isolated unit, preventing race conditions.
- term: compare-and-swap (CAS)
  definition: Compare-and-swap is an atomic instruction that reads a memory location,
    compares its value with an expected value, and if they match, writes a new value
    to that location. It's a fundamental building block for lock-free data structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bab1ed6f96a90398ad55eb73978a0ea2b97adec7
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

This commit adds minimal support for the RISC-V Ziccamoc extension, which enables compare-and-swap (CAS) atomic operations on main memory. The changes involve updating the extension definitions, options, and documentation, and also include a new test case.
