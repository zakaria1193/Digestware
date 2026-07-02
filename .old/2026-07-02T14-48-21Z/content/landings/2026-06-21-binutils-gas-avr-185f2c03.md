---
project: binutils
subsystem: binutils/gas/avr
patch_id: null
tags:
- avr
- assembler
- bugfix
- diagnostics
commit_hash: 185f2c03f6dbbb1d739be919cf625d687872b50d
source_type: public_inbox
author: Georg-Johann Lay
headline: AVR assembler now correctly diagnoses unknown opcodes for specific MCUs
tldr: The AVR assembler (gas) now provides accurate error messages when an opcode
  is not supported by the target microcontroller, fixing misleading diagnostics.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The AVR assembler (`gas`) uses the `md_assemble` function in `gas/config/tc-avr.c`
  to translate assembly mnemonics into machine code. The `opcode` lookup table, defined
  by `include/opcode/avr.h`, contains instructions, each with associated `isa` flags
  indicating supported instruction set architectures. When an instruction (`opcode->isa`)
  is not supported by the target MCU (`avr_mcu->isa`), the `while` loop within `md_assemble`
  iterates to find a match. The bug was that `opcode++` was executed before the `as_bad`
  diagnostic, causing the error message to display the name of the *next* opcode in…
primer_general: When you write assembly code for an AVR microcontroller, you use specific
  instructions (opcodes) that your chosen chip understands. The assembler (part of
  Binutils, often called `gas`) translates this human-readable assembly into machine
  code. Different AVR microcontrollers support different sets of instructions. This
  update fixes a bug in how the assembler reports errors when you try to use an instruction
  that your specific microcontroller doesn't support. Previously, if you used an unsupported
  instruction, the error message would incorrectly tell you that the *next* instruction
  in your code was the problem, which could be confusing. Now, the assembler will
  correctly identify the actual instruction that your microcontroller doesn't understand,
  making it much easier to fix your assembly code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260621165345.6DAB54BA2E0D@sourceware.org
date: '2026-06-21'
is_stub: false
---

The AVR assembler (gas) has corrected a diagnostic bug where error messages for unsupported opcodes on a given MCU would incorrectly report the mnemonic of the *subsequent* instruction. The fix modifies `md_assemble` in `gas/config/tc-avr.c` to use the correct opcode index when reporting the error, ensuring the diagnostic precisely identifies the instruction causing the issue. This improves the clarity and helpfulness of assembly error messages for AVR developers.
