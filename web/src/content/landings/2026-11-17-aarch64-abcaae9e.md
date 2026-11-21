---
project: gcc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- optimization
- instruction selection
commit_hash: abcaae9e947e7de5b4dfeabd852dfb2232fefe07
source_type: github
author: Samarth Tandale
headline: Optimize unsigned conditional subtraction using SUBS/CSEL.
tldr: Improves AArch64 code generation for unsigned conditional subtractions.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The AArch64 backend now includes a new pattern `aarch64_conditional_subtract<mode>`
  in `aarch64.md`. This pattern targets RTL generated for expressions equivalent to
  `x - (x >= q ? q : 0)` where the subtraction is unsigned. It splits into a `SUBS`
  instruction (which sets flags) and a `CSEL` instruction that uses those flags, effectively
  replacing a less optimal sequence of CMP, CSEL, and SUB instructions. This optimization
  is specifically for unsigned comparisons and subtractions.'
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture instruction set.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used within
    GCC to describe operations on hardware registers.
- term: SUBS
  definition: An AArch64 instruction that performs subtraction and sets the condition
    flags based on the result.
- term: CSEL
  definition: An AArch64 instruction that conditionally selects one of two values
    based on the condition flags.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/abcaae9e947e7de5b4dfeabd852dfb2232fefe07
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

This commit optimizes the generation of code for unsigned conditional subtractions on AArch64. Previously, expressions like `x - (x >= q ? q : 0)` were not recognized by the backend and resulted in separate compare, conditional move, and subtraction instructions. The patch introduces a new `define_insn_and_split` pattern that combines these operations into a more efficient sequence using the `SUBS` instruction (which updates condition flags) followed by a `CSEL` (conditional select), leading to improved instruction scheduling and potentially better performance.
