---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- sframe
- cfi
- debugging
discussion_id: 20260729163445.2563223-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 0/2] gas: sframe: Fix for flefible FDE and new test'
headline: 'gas: sframe: Fix for flexible FDE and new test'
tldr: Series updates gas SFrame generation for flexible FDEs and adds a test for unsupported
  CFI in signal frames.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Supporting SFrame v3 flexible FDEs without breaking existing functionality.
- Ensuring robust handling of unsupported CFI directives in signal frames.
- Balancing detail in debugging information with potential for errors.
exchanges: []
primer_expert: This patch series addresses two aspects of SFrame generation within
  the GNU Assembler (gas). The first patch rectifies issues with generating flexible
  FDEs, specifically for SFrame v3, ensuring correct handling of non-standard PC/SP/FP
  register usage for CFA (Call Frame Address) definitions. The second patch introduces
  a test case to validate behavior when encountering unsupported CFI directives within
  signal frames, ensuring graceful handling by generating an empty FDE. These changes
  contribute to more reliable debugging information.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils suite.
- term: sframe
  definition: Stack Frame, a data structure that aids in stack unwinding for debugging
    purposes.
- term: FDE
  definition: Frame Description Entry, a part of DWARF debugging information that
    describes how to construct or deconstruct a function's stack frame.
- term: flexible FDE
  definition: A type of FDE that allows for more dynamic or non-standard ways of defining
    the Call Frame Address (CFA), potentially using different base registers or offsets.
- term: CFI
  definition: Call Frame Information, directives used in debugging symbols to describe
    stack frame layout and unwinding.
- term: signal frame
  definition: A special stack frame created when a signal is delivered to a process.
- term: CFA
  definition: Call Frame Address, typically the stack pointer value at the point a
    function is called, used as a reference for unwinding.
series_id: 'binutils:gas: sframe: fix for flefible fde and new test'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260729163445.2563223-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This series consists of two patches: the first fixes the generation of SFrame data when dealing with flexible FDEs (Frame Description Entries) that support SFrame version 3. The second patch introduces a new test case to validate gas's behavior with unsupported CFI (Call Frame Information) directives in signal frames. Together, these patches aim to improve the robustness and correctness of stack frame information generation in the GNU Assembler.
