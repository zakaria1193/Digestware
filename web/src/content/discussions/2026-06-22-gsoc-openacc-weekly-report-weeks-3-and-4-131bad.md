---
project: gcc
subsystem: gcc/OpenACC
patch_id: null
tags:
- OpenACC
- GSoC
- Fortran
- libgomp
- parallel computing
discussion_id: DJF6VR6UNI4R.3M85I95TJU3JW@gmail.com
source_type: public_inbox
title: '[GSoC - OpenACC] Weekly report (weeks 3 and 4)'
headline: GSoC - OpenACC weekly report (weeks 3 and 4)
tldr: A GSoC student provides a bi-weekly report on their progress implementing OpenACC
  directive support in GCC, focusing on initial Fortran front-end and libgomp w…
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Sebastian Galindo
  role: proposer
  position: Reports on the progress of OpenACC `init`, `set`, and `shutdown` directives
    in GCC, focusing on Fortran front-end implementation.
  quote: I finalized the implementation details of the patch, focusing first on the
    Fortran front-end. This approach allows me to gather feedback on the libgomp implementation
    and overall front-end parsing before replicating it in C/C++, preventing the patch
    from becoming too large.
primer_expert: This report details ongoing work within the GCC compiler infrastructure,
  specifically targeting the integration of OpenACC directives. The work involves
  modifying the Fortran front-end (typically `gcc/fortran`) and the OpenACC runtime
  library (`libgomp`). The mention of `default_async` clause semantics and `acc_async_noval`
  suggests interaction with the OpenACC asynchronous execution model and its internal
  representation within `libgomp`.
primer_general: OpenACC is a programming model that allows developers to accelerate
  their applications on parallel hardware like GPUs. This report is about a student's
  progress in adding OpenACC support to GCC, a widely used compiler collection. The
  student is implementing specific OpenACC commands (directives like `init`, `set`,
  and `shutdown`) first for Fortran programs, which are often used in scientific computing.
  The goal is to make it easier for Fortran code to take advantage of parallel processing,
  leading to faster execution of programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/DJF6VR6UNI4R.3M85I95TJU3JW@gmail.com
bugzilla_url: null
date: '2026-06-22'
is_stub: false
---

This is a bi-weekly progress report from a Google Summer of Code student working on OpenACC implementation for GCC. The student details finalizing initial Fortran front-end and libgomp implementation for `init`, `set`, and `shutdown` directives, encountering some regression test issues, yet successfully submitting the patch for review. This work will bring OpenACC support to GCC, enabling accelerated computing for Fortran programs.
