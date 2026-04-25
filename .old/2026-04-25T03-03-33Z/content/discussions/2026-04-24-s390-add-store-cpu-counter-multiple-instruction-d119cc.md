---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction
- CPUMF
- z13
discussion_id: 20260424084026.2959245-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH] s390: Add store CPU counter multiple instruction'
headline: 's390: Add store CPU counter multiple instruction'
tldr: Adds support for the 'store CPU counter multiple' instruction on IBM z13 to
  binutils.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds a new instruction, increasing the size of the opcode table.
- Increases complexity of the assembler, though minimally.
exchanges: []
primer_expert: This patch introduces the `stcctm` instruction to `opcodes/s390-opc.txt`,
  enhancing s390 assembler support. The instruction is specific to IBM z13 CPUs and
  part of the CPUMF. Toolchain developers working with s390 assembly or performance
  analysis tools might find this relevant.
primer_general: This patch updates the binutils assembler to support a new instruction
  (`stcctm`) on IBM's z13 mainframe architecture. Assemblers translate human-readable
  assembly code into machine code that CPUs can execute.  This instruction is related
  to CPU performance monitoring. Developers working on s390 systems who need to use
  this new instruction will benefit from this update.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260424084026.2959245-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-04-24'
---

This patch adds the `stcctm` instruction, introduced with the IBM z13, to the s390 opcode table in binutils. It also includes a test case for the new instruction in the assembler's test suite and adds comments to existing CPUMF instructions.  This instruction is part of the CPU-Measurement Facilities (CPUMF).
