---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-validation
discussion_id: 20260930081834.2948939-30-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 08/20] s390: mvcl operands R1 and R2 must be register pairs'
headline: 's390: mvcl operands R1 and R2 must be register pairs'
tldr: Ensures the mvcl instruction in binutils assembler correctly handles register
  pair operands.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses the s390 'mvcl' instruction within the binutils
  assembler. It corrects the operand validation to ensure that registers R1 and R2,
  which are interpreted as even-odd pairs, are indeed even-numbered registers as required
  by the architecture. This impacts the assembler's correctness for specific s390
  instructions.
primer_glossary: []
series_id: 'binutils:s390: mvcl operands r1 and r2 must be register pairs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-30-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects the binutils assembler's handling of the s390 'mvcl' instruction. It enforces that the R1 and R2 operands must designate an even-numbered register, which forms an even-odd pair, aligning with the s390 architecture specification. Changes are made to opcode definitions and gas test suites.
