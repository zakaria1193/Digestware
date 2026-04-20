---
project: binutils
subsystem: hppa64-hpux
patch_id: null
tags:
- linker
- HPPA
- HPUX
- testsuite
- linker script
discussion_id: alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [SPAM] Re: [PATCH] hppa64-hpux: Create dummy milli.a archives for binutils
  and ld testsuites [v2]'
headline: Create dummy milli.a archives for binutils and ld testsuites
tldr: This is a discussion about HPPA64-HP-HPUX linker failures related to merging
  `.text` sections in relocatable links and missing `milli.a` archive, with suggesti…
stakes: Ensuring correct linker behavior and testsuite pass rates for the HPPA64-HP-HPUX
  target.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modifying the linker script could affect other linking scenarios.
- Using `UNIQUE` or `NOUNIQUE` keywords might not be the standard approach.
- A more general solution might be needed to handle different architectures.
primer_expert: The thread discusses linker regressions on hppa64-hpux, specifically
  `ld-elf/pr30791b` failing due to `.text` section merging during relocatable linking,
  influenced by `lang_add_unique (".text")` in `hppa64elf_after_parse`. The suggested
  fix involves modifying the linker script to prevent this merging, potentially using
  `UNIQUE` or `NOUNIQUE` keywords. The interaction with target-specific linker scripts
  is key here, as these scripts dictate section merging behavior.
primer_general: Linkers combine compiled code files into a final program or library.
  During this process, they resolve references between different parts of the code
  and organize the code and data into sections.  Linker scripts control how these
  sections are merged and arranged in the output file. This discussion focuses on
  the HPPA64 architecture, where a specific linker behavior (merging `.text` sections,
  which contain the program's instructions) is causing test failures. The proposed
  solution involves tweaking the linker script, which acts as an instruction manual
  for the linker, to prevent this merging and fix the tests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

The discussion revolves around linker failures on the HPPA64-HP-HPUX target. The failures are due to missing `milli.a` archive and the linker's behavior of merging `.text` sections in relocatable links.  Maciej suggests modifying the default linker script to prevent merging `.text` sections for incremental links.
