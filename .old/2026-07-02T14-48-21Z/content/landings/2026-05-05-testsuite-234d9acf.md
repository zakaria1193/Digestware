---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- optimization
- ctz
- clz
- target architecture
commit_hash: 234d9acfd25aa3b74958e2f1c41e46d483b92d24
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Refine requirements for pr122569*.c tests.'
tldr: Updates testsuite to require ctzll/clzll targets and lp64/llp64 for pr122569
  tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `pr122569*.c` tests check for optimizations related to `__builtin_ctz`
  and `__builtin_clz`. This patch modifies the test requirements to ensure that the
  target architecture supports `ctzll` and `clzll` and is either LP64 or LLP64. The
  original tests failed on x86-64 with -m32 because the double-word implementations
  of `__builtin_c[tl]zll` are not optimized in the same way. The changes affect `gcc.dg/tree-ssa/pr122569-1.c`
  and `gcc.dg/tree-ssa/pr122569-2.c`.
primer_general: The GCC testsuite includes a collection of programs used to verify
  the correctness and performance of the compiler. These tests are designed to exercise
  different parts of the compiler and ensure that it generates correct code for various
  target architectures. This commit refines the requirements for specific test cases,
  ensuring that they are only run on systems where the tested features are actually
  supported. This helps to avoid false failures and ensures that the testsuite provides
  accurate feedback on the compiler's behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/234d9acfd25aa3b74958e2f1c41e46d483b92d24
date: '2026-05-05'
---

This commit refines the requirements for the `pr122569*.c` test cases to ensure they are only run on appropriate targets. It now requires that the target architecture supports `ctzll` and `clzll` (count trailing/leading zeros long long) and is either an LP64 or LLP64 architecture. This prevents the tests from failing on architectures where these features are not available or not optimized in the expected way.
