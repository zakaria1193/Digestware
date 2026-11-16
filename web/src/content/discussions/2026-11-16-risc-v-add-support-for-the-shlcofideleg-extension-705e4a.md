---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- extension
- interrupts
- patch
discussion_id: 20261116043151.164804-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v2] RISC-V: Add support for the Shlcofideleg extension'
headline: 'RISC-V: Add support for the Shlcofideleg extension'
tldr: Patch adds support for the RISC-V Shlcofideleg extension to binutils, enabling
  delegation of counter-overflow interrupts.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring correct recognition and implication of the Shlcofideleg extension alongside
  the 'H' extension.
exchanges: []
primer_expert: This patch introduces support for the Shlcofideleg extension to the
  RISC-V toolchain within binutils. This extension, part of the RISC-V Privileged
  Specification, enables delegation of performance monitoring counter overflow interrupts
  to a Virtualization Subsystem (VS) mode. The changes are primarily in `bfd/elfxx-riscv.c`
  for ELF recognition and `gas/` for assembler support and testing, specifically noting
  its implication of the 'H' (Hypervisor) extension.
primer_glossary:
- term: Shlcofideleg
  definition: A RISC-V extension that permits delegation of local counter-overflow
    interrupts to Virtualization Subsystem (VS) mode.
- term: VS-mode
  definition: Virtualization Subsystem mode in RISC-V, related to hypervisor functionalities.
- term: H extension
  definition: The RISC-V Hypervisor extension, providing hardware support for virtualization.
- term: BFD
  definition: Binary File Descriptor library, a backend for GNU Binutils that provides
    a common interface to various object file formats.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116043151.164804-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch adds support for the RISC-V Shlcofideleg extension, version 1.0. This extension allows the delegation of local counter-overflow interrupts to VS-mode. The changes include updates to the BFD library to recognize the extension and its dependency on the 'H' extension, as well as modifications to the gas assembler's testsuite to verify implication and support.
