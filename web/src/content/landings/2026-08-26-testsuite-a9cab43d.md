---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- compiler
- feature
commit_hash: a9cab43d5a17b7eabcbd65f37bcdf2ef6c00ba7a
source_type: github
author: Rainer Orth
headline: Require bitint for gcc.dg/pr126538.c test
tldr: 'testsuite: gcc.dg/pr126538.c now requires bitint to avoid target-specific failures.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the `gcc.dg/pr126538.c` testcase to include a
  `dg-require` directive for `bitint`. This is necessary because the testcase utilizes
  `_BitInt(65535)`, a feature not supported on all targets, leading to compilation
  failures (e.g., on SPARC). Requiring `bitint` ensures the test is only executed
  on platforms with this capability.
primer_glossary:
- term: bitint
  definition: A C language extension for arbitrary-precision integers, allowing the
    specification of integer types with a user-defined number of bits, beyond standard
    types like int or long long.
- term: dg-require
  definition: A directive used in the GCC testsuite to specify prerequisites for running
    a test case. If the condition is not met, the test is skipped.
- term: SPARC
  definition: A RISC instruction set architecture developed by Sun Microsystems. Compilers
    may have varying levels of support for its features.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a9cab43d5a17b7eabcbd65f37bcdf2ef6c00ba7a
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

The test case gcc.dg/pr126538.c previously failed on SPARC due to an unimplemented feature: '_BitInt(65535)'. This commit resolves the issue by adding a requirement for bitint support to the test case, ensuring it only runs on targets where this feature is available. Testing was performed on SPARC and i386 Solaris systems.
