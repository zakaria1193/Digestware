---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- MIPS
- microMIPS
- ISA mode
discussion_id: 20261124115136.1725483-2-luolongjuna@gmail.com
source_type: public_inbox
title: '[PATCH 1/2] gas: Keep the ISA bit for a local alias of a weak microMIPS function'
headline: 'gas: Keep the ISA bit for a local alias of a weak microMIPS function'
tldr: Preserves ISA mode in weak microMIPS function aliases to prevent illegal instruction
  exceptions.
proposer: Longjun Luo <luolongjuna@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds specific handling for microMIPS ISA mode preservation, increasing code complexity.
- Ensures correctness for a niche but critical case of weak function aliasing.
exchanges: []
primer_expert: This patch modifies `gas/config/tc-mips.c` to prevent the loss of ISA
  mode (Thumb/microMIPS) information stored in `st_other` for weak function aliases.
  Previously, when a relocation against such an alias was reduced to a section symbol,
  the ISA mode was lost. This change ensures that if the symbol's value doesn't inherently
  carry the ISA mode (i.e., the lowest bit is not used for it), the relocation must
  be kept to preserve the mode information from `st_other`. This is crucial for correct
  execution of microMIPS code via these aliases.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project, which translates
    assembly language code into machine code.
- term: ISA mode
  definition: Instruction Set Architecture mode, referring to different operational
    modes of a processor, such as ARM's Thumb mode for 16-bit instructions or MIPS's
    microMIPS mode.
- term: Relocation
  definition: A process performed by the linker to adjust addresses in machine code
    or data sections to reflect the final memory layout of the program.
- term: Section symbol
  definition: A symbol that represents an entire section of code or data within an
    object file.
- term: microMIPS
  definition: A compact instruction set architecture variant of MIPS, designed for
    smaller embedded systems, which uses the least significant bit of addresses to
    distinguish between MIPS16/microMIPS and standard MIPS modes.
series_id: 'binutils:gas: keep the isa bit for a local alias of a weak micromips function'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124115136.1725483-2-luolongjuna@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in GAS where the ISA mode of a weak microMIPS function's local alias could be lost when a relocation is reduced to a section symbol. This loss of mode information can lead to illegal instruction exceptions when calling through the alias. The fix ensures that the ISA mode is preserved, maintaining correct execution for microMIPS functions under these specific conditions.
