---
project: binutils
subsystem: gas/aarch64
patch_id: null
tags:
- binutils
- gas
- aarch64
- arm
- assembly
discussion_id: ausVpH7bXbomucU-@D2G2X7XGD1
source_type: public_inbox
title: 'gas/aarch64: Allow movprfx with bfmmla, sve-f16mm fmmla'
headline: 'gas/aarch64: Allow movprfx with bfmmla, sve-f16mm fmmla'
tldr: Patch is pushed; previously incorrectly disallowed movprfx with specific aarch64
  fmmla instructions.
proposer: Ezra Sitorus <ezra.sitorus@arm.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Ezra Sitorus <ezra.sitorus@arm.com>
  role: proposer
  position: Confirms that the patch has been pushed, which corrects an error in allowing
    `movprfx` with certain aarch64 floating-point instructions.
  quote: Pushed - thanks!
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: reviewer
  position: Acknowledges the correction and notes a recurring pattern of similar mistakes
    with new instructions.
  quote: 'Oops - ok, thanks!


    (I''m getting a sense of d�j� vu here - because it seems we made the same

    mistake with new b?mmla instructions two years running.  I''ll have to keep an

    eye out for that next year.)'
primer_expert: This patch corrects an opcode table entry in the GNU Assembler for
  the aarch64 architecture. Specifically, it allows the `movprfx` instruction to precede
  certain matrix multiply-accumulate instructions (`bfmmla`, `sve-f16mm fmmla`) which
  were incorrectly marked as incompatible. The `movprfx` instruction is a prefix that
  enables specific behaviors for subsequent instructions, and its incorrect restriction
  would have prevented valid instruction sequences.
primer_glossary:
- term: movprfx
  definition: A prefix instruction in ARM's A64 instruction set that modifies the
    behavior of the immediately following instruction, often related to vector processing
    or special operations.
- term: fmmla
  definition: Floating-point Matrix Multiply-Accumulate instruction, used for high-performance
    numerical computations.
- term: bfmmla
  definition: A specific type of fmmla instruction in ARM's SVE2 (Scalable Vector
    Extension) that operates on BFloat16 data types.
- term: sve-f16mm
  definition: Refers to SVE2 instructions for fmmla operations using 16-bit floating-point
    (FP16) data types.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set.
- term: gas
  definition: GNU Assembler, the assembler used by the GCC compiler toolchain.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ausVpH7bXbomucU-@D2G2X7XGD1
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This short thread confirms that a patch allowing the `movprfx` instruction to be used with specific aarch64 floating-point matrix multiply-accumulate (fmmla) instructions has been pushed. The instructions `bfmmla` and `sve-f16mm fmmla` were previously marked as not accepting `movprfx`, which was an error. The patch corrects this and adds corresponding test cases.
