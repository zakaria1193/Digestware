---
project: gcc
subsystem: gcc/alpha
patch_id: null
tags:
- alpha
- security
- optimization
commit_hash: 1b9edbeca4bb77a4116610094824de738b64c8f1
source_type: github
author: Matt Turner
headline: 'Alpha: Add stack protector patterns'
tldr: New instructions for stack protector set/test improve canary handling on Alpha.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: On Alpha, the generic stack protector expansion would use ordinary
  pseudos for the canary, allowing the register allocator to spill them. This commit
  introduces new `alpha.md` patterns for `UNSPEC_SSP_SET` and `UNSPEC_SSP_TEST`. These
  are defined as single, atomic insns that clear their scratch registers upon completion.
  This restricts the lifetime of the canary value to only the necessary instructions,
  preventing accidental spills and improving efficiency, aligning Alpha's stack protector
  implementation with other targets like RISC-V and ARM.
primer_glossary:
- term: stack protector
  definition: A security feature (e.g., -fstack-protector) that adds a 'canary' value
    to the stack to detect buffer overflows. If the canary is overwritten, it indicates
    an overflow, and the program typically terminates to prevent exploitation.
- term: pattern
  definition: In GCC's target description files (e.g., `.md` files), a pattern defines
    a machine-specific instruction or a sequence of instructions that can be generated
    by the compiler.
- term: UNSPEC
  definition: An internal GCC construct representing a machine-specific operation
    that does not directly map to a standard instruction mnemonic.
- term: insn
  definition: Abbreviation for 'instruction', referring to a machine code instruction
    recognized by the target architecture.
- term: register allocator
  definition: A compiler component responsible for assigning program variables and
    temporary values to the limited number of physical registers available on the
    target CPU.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:alpha: add stack_protect_set and stack_protect_test patterns'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1b9edbeca4bb77a4116610094824de738b64c8f1
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

This commit introduces new target patterns, `UNSPEC_SSP_SET` and `UNSPEC_SSP_TEST`, for the Alpha architecture. These patterns define stack protector set and test operations as single, unsplittable instructions. This prevents the compiler from spilling the canary value across function calls, ensuring it remains available for the critical few instructions that require it, similar to optimizations on other architectures.
