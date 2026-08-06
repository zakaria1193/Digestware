---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- static-analysis
- C++
discussion_id: DKH0OGC2G59B.3REH1EGI2Y4ZI@gmail.com
source_type: public_inbox
title: '[GSoC] Extending C++ Support in -fanalyzer - Status Report 3'
headline: Extending C++ Support in -fanalyzer - Status Report 3
tldr: GSoC student reports progress on C++ support for -fanalyzer, with exception
  handling and vfunc patches merged, and dynamic_cast support nearing review.
proposer: Egas Ribeiro
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Egas Ribeiro
  role: proposer
  position: Provides a status update on the GSoC project, detailing merged patches
    and the current state of the `dynamic_cast` implementation.
  quote: 'I didn''t submit a status report for a few weeks because I was busy

    trying to finish dynamic_cast cast support, which took a lot longer than

    I expected and became quite a big feature patch.'
primer_expert: This GSoC project aims to enhance GCC's static analyzer to understand
  and analyze C++ code more effectively. The student has successfully integrated support
  for C++ exception handling and virtual function calls, key features for analyzing
  C++ object-oriented code. The current focus is on `dynamic_cast`, a complex C++
  runtime feature, which requires significant analysis infrastructure changes.
primer_glossary:
- term: GSoC
  definition: Google Summer of Code, an annual program that offers stipends to students
    who contribute to open-source projects.
- term: -fanalyzer
  definition: A GCC compiler flag that enables a static analysis pass to detect potential
    bugs and vulnerabilities in code without executing it.
- term: exception handling
  definition: A programming construct used to handle runtime errors or exceptional
    conditions that disrupt the normal flow of program execution.
- term: vfunc
  definition: Short for virtual function, a member function in a base class that can
    be redefined in a derived class. Used for polymorphism.
- term: dynamic_cast
  definition: A C++ operator used for converting pointers or references to derived
    class types at runtime, performing type checking.
- term: GIMPLE
  definition: GCC's internal tuple representation for intermediate language, used
    after parsing and before optimization.
- term: ipa-devirt
  definition: Interprocedural analysis (IPA) for devirtualization, a GCC optimization
    technique.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/DKH0OGC2G59B.3REH1EGI2Y4ZI@gmail.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

This is a status report for a Google Summer of Code project to extend C++ support in GCC's static analyzer (-fanalyzer). The student has merged patches for exception handling and virtual function support. The main focus for the past few weeks was implementing `dynamic_cast` support, which resulted in a large patch that is now awaiting review. The project also involves updating the analyzer's C++ wiki page.
