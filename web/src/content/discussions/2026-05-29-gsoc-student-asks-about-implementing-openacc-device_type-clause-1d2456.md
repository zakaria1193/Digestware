---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- OpenACC
- OpenMP
- device_type
- clause
discussion_id: DIUYMDLBV3I7.2571EKJWICMHG@gmail.com
source_type: public_inbox
title: '[GSoC - OpenACC] Question implementing device_type clause'
headline: GSoC Student Asks About Implementing OpenACC device_type Clause
tldr: A GSoC student asks about naming and resolving the type of the OpenACC device_type
  clause, which conflicts with an OpenMP clause.
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This email concerns implementation details of OpenACC directives within
  GCC. The student is facing a naming conflict between OpenACC and OpenMP clauses,
  both of which use `device_type`. They also need to determine how to resolve the
  device type argument, which is defined in `openacc.h`. This relates to the parsing
  and semantic analysis stages of the compiler.
primer_general: This email is a question from a student participating in Google Summer
  of Code (GSoC), working on the GCC compiler. The student is adding support for OpenACC,
  a way to write code that can run on different kinds of hardware, including GPUs.  They've
  run into a problem where OpenACC and OpenMP (another parallel programming standard)
  both use the same name (`device_type`) for different things. The student is asking
  for advice on how to resolve this conflict and how to determine the specific type
  of device being targeted.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/DIUYMDLBV3I7.2571EKJWICMHG@gmail.com
bugzilla_url: null
date: '2026-05-29'
is_stub: false
---

A Google Summer of Code (GSoC) student is implementing the parsing for the `acc init` directive clauses in GCC and encounters a naming conflict with `OMP_CLAUSE_DEVICE_TYPE` from OpenMP 5.0 when implementing the `device_type` clause. The student asks how to name the new OpenACC clause and how to resolve the type of the device argument, given that the types are defined in `openacc.h`.
