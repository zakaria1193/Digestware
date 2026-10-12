---
project: gcc
subsystem: gcc/m2
patch_id: null
tags:
- modula2
- memory
- large-allocation
- compiler-runtime
commit_hash: dde7adea08d7738ca822e2badb683354bf95815b
source_type: github
author: Gaius Mulley
headline: 'Modula-2: Add LongStorage module for large memory allocations'
tldr: New Modula-2 modules allow allocating more than 4GB of memory.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch introduces `LongStorage` and `LongSysStorage` modules for
  GCC's GNU Modula-2 implementation. These modules provide procedures to manage dynamic
  memory allocation beyond the typical 4GB limit imposed by `CARDINAL` types on 32-bit
  systems or standard library interfaces. The `M2Diagnostic` module is enhanced with
  corresponding `Long` procedures to track memory usage accurately. A new test suite
  `largestore.mod` verifies these large memory allocation capabilities. This addresses
  a significant limitation for applications requiring substantial memory, particularly
  relevant in scientific…
primer_glossary:
- term: Modula-2
  definition: A procedural programming language designed by Niklaus Wirth, known for
    its emphasis on modularity and strong typing. GCC includes an implementation for
    it.
- term: PIM
  definition: ' a design style in Modula-2 that stands for "Programming In Modula-2".
    It refers to generic modules that can be adapted to specific types, often achieved
    through parameterization or other mechanisms.'
- term: CARDINAL
  definition: In Modula-2, a data type representing non-negative integers. Its maximum
    value typically depends on the system's word size (e.g., 2^32-1 on a 32-bit system).
- term: GNU Modula-2
  definition: GCC's implementation of the Modula-2 programming language, providing
    a compiler and associated libraries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dde7adea08d7738ca822e2badb683354bf95815b
date: '2026-10-09'
is_stub: false
stub_reason: ''
---

Two new Modula-2 PIM (<bos>/Generic) style modules, LongStorage and LongSysStorage, have been introduced to enable dynamic memory allocations exceeding 4GB. This significantly enhances the capability for handling large datasets within Modula-2 programs. The changes also include updates to M2Diagnostic for tracking overall application memory usage and a new test case.
