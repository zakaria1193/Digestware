---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- x86
- assembly
- optimization
- AVX
commit_hash: 1f0b25dbcbf4b980474d0a2caa070680a4275700
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: 'x86: Fold F16C templates with AVX512VL counterparts'
tldr: Consolidates F16C instruction templates with AVX512VL, improving assembler logic
  and fixing related issues.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the x86 gas backend's instruction template handling.
  It merges F16C (FP16 Convert) instruction templates with AVX512VL templates, recognizing
  that F16C is not a prerequisite for AVX512F. This aligns the handling with FMA templates
  and corrects a bug where AVX512VL could be enabled without sufficient underlying
  support for F16C, impacting 128/256-bit forms.
primer_glossary:
- term: F16C
  definition: Instruction set extension for x86 that provides efficient conversion
    between 16-bit half-precision and 32-bit single-precision floating-point formats.
- term: AVX512VL
  definition: AVX-512 Vector Length Extensions, which allow AVX-512 instructions to
    operate on 128-bit (XMM) and 256-bit (YMM) registers in addition to 512-bit (ZMM)
    registers.
- term: FMA
  definition: Fused Multiply-Add instruction set extension for x86 processors, which
    combines a multiplication and an addition into a single operation.
- term: 'EVE

    X encoding'
  definition: A form of instruction encoding used by advanced AVX extensions, specifically
    AVX-512, for efficient and compact representation of instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260724063053.C556E4BA2E3B@sourceware.org
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

The assembler now folds F16C instruction templates with their AVX512VL counterparts, similar to FMA templates. This change simplifies the instruction handling logic and resolves an issue where enabling AVX512VL could incorrectly assemble 128- and 256-bit forms even when F16C was not supported.
