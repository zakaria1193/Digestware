---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- Zvabd
- extension
- binutils
- assembler
discussion_id: 449a3875-1e31-4fb0-9d1f-f54e63d99ef6@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add experimental support for Zvabd extension'
headline: 'RISC-V: Add experimental support for Zvabd extension'
tldr: Jiawei will update the binutils patch for the Zvabd extension, which is now
  in Freeze, after renaming the mnemonic.
proposer: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
  role: other
  position: Thanks Jiawei for picking this up.
  quote: Thanks a ton!
primer_expert: The RISC-V Zvabd extension adds instructions for dealing with bfloat16
  floating-point numbers. This patch series updates binutils to support the new instructions
  and mnemonics. The patch will primarily affect `opcodes/riscv-opc.c` and the gas
  assembler.
primer_general: The RISC-V architecture is modular, allowing for various extensions
  to be added to the base instruction set. These extensions provide additional functionality,
  such as specialized instructions for floating-point arithmetic or cryptography.
  Supporting these extensions in binutils (the GNU assembler, linker, and related
  tools) involves updating the assembler to recognize the new instructions and generate
  the appropriate machine code.  This allows developers to use the new instructions
  in their programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/449a3875-1e31-4fb0-9d1f-f54e63d99ef6@oss.qualcomm.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

Jiawei is picking up Zhongyao's work to add experimental support for the RISC-V Zvabd extension in binutils. The Zvabd extension specification is now in Freeze, and the only remaining change is a mnemonic rename. Jiawei will refresh the binutils patch and update it against the current specification, including opcodes, gas changes, and tests.
