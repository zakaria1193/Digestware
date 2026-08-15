---
project: gcc
subsystem: gcc/testsuite/x86
patch_id: null
tags:
- testsuite
- x86
- darwin
commit_hash: dcf34067a80904e66a91db127f39f27fdb1b6ee5
source_type: github
author: Iain Sandoe
headline: Fix missing user label prefix in Darwin X86 tests
tldr: Corrects test failures on Darwin by accounting for user label prefixes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: These test files (`gcc.target/i386/pr126293-1b.c` and `pr126293-1c.c`)
  were failing on Darwin because they did not correctly handle the `USER_LABEL_PREFIX`.
  This prefix is used by the Darwin linker to control symbol visibility, and tests
  that rely on specific symbol naming conventions need to account for it. The fix
  involves adjusting the test code to properly incorporate `USER_LABEL_PREFIX` when
  defining or referencing labels, thus ensuring correct assembly and linking behavior
  on Darwin.
primer_glossary:
- term: testsuite
  definition: A collection of automated tests used to verify the correctness of the
    compiler. It includes various test cases covering different language features,
    optimizations, and target architectures.
- term: X86
  definition: A family of instruction set architectures (ISAs) for computer processors,
    commonly used in personal computers and servers. GCC supports targeting various
    X86 processors.
- term: Darwin
  definition: The open-source Unix-based operating system foundation of macOS, iOS,
    and other Apple operating systems. GCC includes specific support for Darwin targets.
- term: USER_LABEL_PREFIX
  definition: A compiler or linker macro that defines the prefix used for user-defined
    labels (symbols) in assembly code, often influenced by the target operating system
    or ABI.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcf34067a80904e66a91db127f39f27fdb1b6ee5
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

Two test cases for Darwin's X86 architecture (`pr126293-1b.c` and `pr126293-1c.c`) were failing due to a missing user label prefix. This commit updates the tests to correctly account for `USER_LABEL_PREFIX`, ensuring they pass on Darwin systems where this prefix is used for symbol visibility.
