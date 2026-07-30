---
project: binutils
subsystem: binutils/gas,binutils/bfd
patch_id: null
tags:
- x86
- relocation
- gas
- bfd
- plt
commit_hash: 53902b30c66ad5edc95db93e8d5c1cb3c29d684d
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: 'x86: Support PLT32 relocation for AT&T syntax directives'
tldr: Binutils now supports LLVM-style AT&T syntax for generating PC-relative PLT
  relocations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces support for the `BFD_RELOC_386_PC32_TO_PLT32`
  and `BFD_RELOC_X86_64_PC32_TO_PLT32` relocation types to GAS and BFD. It allows
  GAS to generate these new relocation types for directives like ".long foo@PLT -
  .L4", which LLVM already supported. BFD's relocation handling and x86/x86-64 specific
  code are updated to correctly compute the addend for these relocations, addressing
  PR gas/34423.
primer_glossary:
- term: PLT32 relocation
  definition: A specific type of relocation used on x86 architectures where a 32-bit
    value needs to be calculated relative to the Program Counter (PC) and is intended
    for use with the Procedure Linkage Table (PLT). It's used for indirect function
    calls.
- term: PC32 relocation
  definition: A 32-bit relocation where the target address is calculated relative
    to the current Program Counter (PC). This is common for position-independent code.
- term: AT&T syntax
  definition: An assembly language syntax convention, commonly used by the GNU Assembler
    (gas), distinguishable by operand order (source, destination) and the use of '%'
    for registers and '$' for immediate values.
- term: LLVM assembler
  definition: The assembler component of the LLVM compiler infrastructure, which supports
    various assembly syntaxes and features.
- term: BFD
  definition: Binary Descriptor format, a library within GNU Binutils for handling
    various object file formats.
- term: GAS
  definition: GNU Assembler, the assembler used by the GCC toolchain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260729214435.C53064BB5912@sourceware.org
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

Binutils has gained support for generating PLT32 relocations from AT&T assembly syntax directives, mirroring a feature previously supported by LLVM. This change enables the use of constructs like ".long foo@PLT - .L4", allowing the assembler and linker to correctly resolve PC32 (Program Counter Relative 32-bit) relocations against function symbols by using the PLT. This improves compatibility and optimization options for x86 and x86-64 targets.
