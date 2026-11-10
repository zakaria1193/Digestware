---
project: binutils
subsystem: hppa
patch_id: null
tags:
- hppa
- linker
- relocation
- dynamic-linking
discussion_id: avJDcffzwqrk9nuy@mx3210.local
source_type: public_inbox
title: New Latvian PO file for 'gas' (version 2.46.90)
headline: 'hppa: Fix register extraction logic for ldil instruction'
tldr: Corrects register extraction for HPPA's ldil instruction, enabling proper relocation
  handling for dynamic linking.
proposer: John David Anglin <dave.anglin@bell.net>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves relocation accuracy for a specific instruction sequence, enabling correct
  dynamic linking on HPPA.
exchanges:
- author: John David Anglin <dave.anglin@bell.net>
  role: proposer
  position: Submitted a patch to fix relocation handling for HPPA's ldil instruction.
  quote: 'This fixes two issues in the code to handle converting the relocation

    in ldil+addl sequences.  I extracted the target address of the ldil

    instruction from the wrong bit position.  Secondly as with addil, we

    need to accept any base register in the R_PARISC_DLTIND21L conversion

    to R_PARISC_DPREL21L.'
primer_expert: This change updates the HPPA ELF linker's `final_link_relocate` function
  to correctly handle relocations involving `ldil` and `addl` instruction pairs. Specifically,
  it fixes the bitmask used to extract the source/base register from the `ldil` instruction
  and broadens the `addl` instruction check to accommodate arbitrary target registers
  emitted by the compiler (likely related to Link-Time Relocation, LRA). This ensures
  correct address calculation for dynamically linked executables.
primer_glossary:
- term: HPPA
  definition: Hewlett-Packard Precision Architecture. A RISC instruction set architecture.
- term: ldil
  definition: Load Immediate Long. An HPPA instruction used to load a 21-bit immediate
    value.
- term: addl
  definition: Add Long. An HPPA instruction for addition.
- term: relocation
  definition: The process of updating symbolic references in object code to absolute
    or relocatable addresses during linking.
- term: R_PARISC_DLTIND21L
  definition: A specific relocation type for HPPA, likely related to loading a 21-bit
    value.
- term: R_PARISC_DPREL21L
  definition: Another HPPA relocation type, likely for a 21-bit data-relative address.
- term: LRA
  definition: Likely refers to Link-Time Relocation, a feature where relocations are
    resolved at link time rather than load time.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avJDcffzwqrk9nuy@mx3210.local
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This committed patch fixes two issues in the HPPA ELF linker's handling of `ldil` and `addl` instruction sequences, which are used for dynamic linking relocations. It corrects the bit shifting for extracting the target address from `ldil` and allows for arbitrary base registers in the subsequent `addl` instruction, resolving issues with relocated code generation.
