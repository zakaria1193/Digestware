---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- binutils
- GFNI
- opcodes
- cleanup
discussion_id: 6ac5e152-19c7-46b9-ba08-b359ee3d4ed8@suse.com
source_type: public_inbox
title: '[PATCH] x86: fold left-over GFNI templates'
headline: 'x86: fold left-over GFNI templates'
tldr: Cleans up x86 opcode table by folding unused GFNI instruction templates and
  removing redundant encoding flags.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves code maintainability by cleaning up the opcode table.
- No direct functional change; serves as a minor refactoring.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes cleaning up GFNI instruction templates in the x86 opcode table.
  quote: 'It''s unclear why they weren''t folded back at the time; VEX.W vs EVEX.W

    requirements certainly weren''t getting in the way here.


    While there also drop the redundant EVexDYN from VGF2P8MULB, making all

    three GFNI templates uniform in this regard.'
primer_expert: The opcode table for x86 (`opcodes/i386-opc.tbl`) contains definitions
  for various instruction sets, including GFNI. This patch addresses a minor cleanup
  task by consolidating instruction templates for GFNI instructions, specifically
  `vgf2p8affineinvqb`, `vgf2p8affineqb`, and `vgf2p8mulb`. It removes an outdated
  or redundant encoding flag (`EVexDYN`) and ensures that the templates are more uniformly
  defined, possibly hinting at a previous lack of optimization or a historical inconsistency
  in how these templates were handled.
primer_glossary:
- term: GFNI
  definition: Generational Function Network Interface, a set of Intel instructions
    for accelerating polynomial arithmetic, often used in cryptography and other areas.
- term: AVX
  definition: Advanced Vector Extensions, a set of SIMD instructions for x86 processors
    that increase performance for floating-point and integer operations.
- term: AVX512F
  definition: The foundational subset of the AVX-512 instruction set, introducing
    512-bit vector registers and operations.
- term: VEX
  definition: Vector Extension, a prefix used in x86 instruction encoding to support
    wider vector registers (e.g., 128-bit, 256-bit) and new instructions.
- term: EVEX
  definition: Another prefix used for encoding instructions, primarily associated
    with AVX-512, offering more features and flexibility than VEX.
- term: opcode table
  definition: A data structure used by assemblers and disassemblers to map mnemonic
    instruction names to their corresponding machine code byte sequences.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/6ac5e152-19c7-46b9-ba08-b359ee3d4ed8@suse.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch refactors the x86 opcode table (`opcodes/i386-opc.tbl`) by folding unused Generational Function Network Interface (GFNI) instruction templates. It removes the redundant `EVexDYN` flag from the `VGF2P8MULB` instruction and ensures consistency across GFNI templates. This cleanup aims to streamline the opcode definitions and potentially improve assembly efficiency.
