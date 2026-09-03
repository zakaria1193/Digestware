---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- x86
- assembly
commit_hash: 00dafc5b715e0ba6adb42356addd6859e72b094b
source_type: github
author: Iain Sandoe
headline: x86 testsuite matches multi-word constants explicitly.
tldr: x86 testsuite now explicitly matches multi-word constants, improving accuracy
  and reliability on Darwin and other targets.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refines the GCC x86 testsuite by changing how multi-word
  literals are matched in assembly output. Previously, tests might match sequences
  of `.long` directives independently. Now, the tests explicitly match the entire
  16-byte literal, improving robustness and accuracy by ensuring the literal's value
  and memory layout are checked, particularly for Darwin's assembler.
primer_glossary:
- term: builtin
  definition: A function or operation that is part of the programming language itself,
    rather than a library function. Compilers can often optimize builtins more effectively.
- term: Darwin
  definition: The name of Apple's Unix-like operating system, used as a target in
    GCC.
- term: eh_frame
  definition: A DWARF debugging information section that contains information for
    stack unwinding, enabling debuggers to reconstruct the call stack.
- term: cfi-asm
  definition: Common Format Information Assembly, used for generating stack unwinding
    information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/00dafc5b715e0ba6adb42356addd6859e72b094b
date: '2026-08-19'
is_stub: true
stub_reason: low_score
---

Several x86 testsuite cases for `copysign` and `fabs` builtins have been updated to explicitly match multi-word constants. This change prevents spurious matches on unrelated code, such as `eh_frame` literals, which previously caused failures on Darwin. The explicit matching also improves the accuracy of checking literal values and their memory order, even on `cfi-asm` targets.
