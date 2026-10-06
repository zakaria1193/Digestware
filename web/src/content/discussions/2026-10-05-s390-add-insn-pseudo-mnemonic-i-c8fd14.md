---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- assembler
- instruction-formats
- documentation
discussion_id: 20261005153947.363053-60-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 12/46] s390: Add .insn pseudo-mnemonic i'
headline: 's390: Add .insn pseudo-mnemonic i'
tldr: Adds support for the .insn i pseudo-mnemonic in the s390 assembler and updates
  the svc instruction to use the new I_U format.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removal of the RR_U0 format might affect older codebases expecting it, though it's
  marked as deprecated.
- Ensuring correct mapping between the pseudo-mnemonic and the underlying instruction
  format.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds the .insn i pseudo-mnemonic, defines the I_U instruction format,
    and updates the svc instruction to use it, along with adding test cases.
  quote: null
primer_expert: This patch integrates the 'I' instruction format and its corresponding
  '.insn i' pseudo-mnemonic into the s390 assembler. It updates the opcode definitions
  to include the I_U format, removes an older RR_U0 format, and modifies the `svc`
  instruction to conform to the new format as per the z/Architecture specification.
  Test coverage is expanded for both ESA/390 and z/Architecture.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
- term: svc instruction
  definition: Supervisor Call instruction, used to transfer control from user mode
    to the operating system's supervisor mode.
- term: I_U format
  definition: A specific s390 instruction format used for instructions like '.insn
    i', characterized by an opcode and a single immediate operand.
series_id: 'binutils:s390: add .insn pseudo-mnemonic i'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-60-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces the '.insn i' pseudo-mnemonic for the s390 architecture in the GNU Assembler. It defines the I_U instruction format, removes the deprecated RR_U0 format, and modifies the 'svc' instruction to utilize the new I_U format, aligning it with the z/Architecture Principles of Operation. Test cases are added for both ESA/390 and z/Architecture.
