---
project: gcc
subsystem: gcc/hard-reg-set
patch_id: null
tags:
- rtl-optimization
- compiler-internals
- build-time-check
commit_hash: 20c529f47542e94e921556684f8ce27495135926
source_type: github
author: Xi Ruoyao
headline: 'Hard-reg-set: Make temporary SET for EXECUTE_IF_SET_IN_HARD_REG_SET a build-time
  error'
tldr: GCC now prevents the use of temporary `SET` objects with `EXECUTE_IF_SET_IN_HARD_REG_SET`
  at build time, avoiding future errors.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's `hard-reg-set` (`hard-reg-set.h`) defines a data structure for
  representing sets of hardware registers, crucial for register allocation and other
  RTL-level optimizations. The `EXECUTE_IF_SET_IN_HARD_REG_SET` macro is used to iterate
  over these sets. This commit introduces a build-time check to prevent the use of
  rvalue `SET` objects (temporary, unnamed objects) with this macro. Such usage could
  lead to undefined behavior or difficult-to-debug issues because the macro expects
  a stable `SET` object throughout its execution. The new `build_error_on_rvalue`
  function, called from the macro,…
primer_general: Imagine a computer program as a series of steps your CPU needs to
  perform. These steps often involve storing and retrieving data from special very
  fast memory locations called 'registers'. Compilers like GCC are responsible for
  intelligently assigning data to these registers to make the program run as quickly
  as possible. This process is called 'register allocation'. GCC has internal mechanisms
  to keep track of which registers are available or in use, often represented as 'sets'
  of registers. This change is about preventing a specific misuse of an internal compiler
  tool (`EXECUTE_IF_SET_IN_HARD_REG_SET`) that works with these register sets. Previously,
  it was possible to accidentally use temporary register sets that don't persist correctly,
  leading to potential bugs in the generated machine code. Now, the compiler itself
  will flag this as an error during *its own* compilation, making GCC more robust
  and preventing such mistakes from happening in the future.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/20c529f47542e94e921556684f8ce27495135926
date: '2026-06-05'
is_stub: false
---

This change enhances the GCC compiler's internal consistency by making it a build-time error to use temporary `SET` objects with the `EXECUTE_IF_SET_IN_HARD_REG_SET` macro. Previously, this could lead to subtle issues that were difficult to diagnose. By introducing a new `build_error_on_rvalue` function and calling it from the macro, future incorrect usage is proactively caught during GCC's own compilation.
