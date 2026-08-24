---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- avx
- x86-64
commit_hash: 9107afafcda6c361499b9f2f01d4d5901e5dd71d
source_type: github
author: H.J. Lu
headline: 'pr82625.C: Compile with -march=x86-64'
tldr: Ensures a specific test case compiles with a baseline x86-64 march to avoid
  AVX issues.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test case pr82625.C uses function attributes to specify target
  instruction sets. Without explicit control, on AVX512 hardware with native detection,
  the compiler might infer AVX512 support, altering code generation for functions
  explicitly marked for 'avx'. This commit fixes the test by forcing a baseline -march=x86-64,
  ensuring the 'avx' attribute is interpreted correctly.
primer_glossary:
- term: -march=x86-64
  definition: A GCC flag that enables code generation for the x86-64 architecture,
    including specific instruction sets available on that baseline. It's used here
    to ensure tests targeting specific features don't inadvertently enable newer,
    potentially incompatible ones.
- term: --with-arch=native --with-cpu=native
  definition: GCC configuration options that instruct the compiler to detect and use
    the architecture and CPU features of the build machine. This commit aims to counteract
    potential over-detection for test purposes.
- term: target attribute
  definition: A function attribute in GCC that allows specifying a particular architecture
    or instruction set for a function, influencing the code generation for that function
    only.
- term: AVX
  definition: Advanced Vector Extensions, an x86 instruction set extension that improves
    performance by enabling larger SIMD registers and new instructions.
- term: pr82625.C
  definition: A GCC test case file, likely in C, related to a specific bug report
    (PR 82625), focusing on function target attributes and AVX instruction sets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9107afafcda6c361499b9f2f01d4d5901e5dd71d
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

This commit modifies the test suite to compile pr82625.C with the -march=x86-64 flag. The test case defines functions with different target attributes, including 'default' and 'avx'. Compiling with -march=x86-64 ensures that only AVX is enabled by the target attribute, preventing issues that arise on AVX512 machines when GCC is configured with --with-arch=native --with-cpu=native.
