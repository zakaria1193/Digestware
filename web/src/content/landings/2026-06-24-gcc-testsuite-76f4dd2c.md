---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- vectorization
- sparc
- bugfix
commit_hash: 76f4dd2c8f296a950f4cac04fa9a30ae0892cdb9
source_type: github
author: Rainer Orth
headline: Fix gcc.dg/vect/pr125567.c on SPARC
tldr: A GCC test case for vectorization now explicitly requires hardware support for
  unaligned memory access, ensuring it passes on SPARC architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `gcc.dg/vect/pr125567.c` was failing on SPARC targets because
  it implicitly expected support for unaligned memory accesses during vectorization.
  The fix adds `#pragma GCC target ("vect_hw_misalign")` to the test case, explicitly
  indicating this hardware requirement. This ensures that the vectorizer's unaligned
  access transformations are only tested on architectures that can handle them efficiently,
  preventing false negatives on platforms like SPARC where such accesses might not
  be fully supported by vector hardware.
primer_general: When a computer program processes lots of data, especially numbers,
  it can often be sped up by using 'vector instructions.' These instructions allow
  the CPU to perform the same operation on multiple pieces of data at once, like processing
  a whole row of spreadsheet numbers in a single step. Sometimes, to do this efficiently,
  the CPU needs to be able to read data from memory that isn't perfectly lined up
  (called 'unaligned access'). This change adjusts a test case in GCC, the compiler,
  to explicitly state that it needs a CPU with hardware support for these unaligned
  memory accesses to pass. This prevents the test from failing incorrectly on systems
  like SPARC, which might not have this specific hardware capability, ensuring that
  the compiler's vectorization features are tested accurately.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/76f4dd2c8f296a950f4cac04fa9a30ae0892cdb9
date: '2026-06-24'
is_stub: false
---

This commit fixes a failing GCC test case, `gcc.dg/vect/pr125567.c`, on SPARC architectures. The test, designed to verify auto-vectorization, implicitly relied on the target processor's ability to handle unaligned memory accesses, which SPARC systems may not fully support in hardware. By adding a requirement for `vect_hw_misalign`, the test now correctly reflects its dependencies and passes on SPARC.
