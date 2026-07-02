---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- niter analysis
- ubsan
- ice
- loop optimization
commit_hash: 6d218b0ffbd54ca438e904fccad86d226f26bb91
source_type: github
author: Richard Biener
headline: 'Tree-optimization: Avoids ICE with niter Analysis and UBSAN.'
tldr: The compiler now avoids an internal compiler error (ICE) when using niter analysis
  with UBSAN by preventing negation of the most negative signed integer.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR125025, an ICE in `tree-ssa-loop-niter.cc`.
  The functions `number_of_iterations_ne` and `number_of_iterations_lt` were attempting
  to negate a signed step, potentially leading to undefined behavior when negating
  the most negative signed integer. This commit changes the code to convert the step
  to unsigned before negating, mirroring existing practice elsewhere in the code.  The
  associated testcase is `gcc.dg/torture/pr125025.c`.
primer_general: Loop iteration analysis (niter analysis) is a compiler optimization
  technique that attempts to determine the number of times a loop will execute. This
  information can be used to optimize the loop and generate more efficient code. UBSAN
  (Undefined Behavior Sanitizer) is a tool that detects undefined behavior in C and
  C++ programs at runtime. This commit fixes a bug where the compiler would crash
  (ICE) when performing loop iteration analysis on code that also used UBSAN. The
  fix prevents the compiler from trying to negate the most negative signed integer,
  which is an undefined operation.  This ensures that the compiler can correctly analyze
  loops and generate optimized code, even when UBSAN is enabled.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d218b0ffbd54ca438e904fccad86d226f26bb91
date: '2026-04-27'
---

This commit fixes an internal compiler error (ICE) that occurred when using the niter analysis (loop iteration analysis) in conjunction with UBSAN (Undefined Behavior Sanitizer). The issue arose when computing the absolute step of a loop by negating a signed step, which could result in negating the most negative signed integer.  The fix converts the signed step to an unsigned value before negating it, thus avoiding the undefined behavior.  A new testcase was added to verify the fix.
