---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- opcode
discussion_id: 22be894e-c7f4-8f71-7abc-0efeec426553@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 07/28] aarch64: Adjust alias priorities and make F_P1 default'
headline: 'aarch64: Adjust alias priorities and make F_P1 default'
tldr: Revises AArch64 opcode alias priorities and sets F_P1 as the new default.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Provides a more flexible alias prioritization system.
- Simplifies handling of overlapping opcodes by using a default priority.
- Requires explicit setting of non-alias priorities for compatibility.
exchanges: []
primer_expert: This change in `include/opcode/aarch64.h` and `opcodes/aarch64-asm-2.c`
  redefines how alias priorities are handled. Previously, `F_P1` through `F_P3` represented
  priorities 1-3, with 0 as the default. Now, `F_P0` to `F_P3` represent priorities
  0-3, and the default priority for aliases is `F_P1` (which maps to priority 0 after
  the bit shift). The `opcode_priority` function is updated to reflect this, ensuring
  non-aliases correctly get priority 0.
primer_glossary:
- term: F_P1
  definition: A flag representing a disassembly preference priority. In this context,
    it's being redefined to signify a default priority level for alias opcodes.
- term: alias priority
  definition: A mechanism to determine which opcode should be preferred when multiple
    opcodes match the same instruction encoding, affecting how the instruction is
    disassembled or assembled.
series_id: 'binutils:aarch64: adjust alias priorities and make f_p1 default'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/22be894e-c7f4-8f71-7abc-0efeec426553@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch adjusts the AArch64 opcode alias priorities to decouple them from opcode table ordering and the default priority value. The default alias priority is changed to `F_P1`, allowing less specific opcodes to be deprioritized without explicitly raising the priority of overlapping, more specific opcodes. For now, non-aliases are explicitly set to priority 0 in `opcode_priority()` to meet `aarch64-gen.c`'s requirements.
