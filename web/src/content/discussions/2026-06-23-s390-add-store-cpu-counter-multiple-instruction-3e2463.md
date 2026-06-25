---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- instruction set
- performance monitoring
- assembler
- hardware feature
discussion_id: 4a288de2-674e-4ae8-80da-f2d430cf332e@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] s390: Add store CPU counter multiple instruction'
headline: 'S390: Add store CPU counter multiple instruction'
tldr: Binutils gains support for the s390 'store CPU counter multiple' (stcctm) instruction,
  enhancing performance monitoring capabilities on IBM z13 and newer syste…
proposer: Andreas Krebbel <krebbel@linux.ibm.com>
consensus: Committed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables software to fully leverage hardware performance monitoring capabilities
  on IBM z13 and newer s390 processors.
- Adds complexity to the s390 instruction set support within Binutils, requiring maintenance
  of new opcodes and test cases.
- Improves the precision and efficiency of performance analysis tools for s390 platforms.
exchanges:
- author: Andreas Krebbel <krebbel@linux.ibm.com>
  role: proposer
  position: Proposes to add support for the `stcctm` instruction to Binutils for the
    s390 architecture, enabling full use of IBM z13 CPU-Measurement Facilities. The
    maintainer approved the patch.
  quote: Ok, Thanks!
primer_expert: The s390 architecture, used in IBM Z mainframes, includes specialized
  hardware facilities for performance monitoring and measurement. The CPU-Measurement
  Facilities (CPUMF) provide access to various CPU-internal counters. The `stcctm`
  (store CPU counter multiple) instruction, introduced with the z13 processor, is
  a feature that allows a program to read the values of multiple such counters in
  a single operation, improving efficiency for performance profiling and diagnostics.
  This patch integrates support for this instruction into Binutils' assembler (`gas`)
  and opcode definitions, ensuring tha…
primer_general: Modern computer processors, like those in IBM's large 'mainframe'
  computers (s390 architecture), have special built-in counters that track various
  aspects of their operation, such as how many instructions they execute or how often
  they access memory. These 'CPU counters' are crucial for understanding and optimizing
  program performance. This proposal adds support to Binutils (a set of tools that
  help turn human-readable code into machine code) for a specific instruction called
  `stcctm`. This instruction, available on newer IBM Z processors, allows a program
  to quickly read multiple CPU counters at once. This means developers can more efficiently
  gather performance data, which helps them make their software run faster on these
  powerful machines.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/4a288de2-674e-4ae8-80da-f2d430cf332e@linux.ibm.com
bugzilla_url: null
date: '2026-06-23'
is_stub: false
stub_reason: ''
---

This patch adds support for the `stcctm` (store CPU counter multiple) instruction to Binutils for the s390 architecture. This instruction, introduced with the IBM z13 processor and part of the CPU-Measurement Facilities (CPUMF), allows for storing multiple CPU performance counters simultaneously. The change includes updates to the s390 opcode table and corresponding test cases for `gas/s390`. The maintainer approved the patch.
