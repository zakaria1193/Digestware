---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- AVX
- assembler
- compiler
discussion_id: 0b12f559-3206-4cfe-ae6d-f74035af8473@suse.com
source_type: public_inbox
title: '[PATCH 1/2] x86: correct implied-AVX512VL checking'
headline: 'x86: correct implied-AVX512VL checking'
tldr: Fixes assembler logic that incorrectly bypassed operand size checks for instructions
  implicitly using AVX512VL.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Accurately checking implied CPU features prevents incorrect instruction generation
  but adds complexity to the assembler's parsing logic.
- The fix ensures that instructions requiring AVX512VL are only generated when appropriate,
  preventing potential runtime errors or incorrect behavior.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Submits a patch to correct the handling of implied AVX512VL checks in
    the assembler.
  quote: 'Templates specifying e.g. AVX2|AVX512F (i.e. providing all of AVX2,

    AVX512F, and AVX512VL form(s) at the same time) would presently bypass the

    operand size checking in check_VecOperands(). Both t->cpu and t->cpu_any

    need taking into account.'
primer_expert: This patch addresses a bug in `gas`'s x86 instruction parsing, specifically
  concerning the detection and validation of instructions that implicitly require
  AVX512VL. Previously, the `check_VecOperands` function failed to account for cases
  where AVX512VL was enabled through combinations of `t->cpu` (explicitly set features)
  and `t->cpu_any` (features implied by other features). This could lead to incorrect
  assembly by bypassing necessary checks, potentially allowing instructions to be
  generated with incorrect operand sizes (e.g., YMM/XMM instead of ZMM when AVX512VL
  requires it). The fix ensur…
primer_glossary:
- term: AVX512VL
  definition: AVX-512 Vector Length Extensions, which allow AVX-512 instructions to
    operate on 128-bit (XMM) and 256-bit (YMM) registers, in addition to 512-bit (ZMM)
    registers.
- term: operand size
  definition: The size (e.g., 128-bit, 256-bit, 512-bit) of the data registers used
    by an instruction.
- term: check_VecOperands
  definition: A function within the `gas` assembler that validates the operands of
    vector instructions based on the target CPU features and enabled instruction sets.
- term: t->cpu
  definition: Likely refers to a structure or variable within the assembler's internal
    representation of an instruction template, holding explicitly set CPU features.
- term: t->cpu_any
  definition: Likely refers to a structure or variable within the assembler's internal
    representation of an instruction template, holding CPU features that are implied
    by other features.
- term: instruction template
  definition: A pattern or schema used by an assembler to represent a machine instruction,
    often including variations for different operands or features.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
series_id: 'binutils:x86: correct implied-avx512vl checking'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0b12f559-3206-4cfe-ae6d-f74035af8473@suse.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the GNU assembler's x86 backend where operand size checks for instructions that implicitly use AVX512VL were being bypassed. The `check_VecOperands` function was not correctly considering both `t->cpu` and `t->cpu_any` when determining if AVX512VL was implied. This led to incorrect assembly of instructions that require AVX512VL, even when it wasn't explicitly enabled or when incorrect operand sizes were used. The patch modifies the logic to OR the CPU flags from both `t->cpu` and `t->cpu_any` before ANDing with `avx512`, and also corrects the check for `cpu.bitfield.cpuavx512vl`.
