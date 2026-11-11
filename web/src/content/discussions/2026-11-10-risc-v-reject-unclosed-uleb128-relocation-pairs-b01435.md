---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- ABI compliance
- relocation
discussion_id: 20261110201522.2149977-5-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 4/5] RISC-V: reject unclosed ULEB128 relocation pairs'
headline: 'RISC-V: reject unclosed ULEB128 relocation pairs'
tldr: Enforces RISC-V psABI by rejecting linker inputs with unclosed R_RISCV_SET_ULEB128
  relocations.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enforces stricter ABI compliance, potentially causing builds to fail if older toolchains
  produced malformed relocation pairs, but improves correctness.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Adds a check to detect and reject trailing, unclosed R_RISCV_SET_ULEB128
    relocations in RISC-V object files to comply with the psABI.
  quote: 'The RISC-V psABI requires each R_RISCV_SET_ULEB128 relocation to pair

    with an R_RISCV_SUB_ULEB128 relocation at the same offset.  Previously,

    the linker silently ignored an unclosed SET relocation at section end.


    Check whether a SET relocation remains open after the relocation loop

    completes.  If uleb128_set_rel is non-NULL, report an error to enforce

    psABI pairing rules.'
primer_expert: This patch enforces a specific pairing rule from the RISC-V psABI concerning
  ULEB128 encoded relocations. It modifies `riscv_elf_relocate_section` to detect
  and error out on `R_RISCV_SET_ULEB128` relocations that do not have a corresponding
  `R_RISCV_SUB_ULEB128` at the same location, preventing silent failures where the
  linker would previously ignore such unmatched relocations.
primer_glossary:
- term: psABI
  definition: The Application Binary Interface for the specific architecture and operating
    system. For RISC-V, it defines conventions for how software is compiled and linked.
- term: R_RISCV_SET_ULEB128
  definition: A RISC-V relocation type used in conjunction with R_RISCV_SUB_ULEB128
    to encode variable-length unsigned integers.
- term: R_RISCV_SUB_ULEB128
  definition: A RISC-V relocation type used in conjunction with R_RISCV_SET_ULEB128
    to encode variable-length unsigned integers.
- term: ULEB128
  definition: Unsigned LEB128 (Little-Endian Base 128) is a variable-length encoding
    format for integers, commonly used in DWARF debugging information and some ABIs.
series_id: 'binutils:risc-v: reject unclosed uleb128 relocation pairs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-5-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch enforces the RISC-V psABI requirement that `R_RISCV_SET_ULEB128` relocations must be paired with `R_RISCV_SUB_ULEB128` relocations at the same offset. Previously, unclosed SET relocations at the end of a section were silently ignored. The change adds a check after the relocation loop to detect and report an error if a `SET` relocation remains open, ensuring ABI compliance.
