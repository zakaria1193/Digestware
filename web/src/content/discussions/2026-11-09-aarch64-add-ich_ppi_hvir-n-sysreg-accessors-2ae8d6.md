---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembly
- disassembler
- system-registers
discussion_id: 5a335a48-3ede-7bb3-707d-b75460ad155c@e124511.cambridge.arm.com
source_type: public_inbox
title: '[committed] aarch64: Add ICH_PPI_HVIR<n> sysreg accessors'
headline: 'aarch64: Add ICH_PPI_HVIR<n> sysreg accessors'
tldr: Adds assembler and disassembler support for new AArch64 system registers related
  to interrupt controllers.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Keeps the assembler and disassembler up-to-date with the latest AArch64 architecture
  features.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Submitted a patch to add system register accessors for ICH_PPI_HVIR<n>.
  quote: 'These system registers were added retrospectively to FEAT_GCIE in the

    2026-03 release of the Arm A-Profile Architecture Registers.'
primer_expert: This patch extends the AArch64 assembler and disassembler to recognize
  and handle the ICH_PPI_HVIR0_EL2 and ICH_PPI_HVIR1_EL2 system registers. These registers
  are associated with the FEAT_GCIE feature and were recently added to the architecture
  specification. The changes involve updating the testsuite (`gcie-sysregs.d`, `gcie-sysregs.s`)
  and the opcode definition file (`aarch64-sys-regs.def`).
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: system registers
  definition: Special-purpose registers in ARM processors used for configuration,
    control, and status of system-level features, such as interrupt handling.
- term: ICH_PPI_HVIR<n>
  definition: Interrupt Controller Host Virtual Interrupt Registers. These are AArch64
    system registers used for interrupt management in virtualized environments.
- term: FEAT_GCIE
  definition: Generic Control Interrupt Enable. An AArch64 architecture feature related
    to interrupt handling.
- term: assembler
  definition: A program that translates assembly language code into machine code.
- term: disassembler
  definition: A program that translates machine code back into assembly language.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/5a335a48-3ede-7bb3-707d-b75460ad155c@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This committed patch adds support for accessing the ICH_PPI_HVIR<n> system registers in the AArch64 assembler and disassembler. These registers were retrospectively added to the FEAT_GCIE feature in the March 2026 update of the Arm Architecture Registers. The changes include updates to test suite definitions and the system register definition file.
