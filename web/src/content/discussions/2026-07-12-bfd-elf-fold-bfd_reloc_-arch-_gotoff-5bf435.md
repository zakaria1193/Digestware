---
project: binutils
subsystem: bfd/elf
patch_id: null
tags:
- binutils
- bfd
- elf
- relocation
- buildfix
discussion_id: alOHg9eSsSjwDLaI@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: bfd/ELF: fold BFD_RELOC_<arch>_GOTOFF*'
headline: 'bfd/ELF: fold BFD_RELOC_<arch>_GOTOFF*'
tldr: Fixes build breakage in frv and lm32 opcode files for binutils.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Corrects issues in opcodes/frv.opc and opcodes/lm32.opc where specific
  BFD_RELOC_FRV_GOTOFF* and BFD_RELOC_LM32_GOTOFF_* constants were not folded into
  the generic BFD_RELOC_LO16_GOTOFF and BFD_RELOC_HI16_GOTOFF constants as intended
  by commit 705b90feb82c. This prevented correct regeneration of opcode files, leading
  to build failures. This patch is backported to the 2.47 branch.
primer_glossary:
- term: bfd/ELF
  definition: Refers to the integration between the Binary File Descriptor (BFD) library
    and the Executable and Linkable Format (ELF) object file format within binutils.
- term: BFD_RELOC_<arch>_GOTOFF*
  definition: Relocation types used by the BFD library to access Global Offset Table
    (GOT) entries, specific to different architectures and addressing modes (e.g.,
    GOTOFFLO, GOTOFFHI).
- term: fold
  definition: In this context, 'fold' means to consolidate or merge multiple similar
    relocation types into a more generic set.
- term: opcodes/
  definition: A directory within binutils that contains files defining instruction
    sets for various architectures, used for generating assembler and disassembler
    code.
- term: 2.47 branch
  definition: A development branch for the upcoming version 2.47 of binutils, typically
    used for bug fixes and release preparations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alOHg9eSsSjwDLaI@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-12'
is_stub: false
stub_reason: ''
---

This patch addresses build breakage in the 'frv' and 'lm32' opcode files that resulted from a previous commit (705b90feb82c). The issue occurred when generated files in 'opcodes/' were re-generated. The fix involves updating relocation constants to standardize them. The changes are being applied to the 2.47 branch.
