---
project: binutils
subsystem: binutils/loongarch
patch_id: null
tags:
- binutils
- loongarch
- elf
- relocation
discussion_id: 20261030073337.3605-1-zhaozhou@loongson.cn
source_type: public_inbox
title: 'LoongArch: Reject foreign ELF inputs during relocation'
headline: 'LoongArch: Reject foreign ELF inputs during relocation'
tldr: Add a check in binutils to reject non-LoongArch ELF files before processing
  relocations to prevent errors.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds a small overhead for the `is_loongarch_elf` check on every relocation, but
  improves robustness by preventing incorrect processing of foreign objects.
exchanges: []
primer_expert: This patch adds a sanity check in the LoongArch BFD backend's relocation
  handling. It verifies that the input BFD file is indeed a LoongArch ELF object before
  proceeding with relocation, addressing potential issues where unrelated ELF files
  might be passed to the relocation functions.
primer_glossary:
- term: LoongArch
  definition: A RISC instruction set architecture developed by the Loongson Technology
    Corporation.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like operating systems.
- term: Relocation
  definition: The process by which the linker or loader adjusts memory addresses in
    code or data to their final locations in memory. This is necessary for position-independent
    code and linking object files.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to provide
    a common interface for handling various object file formats, including ELF.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261030073337.3605-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch for the LoongArch toolchain in binutils introduces a check to reject ELF files that are not intended for LoongArch architecture. This validation occurs before the relocation processing stage, aiming to prevent potential errors and ensure correct handling of architecture-specific inputs.
