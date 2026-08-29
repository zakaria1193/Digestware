---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- compiler-options
discussion_id: 20260827151014.9719-4-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH 3/7] aarch64: add pauth-lr feature option'
headline: 'aarch64: add pauth-lr feature option'
tldr: Introduces a new '+pauth-lr' feature option for AArch64, dependent on '+pauth',
  to control PAuth_LR instructions.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new feature flag that increases the complexity of target feature management
  but provides finer-grained control over instruction set usage.
exchanges: []
primer_expert: This patch introduces a new CPU feature flag, `+pauth-lr`, to the AArch64
  target configuration in binutils. This flag controls the availability of instructions
  associated with the FEAT_PAuth_LR extension. The `+pauth-lr` option is defined to
  implicitly depend on the `+pauth` feature, ensuring that the necessary base Pointer
  Authentication features are enabled before PAuth_LR specific instructions can be
  used. This is a standard practice for managing hardware feature extensions in toolchains.
  The change is made in `gas/config/tc-aarch64.c`, `include/opcode/aarch64.h`, and
  `opcodes/aarch64-tbl.…
primer_glossary:
- term: feature option
  definition: A compiler or assembler flag (e.g., `+pauth-lr`) that enables or disables
    support for specific hardware features or instruction sets.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: FEAT_PAuth_LR
  definition: A specific AArch64 hardware feature extension for Pointer Authentication
    of the Link Register.
- term: +pauth
  definition: A feature flag indicating support for the base Pointer Authentication
    (PAuth) extension in AArch64.
- term: +pauth-lr
  definition: A feature flag indicating support for the Pointer Authentication extension
    specifically for the Link Register (PAuth_LR) in AArch64. It depends on the +pauth
    feature.
series_id: 'binutils:aarch64: add pauth-lr feature option'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827151014.9719-4-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch adds a new compiler/assembler feature option, `+pauth-lr`, for the AArch64 architecture. This option is specifically designed to gate the use of FEAT_PAuth_LR instructions. It is dependent on the existing `+pauth` feature, meaning `+pauth-lr` can only be enabled if `+pauth` is also enabled. This mechanism allows developers to selectively enable or disable these security-related instructions.
