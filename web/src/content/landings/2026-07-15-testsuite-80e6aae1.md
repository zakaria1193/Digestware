---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- x86
- solaris
commit_hash: 80e6aae1d5088f75def9ea0963a068dfbe0a833e
source_type: github
author: Rainer Orth
headline: Fix test case for 32-bit Solaris on x86
tldr: Corrects a test suite failure on 32-bit Solaris/x86 by adding a specific compiler
  flag.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test generator for i386 specific issues regressed on 32-bit Solaris/x86.
  The `dg-options` for `gcc.target/i386/pr64731.c` now explicitly includes `-mno-stackrealign`
  to pass the assembler scan-test.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/80e6aae1d5088f75def9ea0963a068dfbe0a833e
date: '2026-07-15'
is_stub: true
stub_reason: low_score
---

A test case, gcc.target/i386/pr64731.c, was failing on 32-bit Solaris/x86 systems. The failure was related to assembler output for movaps/movaps instructions. This commit resolves the issue by adding the '-mno-stackrealign' option to the test's dg-options, ensuring the test passes on the affected platform.
