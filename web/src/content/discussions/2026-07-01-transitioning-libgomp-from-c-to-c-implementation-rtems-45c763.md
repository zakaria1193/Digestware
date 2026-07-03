---
project: gcc
subsystem: gcc
patch_id: null
tags:
- libgomp
- OpenMP
- C++
- GCC
- porting
discussion_id: 87ik8zzcyc.fsf@euler.schwinge.ddns.net
source_type: public_inbox
title: 'Re: Transitioning libgomp from C to C++ implementation: RTEMS'
headline: 'Transitioning libgomp from C to C++ implementation: RTEMS'
tldr: GCC's libgomp, currently C-based, is being transitioned to C++.
proposer: Thomas Schwinge <tschwinge@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Transitioning from C to C++ may introduce new dependencies or require more complex
  build configurations.
- Ensuring ABI compatibility across different C and C++ codebases is crucial.
- Maintaining support for diverse operating systems and build environments adds complexity.
exchanges:
- author: Thomas Schwinge <tschwinge@baylibre.com>
  role: proposer
  position: Seeks confirmation that a standard GCC build with libgomp enabled will
    work on the cfarm104 macOS ARM system once it's back online.
  quote: null
- author: Thomas Schwinge <tschwinge@baylibre.com>
  role: proposer
  position: Inquires about libgomp support for Cygwin and MinGW targets, noting that
    it requires a pthread implementation and discussing the nuances of different triplets.
  quote: null
- author: Iain Sandoe <iain@sandoe.co.uk>
  role: contributor
  position: Confirms that libgomp is supported on Darwin.
  quote: null
- author: Jonathan Yong <10walls@gmail.com>
  role: contributor
  position: Acknowledges the inquiry regarding Cygwin and MinGW targets and suggests
    involving other developers for those platforms.
  quote: null
- author: LIU Hao <lh_mouse@126.com>
  role: contributor
  position: Clarifies the triplet naming for MinGW targets and points out that libgomp
    depends on a pthread implementation, which is not a default for mingw* targets.
  quote: null
primer_expert: This discussion concerns the porting of libgomp, GCC's OpenMP runtime
  library, from C to C++. The goal is to ensure that this transition does not break
  existing support for various operating systems and build environments, including
  RTEMS, Darwin, and Windows (Cygwin/MinGW). Maintainers are being consulted about
  build configurations and potential target-specific issues.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/878q7uuy9w.fsf@euler.schwinge.ddns.net
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

The libgomp library, which provides OpenMP support in GCC, is being rewritten from C to C++. This transition is expected to affect various targets, including those using RTEMS, Darwin, and Cygwin. "embedded-brains.de" notes that libgomp is enabled for RTEMS targets supporting SMP, and there's ongoing work sponsored by the European Space Agency for critical systems. "sandoe.co.uk" confirms libgomp support on Darwin, while "10walls@gmail.com" and "lh_mouse@126.com" discuss Cygwin and MinGW considerations, particularly regarding pthread implementations.
