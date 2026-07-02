---
project: gcc
subsystem: gcc
patch_id: null
tags:
- libgomp
- OpenMP
- OMPT
- C++
- ABI
discussion_id: 87ik8zzcyc.fsf@euler.schwinge.ddns.net
source_type: public_inbox
title: Transitioning libgomp from C to C++ implementation
headline: Transitioning libgomp from C to C++ implementation
tldr: Thomas Schwinge proposes transitioning libgomp from C to C++ to improve type
  safety and enable better OpenMP OMPT implementation.
proposer: Thomas Schwinge <tschwinge@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential for increased code complexity due to C++ features.
- Risk of introducing performance regressions.
- Need to maintain ABI compatibility with existing C interface.
- Increased build time due to C++ compilation.
- Learning curve for developers unfamiliar with C++.
exchanges:
- author: Thomas Schwinge <tschwinge@baylibre.com>
  role: proposer
  position: Proposes transitioning libgomp from C to C++ to enhance type safety and
    improve OpenMP OMPT implementation using boolean templates.
  quote: The idea of transitioning libgomp from C to C++ implementation has come up
    a number of times, where the clunkiness that comes with C++ is believed to be
    favorable compared to the clunkiness of the C implementation.
- author: Richard Biener <richard.guenther@gmail.com>
  role: other
  position: No stance expressed.
  quote: null
- author: Tobias Burnus <tburnus@baylibre.com>
  role: other
  position: Highlights the intention to maintain ABI compatibility between the compiler
    and libgomp and between libgomp and its plugins and asks about ABI changes that
    would affect the middle-end interfacing.
  quote: 'Do you plan there to be changes of the ABI and thus GCCs middle-end interfacing?


    The idea is to use a lot of  ''extern "C" {''.'
- author: Tobias Burnus <tburnus@baylibre.com>
  role: other
  position: Asks about handling of untyped `gomp_malloc`.
  quote: 'So, first item: what do we do with the untyped ''gomp_malloc'' etc.?'
primer_expert: libgomp implements OpenMP runtime support for GCC. OMPT (OpenMP Tools)
  is the OpenMP profiling interface.  The proposal is to transition the implementation
  from C to C++ to take advantage of C++ templates for conditional compilation of
  OMPT support. The goal is to avoid performance overhead when OMPT is not used. ABI
  compatibility between the compiler and libgomp is a concern.
primer_general: OpenMP is an API for parallel programming.  libgomp is GCC's implementation
  of the OpenMP runtime. OMPT (OpenMP Tools) is an interface for profiling OpenMP
  applications.  This proposal discusses transitioning the implementation of libgomp
  from C to C++ to improve maintainability and allow for more efficient implementation
  of OMPT. The use of C++ templates would allow for conditional compilation of OMPT
  support, reducing overhead when profiling is not needed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/87ik8zzcyc.fsf@euler.schwinge.ddns.net
bugzilla_url: null
date: '2026-05-07'
---

Thomas Schwinge proposes transitioning libgomp, the GNU Offloading and Multi Processing Runtime Library, from C to C++. The goal is to enhance type safety, refactor data structures, and improve the implementation of OpenMP OMPT (OpenMP Tools) by using C++ boolean templates. The transition will avoid libstdc++ dependencies, RTTI, and C++ exceptions, and performance will be evaluated to ensure negligible overhead when OMPT is not loaded.
