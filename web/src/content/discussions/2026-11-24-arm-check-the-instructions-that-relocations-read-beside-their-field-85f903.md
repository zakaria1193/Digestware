---
project: binutils
subsystem: arm
patch_id: null
tags:
- arm
- relocation
- security
- elf
- binutils
discussion_id: 20261124080017.3387430-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/2] arm: check the instructions that relocations read beside their
  field'
headline: 'arm: check the instructions that relocations read beside their field'
tldr: Binutils arm ELF support now validates that instructions read by relocations
  are within section bounds.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves security by preventing out-of-bounds reads for specific ARM relocations.
- Adds complexity to the relocation handling code.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes adding checks for instruction bounds when read by relocations
    in ARM ELF.
  quote: "Three paths read section contents away from the relocated field, where\n\
    the field check in elf32_arm_relocate_section does not reach:\n\n- R_ARM_TLS_GOTDESC:\
    \ elf32_arm_final_link_relocate reads the field as\n  the signed distance from\
    \ the instruction that uses it, then reads\n  that instruction.  The distance\
    \ comes from the input, so a crafted\n  value read before or far outside the section.\
    \  Check tha…"
primer_expert: This patch series (2/2) addresses security vulnerabilities in binutils'
  ARM ELF handling. Specifically, it adds bounds checks for instructions that are
  indirectly accessed by relocations like R_ARM_TLS_GOTDESC, R_ARM_V4BX, and R_ARM_THM_TLS_DESCSEQ.
  These checks ensure that the instruction being read, which might span across halfwords
  for Thumb instructions, is entirely contained within the section's boundaries, preventing
  heap overflows and other memory corruption issues on malformed inputs.
primer_glossary:
- term: relocation
  definition: A placeholder in object code that specifies how to modify an address
    or symbol reference when linking.
- term: R_ARM_TLS_GOTDESC
  definition: An ARM relocation type related to Thread-Local Storage (TLS) GOT (Global
    Offset Table) descriptor entries.
- term: R_ARM_V4BX
  definition: An ARM relocation type associated with the BX (Branch and Exchange)
    instruction, used for interworking between ARM and Thumb states.
- term: R_ARM_THM_TLS_DESCSEQ
  definition: An ARM relocation type for Thumb instructions related to TLS descriptor
    sequences.
- term: Thumb
  definition: A 16-bit instruction set architecture for ARM processors, designed for
    better code density.
- term: TLS
  definition: Thread-Local Storage, a mechanism that allows each thread in a process
    to have its own private copy of a variable.
- term: GOT
  definition: Global Offset Table, a table used in position-independent code to store
    addresses of external symbols or data.
- term: BFD
  definition: Binary File Descriptor library, used by binutils to handle various object
    file formats.
series_id: 'binutils:arm: check the instructions that relocations read beside their
  field'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124080017.3387430-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch enhances binutils' ARM ELF support by ensuring that instructions read by certain relocations (R_ARM_TLS_GOTDESC, R_ARM_V4BX, R_ARM_THM_TLS_DESCSEQ) are located within the section bounds. This prevents potential out-of-bounds reads and writes when processing crafted objects.
