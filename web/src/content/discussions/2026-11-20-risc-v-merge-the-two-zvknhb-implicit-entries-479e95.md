---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- binutils
- cleanup
- refactoring
- config
discussion_id: 20261120141636.3964825-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[committed] RISC-V: Merge the two zvknhb implicit entries'
headline: 'RISC-V: Merge the two zvknhb implicit entries'
tldr: Clean up RISC-V Zvknhb implicit subset definitions by merging duplicate entries.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: 8
technical_tradeoffs:
- Improves code clarity and maintainability by removing redundancy.
- No functional impact, as the behavior remains the same.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits a patch to merge duplicate 'zvknhb' implicit subset entries in
    binutils' RISC-V configuration, improving clarity without functional change.
  quote: 'Commit 60667464054 added a second zvknhb entry to

    riscv_implicit_subsets.  Both were applied, since the table is scanned

    once and every matching entry is used, but one entry is clearer.  No

    functional change.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the commit and the reasoning for merging the duplicate entries.
  quote: null
primer_expert: The patch modifies `bfd/elfxx-riscv.c` by removing a redundant entry
  for the `zvknhb` implicit subset from the `riscv_implicit_subsets` array. This array
  maps ISA extension names to their dependencies. Previously, two identical entries
  existed for `zvknhb`, both pointing to `+zvknha` and `+zve32x`. The commit consolidates
  these into a single, clearer entry, addressing an inefficiency in the configuration.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: implicit subset
  definition: A predefined set of ISA extensions that are automatically enabled when
    a larger extension is selected.
- term: zvknhb
  definition: A specific RISC-V ISA extension, likely related to vector or cryptographic
    operations.
- term: BFD
  definition: Binutils Format Description, a library used by binutils to support various
    object file formats.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120141636.3964825-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This committed patch cleans up the RISC-V implicit subset definitions by merging two identical entries for 'zvknhb'. While both entries were functional, one was redundant and less clear. This change simplifies the internal representation without altering functionality.
