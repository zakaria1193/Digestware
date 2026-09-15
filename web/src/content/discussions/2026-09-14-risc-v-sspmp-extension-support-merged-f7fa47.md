---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- extension
- sspmp
- merged
discussion_id: CA+yXCZB-jBbKPT51E-aAufNRVu=Ga7kO+a_c6QAwHD7CmmNSCA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add Sspmp extension support'
headline: RISC-V Sspmp extension support merged
tldr: Patch adding RISC-V Sspmp extension support has been merged.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: proposer
  position: Announces that the patch for RISC-V Sspmp extension support has been merged
    after a minor format correction.
  quote: Thanks, pushed with minor format fix :)
primer_expert: This is a brief status update regarding a patch that adds support for
  the RISC-V Supervisor Protection Memory (Sspmp) extension, along with its related
  `Sspmpen` and `Smpmpdeleg` extensions, and their associated Control and Status Registers
  (CSRs). The change has been merged into the `binutils` project, affecting components
  like BFD (for ELF handling) and GAS (for assembly syntax and CSR recognition).
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that allows for flexible
    and customizable processor designs.
- term: Sspmp
  definition: Supervisor Protection Memory, a RISC-V extension focused on memory protection
    mechanisms for the supervisor mode.
- term: CSR
  definition: Control and Status Register. Special registers in a processor used for
    controlling its operation and monitoring its status.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface within binutils
    for handling various object file formats.
- term: GAS
  definition: GNU Assembler, part of the binutils package, responsible for assembling
    assembly language code into machine code.
- term: Smpmpdeleg
  definition: A RISC-V extension related to delegation of protection or memory management
    responsibilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZB-jBbKPT51E-aAufNRVu=Ga7kO+a_c6QAwHD7CmmNSCA@mail.gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

Kito Cheng announces that the patch for adding support for RISC-V Sspmp, Sspmpen, and Smpmpdeleg extensions, including their CSRs, has been pushed. A minor format fix was applied before merging. The patch updates BFD and GAS components to recognize these new extensions and their associated Control and Status Registers (CSRs).
