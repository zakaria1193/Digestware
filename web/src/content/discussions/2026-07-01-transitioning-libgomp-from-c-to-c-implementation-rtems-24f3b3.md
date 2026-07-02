---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- libgomp
- OpenMP
- RTEMS
- C++
discussion_id: 878q7uuy9w.fsf@euler.schwinge.ddns.net
source_type: public_inbox
title: 'Re: Transitioning libgomp from C to C++ implementation: RTEMS'
headline: 'Transitioning libgomp from C to C++ implementation: RTEMS'
tldr: Discussion on the ongoing effort to rewrite libgomp in C++ and its implications
  for RTEMS support.
proposer: Thomas Schwinge <tschwinge@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Rewriting libgomp in C++ may improve maintainability and introduce modern language
  features but could introduce new challenges or regressions.
- Ensuring compatibility with embedded systems like RTEMS requires careful testing
  and validation.
- The transition to C++ might impact ongoing efforts related to using libgomp in critical
  systems, necessitating careful management.
exchanges:
- author: Thomas Schwinge
  role: proposer
  position: Seeks confirmation on RTEMS support for the ongoing transition of libgomp
    from C to C++ and expresses interest in concerns related to its use in critical
    systems.
  quote: null
- author: Sebastian Huber
  role: contributor
  position: Confirms RTEMS support for libgomp on SMP-capable targets and notes that
    the C++ transition may impact ongoing critical systems work sponsored by ESA.
  quote: null
primer_expert: This thread discusses the ongoing effort to rewrite GCC's OpenMP runtime
  library, libgomp, from C to C++. The context involves verifying compatibility and
  potential impacts on specific embedded systems like RTEMS, which actively uses libgomp.
  The discussion also touches upon the implications of this transition for the use
  of libgomp in safety-critical systems.
primer_glossary:
- term: libgomp
  definition: GCC's implementation of the OpenMP Application Program Interface, providing
    support for shared-memory parallel programming.
- term: OpenMP
  definition: An API for shared-memory parallel programming that supports a mix of
    shared and private data, fortified routines, and recursive routines.
- term: RTEMS
  definition: A real-time operating system designed for embedded systems, often used
    in space and defense applications.
- term: SMP
  definition: Symmetric Multiprocessing, an architecture where two or more identical
    processors are connected to a single shared main memory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/878q7uuy9w.fsf@euler.schwinge.ddns.net
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Thomas Schwinge provides an update on the effort to transition libgomp from a C to a C++ implementation, seeking confirmation on RTEMS support. Sebastian Huber confirms that libgomp is enabled by default for RTEMS targets supporting SMP and is actively used. Huber also notes that the switch to C++ might cause 'headaches' for ongoing ESA-sponsored critical systems work, but expresses confidence that it should not be a concern for the RTEMS implementation itself.
