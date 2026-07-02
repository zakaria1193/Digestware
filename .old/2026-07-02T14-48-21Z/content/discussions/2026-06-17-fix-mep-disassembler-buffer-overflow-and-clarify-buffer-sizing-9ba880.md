---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- buffer-overflow
- disassembler
- mep
- binutils
discussion_id: ajMznI_E0S-ZgZIc@squeak.grove.modra.org
source_type: public_inbox
title: mep disassembler buffer overflow
headline: Fix mep disassembler buffer overflow and clarify buffer sizing
tldr: Corrects a buffer overflow in the MEPO disassembler and improves buffer sizing
  clarity.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes to fix a buffer overflow in the MEP disassembler and to clarify
    buffer sizing across related functions.
  quote: mep_examine_vliw64_insns uses a buffer of size 4 to read 8 bytes. Fix that,
    and tidy other places obscuring the code by using a macro to size buffers.
primer_expert: This patch targets `cpu/mep.opc` and `opcodes/mep-dis.c`, which are
  components of the Binutils disassembler for the MEP architecture (a VLIW processor).
  The critical fix is in `mep_examine_vliw64_insns`, where a `bfd_byte` buffer was
  incorrectly sized for 4 bytes when 8 bytes were being read, leading to a heap buffer
  overflow. The patch also standardizes buffer declarations to `sizeof(buf)` instead
  of using `CGEN_MAX_INSN_SIZE` or hardcoded literals, improving maintainability and
  preventing similar errors. This is a critical correctness and security fix for handling
  MEP instruction streams du…
primer_general: This change fixes a serious error, known as a 'buffer overflow,' in
  the Binutils disassembler specifically for the MEP processor architecture. Disassemblers
  translate machine code (the raw instructions a computer understands) back into human-readable
  assembly language. In this case, a function responsible for disassembling 64-bit
  instructions on MEP (`mep_examine_vliw64_insns`) was trying to store 8 bytes of
  data into a temporary storage area (buffer) that was only big enough for 4 bytes.
  This overflow could lead to program crashes or, in some cases, could be exploited
  for malicious purposes. The fix correctly sizes the buffer and also tidies up other
  related code to make sure buffer sizes are calculated reliably, preventing similar
  issues in the future and improving the overall stability of the disassembler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajMznI_E0S-ZgZIc@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-17'
is_stub: false
---

This patch addresses a buffer overflow in the MEP disassembler where `mep_examine_vliw64_insns` attempts to read 8 bytes into a 4-byte buffer. It also refactors other related code to use `sizeof()` for buffer sizing, eliminating the use of a macro and improving clarity and correctness. This fix is crucial for the stability and security of the MEP disassembler.
