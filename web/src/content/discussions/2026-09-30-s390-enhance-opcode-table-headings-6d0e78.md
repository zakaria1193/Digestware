---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- opcodes
- maintainability
discussion_id: 20260930081834.2948939-23-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 01/20] s390: Enhance opcode table headings'
headline: 's390: Enhance opcode table headings'
tldr: Improves readability of s390 opcode definitions in binutils.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the opcodes/s390-opc.txt file in binutils, which
  defines the assembler's understanding of s390 instructions. It reorganizes the table
  with clearer headings for different CPU architectures (e.g., z990, z9-109) and instruction
  facilities. Additionally, it cleans up comments related to instruction names, assuming
  they are adequately represented elsewhere in the definition.
primer_glossary:
- term: opcode table
  definition: A data structure or file used by an assembler or disassembler to map
    instruction mnemonics to their binary representations and associate them with
    specific CPU architectures and features.
- term: facility name
  definition: A designation for a specific set of hardware features or capabilities
    available on a particular processor architecture.
series_id: 'binutils:s390: enhance opcode table headings'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-23-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch enhances the headings in the s390 opcode table within binutils to provide clearer categorization for instructions based on CPU architecture levels and facility names. It also removes redundant comments, as instruction names are now directly available in the description field, improving the maintainability of the opcode definitions.
