---
project: binutils
subsystem: gas
patch_id: null
tags:
- AArch64
- linker
- relocation
discussion_id: 20260908143017.501355-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] AArch64 GAS: Reject nonzero GOT-entry relocation addends'
headline: 'AArch64 GAS: Reject nonzero GOT-entry relocation addends'
tldr: Patch enforces zero addends for specific AArch64 GOT-entry relocations as required
  by AAELF.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Stricter adherence to the AAELF specification for GOT relocations versus potential
  compatibility issues if non-zero addends were previously accepted.
exchanges:
- author: Sivan Shani
  role: proposer
  position: Submitted a patch to enforce zero addends for specific AArch64 GOT-entry
    relocations, adding tests for LP64 and ILP32.
  quote: 'AAELF requires relocations using GDAT, GTLSIDX, GTPREL or GTLSDESC

    operations to have a zero addend.


    Add a common predicate for the affected BFD relocation codes.  Use it

    in tc_gen_reloc to reject nonzero addends before PC-relative adjustment,

    and in aarch64_fix_adjustable to preserve symbol identity.


    Add LP64 and ILP32 tests covering rejected +1/-1 expressions and

    accepted +0/-0 expressions fo…'
primer_expert: This patch addresses a compliance issue in the AArch64 backend of GAS
  concerning Global Offset Table (GOT) entries. Specifically, it enforces the AAELF
  standard's requirement that certain GOT-related relocations (GDAT, GTLSIDX, GTPREL,
  GTLSDESC) must have a zero addend. The change involves adding a new predicate function
  `aarch64_reloc_creates_got_entry_p` to identify these relocations and integrating
  checks in `tc_gen_reloc` and `aarch64_fix_adjustable` to reject non-zero addends.
  New test cases are provided for both LP64 and ILP32 data models.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: GOT
  definition: Global Offset Table. A data structure used in position-independent code
    (PIC) to store addresses of external functions or global variables.
- term: Relocation
  definition: A process performed by the linker to adjust symbolic addresses in machine
    code after it has been assembled, ensuring correct addresses at runtime.
- term: Addend
  definition: A constant value added to a symbol's address during the relocation process.
- term: AAELF
  definition: Arm Architecture ELF (Executable and Linkable Format) specification.
    Defines the object file format and conventions for the Arm architecture.
- term: LP64
  definition: A data model where long pointers and integers are 64-bit. Used in many
    64-bit operating systems, including AArch64.
- term: ILP32
  definition: A data model where integers are 32-bit, but pointers are also 32-bit.
    It's a variant for 64-bit architectures like AArch64.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260908143017.501355-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Sivan Shani submits a patch to the AArch64 assembler (GAS) that enforces the AAELF requirement for zero addends on relocations involving GDAT, GTLSIDX, GTPREL, or GTLSDESC operations. The patch introduces a common predicate to identify these relocation types and rejects non-zero addends, ensuring symbol identity preservation. New tests for both LP64 and ILP32 ABIs are included.
