---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- assembler
- deprecation
- isa
discussion_id: 20260625143639.3909071-1-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH 0/3] aarch64: deprecate some ISA features'
headline: 'Aarch64: Deprecate some ISA features'
tldr: A three-patch series introduces warnings for deprecated AArch64 ISA features
  (TME, MPAMv2_VID sysregs) in the assembler, aiming for eventual removal of support.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: withdrawn
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Streamlines the toolchain by removing support for unused and unimplemented architectural
  features, reducing complexity.
- Informs developers about deprecated features, preventing the use of non-functional
  instructions and registers.
- Prepares for a cleaner, more focused toolchain in the long term.
- Requires developers to update their code if it relies on these deprecated features.
exchanges: []
primer_expert: This patch series for Binutils' AArch64 target addresses the deprecation
  of unimplemented architectural features. Specifically, it targets the Transactional
  Memory Extension (TME) and certain `mpamv2_vid` system registers, which were part
  of the AArch64 ISA specification but were never realized in actual silicon. The
  changes impact the GNU Assembler (`gas`), primarily `gas/config/tc-aarch64.c` and
  related test suites, to introduce warnings when these features are used. This pre-conditions
  the codebase for the eventual removal of these instruction and register definitions,
  simplifying the `opc…
primer_general: 'This series of three updates to the Binutils software for ARM''s
  64-bit processors (AArch64) is about removing features that were designed but never
  actually put into computer chips. Computer processors have a set of instructions
  they can understand, called an ''Instruction Set Architecture'' (ISA). Sometimes,
  features are planned for an ISA but never implemented in real hardware. This update
  begins the process of telling developers not to use two such features: the ''Transactional
  Memory Extension'' (TME) and some specific ''system registers'' related to memory
  management. The assembler tool will now give warnings if it sees code using these
  features, guiding developers toward more current and supported instructions. Eventually,
  the Binutils tools will completely stop supporting these unused features.'
series_id: 'binutils:aarch64: deprecate some isa features'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260625143639.3909071-1-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion introduces a three-patch series for the AArch64 assembler that aims to deprecate several Instruction Set Architecture (ISA) features that were specified but never implemented in hardware. The initial step is to issue warnings when these features – specifically the Transactional Memory Extension (TME) and certain `mpamv2_vid` system registers – are encountered during assembly. The long-term goal is to completely remove support for these unused features from the Binutils toolchain, with this deprecation acting as the first phase to guide developers away from them. The proposer intends to commit this series within the next week to allow sufficient time before the upcoming branch.
