---
project: binutils
subsystem: binutils/gas/risc-v
patch_id: null
tags:
- risc-v
- assembler
- naming-convention
- code-clarity
commit_hash: 5a47f17d1d82edf037e156f921d0c4b3c37fce6a
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: RISC-V `O4` operand descriptor renames to `O7` for clarity.
tldr: Binutils RISC-V assembler's `.insn` operand descriptor `O4` has been renamed
  to `O7` to accurately reflect its 7-bit field size, improving consistency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Within the RISC-V GNU Assembler (GAS), specifically in `gas/config/tc-riscv.c`
  and `opcodes/riscv-opc.c`, the `.insn` directive allows for the direct encoding
  of instructions. Operands like 'O' and 'F' control which fields of the instruction
  are being specified. The 'O4' operand descriptor was previously used to represent
  a 7-bit opcode field. This name was inconsistent with the convention of naming such
  descriptors after their bit-width (e.g., 'F3' for a 3-bit funct3 field). This commit
  renames 'O4' to 'O7' to accurately reflect the 7-bit size of the field it describes,
  improving consistency…
primer_general: When writing assembly code for RISC-V, you can use a special command
  called `.insn` to directly specify the exact bit patterns of an instruction. This
  command uses various codes (like 'O' for opcode fields and 'F' for function fields)
  to tell the assembler which part of the instruction you're defining. Previously,
  there was a code called `O4` which was used for a part of the instruction that actually
  took up 7 bits. This was a bit confusing because `O4` seemed to imply a 4-bit field.
  This change simply renames `O4` to `O7` to accurately reflect that it controls a
  7-bit part of the instruction. This makes the assembly language more consistent
  and easier to understand, especially for toolchain developers, as the name now clearly
  indicates the size of the instruction field it affects.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260605091326.D6F534BCA40C@sourceware.org
date: '2026-06-05'
is_stub: false
---

The RISC-V assembler's `.insn` directive previously used the `O4` operand descriptor to represent a 7-bit field. This descriptor has been renamed to `O7` to align with the field's actual width, consistent with existing `O<n>` and `F<n>` descriptors that denote bit-field sizes. This change improves the clarity and long-term maintainability of the assembler's operand handling.
