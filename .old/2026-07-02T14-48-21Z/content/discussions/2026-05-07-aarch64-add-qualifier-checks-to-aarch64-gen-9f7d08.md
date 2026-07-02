---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- disassembler
- qualifiers
- validation
discussion_id: b4a27729-d5b3-7ea2-b25f-3dbfbc8ea407@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 23/23] aarch64: Add qualifier checks to aarch64-gen'
headline: 'aarch64: Add qualifier checks to aarch64-gen'
tldr: Adds checks to aarch64-gen.c to verify correct lengths of qualifier sequences.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in `aarch64-gen.c` due to the addition of the qualifier
  checks.
- Potential for increased build time, although this is likely negligible.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Proposes adding checks to verify that all qualifier sequences have the
    correct length in aarch64-gen.c.
  quote: Add checks to verify that all qualifier sequences have the correct length.
primer_expert: '`aarch64-gen.c` is responsible for generating the AArch64 opcode tables
  used by the assembler and disassembler.  Qualifiers are used to differentiate between
  different forms of an instruction based on operand types or other characteristics.
  Incorrectly sized qualifier sequences can lead to misassembly or incorrect disassembly.'
primer_general: This patch adds validation checks to the code that generates AArch64
  instruction definitions within binutils. AArch64 instructions can have different
  forms depending on the types of operands they use.  These forms are distinguished
  by "qualifiers." This patch ensures that the information describing these qualifiers
  is consistent with the instruction's operands, which helps prevent errors during
  the assembly and disassembly processes.
series_id: 'binutils:aarch64: add qualifier checks to aarch64-gen'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b4a27729-d5b3-7ea2-b25f-3dbfbc8ea407@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch adds checks to `aarch64-gen.c` to ensure that the qualifier sequences for AArch64 instructions have the correct length. These checks verify that each qualifier sequence corresponds to the number of operands in the instruction, preventing potential errors during assembly and disassembly.  This improves the robustness of the AArch64 assembler and disassembler.
