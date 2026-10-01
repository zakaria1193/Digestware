---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-validation
discussion_id: 20260930081834.2948939-28-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 06/20] s390: cmpsc operands R1 and R2 must be register pairs'
headline: 's390: cmpsc operands R1 and R2 must be register pairs'
tldr: Ensures the cmpsc instruction in binutils assembler correctly handles register
  pair operands.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses the s390 'cmpsc' instruction within the binutils
  assembler. It enforces the architectural rule that the R1 and R2 operands must refer
  to even-numbered registers, which are used in pairs. This validation is crucial
  for preventing specification exceptions that could arise from incorrect register
  pair usage on s390 processors.
primer_glossary: []
series_id: 'binutils:s390: cmpsc operands r1 and r2 must be register pairs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-28-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects the binutils assembler's validation for the s390 'cmpsc' instruction, ensuring that its R1 and R2 operands correctly designate an even-numbered register, forming an even-odd pair. This adherence to the architecture specification prevents specification exceptions. Changes include opcode definitions and updates to the gas test suite.
