---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- disassembler
- endianness
- bugfix
commit_hash: f4ccf01a9652ece6c16620630cbdce04ab2373fa
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Fix disassembly on big-endian hosts'
tldr: Corrects LoongArch instruction decoding on big-endian systems.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `print_insn_loongarch` function directly read a 4-byte instruction
  into an `insn_t` (assumed `uint32_t`). On big-endian hosts, this performed an implicit
  byte swap. The fix introduces a `bfd_byte` buffer and uses `bfd_getl32()` to read
  the instruction, ensuring correct interpretation regardless of host endianness.
  This resolves `binutils`, `gas`, and `ld` test failures on big-endian platforms
  like `s390x`.
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA (Reduced Instruction Set Computer Instruction Set Architecture)
    developed in China, used in servers, desktops, and embedded systems.
- term: big-endian
  definition: A computer architecture where the most significant byte of a multi-byte
    word is stored at the lowest memory address. This is in contrast to little-endian.
- term: disassembler
  definition: A program that translates machine code (binary instructions) back into
    human-readable assembly language.
- term: bfd_getl32
  definition: A function from the BFD library that reads a 32-bit value from memory,
    interpreting it as little-endian, irrespective of the host system's endianness.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261009081510.0963E4BA5433@sourceware.org
date: '2026-10-09'
is_stub: false
stub_reason: ''
---

The LoongArch disassembler incorrectly read 4-byte instruction words directly into a `uint32_t` on big-endian hosts. This resulted in byte-swapped instructions, causing all subsequent decoding to fail. The fix reads the instruction into a byte buffer and uses `bfd_getl32` to ensure it's interpreted in little-endian order, regardless of the host's endianness, resolving test failures observed on `s390x`.
