---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- documentation
discussion_id: 20261106155649.2987420-51-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH v2 02/47] s390: Correct mode and minimum CPU level of .insn pseudo-mnemonics'
headline: 's390: Correct mode and minimum CPU level of .insn pseudo-mnemonics'
tldr: Corrects the documented mode and minimum CPU level for several .insn pseudo-mnemonics
  in the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch corrects the mode and minimum CPU level metadata associated
  with several s390 `.insn` pseudo-mnemonics within `opcodes/s390-opc.c`. These mnemonics
  (RIE, RIL, RILU, RIS, RRS, SIL, SIY, SSF, VRI, VRR, VRS, VRV, VRX, VSI) map to specific
  instruction formats whose availability is tied to particular z/Architecture or ESA/390
  modes and CPU levels. The change is purely informational as the assembler itself
  does not validate these constraints.
primer_glossary: []
series_id: 'binutils:s390: correct mode and minimum cpu level of .insn pseudo-mnemonics'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261106155649.2987420-51-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch corrects the documented mode and minimum CPU level for various .insn pseudo-mnemonics in the s390 assembler. While the assembler does not enforce these levels, the update ensures accuracy in documentation, reflecting the introduction of these instruction formats across different IBM mainframe architectures.
