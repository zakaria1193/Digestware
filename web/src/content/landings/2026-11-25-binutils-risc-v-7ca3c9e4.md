---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- binutils
- compression
- assembler
commit_hash: 7ca3c9e43a3437835f1f181b007658264258e938
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Compress RISC-V jr and jalr with zero offset
tldr: Binutils adds compressed instruction forms for RISC-V 'jr' and 'jalr' with explicit
  zero offsets.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit updates the RISC-V assembler in Binutils (`gas`) to recognize
  and generate compressed instruction forms for `jr` and `jalr` when an explicit zero
  offset is provided. It introduces new operand types ('r' for `ra` and 'z' for `x0`)
  and updates `riscv_ip` in `tc-riscv.c` to handle these. Specifically, it adds Zca
  aliases for `jalr` and `jr` to match LLVM's behavior, ensuring that forms like `jalr
  x0, 0(a2)` or `jalr ra, 0(a2)` are compressed to `c.jalr` and `c.jr` respectively.
  This improves code density for jump instructions by leveraging the RISC-V C-extension.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles. It is designed to be simple, modular, and
    extensible, making it popular for embedded systems and custom hardware.
- term: jr
  definition: Jump Register. An instruction that transfers control to a target address
    stored in a register.
- term: jalr
  definition: Jump and Link Register. An instruction that jumps to a target address
    in a register and saves the return address in another register. It's commonly
    used for function calls and returns.
- term: C-extension
  definition: The compressed instruction extension for RISC-V, which provides 16-bit
    instruction encodings for common 32-bit instructions, improving code density.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261125100041.CF555475917D@sourceware.org
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit enhances the RISC-V assembler in Binutils by adding support for compressed instruction forms (C-extension) for `jr` and `jalr` instructions when they involve a zero offset. Previously, the assembler compressed these instructions only in their most basic forms. Now, sequences like `jalr x0, 0(a2)` will correctly map to the compressed `c.jalr` instruction, matching the behavior of LLVM. This improves code density by enabling shorter instruction encodings for common jump operations.
