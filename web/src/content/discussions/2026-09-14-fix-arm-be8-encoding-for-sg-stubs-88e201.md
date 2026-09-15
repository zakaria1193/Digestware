---
project: binutils
subsystem: arm
patch_id: null
tags:
- binutils
- arm
- linker
- encoding
- be8
discussion_id: 20260914121403.499252-1-christophe.lyon@arm.com
source_type: public_inbox
title: '[PATCH] arm: Fix encoding of SG stubs in BE8 mode'
headline: Fix ARM BE8 encoding for SG stubs
tldr: Fixes incorrect byte encoding for ARM Secure Gateway stubs in BE8 mode.
proposer: Christophe Lyon <christophe.lyon@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring correct instruction encoding for security features (CMSE) across different
  endianness modes.
- Integrating security-specific stub handling into the general linker stub processing
  pipeline.
exchanges:
- author: Christophe Lyon <christophe.lyon@arm.com>
  role: proposer
  position: Submits a patch to fix incorrect BE8 encoding of ARM SG stubs by ensuring
    they are processed correctly during the final linking stage.
  quote: 'This patch adds the same handling for cmse_stub_sec, and a new

    testcase which checks the raw encoding of the instructions in the

    veneer.'
primer_expert: This patch targets the ARM support within the binutils linker (`ld`),
  specifically addressing issues with instruction encoding in Big-Endian 8-bit (BE8)
  mode. The problem lies in how Secure Gateway (SG) stubs, which are part of the CMSE
  (Code Musing Security Extension) security feature, are handled. Because they were
  not correctly grouped with other stubs, the linker's final linking pass failed to
  apply the BE8 encoding transformation to their veneers, resulting in incorrect machine
  code. The fix involves ensuring these stubs are processed and encoded correctly,
  with a new test case added for…
primer_glossary:
- term: ARM
  definition: A family of reduced instruction set computing (RISC) architectures for
    processors, widely used in mobile devices and embedded systems.
- term: BE8 mode
  definition: Big-Endian 8-bit mode, a specific endianness and byte ordering used
    in ARM architectures, particularly relevant for instruction encoding.
- term: SG stubs
  definition: Secure Gateway stubs, which are small pieces of code used in ARM's TrustZone
    or CMSE security extensions to mediate calls between secure and non-secure worlds.
- term: CMSE
  definition: Code Musing Security Extension, an ARM security feature that provides
    enhanced protection for software execution environments.
- term: linker
  definition: A program that combines various object files and libraries into a single
    executable file or shared library.
- term: veneer
  definition: In the context of function calls or security mechanisms, a veneer is
    a small piece of code that acts as an intermediary or wrapper to facilitate the
    call or enforce security policies.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260914121403.499252-1-christophe.lyon@arm.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This patch corrects the byte encoding for Secure Gateway (SG) stubs in ARM's Big-Endian 8-bit (BE8) mode within the binutils linker. The issue arises because these veneers are not correctly identified as part of the stub group, preventing the linker from applying the proper BE8 encoding. The fix ensures correct handling for `cmse_stub_sec` and includes a new test case to verify the raw instruction encoding.
