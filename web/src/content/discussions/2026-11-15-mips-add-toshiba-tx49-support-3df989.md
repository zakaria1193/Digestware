---
project: binutils
subsystem: mips
patch_id: null
tags:
- binutils
- mips
- processor
- commit
- embedded
discussion_id: alpine.DEB.2.21.2610200049100.22065@angie.orcam.me.uk
source_type: public_inbox
title: '[committed v4] MIPS: Add Toshiba TX49 support'
headline: 'MIPS: Add Toshiba TX49 support'
tldr: Commit adds support for the Toshiba TX49 MIPS processor, including its specific
  extensions and instruction interlocks.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Committed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Implementing specific interlock logic for the TX49 requires careful analysis of
  its microarchitecture to avoid pipeline stalls or data corruption.
- Adapting existing test suites for new hardware support helps ensure correctness
  but may not cover all unique aspects of the target architecture.
exchanges:
- author: Nathan Sidwell
  role: proposer
  position: Provided the technical details and rationale for supporting the Toshiba
    TX49 processor.
  quote: The Toshiba TX49 processor implements the MIPS III ISA along with TX39 extensions
    and additionally three-operand DMULT and DMULTU instruction variants plus the
    MIPS IV PREF instruction.
- author: Maciej W. Rozycki
  role: maintainer
  position: Committed the patch adding support for the Toshiba TX49, including handling
    its instruction set extensions and interlock logic.
  quote: "From: Nathan Sidwell\n\nThe Toshiba TX49 processor implements the MIPS III\
    \ ISA along with TX39 \nextensions..."
primer_expert: This commit enhances binutils support for the MIPS architecture by
  adding the Toshiba TX49 processor. This includes recognition of its ISA (MIPS III
  + TX39 extensions), specific instructions (3-operand DMULT/DMULTU, MIPS IV PREF),
  and crucially, its pipeline interlock behavior. The interlock logic mirrors that
  of the TX39, addressing hazards related to HI/LO register updates by division and
  MADD instructions. The changes affect BFD, binutils' internal CPU definitions, and
  ELF object file handling for MIPS.
primer_glossary:
- term: MIPS III ISA
  definition: The third generation of the MIPS (Microprocessor without Interlocked
    Pipeline Stages) instruction set architecture, a 64-bit RISC architecture.
- term: TX39 extensions
  definition: Specific extensions developed by Toshiba for their TX39 family of MIPS
    processors.
- term: DMULT/DMULTU
  definition: Instructions for performing multiplication operations in MIPS. The 'U'
    typically denotes unsigned multiplication.
- term: PREF
  definition: The PREF instruction in MIPS is used for prefetching data or instructions,
    influencing memory access patterns.
- term: MFHI/MFLO
  definition: MIPS instructions that move the results of multiplication (HI) and division
    (LO) from special registers into general-purpose registers.
- term: MADD
  definition: Multiply-Add instruction in MIPS, performing (A * B) + C and storing
    the result.
- term: pipeline interlock
  definition: A hardware mechanism that prevents instruction execution from proceeding
    if it would cause a data hazard (e.g., an instruction needs data that hasn't been
    computed yet).
- term: BFD
  definition: Binary File Descriptor library, a backend for GNU Binutils that provides
    a common interface to various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2610200049100.22065@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This committed change adds support for the Toshiba TX49 processor, which implements the MIPS III ISA with TX39 extensions. It incorporates specific three-operand DMULT/DMULTU instruction variants and the MIPS IV PREF instruction. The patch also addresses pipeline interlock behavior, particularly concerning division instructions and their interaction with MFHI/MFLO and MADD/MADDU, using logic similar to that for the TX39. Existing test cases are adapted to cover TX49, with a focus on the HI/LO interlock tests.
