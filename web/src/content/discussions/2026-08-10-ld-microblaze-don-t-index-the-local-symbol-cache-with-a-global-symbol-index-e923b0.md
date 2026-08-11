---
project: binutils
subsystem: ld/microblaze
patch_id: null
tags: []
discussion_id: 20260810054841.4177591-1-neal.frager@amd.com
source_type: public_inbox
title: '[PATCH] ld/microblaze: don''t index the local symbol cache with a global symbol
  index'
headline: 'ld/microblaze: don''t index the local symbol cache with a global symbol
  index'
tldr: Patch fixes an out-of-bounds read in microblaze ELF relaxation by adding a missing
  bounds check.
proposer: Neal Frager <neal.frager@amd.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Neal Frager
  role: proposer
  position: Submits a patch to fix an out-of-bounds read in microblaze ELF relaxation
    by adding a missing bounds check.
  quote: 'microblaze_elf_relax_section() was copied from sh_elf_relax_delete_bytes()

    in 2009 (7ba29e2a41) but the copy dropped a bounds check that was already

    present in the sh original.  This adds the missing two-line guard from

    bfd/elf32-sh.c:1227-1228, preventing an out-of-bounds read that silently

    corrupts relocation addends.


    The bug: when scanning relocations in other sections, the code indexes

    isymb…'
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260810054841.4177591-1-neal.frager@amd.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the microblaze ELF relaxation process where an out-of-bounds read could silently corrupt relocation addends. The issue stems from indexing the local symbol cache with a global symbol index without a proper bounds check, a guard that was present in the original code but dropped during a copy. The fix reintroduces this two-line guard, preventing incorrect adjustments to relocation addends and ensuring data integrity, as evidenced by passing new tests.
