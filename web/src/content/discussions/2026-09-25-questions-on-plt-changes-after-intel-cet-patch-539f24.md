---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- PLT
- GOT
- CET
discussion_id: CAKQiWZG2TMkLAGMji+x3MT+Kp0bA78A_LgxJ7Xd=vMs9nhzO3A@mail.gmail.com
source_type: public_inbox
title: Questions on how the implementation of PLT changed after the Intel CET patch
headline: Questions on PLT changes after Intel CET patch
tldr: A developer is seeking clarification on how the Intel CET patch has affected
  the implementation of the Procedure Linkage Table (PLT) in binutils.
proposer: 김형원 <hwkim568@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This inquiry concerns the interaction between Intel CET (Control-flow
  Enforcement Technology) and the Procedure Linkage Table (PLT) implementation within
  binutils. Specifically, the author is trying to understand how the introduction
  of CET, which provides hardware-based protections against control-flow hijacking
  attacks, has altered the way PLT entries are generated or handled by the linker,
  particularly in relation to the Global Offset Table (GOT).
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to achieve indirection for function calls, allowing code to call functions in
    shared libraries without needing to know their absolute addresses at link time.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code (PIC)
    to store addresses of global variables and functions, enabling dynamic linking.
- term: Intel CET
  definition: Control-flow Enforcement Technology. A set of hardware features designed
    to protect against control-flow hijacking attacks, such as Return-Oriented Programming
    (ROP) and Jump-Oriented Programming (JOP).
- term: Dynamic linking
  definition: A process in which executable files are linked with shared libraries
    at runtime, rather than at compile time. This allows multiple programs to use
    the same library code efficiently.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKQiWZG2TMkLAGMji+x3MT+Kp0bA78A_LgxJ7Xd=vMs9nhzO3A@mail.gmail.com
bugzilla_url: null
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

Hyungwon Kim is investigating changes to the Procedure Linkage Table (PLT) in binutils that resulted from the Intel Control-flow Enforcement Technology (CET) patch. After studying resources on PLT and GOT, Kim is compiling code examples and seeking to understand the specific modifications made to the PLT implementation due to CET.
