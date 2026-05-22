---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- optimization
- floating-point
- performance
- precision
discussion_id: 1BDAC475-C1FD-457D-8EB3-C65F7B40ED88@aruba.it
source_type: public_inbox
title: Constant divisions not converted to multiplications
headline: Constant divisions are not converted to multiplications with -O3
tldr: GCC with -O3 doesn't always turn divisions by constants into multiplications;
  -freciprocal-math enables this optimization at the cost of precision.
proposer: Undisclosed <1007140@aruba.it>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Performance gain from using multiplication instead of division.
- Potential loss of precision in floating-point calculations when using reciprocal
  math.
- Default behavior prioritizes precision over performance.
exchanges:
- author: Undisclosed <1007140@aruba.it>
  role: proposer
  position: Reports that GCC 14.2 doesn't convert divisions by constants into multiplications,
    even with -O3, and expresses surprise.
  quote: 'I always gave for granted that any compiler would automatically turn constant
    divisions into multiplications. Thus, I never cared of writing i.e

    float x = a * 0.1f

    but I always wrote

    float x = a / 10.f

    trusting the compiler.'
- author: Matteo Nicoli <matteo.nicoli001@gmail.com>
  role: other
  position: Confirms the behavior on GCC 16.1.1.
  quote: "On GCC 16.1.1 I observe the same behavior (except from the fact that it\
    \ uses the \nAVX instruction vdivss)."
- author: LIU Hao <lh_mouse@126.com>
  role: contributor
  position: States that the `-freciprocal-math` option enables the optimization, but
    it's off by default due to potential precision loss. Mentions `-funsafe-math-optimizations`
    or `-ffast-math` also enables it.
  quote: "The option which enables such optimization is `-freciprocal-math`:\n\nIt's\
    \ off by default as it may result in precision loss. It can also be enabled indirectly\
    \ with \n`-funsafe-math-optimizations` or `-ffast-math`."
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Quotes the original poster's surprise at the lack of constant division
    optimization by default.
  quote: 'Hi, I am using gcc 14.2 on windows (mingw64).

    I always gave for granted that any compiler would automatically turn constant
    divisions into multiplications. Thus, I never cared of writing i.e

    float x = a * 0.1f

    but I always wrote

    float x = a / 10.f

    trusting the compiler.'
primer_expert: GCC's middle-end optimization pass doesn't always transform division
  by constants into multiplication, even with -O3.  This is controlled by `-freciprocal-math`,
  which is disabled by default for floating-point precision reasons. Compiler writers
  outside the FP optimization team might not immediately be aware of the exact circumstances
  where this optimization is skipped.
primer_general: Compilers optimize code to improve performance. One common optimization
  is replacing division by a constant number with multiplication by its reciprocal,
  which is faster. However, this transformation can change the result slightly due
  to how computers represent numbers. GCC, a widely-used compiler, has an option to
  enable this optimization (`-freciprocal-math`), but it's turned off by default to
  ensure the most accurate results. This means that even with optimizations enabled,
  the compiler might still use division instructions in certain cases.  The choice
  depends on a tradeoff between speed and precision.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/1BDAC475-C1FD-457D-8EB3-C65F7B40ED88@aruba.it
bugzilla_url: null
date: '2026-05-21'
is_stub: false
---

A user found that GCC 14.2 with optimization level -O3 doesn't convert divisions by constants into multiplications, leading to slower code. This behavior was confirmed on GCC 16.1.1.  The `-freciprocal-math` option enables this optimization, though it's off by default due to potential precision loss.  Enabling unsafe math optimizations also turns on this optimization.
