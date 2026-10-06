---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- plt
- abi
discussion_id: 20261005104458.2633975-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Update the unlabeled landing pad PLT to the latest psABI'
headline: 'RISC-V: Update the unlabeled landing pad PLT to the latest psABI'
tldr: Update the RISC-V assembler's PLT generation to match the latest psABI for improved
  compatibility and efficiency.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Minor code size reduction in PLT header.
- Alignment with evolving psABI standards.
exchanges: []
primer_expert: This change modifies the `bfd/elfnn-riscv.c` file to align the PLT
  (Procedure Linkage Table) generation for RISC-V with the latest psABI. Specifically,
  it updates the `PLT_ZICFILP_UNLABELED_HEADER_INSNS` to 8 from 12 and adjusts register
  usage and header structure. This impacts how dynamically linked code is resolved
  on RISC-V targets, particularly when using the Zicfilp extension, aiming for a more
  efficient and standard-compliant implementation.
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to indirect calls to shared libraries.
- term: psABI
  definition: Processor Specification Application Binary Interface. Defines standard
    ABI conventions for a given processor architecture, ensuring binary compatibility.
- term: Zicfilp
  definition: A RIS-V extension that provides support for filtered loads and stores,
    impacting memory access and potentially branches.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005104458.2633975-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch updates the RISC-V assembler's handling of the unlabeled landing pad PLT to align with the latest Processor Specification ABI (psABI). The changes involve using register t2 instead of t3 in PLT entries and swapping t2 and t3 in the PLT header. Additionally, the PLT header no longer starts with a landing pad and its size is reduced by removing trailing nops, bringing it to 32 bytes. These modifications are backward compatible as the linker generates the PLT.
