---
project: gcc
subsystem: gcc/libgomp
patch_id: null
tags:
- libgomp
- C++ rewrite
- RTEMS
- OpenMP
- runtime library
discussion_id: 87o6h4bcea.fsf@euclid.schwinge.ddns.net
source_type: public_inbox
title: 'Transitioning libgomp from C to C++ implementation: RTEMS'
headline: 'Transitioning libgomp from C to C++ implementation: RTEMS'
tldr: A developer plans to transition libgomp's implementation from C to C++ and seeks
  to ensure RTEMS support is maintained, requesting assistance with testing.
proposer: Thomas Schwinge <tschwinge@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Thomas Schwinge
  role: proposer
  position: Informs RTEMS maintainers about the planned transition of libgomp from
    C to C++ and seeks confirmation of RTEMS support, along with details for self-testing.
  quote: 'Per my understanding, for GCC/RTEMS, libgomp is not enabled by default in
    GCC ''configure.ac'' (needs explicit ''--enable-libgomp''), but it appears to
    be supported: RTEMS is mentioned in ''libgomp/configure.ac'', ''libgomp/configure.tgt'',
    and has ''libgomp/config/rtems/'' files. Please let me know in case libgomp/RTEMS
    is in fact not supported (anymore).'
primer_expert: This discussion concerns `libgomp`, the GCC OpenMP runtime library,
  and its planned migration from C to C++. The proposer is specifically addressing
  the RTEMS target, a real-time operating system. The `libgomp/configure.ac` and `libgomp/configure.tgt`
  files, along with `libgomp/config/rtems/` files, are part of the GCC build system
  that determine how `libgomp` is configured and built for different architectures
  and operating systems. The core issue involves ensuring that the C++ rewrite does
  not break existing RTEMS configurations, which may have specific synchronization
  object implementation…
primer_general: This is a technical discussion about changing a part of the GCC compiler
  called `libgomp`. `libgomp` is responsible for making programs run faster on systems
  with multiple processors by using something called OpenMP. The developer wants to
  rewrite `libgomp` from the C programming language to C++. This change could affect
  how `libgomp` works on specific systems, particularly on RTEMS, which is a specialized
  operating system used in real-time applications (like in embedded systems or aerospace).
  The developer wants to make sure that this rewrite won't break `libgomp` for RTEMS
  users and is asking for help from those who maintain GCC for RTEMS to ensure compatibility
  and testing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/87o6h4bcea.fsf@euclid.schwinge.ddns.net
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This message announces an upcoming effort to rewrite `libgomp` from C to C++ and seeks input from RTEMS maintainers to ensure continued support for that target. The developer plans to undertake native builds for RTEMS to verify the changes and is asking for information regarding RTEMS's status and testing procedures. This is a heads-up to the community about a significant rewrite that may impact various targets.
