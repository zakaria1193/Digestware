---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- s390
- assembler
- stcctm
- CPU counter
discussion_id: 20260424084026.2959245-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH] s390: Add store CPU counter multiple instruction'
headline: 's390: Add store CPU counter multiple instruction'
tldr: Adds support for the 'store CPU counter multiple' (stcctm) instruction for the
  s390 architecture, introduced with the IBM z13.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased complexity of the s390 opcode table.
- Minimal impact on other architectures or binutils components.
exchanges: []
primer_expert: This patch adds the `stcctm` instruction to the s390 opcode table (`opcodes/s390-opc.txt`)
  and provides gas test cases.  The `stcctm` instruction is part of the CPU-Measurement
  Facilities (CPUMF) on IBM z13.  Assembler support is required to use this instruction,
  which is relevant for performance monitoring and analysis on s390 systems. CPUMF
  provides low-level access to hardware counters.
primer_general: This patch extends the s390 assembler in binutils to recognize a new
  instruction, `stcctm`. The assembler translates human-readable assembly code into
  machine code that the processor can execute. `stcctm` is a CPU instruction that
  allows reading multiple performance counters at once.  Performance counters are
  special hardware registers that track various metrics like CPU cycles, cache misses,
  and branch predictions. By adding support for `stcctm`, developers can write code
  to monitor the performance of their applications on s390 systems more effectively.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260424084026.2959245-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-04-24'
---

This patch adds support for the `stcctm` (store CPU counter multiple) instruction to the s390 assembler.  The instruction, introduced with the IBM z13, is part of the CPU-Measurement Facilities and allows storing multiple CPU counters.  The patch updates the opcode table and adds corresponding tests, enabling developers to utilize this instruction when targeting the z13 architecture and later.
