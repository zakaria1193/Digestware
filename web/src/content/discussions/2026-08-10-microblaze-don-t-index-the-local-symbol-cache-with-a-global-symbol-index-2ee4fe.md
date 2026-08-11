---
project: binutils
subsystem: microblaze
patch_id: null
tags: []
discussion_id: CAEekfLaapRDKPRzsTWeU0nC0AZL5yWgYgeqi1sw7ObkxHh-=6g@mail.gmail.com
source_type: public_inbox
title: '[PATCH] microblaze: don''t index the local symbol cache with a global symbol
  index'
headline: 'microblaze: don''t index the local symbol cache with a global symbol index'
tldr: Patch fixes an out-of-bounds read in microblaze ELF relaxation by adding a missing
  bounds check.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Sam Price
  role: proposer
  position: Submits a patch to fix an out-of-bounds read in microblaze ELF relaxation
    by reintroducing a missing bounds check.
  quote: 'microblaze_elf_relax_section() was copied from

    sh_elf_relax_delete_bytes() in 2009 (7ba29e2a41) but the copy dropped

    a bounds check that was already present in the sh original.  This adds

    the missing two-line guard from bfd/elf32-sh.c:1227-1228, preventing

    an out-of-bounds read that silently corrupts relocation addends.'
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAEekfLaapRDKPRzsTWeU0nC0AZL5yWgYgeqi1sw7ObkxHh-=6g@mail.gmail.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

Sam Price has submitted a patch to fix an issue in microblaze_elf_relax_section where a bounds check was dropped during a code copy, leading to an out-of-bounds read that could corrupt relocation addends. The patch reintroduces the missing guard, preventing silent miscompilations and ensuring data integrity, as confirmed by new test cases.
