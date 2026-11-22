---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- attribute
- compiler-backend
- low-level-code
commit_hash: b4b2c9cc882d8fdbf1fc1923a59b7c71d02201ba
source_type: github
author: Guo Jie
headline: 'LoongArch: Implement support for naked functions'
tldr: LoongArch GCC now supports the 'naked' function attribute.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Support for the `__attribute__((naked))` function attribute has been
  added to the LoongArch backend. This attribute instructs the compiler not to generate
  a standard prologue or epilogue for the function. The implementation in `config/loongarch/loongarch.cc`
  and related files ensures that: frame register masks are not computed for naked
  functions; the prologue and epilogue emission is skipped (`loongarch_expand_prologue`/`epilogue`);
  static stack size is reported as zero; `TARGET_ALLOCATE_STACK_SLOTS_FOR_ARGS` is
  handled by a new function; `TARGET_WARN_FUNC_RETURN` is implemented; the `naked_…'
primer_glossary:
- term: Naked function
  definition: A function for which the compiler generates no prologue or epilogue
    code, allowing the programmer to provide custom entry and exit sequences.
- term: Prologue
  definition: The initial sequence of instructions in a function that sets up the
    stack frame, saves registers, and prepares for function execution.
- term: Epilogue
  definition: The final sequence of instructions in a function that restores saved
    registers, tears down the stack frame, and returns control to the caller.
- term: Stack frame
  definition: A region of memory on the call stack allocated for a function call,
    used to store local variables, parameters, and return addresses.
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b4b2c9cc882d8fdbf1fc1923a59b7c71d02201ba
date: '2026-09-17'
is_stub: false
stub_reason: ''
---

This commit introduces support for the `naked` function attribute on the LoongArch architecture. Naked functions allow developers to bypass the compiler's standard function prologue and epilogue generation, providing fine-grained control over function entry and exit code. This is useful for low-level code like bootloaders or interrupt handlers. The changes involve modifying frame information calculation, preventing prologue/epilogue emission, handling stack slot allocation for arguments, and recording the naked status in machine-specific function data. New test cases are included to verify this functionality.
