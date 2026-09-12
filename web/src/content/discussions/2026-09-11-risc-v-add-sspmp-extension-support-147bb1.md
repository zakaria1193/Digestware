---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- extension
- memory protection
- csr
discussion_id: 20260911075136.812304-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH] RISC-V: Add Sspmp extension support'
headline: 'RISC-V: Add Sspmp extension support'
tldr: Patch adds minimal support for RISC-V Sspmp, Sspmpen, and Smpmpdeleg extensions
  and their CSRs to binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds support for new RISC-V extensions, enabling developers to utilize advanced
  memory protection features.
- The 'minimal support' indicates that further enhancements might be needed for full
  functionality.
exchanges: []
primer_expert: This patch adds minimal assembler support in binutils for the RISC-V
  Sspmp (Scalar Secure Physical Memory Protection), Sspmpen (Secure Physical Memory
  Protection Enable), and Smpmpdeleg (Secure Physical Memory Protection Delegation)
  extensions. It involves updating BFD to recognize these extensions as implicit subsets
  and modifying GAS to handle the new CSR addresses and definitions, along with adding
  corresponding test suite entries.
primer_glossary:
- term: Sspmp
  definition: RISC-V Scalar Secure Physical Memory Protection extension. It provides
    mechanisms for fine-grained memory protection, particularly for scalar operations.
- term: Sspmpen
  definition: RISC-V Scalar Secure Physical Memory Protection Enable extension. This
    likely relates to enabling or configuring the Sspmp features.
- term: Smpmpdeleg
  definition: RISC-V Secure Physical Memory Protection Delegation extension. This
    extension likely deals with delegating memory protection management responsibilities.
- term: CSR
  definition: Control and Status Register. Special-purpose registers in RISC-V architecture
    used for controlling processor operations and monitoring system status.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles.
- term: BFD
  definition: Binary File Descriptor library, a component of binutils that provides
    a portable interface to object file formats like ELF.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260911075136.812304-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

This patch introduces basic support for the RISC-V Sspmp, Sspmpen, and Smpmpdeleg extensions, along with their associated Control and Status Registers (CSRs). The changes are applied to BFD, GAS, and include new test cases to verify the functionality. The update reflects the specifications found in the RISC-V SPMP extension document.
