---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- opcode
- operand descriptor
- consistency
discussion_id: 971a7d74-1e80-4958-8942-d7ec75263087@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH v2 01/16] RISC-V: rename operand descriptor O4'
headline: 'RISC-V: rename operand descriptor O4'
tldr: Renames the RISC-V operand descriptor `O4` to `O7` for consistency, as it describes
  a 7-bit field.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improved code readability and maintainability at the cost of a simple renaming change.
exchanges: []
primer_expert: This patch modifies the RISC-V opcode definitions in `gas/config/tc-riscv.c`
  and `opcodes/riscv-opc.c`.  Operand descriptors define the format of operands in
  RISC-V assembly instructions. The change ensures consistency in naming operand descriptors
  that represent bit fields.
primer_general: In computer architecture, opcodes (operation codes) are instructions
  that tell the CPU what to do.  Assemblers use operand descriptors to define the
  format, size and location of instruction arguments.  This patch renames an operand
  descriptor in the RISC-V architecture's assembly definition to better reflect the
  size of the opcode field it describes, improving code clarity and maintainability.
series_id: 'binutils:risc-v: rename operand descriptor o4'
series_role: reply
series_parts:
- title: 'RISC-V: rename operand descriptor O4'
  url: https://inbox.sourceware.org/binutils/25ba2a4c-a254-4276-b03a-aae99d5b9eb1@suse.com
  n: 1
  total: 16
url: https://inbox.sourceware.org/binutils/971a7d74-1e80-4958-8942-d7ec75263087@iscas.ac.cn
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch renames the RISC-V operand descriptor `O4` to `O7` to better reflect that it represents a 7-bit opcode field. The renaming improves consistency with other operand descriptors (`O<n>` and `F<n>`). This change simplifies subsequent code modifications. Reviewers have indicated that the patch looks good.
