---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- OpenACC
- Fortran
- libgomp
discussion_id: DIUZBBSEKP8V.30IFWOGVFE6GI@gmail.com
source_type: public_inbox
title: '[GSoC] Weekly report - week 1'
headline: GSoC Student Reports on First Week Implementing OpenACC Directives
tldr: A GSoC student details their progress implementing OpenACC init/shutdown/set
  directives in GCC, focusing on parsing in the Fortran front-end and linking API
  ru…
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This report concerns the implementation of OpenACC directives within
  GCC, specifically focusing on the init, shutdown, and set directives. OpenACC is
  a parallel programming standard that allows developers to offload computations to
  accelerators like GPUs.  The student is working on the Fortran front-end, libgomp
  (the GNU Offloading and Multi Processing Runtime Library), and the integration between
  them.
primer_general: This email is a progress report from a student participating in Google
  Summer of Code (GSoC), working on the GCC compiler. The student is implementing
  features from OpenACC, a standard for writing code that can run on different kinds
  of hardware, including GPUs. They are focusing on the "init", "shutdown", and "set"
  directives, which control how OpenACC is initialized and configured. The student
  is working on making the compiler understand these directives in the Fortran language.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/DIUZBBSEKP8V.30IFWOGVFE6GI@gmail.com
bugzilla_url: null
date: '2026-05-29'
is_stub: false
---

A Google Summer of Code (GSoC) student reports on their first week of implementing the init/shutdown/set directives from OpenACC in GCC. The work involves detailing the existing patch regarding API runtime functions, implementing the parsing of the directives in the Fortran front-end, and linking the existing API calls to the lowered function from the front and middle-end. The student has implemented parsing for the init directive in Fortran and included the corresponding built-in function in libgomp and is now working on clause parsing.
