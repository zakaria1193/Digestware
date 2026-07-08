---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- binutils
- linker
- relocation
- tls
discussion_id: 20260707174719.1883721-2-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v0 1/4] LoongArch: Fix the size of tls desc relocations'
headline: 'LoongArch: Fix the size of TLS descriptor relocations'
tldr: Corrects the size of R_LARCH_TLS_DESC64_* relocations from 8 to 4 bytes in binutils.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Correcting relocation sizes is essential for linker and runtime correctness.
- Ensures compliance with LoongArch ABI specifications for TLS handling.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submits a patch to fix the size of LoongArch TLS descriptor relocations
    from 8 to 4 bytes.
  quote: 'Change the size of R_LARCH_TLS_DESC64_* from 8 to 4.

    ---'
primer_expert: "This patch addresses an incorrect size definition for LoongArch's\
  \ Thread-Local Storage (TLS) descriptor relocations (`R_LARCH_TLS_DESC64_PC_LO20`,\
  \ `R_LARCH_TLS_DESC64_PC_HI12`, `R_LARCH_TLS_DESC64_LO20`, `R_LARCH_TLS_DESC64_HI12`)\
  \ within the binutils `elfxx-loongarch.c` file. The `size` field in the `loongarch_howto_table`\
  \ was \nset to 8, but it should be 4, as these relocations deal with 32-bit offsets\
  \ within a 64-bit TLS descriptor. Rectifying this ensures the assembler and linker\
  \ correctly interpret and process TLS-related references."
primer_glossary:
- term: LoongArch
  definition: A RISC-V-based instruction set architecture developed by Loongson Technology.
- term: TLS
  definition: Thread-Local Storage, a mechanism that allows variables to have distinct
    values for each thread of execution.
- term: relocations
  definition: Information in an object file that describes how to modify addresses
    and references when the code is linked or loaded into memory.
- term: binutils
  definition: A collection of programming tools for creating and managing executable
    programs, including the GNU Assembler (gas) and the GNU Binary File Descriptor
    library (BFD).
- term: R_LARCH_TLS_DESC64_*
  definition: Specific relocation types defined for LoongArch that handle Thread-Local
    Storage descriptor access, likely involving 64-bit addressing or data structures.
- term: elfxx-loongarch.c
  definition: The C source file in binutils responsible for handling ELF object files
    for the LoongArch architecture.
series_id: 'binutils:loongarch: fix the size of tls desc relocations'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-2-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch corrects the size definition for `R_LARCH_TLS_DESC64_*` relocations in the LoongArch binutils backend. Previously, their size was incorrectly set to 8 bytes; this change sets it to the correct value of 4 bytes, ensuring proper handling of Thread-Local Storage descriptor relocations.
