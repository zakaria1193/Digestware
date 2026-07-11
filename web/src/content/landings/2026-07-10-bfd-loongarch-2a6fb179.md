---
project: binutils
subsystem: bfd/loongarch
patch_id: null
tags:
- loongarch
- bfd
- relocations
- tls
commit_hash: 2a6fb1798b6a81d57985494bba284239505a23ff
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Correct size for TLS DESC64 relocations'
tldr: Fixes LoongArch TLS DESC64 relocation sizes from 8 bytes to 4 bytes for improved
  accuracy.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `bfd/elfxx-loongarch.c`, the `loongarch_howto_table` is updated
  to fix the `size` field for several `R_LARCH_TLS_DESC64_*` relocation types (specifically
  `_PC_LO20`, `_PC_HI12`, `_LO20`, and `_HI12`). The size has been changed from `8`
  to `4`. This corrects an erroneous definition that likely stemmed from assuming
  a 64-bit value when a smaller, 32-bit field was intended for these specific TLS
  descriptor access calculations, ensuring the BFD backend aligns with the actual
  instruction encoding.
primer_glossary:
- term: R_LARCH_TLS_DESC64_*
  definition: LoongArch-specific relocation types used for accessing Thread-Local
    Storage (TLS) descriptors. The 'DESC64' indicates a 64-bit variant, and the trailing
    parts specify the type of offset (e.g., PC-relative).
- term: TLS (Thread-Local Storage)
  definition: A memory model where each thread in a program gets its own private copy
    of a variable. Toolchains generate special relocations to manage access to these
    thread-specific variables.
- term: Relocation Size
  definition: In the context of ELF relocations, this refers to the number of bits
    (e.g., 32 or 64) that the relocation value will occupy in the target instruction
    or data field.
- term: BFD (Binary File Descriptor)
  definition: A library within the GNU toolchain that provides a unified interface
    for reading and writing various binary file formats, including object files and
    executables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260710070137.C73CA4BA5435@sourceware.org
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This commit corrects the size specification for LoongArch's `R_LARCH_TLS_DESC64_*` relocations in the BFD library. Previously, these relocations were incorrectly defined as 8 bytes in size. This change rectifies the size to 4 bytes, ensuring that the assembler and linker handle these specific Thread-Local Storage descriptor relocations accurately, which is crucial for correct program execution.
