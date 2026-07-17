---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- aarch64
- neon
- testing
commit_hash: a0f7c857279aa4f2830b65813b9ed68d9fa9098d
source_type: github
author: Iain Sandoe
headline: 'aarch64: Remove redundant big-endian Neon tests.'
tldr: Big-endian AArch64 Neon tests are removed from the testsuite driver to avoid
  duplication.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `aarch64-neon.exp` test driver script for GCC includes logic to
  re-run Neon tests in a big-endian mode. This is problematic because AArch64 is predominantly
  used in little-endian configurations, leading to many 'UNRESOLVED' test cases when
  this big-endian execution path is attempted on unsupported targets. Furthermore,
  for actual big-endian AArch64 targets, this section results in the same tests being
  executed twice. This commit removes the redundant big-endian re-execution section,
  simplifying the test suite and avoiding unnecessary computations.
primer_glossary:
- term: AArch64
  definition: The 64-bit implementation of the ARM architecture, commonly used in
    mobile devices and servers.
- term: Neon
  definition: ARM's Advanced SIMD (Single Instruction, Multiple Data) extension for
    AArch64, providing advanced vector processing capabilities similar to SSE/AVX
    on x86.
- term: test driver script
  definition: A script that orchestrates the execution of test cases, setting up environments,
    invoking the compiler or program under test, and evaluating the results. In GCC,
    `.exp` files often serve as test driver scripts.
- term: big-endian
  definition: A byte order where the most significant byte of a multi-byte word is
    stored at the lowest memory address. This is opposed to little-endian, where the
    least significant byte is stored at the lowest address.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0f7c857279aa4f2830b65813b9ed68d9fa9098d
date: '2026-07-16'
is_stub: true
stub_reason: low_score
---

This commit removes a section from the `aarch64-neon.exp` test driver script that caused tests to be re-run specifically for big-endian execution. Since most targets are little-endian and cannot perform these tests, re-running them on big-endian systems only served to duplicate effort. Removing this section streamlines the test execution for AArch64 Neon tests.
