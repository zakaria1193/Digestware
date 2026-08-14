---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- arm
- rtl-optimization
- gcc
commit_hash: 67ec3f5215298dd7f3177ed16c10c84392db8bb6
source_type: github
author: Roger Sayle
headline: 'ARM: Fix missed optimization for lsls instruction'
tldr: Corrects a regression in GCC's ARM backend that prevented the use of the efficient
  'lsls' instruction on Thumb.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: A regression introduced by a prior change related to PR tree-optimization/123236
  caused `combine` to generate suboptimal RTL for ARM Thumb targets. Specifically,
  the pattern involving `(set (reg:SI ... ) (and:QI ...))` followed by a comparison
  was being translated in a way that prevented matching the efficient `lsls` instruction.
  This commit disables the problematic transformation in `combine`, restoring the
  ability to match the correct Thumb instruction by generating more suitable RTL,
  likely involving `zero_extract`.
primer_glossary:
- term: RTL (Register Transfer Language)
  definition: GCC's intermediate representation used after GIMPLE. It describes operations
    in terms of registers and memory locations, closer to machine code but still abstract.
- term: lsls instruction
  definition: A Thumb (ARM's 16-bit instruction set) instruction for logical shift
    left, often smaller and faster than its general-purpose equivalent.
- term: Combine pass
  definition: A GCC optimization pass that attempts to merge or simplify sequences
    of RTL instructions into more efficient forms.
- term: WORD_REGISTER_OPERATIONS
  definition: A target-specific option in GCC that indicates whether the architecture
    supports operations on operands wider than the native word size (e.g., 32-bit
    operations on a 16-bit machine).
- term: ARM
  definition: A widely used family of Reduced Instruction Set Computer (RISC) architectures,
    common in mobile devices and embedded systems.
- term: Thumb
  definition: A 16-bit instruction set architecture for ARM processors, designed for
    code density. It is a subset of the full ARM instruction set.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/67ec3f5215298dd7f3177ed16c10c84392db8bb6
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

A recent change intended to fix PR tree-optimization/123236 inadvertently caused a regression in GCC's ARM backend, specifically affecting Thumb code. The compiler now fails to emit the shorter `lsls` instruction for a particular optimization pattern, leading to less efficient code. This commit disables the offending transformation in the `combine` pass, resolving the issue and allowing GCC to generate the expected, more optimal RTL that matches ARM's Thumb instruction set.
