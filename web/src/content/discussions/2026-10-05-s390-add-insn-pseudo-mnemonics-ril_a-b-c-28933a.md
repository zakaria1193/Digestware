---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- pseudo-mnemonic
- instruction-format
discussion_id: 20261005153947.363053-65-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 17/46] s390: Add .insn pseudo-mnemonics ril_a/b/c'
headline: 's390: Add .insn pseudo-mnemonics ril_a/b/c'
tldr: Adds support for RIL-a, RIL-b, and RIL-c pseudo-mnemonics for s390 architecture.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds specific instruction formats that may increase assembler complexity.
- Ensures backward compatibility by using the existing RIL minimum architecture levels.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds support for RIL-a, RIL-b, and RIL-c pseudo-mnemonics, requiring specific
    minimum architecture levels and including tests for rilu.
  quote: 'History of instruction format RIL:

    - RIL-b/c got initially introduced as RIL with IBM z900. [1, 2]

    - RIL-a got introduced with IBM z9-109. [3, 4]


    Require the respective minimum architecture/CPU level.


    While at it add test for non-standard RIL .insn pseudo-mnemonic rilu.'
primer_expert: This patch extends the s390 assembler's support for the `.insn` directive
  by adding pseudo-mnemonics for the RIL-a, RIL-b, and RIL-c instruction formats.
  These formats, variations of the Relative ISTRUCTION List (RIL) format, were introduced
  in different IBM mainframe generations (z900, z9-109). The changes involve updating
  the `s390-opc.c` to recognize these new mnemonics and adding corresponding test
  cases in `gas/testsuite/gas/s390/` to verify their encoding and disassembly.
primer_glossary: []
series_id: 'binutils:s390: add .insn pseudo-mnemonics ril_a/b/c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-65-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the RIL-a, RIL-b, and RIL-c instruction formats on the s390 architecture using the .insn pseudo-mnemonic. It requires specific minimum architecture levels for each variant and adds tests for the rilu pseudo-mnemonic. The changes update opcode definitions and gas test suites.
