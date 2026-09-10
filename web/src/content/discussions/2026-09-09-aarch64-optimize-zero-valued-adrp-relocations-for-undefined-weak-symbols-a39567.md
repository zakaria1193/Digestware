---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- AArch64
- binutils
- linker
- optimization
- relocations
discussion_id: 20260909160555.66067-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] AArch64: Optimize zero-valued ADRP relocations for undefined weak
  symbols'
headline: 'AArch64: Optimize zero-valued ADRP relocations for undefined weak symbols'
tldr: Optimizes zero-valued ADRP relocations for undefined weak symbols on AArch64
  by rewriting them as MOVZ, also addressing Cortex-A53 erratum 843419.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves code size and potentially performance by replacing ADRP with MOVZ.
- Adds complexity to handle errata and `--no-relax` flag.
exchanges: []
primer_expert: The AArch64 ELF loader permits ADRP (Add upper address, page) relocations
  against undefined weak symbols to be emitted as a MOV instruction with a zero immediate.
  This patch optimizes this by rewriting such ADRP instructions as MOVZ (Move immediate,
  zero-extended) when the page value is zero. This is particularly relevant for code
  generation on AArch64, where instruction encoding size and runtime performance are
  critical. The patch also handles a specific CPU erratum (Cortex-A53 erratum 843419)
  that is triggered by ADRP instructions in certain contexts.
primer_glossary:
- term: ADRP
  definition: Add upper address, page. An AArch64 instruction used to set the high
    bits of an address, typically for position-independent code.
- term: RELOCATIONS
  definition: Information in an object file that describes how to modify addresses
    when linking or loading.
- term: UNDEFINED WEAK SYMBOLS
  definition: Symbols that are declared weak (meaning they can be overridden by a
    non-weak symbol) and have no definition provided, acting as placeholders.
- term: MOVZ
  definition: Move immediate, zero-extended. An AArch64 instruction that moves an
    immediate value into a register, zero-extending it.
- term: --no-relax
  definition: A linker option that prevents the linker from adjusting certain relocation
    values, preserving their original form.
- term: Cortex-A53 erratum 843419
  definition: A specific hardware bug in the Cortex-A53 processor that affects ADRP
    instructions in certain scenarios.
- term: LP64
  definition: A data model where `long` and pointers are 64 bits wide, and `int` is
    32 bits. Common on 64-bit Unix-like systems.
- term: ILP32
  definition: A data model where `int`, `long`, and pointers are all 32 bits wide.
    It is a subset of LP64 and is used on some 64-bit architectures to maintain compatibility.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260909160555.66067-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

This patch introduces an optimization for AArch64 by rewriting zero-valued ADRP relocations targeting undefined weak symbols as MOVZ instructions. This optimization preserves the destination register and honors the `--no-relax` flag. Additionally, it addresses a Cortex-A53 erratum 843419 by clearing pending entries when an ADRP is rewritten. The change includes new test cases for LP64 and ILP32 modes.
