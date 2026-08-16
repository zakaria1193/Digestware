---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- AVX512
- warnings
- instruction encoding
discussion_id: dcc5f9ab-6f1f-465f-8c55-5643f740b372@suse.com
source_type: public_inbox
title: '[PATCH] x86: emit warnings to avoid potential encoding surprises'
headline: 'x86: emit warnings to avoid potential encoding surprises'
tldr: Adds warnings for x86 instructions that might silently fall back to unintended
  encodings (e.g., AVX512VL) when specific features are disabled.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves safety by warning users about potential unintended instruction encodings.
- Adds complexity to the assembler's instruction selection logic.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes adding warnings to the x86 assembler to prevent silent fallbacks
    to unintended instruction encodings.
  quote: 'FMA and F16C insns have direct AVX512VL counterparts. If the respective
    of

    the two features is disabled, we''d silently fall back to the corresponding

    EVEX encoding, which may not be intended by the user (their code may, for

    example, not be AVX512-aware at all). See also [1], [2].'
primer_expert: The x86 assembler (`gas`) is being updated to issue warnings when instructions
  with direct AVX512VL encodings (like FMA, F16C, VNNI, CRC32) are encountered but
  the necessary AVX512VL feature is not explicitly enabled. Currently, `gas` might
  silently fall back to a more general EVEX encoding, which could lead to program
  misbehavior if the code is not AVX512VL-aware. This patch modifies `install_template`
  in `tc-i386.c` to detect and warn about these fallback scenarios.
primer_glossary:
- term: FMA
  definition: Fused Multiply-Add, an instruction set extension that combines multiplication
    and addition operations.
- term: F16C
  definition: Half-precision floating-point conversion instructions.
- term: AVX512VL
  definition: AVX-512 Vector Length Extensions, which allow AVX-512 instructions to
    operate on 128-bit and 256-bit vectors in addition to 512-bit vectors.
- term: EVEX
  definition: An encoding scheme used for AVX-512 instructions, providing extended
    capabilities and more flexible operand access.
- term: VNNI
  definition: Vector Neural Network Instructions, a set of instructions designed to
    accelerate deep learning workloads.
- term: CRC32
  definition: Cyclic Redundancy Check, an error-detecting code; the patch refers to
    specific instructions for computing CRC32.
- term: encoding surprises
  definition: Situations where an instruction is compiled or assembled into a different
    machine code encoding than the user might expect, potentially due to feature flag
    interactions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/dcc5f9ab-6f1f-465f-8c55-5643f740b372@suse.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch introduces warnings in the x86 assembler to alert users when certain instructions might silently fall back to less-specific or unintended encodings. This occurs when newer ISA extensions (like AVX512VL for FMA and F16C, or VNNI and CRC32 variants) are implicitly selected due to feature flags, potentially leading to unexpected behavior if the user's code is not aware of these extensions. The changes ensure that users are notified of these potential encoding surprises, particularly when using `.arch .no*` directives or when newer ISA extensions are not explicitly enabled.
