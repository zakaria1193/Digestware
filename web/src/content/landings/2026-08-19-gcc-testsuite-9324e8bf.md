---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- avx512
commit_hash: 9324e8bfc8747f73b5a6bc2758c21827dbe6fe51
source_type: github
author: H.J. Lu
headline: 'gcc.target/i386/abi-mix-1.c: Compile with -mno-avx'
tldr: Test file abi-mix-1.c now compiles with -mno-avx to avoid AVX512 instruction
  errors with the no_caller_saved_registers attribute.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies a GCC test case (`gcc.target/i386/abi-mix-1.c`)
  to address a conflict between AVX512 instruction usage and the `no_caller_saved_registers`
  attribute. By adding the `-mno-avx` flag, the test suite avoids attempting to use
  AVX512 instructions in a context where they are disallowed by the attribute, preventing
  a compile-time error that occurred when AVX512 was enabled by default.
primer_glossary:
- term: AVX512
  definition: Advanced Vector Extensions 512, a set of SIMD (Single Instruction, Multiple
    Data) instructions for x86 processors that operate on 512-bit vectors, offering
    significant performance improvements for parallelizable tasks.
- term: no_caller_saved_registers
  definition: A function attribute that instructs the compiler not to use any caller-saved
    registers within the function. This can be important for specific low-level code
    or system calls where register usage must be strictly controlled.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9324e8bfc8747f73b5a6bc2758c21827dbe6fe51
date: '2026-08-19'
is_stub: true
stub_reason: low_score
---

A test case, `gcc.target/i386/abi-mix-1.c`, was failing because AVX512 instructions were not allowed within functions marked with the `no_caller_saved_registers` attribute when AVX512 was enabled by default. This commit adds the `-mno-avx` flag to the test's compilation options to resolve this conflict and allow the test to pass.
