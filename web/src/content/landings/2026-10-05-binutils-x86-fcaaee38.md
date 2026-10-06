---
project: binutils
subsystem: binutils/x86
patch_id: null
tags:
- x86
- assembler
- amx
- optimization
commit_hash: fcaaee3888c6eb48e886fdfd030540ec47287e56
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Templatize AMX_INT8 TDPB* instructions
tldr: x86 assembler simplifies AMX_INT8 TDPB* instruction definitions using templates.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The opcode table entries for AMX_INT8 TDPB* instructions (TDPBUUD,
  TDPBUSD, TDPBSSD, TDPBSUD) are consolidated using a new template macro `<tdpb>`.
  This reduces code duplication and enables simpler definitions for related instructions,
  improving maintainability of the x86 opcode definitions.
primer_glossary:
- term: AMX_INT8
  definition: A mode within AMD's Advanced Matrix Extensions (AMX) that operates on
    8-bit integer matrices.
- term: TDPB*
  definition: A family of AMX instructions for tile data packing and processing, operating
    on 8-bit integer data.
- term: Opcode table
  definition: A data structure used by assemblers and disassemblers to map instruction
    mnemonics and operands to their binary machine code representations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261005091912.4E01B4BA23D2@sourceware.org
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This commit refactors the definition of several AMX_INT8 TDPB* instructions in the x86 assembler. It uses a new template mechanism to reduce redundancy, making the opcode table definitions more concise and reusable for subsequent instructions like TOP4B*.
