---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- x86
- AVX512
commit_hash: 1c29f88ec83ff8eee17295fe7c77d61051bc1edc
source_type: github
author: Iain Sandoe
headline: Add AVX512 requirements to x86 testsuite assemble/run cases.
tldr: x86 testsuite now explicitly requires AVX512 for assemble/run tests, fixing
  Darwin failures and improving 32-bit Darwin compatibility.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the GCC testsuite for x86 targets. It adds `dg-requires`
  directives for tests using AVX512, ensuring they are only run on appropriate hardware.
  For 32-bit Darwin, `-mdynamic-no-pc` is added to compile flags to align codegen
  with that of ELF targets, mitigating failures related to assembler or runtime support.
primer_glossary:
- term: AVX512
  definition: Advanced Vector Extensions 512-bit, a set of SIMD instructions for Intel
    and AMD processors that operate on 512-bit registers.
- term: dg-requires
  definition: A directive used in the GCC testsuite to specify hardware or software
    features required for a test to run, preventing execution on unsuitable platforms.
- term: Darwin
  definition: The name of Apple's Unix-like operating system, used as a target in
    GCC.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: codegen
  definition: Code generation, the process of translating an intermediate representation
    of a program into machine code or another lower-level form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1c29f88ec83ff8eee17295fe7c77d61051bc1edc
date: '2026-08-11'
is_stub: true
stub_reason: low_score
---

Several x86 testsuite cases that assemble and run code requiring AVX512 instructions have been updated. These tests previously failed on Darwin targets due to missing assembler or runtime support. The changes add `dg-requires` directives for AVX512 and include the `-mdynamic-no-pc` compile flag for 32-bit Darwin cases to better match ELF target codegen, ensuring these tests pass reliably.
