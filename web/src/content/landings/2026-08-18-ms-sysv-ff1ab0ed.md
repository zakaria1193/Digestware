---
project: gcc
subsystem: ms-sysv
patch_id: null
tags:
- x86_64
- abi
- compiler
commit_hash: ff1ab0ed4b5221f4d7d3eff2e7aadb826e2c9d9a
source_type: github
author: H.J. Lu
headline: 'ms-sysv: Add call_do_test_unaligned helper for unaligned stacks'
tldr: Introduces an assembly wrapper to correctly call functions with the ms_abi attribute
  when the stack is unaligned.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ms_abi attribute on x86_64 requires a 16-byte stack alignment for
  function arguments. Direct calls to functions with this attribute may fail if GCC
  internally adjusts the stack (e.g., saving arguments via stack), leading to incorrect
  argument values for the callee. This commit introduces `call_do_test_unaligned`
  as an assembly wrapper that explicitly manages stack adjustments, ensuring correct
  alignment for calls to `do_test_unaligned`.
primer_glossary:
- term: ms_abi
  definition: Microsoft x64 calling convention. It has stricter stack alignment requirements
    than the System V AMD64 ABI.
- term: stack alignment
  definition: Ensuring that the stack pointer is aligned to a specific boundary (e.g.,
    16 bytes) before certain operations, which is crucial for performance and correctness
    on some architectures and calling conventions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ff1ab0ed4b5221f4d7d3eff2e7aadb826e2c9d9a
date: '2026-08-18'
is_stub: false
stub_reason: ''
---

The ms-sysv ABI has specific stack alignment requirements. Direct calls to functions marked with ms_abi, like do_test_unaligned, can fail when the stack is not properly aligned due to GCC's potential stack adjustments for argument saving. This change adds a new assembly function, call_do_test_unaligned, to ensure correct stack alignment before calling do_test_unaligned, thus fixing PR126927.
