---
project: gcc
subsystem: gcc/OpenACC
patch_id: null
tags:
- OpenACC
- GSoC
- front-end
- parsing
- Fortran
discussion_id: DJ2AD6OFAEHF.3RIMPYTK5KVR4@gmail.com
source_type: public_inbox
title: '[GSoC - OpenACC] Weekly report - week 2 '
headline: GSoC OpenACC weekly report describes parsing progress
tldr: A GSoC student provides a progress report on implementing OpenACC parsing for
  C, C++, and Fortran front-ends in GCC, noting some debugging challenges.
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Sebastian Galindo <sebastian.galindo143@gmail.com>
  role: proposer
  position: Reports on the implementation progress of OpenACC directives for GCC's
    C, C++, and Fortran front-ends.
  quote: The C++ front-end recognizes the {init,set,shutdown} directives, but there
    are still some bugs that I'm currently fixing. Fortran now accepts the device_type
    clause, and I'm currently working on including the arguments in the parsing logic.
primer_expert: This report details progress on the frontend parsing stage for OpenACC
  within GCC. The student is integrating new directives like `init`, `set`, and `shutdown`
  into the C++ frontend and `device_type` into the Fortran frontend. This involves
  modifications to the respective language parsers (e.g., `cp/parser.cc`, `fortran/parser.cc`)
  and potentially extensions to the internal representation of OpenACC clauses, such
  as `omp_mask` for device type handling. The work touches on how OpenACC constructs
  are syntactically recognized and translated into an internal representation for
  subsequent compilat…
primer_general: This discussion is about implementing support for OpenACC, a programming
  model for parallel computing similar to OpenMP, within the GCC compiler. Specifically,
  it focuses on the "front-end" of the compiler, which is the part that reads and
  understands the source code written by programmers. The student is adding support
  for new OpenACC keywords (directives like ``init``, ``set``, ``shutdown``, and ``device_type``)
  so that the compiler can correctly interpret and process them in C, C++, and Fortran
  programs. This involves modifying the compiler's parsing logic to recognize these
  directives and convert them into an internal format the rest of the compiler can
  understand. The overall goal is to enable GCC to compile OpenACC-accelerated programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/DJ2AD6OFAEHF.3RIMPYTK5KVR4@gmail.com
bugzilla_url: null
date: '2026-06-06'
is_stub: false
---

This is a weekly report from a Google Summer of Code student detailing progress on implementing OpenACC directives within the GCC compiler. The student is working on parsing ``init``, ``set``, and ``shutdown`` directives for C and C++ front-ends, and ``device_type`` for the Fortran front-end. Debugging parsing issues in the C++ front-end and integrating ``OACC_CLAUSE_DEVICE_TYPE`` with ``omp_mask`` in Fortran are current focuses, with slight delays due to the learning curve of the GCC front-ends.
