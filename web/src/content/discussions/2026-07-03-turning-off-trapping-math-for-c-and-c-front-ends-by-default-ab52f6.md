---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- floating-point
- optimization
- C
- C++
discussion_id: 5rnrsrp4-po1s-npo5-7p50-1209p96nnrq3@fhfr.qr
source_type: public_inbox
title: 'Re: [RFC] Turning off trapping-math for C and C++ front-ends by default'
headline: Turning off trapping-math for C and C++ front-ends by default
tldr: GCC developers discuss implications of disabling trapping math by default and
  challenges in accurately modeling floating-point exception flags.
proposer: Richard Biener <rguenther@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Disabling trapping math by default offers potential performance gains but risks
  incorrect behavior if FENV_ACCESS is used.
- Accurately modeling FP exception flags requires significant changes to GCC's intermediate
  representations and optimization passes.
exchanges:
- author: Richard Biener <rguenther@suse.de>
  role: proposer
  position: Discusses the difficulties of supporting `#pragma FENV_ACCESS` beyond
    function scope and suggests using internal functions for IEEE flag setting operations.
  quote: 'Yeah, I think the path of least resistance would be to introduce

    internal functions for IEEE flag setting operations, possibly

    "rich", as in having input and output of flag register(s) and

    argument(s) specifying the EH operations in effect.'
- author: Marc Glisse <marc.glisse@mathematik.uni-bielefeld.de>
  role: contributor
  position: Questions the feasibility of even per-function level FP operation handling
    with the current GCC representation.
  quote: "I am not sure about that. Supporting even the per-function level is not\
    \ \nreally doable with the current representation of FP operations in gcc."
- author: Richard Biener <rguenther@suse.de>
  role: proposer
  position: Further elaborates on the challenges of modeling FP flag registers as
    global memory and their impact on optimization, suggesting a unified solution
    for FP exceptions and 'errno'.
  quote: 'But modeling the flag reg as global memory will be difficult, esp.

    as we go towards representing this on the RTL side where at least

    scheduling has to be aware of this.  It also makes "not doing -O0"

    more difficult.  There''s a similar other case, ''errno'', which is in

    the way of optimizations.  So any good design might help both.'
primer_expert: This RFC thread discusses turning off `-ftrapping-math` by default
  in GCC's C/C++ frontends. The core issue is faithfully representing and optimizing
  floating-point operations, particularly concerning IEEE 754 exception flags (traps).
  Current GIMPLE and RTL representations make it difficult to accurately track per-operation
  FP status and handle pragmas like `#pragma STDC FENV_ACCESS`. Participants explore
  solutions involving internal functions to model FP operations with explicit flag
  inputs/outputs, aiming to balance correctness with optimization potential, and draw
  parallels with the handli…
primer_glossary:
- term: trap
  definition: In floating-point arithmetic, a trap occurs when an operation triggers
    an exception (e.g., division by zero, overflow). `-ftrapping-math` controls whether
    these exceptions are enabled and potentially caught.
- term: FENV_ACCESS
  definition: A C standard pragma that indicates whether the program might access
    the floating-point environment (e.g., status flags, rounding modes). GCC needs
    to ensure correctness when this pragma is in effect.
- term: GIMPLE
  definition: GCC's internal representation of code, used after parsing and before
    final code generation. It's a lower-level, three-address-like form.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC
    at a lower level than GIMPLE, closer to machine code.
- term: IEEE 754
  definition: The standard for floating-point arithmetic, defining formats, operations,
    and exception handling.
- term: errno
  definition: A standard C library macro that holds the error number of the last library
    function call that failed.
series_id: 5rnrsrp4-po1s-npo5-7p50-1209p96nnrq3@fhfr.qr
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/gcc/5rnrsrp4-po1s-npo5-7p50-1209p96nnrq3@fhfr.qr
bugzilla_url: null
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

This exchange delves into the complexities of GCC's handling of floating-point exceptions and the implications of disabling trapping math (`-fno-trapping-math`) by default for C and C++ front-ends. Richard Biener suggests introducing internal functions for IEEE flag operations to better model per-operation exception behavior, acknowledging difficulties with GIMPLE and global state like 'errno'. The discussion highlights the trade-offs between optimization levels, frontend representations, and accurate FPU state management.
