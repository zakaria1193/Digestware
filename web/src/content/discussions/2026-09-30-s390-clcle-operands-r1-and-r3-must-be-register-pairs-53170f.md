---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-validation
discussion_id: 20260930081834.2948939-27-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 05/20] s390: clcle operands R1 and R3 must be register pairs'
headline: 's390: clcle operands R1 and R3 must be register pairs'
tldr: Ensures the clcle instruction in binutils assembler correctly handles register
  pair operands.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch corrects the binutils assembler's implementation for the
  s390 'clcle' instruction. It enforces the architectural requirement that operands
  R1 and R3 must be even-numbered registers, functioning as register pairs. This validation
  prevents potential specification exceptions on s390 hardware by ensuring correct
  instruction usage.
primer_glossary: []
series_id: 'binutils:s390: clcle operands r1 and r3 must be register pairs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-27-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch modifies the binutils assembler to enforce correct operand usage for the s390 'clcle' instruction. It mandates that R1 and R3 operands must specify an even-numbered register, forming an even-odd pair, as required by the architecture specification to prevent specification exceptions. The changes include opcode definitions and gas test suite updates.
