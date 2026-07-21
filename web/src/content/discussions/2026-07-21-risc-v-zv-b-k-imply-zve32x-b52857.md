---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- extensions
- binutils
- isa
- specification
discussion_id: CAHT-pJwkccCTquFHm-grzdWTLX1DAnpK6yprUFAztB0Px1qNOg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3 04/13] bfd/RISC-V: Zv{b,k}* imply Zve32x'
headline: 'RISC-V: Zv{b,k}* imply Zve32x'
tldr: Discussion on correct ordering of RISC-V extensions in binutils, specifically
  concerning 'zve32x' implication.
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring correct adherence to the RISC-V specification versus maintaining compatibility
  with existing binutils handling.
exchanges:
- author: Nelson Chu
  role: proposer
  position: Explains that the alphabetical order of extensions dictates 'zve*' should
    come after 'zvb*' and 'zvk*' based on the ISA spec. Also notes inconsistencies
    in extension naming rules.
  quote: So I think since the alphabetical order, zve* should be placed after zvb*.  The
    order of riscv_supported_* tables doesn't affect the final output, but it would
    be good to be maintained in the right order.
- author: Jan Beulich
  role: reviewer
  position: Queries whether the placement of 'zve32x' after 'zvbb'/'zvbc' is correct,
    suggesting that the order in `riscv_supported_std_z_ext` might be intentional.
  quote: null
primer_expert: This thread debates the correct definition of RISC-V extension implications
  and ordering within binutils. Specifically, it concerns whether extensions like
  `zvbc` should imply `zve32x`, and the correct alphabetical sequencing of extensions
  starting with 'Zv' as per the RISC-V ISA manual. The discussion also touches upon
  potential violations of extension naming conventions.
primer_glossary:
- term: RISC-V
  definition: An open-source Instruction Set Architecture (ISA) that is modular and
    extensible.
- term: Extension
  definition: A set of instructions that can be added to the base RISC-V ISA to provide
    additional functionality (e.g., vector processing, atomic operations).
- term: Implication
  definition: In the context of RISC-V extensions, when supporting one extension automatically
    enables support for another.
- term: Zve32x
  definition: A RISC-V extension that provides 32-bit vector processing capabilities.
- term: bfd
  definition: Binary File Descriptor library, part of GNU Binutils, used for handling
    various object file formats.
series_id: 'binutils:bfd/risc-v: zv{b,k}* imply zve32x'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJwkccCTquFHm-grzdWTLX1DAnpK6yprUFAztB0Px1qNOg@mail.gmail.com
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This discussion centers on the correct placement and implication of RISC-V extensions in binutils, specifically addressing whether 'zve32x' should be implied by extensions like 'zvbc' and 'zvkb'. Nelson Chu argues for the current alphabetical ordering within categories based on the ISA specification, while also noting potential deviations from naming rules in ratified extensions. Jan Beulich's comments raise questions about the ordering within the `riscv_supported_std_z_ext` tables.
