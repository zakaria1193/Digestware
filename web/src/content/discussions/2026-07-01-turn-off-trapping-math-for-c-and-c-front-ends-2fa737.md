---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler-flags
- floating-point
- optimization
discussion_id: CALvbMcA6P_q7WNm1KOopzxhzRJHFi9T9_STaCtZrm1ZA-0nNtQ@mail.gmail.com
source_type: public_inbox
title: '[RFC] Turning off trapping-math for C and C++ front-ends by default'
headline: Turn off trapping-math for C and C++ front-ends
tldr: 'GCC defaults to -ftrapping-math, but this has many issues. Proposal: disable
  it by default for C/C++ and file bugs for problematic cases.'
proposer: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Disabling -ftrapping-math by default may improve performance and stability by avoiding
  issues with problematic optimizations, but could break code that relies on precise
  FP exception behavior.
- Aligning with LLVM's default simplifies comparisons but requires addressing the
  underlying issues in GCC's implementation of -ftrapping-math.
- Adding diagnostics for related functions improves user awareness but adds complexity
  to the compiler.
exchanges:
- author: Andrea Pinski
  role: proposer
  position: Proposes to disable -ftrapping-math by default for C and C++ front-ends
    due to existing issues with code transformations altering exception flag behavior.
  quote: null
- author: Martin Uecker
  role: contributor
  position: 'Agrees with the proposal and asks if #pragma FENV_ACCESS support can
    be added.'
  quote: 'I think I agree, but is there a chance that we can also get

    #pragma FENV_ACCESS support?'
- author: Matthias Kretz
  role: contributor
  position: Supports changing the default and suggests adding a diagnostic for calls
    to relevant functions.
  quote: null
- author: Richard Biener
  role: reviewer
  position: Acknowledges the proposal and the associated problematic definition of
    -ftrapping-math.
  quote: null
primer_expert: The `-ftrapping-math` flag in GCC controls whether floating-point operations
  are allowed to transform in ways that might alter the precise raising of FP exception
  flags or trap handlers. Historically, GCC has defaulted to enabling this flag, but
  this has led to issues where optimizations break the expected exception behavior.
  This proposal suggests disabling it by default for C/C++ to match LLVM's behavior
  and to address known problems, while also intending to fix individual cases where
  the flag might be mishandled.
primer_glossary:
- term: -ftrapping-math
  definition: A GCC flag that enables floating-point exceptions and disallows certain
    code transformations that might affect exception flag behavior or trap handling.
- term: '#pragma FENV_ACCESS'
  definition: A pragma that indicates whether a section of code accesses or modifies
    the floating-point environment, which can influence compiler optimizations related
    to floating-point operations.
- term: DCE
  definition: Dead Code Elimination, a compiler optimization that removes code that
    does not affect the program's output.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CALvbMcA6P_q7WNm1KOopzxhzRJHFi9T9_STaCtZrm1ZA-0nNtQ@mail.gmail.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Andrea Pinski proposes to disable -ftrapping-math by default for GCC's C and C++ front-ends. The current default, -ftrapping-math, has been associated with various issues, including code transformations that incorrectly alter exception flag behavior. Pinski argues that this default has been problematic since at least GCC 3.4. The change aims to align GCC's behavior with Clang/LLVM, which defaults to -fno-trapping-math, and to enable a fair comparison between the two compilers. The discussion also touches on the need for #pragma FENV_ACCESS support and potential diagnostics for calls to related functions.
