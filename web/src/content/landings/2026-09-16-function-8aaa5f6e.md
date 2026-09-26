---
project: gcc
subsystem: function
patch_id: null
tags:
- optimization
- stack alignment
- x86
- aarch64
commit_hash: 8aaa5f6e62075c8bd3cfe7ec2d4f3543b3e6eccd
source_type: github
author: Oleg Tolmatcev
headline: 'function: Honour over-alignment in stack local allocation'
tldr: Ensures stack local object allocation respects required alignment beyond platform
  limits.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Updates `assign_stack_local` to correctly handle objects with alignment
  requirements exceeding `MAX_SUPPORTED_STACK_ALIGNMENT`. It introduces runtime alignment
  for over-aligned temporaries and locals, similar to `expand_stack_vars` and `assign_parm_setup_block`.
  The function `assign_stack_local_2` is introduced to return the address before runtime
  alignment, allowing for proper alignment within reserved space. This addresses PR54412
  and PR1209, where strict alignment requirements could lead to faults or incorrect
  memory access due to under-aligned stack slots.
primer_glossary:
- term: MAX_SUPPORTED_STACK_ALIGNMENT
  definition: A backend-defined limit on the maximum alignment that can be guaranteed
    for stack-allocated variables. Some targets cap this at 128 bits.
- term: assign_stack_local
  definition: A compiler internal function responsible for allocating space and determining
    the address for local variables on the call stack.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used internally
    by GCC to represent code before it is optimized and translated into machine code.
- term: VIRTUAL_STACK_VARS_REGNUM
  definition: A special register number used internally by GCC to represent the base
    address of the stack frame for virtual stack variables.
- term: SJLJ exception handling
  definition: Setjmp/Longjmp exception handling. A method for implementing exceptions
    that relies on stack manipulation rather than a dedicated runtime library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8aaa5f6e62075c8bd3cfe7ec2d4f3543b3e6eccd
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This change modifies how the compiler assigns stack space for local variables, ensuring that objects requiring alignment beyond the platform's maximum supported stack alignment are handled correctly. It reserves extra space and performs run-time alignment, preventing issues like memory access faults on architectures like x86.
