---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- instruction
- patch
discussion_id: 12b4b085-7f94-4051-ab08-447ad90cb880@suse.com
source_type: public_inbox
title: '[PATCH v2] x86: prune redundant x64 from RMPREAD'
headline: 'x86: Prune redundant x64 from RMPREAD'
tldr: Patch removes redundant 'x64' attribute from RMPREAD instruction.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removing redundancy in instruction definitions for clarity and maintainability.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Submitted a patch to remove the redundant 'x64' attribute from the RMPREAD
    instruction and add its operand-less form.
  quote: 'As noticed during review of the RMPOPT/RMPDIRTY patch: CpuRMPREAD depends

    on Cpu64, so the attribute is redundant to specify. This then also matches

    in particular RMPQUERY.


    While there also add the missing operand-less form of the insn.'
primer_expert: This patch modifies `opcodes/i386-opc.tbl` to remove the `x64` flag
  from the RMPREAD instruction entry. The `x64` flag is redundant because RMPREAD
  already implies 64-bit operation through its dependency on `Cpu64`. The change also
  introduces a new entry for the operand-less form of RMPREAD, which was previously
  missing.
primer_glossary:
- term: RMPREAD
  definition: A specific x86 instruction, likely related to memory protection or management,
    possibly for reading a Read-Modify-Protect (RMP) table entry.
- term: x64
  definition: Refers to the 64-bit instruction set architecture extensions for x86
    processors.
- term: Cpu64
  definition: An attribute or flag indicating that an instruction is valid or intended
    for use in 64-bit mode.
- term: Operand-less form
  definition: An instruction that can be executed without any explicit operands, relying
    on implicit register operands or default behavior.
- term: i386-opc.tbl
  definition: A table file used by Binutils to define the opcodes and their properties
    for the i386 (x86) architecture.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/12b4b085-7f94-4051-ab08-447ad90cb880@suse.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Jan Beulich proposes a patch to remove the redundant 'x64' attribute from the RMPREAD instruction in the opcodes table. This attribute was found to be unnecessary because RMPREAD already depends on Cpu64, and removing it aligns with the attributes of RMPQUERY. The patch also adds the operand-less form of the instruction.
