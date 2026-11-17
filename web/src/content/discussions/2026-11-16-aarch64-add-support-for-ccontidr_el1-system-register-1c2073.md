---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- gas
- aarch64
- ARM
- system registers
discussion_id: 20261116105226.173996-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH] aarch64: Add support for ccontidr_el1 system register'
headline: 'aarch64: Add support for ccontidr_el1 system register'
tldr: Patch adds support for the read-only aarch64 system register ccontidr_el1, including
  new test cases.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Submits a patch to add support for the ccontidr_el1 system register on
    AArch64.
  quote: Add the read-only ccontidr_el1 system register and a sysreg test that reads
    it. Extend the sysreg-diagnostic test to attempt to write to the register.
primer_expert: This patch adds support for the `ccontidr_el1` system register to the
  AArch64 assembler. This register is part of the ARMv8-A architecture and provides
  information about the implementation-defined behavior of the component used for
  non-secure state management. The changes involve updating the system register definition
  file (`aarch64-sys-regs.def`) and adding new test cases to the gas testsuite to
  verify both reading from and attempting to write to this read-only register.
primer_glossary:
- term: aarch64
  definition: The 64-bit execution state of the ARMv8-A architecture.
- term: system register
  definition: Special-purpose registers in ARM processors that control system functions,
    configuration, and state.
- term: ccontidr_el1
  definition: A specific AArch64 system register related to component identification
    for non-secure state.
- term: GAS
  definition: GNU Assembler. The assembler used in the GNU toolchain, responsible
    for converting assembly language code into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of software.
    In this context, it's for testing the assembler's support for AArch64 system registers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116105226.173996-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch introduces support for the `ccontidr_el1` system register on the AArch64 architecture within the GNU Assembler (GAS). It includes a new test case specifically for reading this register and extends an existing diagnostic test to verify that attempts to write to this read-only register are properly flagged as errors.
