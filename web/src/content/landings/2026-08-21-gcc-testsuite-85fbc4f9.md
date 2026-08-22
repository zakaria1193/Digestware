---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- x86
- optimization
commit_hash: 85fbc4f968d75cf0a372494f0f122b4b4a226243
source_type: github
author: H.J. Lu
headline: 'x86: Adjust testcase for optimized codegen in pr92080-12.c'
tldr: 'gcc: x86 testsuite adjusted to use check-function-bodies for optimized codegen,
  resolving PR112104.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test case gcc.target/i386/pr92080-12.c is updated to use check-function-bodies
  for verifying optimized code generation. This replaces scan-assembler-times to correctly
  validate the handling of variable trip count XORs in final value replacement, a
  fix for PR112104.
primer_glossary:
- term: check-function-bodies
  definition: A GCC testsuite mechanism that verifies the generated assembly code
    for correctness and optimization, often by comparing it against expected output
    or properties.
- term: scan-assembler-times
  definition: A GCC testsuite mechanism that times assembler output. It's less precise
    for verifying specific code generation patterns compared to check-function-bodies.
- term: PR112104
  definition: A GCC bug report (Problem Report) concerning the incorrect optimization
    of loops with XOR operations and variable trip counts.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/85fbc4f968d75cf0a372494f0f122b4b4a226243
date: '2026-08-21'
is_stub: true
stub_reason: low_score
---

The testcase gcc.target/i386/pr92080-12.c has been modified to use check-function-bodies instead of scan-assembler-times. This change addresses an issue with optimizing loops containing XOR operations, as identified in PR tree-optimization/112104, ensuring correct optimized assembly is verified.
