---
project: binutils
subsystem: binutils/opcodes
patch_id: null
tags:
- security
- disassembler
- mep
- buffer-overflow
commit_hash: 70f2a72f53388a289c17bbb120e268e649b71ab3
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: MEP disassembler fixes buffer overflow
tldr: The Binutils MEP disassembler corrects a buffer overflow vulnerability when
  examining VLIW64 instructions.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `mep_examine_vliw64_insns` function in `cpu/mep.opc` (which generates
  `opcodes/mep-dis.c`) is responsible for disassembling VLIW64 instructions for the
  MEP architecture. This function was vulnerable to a buffer overflow due to an incorrect
  buffer size, attempting to read `8` bytes into a `4`-byte `buf`. The fix corrects
  this by ensuring the `buf` is appropriately sized (`sizeof (buf)`), resolving the
  out-of-bounds write. Additionally, similar functions like `mep_examine_vliw32_insns`
  and `mep_examine_ivc2_insns` have been refactored to use `sizeof (buf)` instead
  of opaque `CGEN_MAX_INSN_S…
primer_general: A disassembler is a tool that takes machine code (the raw instructions
  a computer understands) and translates it back into assembly language, which is
  more readable for humans. This particular update addresses a bug in the Binutils
  disassembler for the MEP (Microcontroller-Embedded Processor) architecture. Specifically,
  a function that examines certain types of MEP instructions (called VLIW64 instructions)
  was trying to read too much data into a small temporary storage area, leading to
  a "buffer overflow." A buffer overflow is a vulnerability where a program attempts
  to write data beyond the boundaries of a fixed-size memory buffer. This can corrupt
  other data or even allow attackers to inject malicious code. The fix ensures that
  the temporary storage area is now correctly sized to prevent this overflow, making
  the disassembler more secure and reliable, particularly when processing potentially
  malformed or unusual MEP instruction sequences.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617235555.135A34BA2E18@sourceware.org
date: '2026-06-17'
is_stub: false
---

The Binutils disassembler for the MEP architecture previously contained a buffer overflow in the `mep_examine_vliw64_insns` function, where it attempted to read 8 bytes into a 4-byte buffer. This vulnerability has been patched by correctly sizing the buffer to prevent out-of-bounds writes. Additional code tidying in related functions eliminates obscure macro usage for buffer sizing, improving code clarity and robustness.
