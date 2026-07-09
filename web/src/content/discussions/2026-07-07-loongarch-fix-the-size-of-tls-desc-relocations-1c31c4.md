---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- LoongArch
- linker
- TLS
- relocations
discussion_id: 20260707174719.1883721-2-mengqinggang@loongson.cn
source_type: public_inbox
title: 'LoongArch: Fix the size of tls desc relocations'
headline: 'LoongArch: Fix the size of tls desc relocations'
tldr: Adjusts relocation sizes for LoongArch TLS descriptors from 8 to 4 bytes.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correctly represents TLS descriptor sizes, potentially enabling smaller code or
  data footprints.
- Ensures ABI compatibility by adhering to the correct relocation encoding.
exchanges: []
primer_expert: This patch modifies the BFD (as in Binary File Descriptor) library's
  ELF definitions for LoongArch. Specifically, it changes the size field associated
  with TLS descriptor relocation types (R_LARCH_TLS_DESC64_{PC_LO20, PC_HI12, LO20,
  HI12}) from 8 to 4. This is a common adjustment when the actual number of bits encoded
  in the relocation is smaller than initially assumed or a more compact representation
  is deemed correct.
primer_glossary:
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows variables to have unique
    instances per thread, managed by the runtime library.
- term: relocation
  definition: Information in an object file that describes how to modify code or data
    after linking, typically to resolve symbol addresses or other layout-dependent
    values. In ELF, these are represented by types like R_LARCH_TLS_DESC64_*.
- term: linker relaxation
  definition: A linker optimization where it analyzes instruction sequences and adjusts
    addresses or instruction forms to reduce code size or improve performance, often
    involving the generation and resolution of relocations.
- term: BFD
  definition: Binary File Descriptor library. A GNU project library that provides
    a common interface to various object file formats, including ELF.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, and shared libraries on many Unix-like systems.
- term: R_LARCH_TLS_DESC64_*
  definition: Specific relocation types for the LoongArch architecture related to
    Thread-Local Storage descriptors, indicating how to calculate an offset or address
    for TLS data.
series_id: 'binutils:loongarch: fix the size of tls desc relocations'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-2-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch corrects the size of R_LARCH_TLS_DESC64_* relocations for the LoongArch architecture from 8 bytes to 4 bytes. This change is part of a larger series aimed at optimizing linker relaxation.
