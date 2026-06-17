---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- risc-v
- testsuite
- regression
- optimization
commit_hash: b5d5f34aa797909b857fb812415538962a61f8c9
source_type: github
author: Jeff Law
headline: Tighten and xfail test for pr120811
tldr: A GCC test case for RISC-V was updated with correct regular expressions and
  now correctly xfails, revealing a long-standing performance regression.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: ' GCC''s `scan-asm` directives within test cases use regular expressions
  to verify the generated assembly output. A common pitfall is overly broad regexes
  that can match incorrect assembly patterns, masking underlying regressions. This
  commit specifically addresses a `gcc.target/riscv/pr12811.c` test where post-reload
  combine optimization is expected but appears to be non-operational, leading to suboptimal
  code generation. The `xfail` directive informs the test runner to expect failure,
  preventing it from marking a working feature as broken when a known issue exists.'
primer_general: When you compile code with GCC, it generates assembly language specific
  to your computer's processor. To ensure the compiler is working correctly and producing
  optimized code, GCC has a large test suite. Some tests involve checking the generated
  assembly code against expected patterns using regular expressions. If a regular
  expression is too general, it might accidentally match incorrect assembly, hiding
  a problem. This commit fixes such a situation for a RISC-V processor test. The compiler
  was supposed to perform an optimization called 'post-reload combine,' which makes
  the code run faster, but it wasn't happening. The test was updated to correctly
  identify this failure and is now marked to 'xfail,' meaning it's expected to fail
  until the underlying optimization issue is resolved. This helps developers know
  about problems without delaying other development.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b5d5f34aa797909b857fb812415538962a61f8c9
date: '2026-06-17'
is_stub: false
---

The test for `pr120811` on RISC-V was not accurately matching assembly output due to overly broad regular expressions, masking a failure for several months. Recent changes in code generation made the faulty matching apparent, prompting an update to the test with precise escape sequences. The test now correctly fails and is marked as an expected failure, highlighting a performance regression related to post-reload combine optimization that is being tracked in a new bug.
