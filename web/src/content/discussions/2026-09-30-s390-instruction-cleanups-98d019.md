---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- maintenance
- cleanup
discussion_id: 20260930081834.2948939-22-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 00/20] s390: Instruction cleanups'
headline: 's390: Instruction cleanups'
tldr: Series of patches to clean up s390 instruction definitions and test cases in
  binutils.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch series targets the s390 architecture support within the
  binutils assembler. It involves routine maintenance such as improving table headings,
  standardizing test case naming conventions, and fixing specific instruction operand
  validations. The series aims to improve code clarity and correctness and serves
  as a prerequisite for more extensive future changes.
primer_glossary: []
series_id: 'binutils:s390: instruction cleanups'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-22-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This is the cover letter for a series of 20 patches that clean up various aspects of s390 instruction definitions and assembler test cases within binutils. The changes include enhancing opcode table headings, standardizing test names, and correcting operand validation for several instructions. This series prepares for future work on adding all instruction formats to .insn pseudo-mnemonics.
