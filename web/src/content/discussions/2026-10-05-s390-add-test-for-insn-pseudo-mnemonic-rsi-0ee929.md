---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- tests
- documentation
- assembler
discussion_id: 20261005153947.363053-74-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 26/46] s390: Add test for .insn pseudo-mnemonic rsi'
headline: 's390: Add test for .insn pseudo-mnemonic rsi'
tldr: Adds gas test cases and documentation for the .insn rsi pseudo-mnemonic on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add test cases and documentation for the .insn rsi
    pseudo-mnemonic in the s390 gas assembler, noting a historical operand order difference.
  quote: 'For historic reasons the .insn rsi pseudo-mnemonic operand order differs

    from the field index order.  Document that.'
primer_expert: This patch adds test cases and documentation for the '.insn rsi' pseudo-mnemonic
  in the s390 GNU Assembler (gas). It updates documentation to reflect the historical
  operand order for RSI and adds corresponding tests to the esa-operands and zarch-operands
  test suites.
primer_glossary:
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic rsi'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-74-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces test cases and documentation for the .insn rsi pseudo-mnemonic in the s390 GNU Assembler (gas). It addresses a historical discrepancy in operand order by documenting it and adding corresponding tests to ensure accurate assembly and disassembly.
