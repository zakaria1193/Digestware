---
project: binutils
subsystem: binutils
patch_id: null
tags:
- loongarch
- binutils
- linker
- optimization
- compiler
discussion_id: 20260707174719.1883721-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v0 0/4] Emit fewer relocations for linker relaxation'
headline: 'LoongArch: Optimize linker relaxation by emitting fewer relocations'
tldr: A series of patches for LoongArch binutils aims to reduce relocations during
  linker relaxation, improving efficiency.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reducing relocations can improve linker performance and potentially code size.
- These optimizations require careful handling of instruction states and fragment
  boundaries to maintain correctness.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Presents a series of four patches for LoongArch binutils focused on reducing
    relocations during linker relaxation.
  quote: "mengqinggang (4):\n  LoongArch: Fix the size of tls desc relocations\n \
    \ LoongArch: Do not emit relocation if addsy and subsy are in the same\n    frag\n\
    \  LoongArch: Emit fewer relocations for label subtraction\n  LoongArch: Emit\
    \ alignment relocations after relaxed instructions\n\n bfd/elfxx-loongarch.c \
    \                        |   8 +-\ngas/config/tc-loongarch.c                 \
    \    | 230 ++++++++++----\nga…"
primer_expert: 'This is the cover letter for a series of patches submitted by mengqinggang
  that optimize linker relaxation for the LoongArch architecture within binutils.
  The series addresses several aspects: correcting the size of TLS descriptor relocations,
  preventing redundant relocations when `addsy` and `subsy` are in the same fragment,
  reducing relocations for label subtraction by considering relaxed instructions,
  and ensuring alignment relocations are emitted only after relaxed instructions.
  The overarching goal is to minimize the number of relocations the linker needs to
  process for LoongArch targets…'
primer_glossary:
- term: linker relaxation
  definition: A process where the linker adjusts addresses and offsets of code and
    data after initial assembly, often to optimize for space or speed, especially
    in position-independent code.
- term: LoongArch
  definition: A RISC-V-based instruction set architecture developed by Loongson Technology.
- term: binutils
  definition: A collection of programming tools for creating and managing executable
    programs, including the GNU Assembler (gas) and the GNU Binary File Descriptor
    library (BFD).
- term: relocations
  definition: Information in an object file that describes how to modify addresses
    and references when the code is linked or loaded into memory.
- term: TLS
  definition: Thread-Local Storage, a mechanism that allows variables to have distinct
    values for each thread of execution.
- term: frag
  definition: A 'fragment', a basic unit of code or data within an assembler's intermediate
    representation, which eventually forms part of an object file section.
series_id: binutils:emit fewer relocations for linker relaxation
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This is the cover letter for a series of four patches intended to optimize linker relaxation for LoongArch targets within the binutils project. The patches address issues with TLS descriptor relocations, consolidate relaxed instructions, reduce relocations for label subtraction, and refine the emission of alignment relocations, all contributing to fewer generated relocations.
