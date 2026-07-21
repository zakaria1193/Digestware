---
project: binutils
subsystem: avr
patch_id: null
tags:
- avr
- linker
- optimization
- code locality
discussion_id: 8f89fd03-7fa2-4c2d-a0fe-b4e99d5b2f12@gjlay.de
source_type: public_inbox
title: '[patch] AVR: Sort .text.* input sections by their name.'
headline: 'AVR: Sort .text.* input sections by their name.'
tldr: Patch to sort AVR .text.* input sections by name to improve code locality.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Potential minor increase in link time due to sorting.
exchanges: []
primer_expert: This patch adds the `SORT(.text.*)` directive to the linker script
  for the AVR target. This ensures that sections like `.text.libgcc.mul` are grouped
  together, improving instruction cache utilization and potentially reducing instruction
  fetch overhead by minimizing the distance between related code blocks.
primer_glossary:
- term: .text section
  definition: A section in an object file or executable that contains the executable
    code of a program.
- term: Input section
  definition: A section from an input object file that is being processed by the linker.
- term: Code locality
  definition: The principle that program instructions that are close to each other
    in memory are likely to be executed close to each other in time. Improving code
    locality can lead to better cache performance.
- term: libgcc
  definition: The GCC runtime library, which provides support functions for the GCC
    compiler, such as functions for arithmetic operations that cannot be efficiently
    implemented in machine code.
- term: AVR-LibC
  definition: A C library specifically designed for the AVR microcontroller architecture.
- term: Linker script
  definition: A script used by the linker to control how sections from input object
    files are combined into sections in the output file and where they are placed
    in memory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8f89fd03-7fa2-4c2d-a0fe-b4e99d5b2f12@gjlay.de
bugzilla_url: null
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This patch modifies the AVR linker script to sort .text.* input sections by their name. The goal is to increase code locality, specifically to prevent functions from libgcc and AVR-LibC that are related and residing in separate .text.* sections from being placed far apart in the final executable. This ordering aims to improve performance by keeping related code closer together.
