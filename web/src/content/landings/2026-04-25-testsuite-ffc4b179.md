---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- abi
- freebsd
- x86_64
commit_hash: ffc4b179a3bc254b7303d7f9ddbe3e9291851cec
source_type: github
author: Rainer Orth
headline: FreeBSD ABI tests now pass with GNU ld.
tldr: The testsuite now emits .note.GNU-stack on FreeBSD, and uses --omit-rbp-clobbers
  to fix ABI test failures.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit fixes testsuite failures on FreeBSD by emitting `.note.GNU-stack`
  in the assembly support files, adding `--omit-rbp-clobbers` to `GEN_ARGS` for ms-sysv
  tests, and adapting a test to account for FreeBSD''s default `-fno-omit-frame-pointer`.  These
  changes ensure correct ABI testing on FreeBSD. search_context: GCC testsuite x86_64
  ABI FreeBSD'
primer_general: The Application Binary Interface (ABI) defines how software components
  interact at the machine code level, including calling conventions and data layout.  The
  GCC testsuite includes ABI tests, which check that the compiler generates code that
  adheres to the platform's ABI.  These tests are essential for ensuring that code
  compiled with GCC can interoperate correctly with other libraries and components
  on the target system.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ffc4b179a3bc254b7303d7f9ddbe3e9291851cec
date: '2026-04-25'
---

The x86_64 ABI tests were failing on FreeBSD when using GNU ld due to a missing `.note.GNU-stack` section and other ABI-related issues. This commit adds `.note.GNU-stack` emission on FreeBSD, uses `--omit-rbp-clobbers` in `GEN_ARGS`, and adjusts a test to account for the default `-fno-omit-frame-pointer` option on FreeBSD, resolving the failures.
