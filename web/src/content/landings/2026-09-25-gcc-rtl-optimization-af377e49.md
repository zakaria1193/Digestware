---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- bugfix
- optimization
- rtl
commit_hash: af377e494233869967d20299bcc228e01f673f46
source_type: github
author: Richard Biener
headline: Fix bogus simplification involving paradoxical subregs
tldr: Corrects an optimization that incorrectly distributed bitwise operations when
  paradoxical subregs were involved.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `combine.cc` function `distribute_and_simplify_rtx` had a bug where
  it would distribute `(and (xor B C) (not A))` into `(xor (ior A B) (ior A C))`.
  This transformation is problematic when `A` is a paradoxical subreg that gets spilled,
  as the two copies of `A` could diverge in value. The fix adds a check to gate this
  distribution, preventing it when `A` contains a paradoxical subreg, as identified
  in PR127606. A new test case `pr127606.c` is added.
primer_glossary:
- term: combine pass
  definition: A GCC optimization pass that attempts to combine multiple RTL instructions
    into a single, more efficient instruction.
- term: paradoxical subreg
  definition: A subregister that, due to its definition and usage, can have unexpected
    or conflicting values, often related to aliasing or overlapping register definitions.
    These can complicate compiler optimizations.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used in GCC
    that describes operations on registers and memory. Optimizations often operate
    on RTL.
- term: spilled
  definition: When a variable or register value cannot be held in a CPU register and
    must be temporarily stored in memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/af377e494233869967d20299bcc228e01f673f46
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

A bug in GCC's `combine` pass could lead to incorrect code generation when simplifying bitwise operations involving paradoxical subregisters. The `distribute_and_simplify_rtx` function incorrectly distributed `(and (xor B C) (not A))` into `(xor (ior A B) (ior A C))`. This caused issues when the paradoxical subregister `A` was spilled, leading to differing values that corrupted the final result. The fix gates this distribution when `A` involves a paradoxical subregister.

This resolves a bug that could produce incorrect output for programs using specific bitwise operations and subregister manipulations, ensuring program correctness.
