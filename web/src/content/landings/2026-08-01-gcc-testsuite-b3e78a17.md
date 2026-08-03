---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- gcc
- optimization
commit_hash: b3e78a17714908dbcd4b968a6c567ce75d424487
source_type: github
author: Andrea Pinski
headline: 'testsuite: Add phiopt factoring test for restrict keyword'
tldr: New testcase verifies phiopt pass handles factoring of loads with 'restrict'
  pointers correctly.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a regression test (`gcc.dg/tree-ssa/factor_op_phi-restrict-1.c`)
  to the GCC testsuite. It targets the phiopt pass, specifically the 'factoring of
  loads' optimization, to ensure correct behavior when `restrict` qualified pointers
  are present. This testcase was apparently missed during the initial implementation
  of the load factoring feature.
primer_glossary:
- term: phiopt
  definition: A compiler optimization pass in GCC that performs optimizations related
    to PHI nodes, particularly those involving conditional loads. It aims to simplify
    control flow and improve code efficiency.
- term: restrict
  definition: A C/C++ type qualifier that acts as a promise to the compiler that,
    for the duration of its lifetime, the object it points to is accessed solely through
    that pointer or objects derived from it. This allows for more aggressive optimizations.
- term: load factoring
  definition: An optimization technique where redundant or conditional loads from
    memory are identified and simplified. This can involve moving loads outside of
    loops or into common subexpression elimination.
- term: testsuite
  definition: A collection of test programs and scripts used to verify the correctness
    of a compiler or toolchain. It covers various language features, optimizations,
    and target architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3e78a17714908dbcd4b968a6c567ce75d424487
date: '2026-08-01'
is_stub: true
stub_reason: low_score
---

A new test case has been added to the GCC testsuite to specifically verify the phiopt optimization pass's handling of load factoring when `restrict` pointers are involved. This ensures that the optimizations related to the `restrict` keyword are correctly applied in conjunction with load factoring.
