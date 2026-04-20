---
project: binutils
subsystem: hppa64-hpux
patch_id: null
tags:
- binutils
- linker
- HPPA
- HP-UX
- relocation
discussion_id: alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [SPAM] Re: [PATCH] hppa64-hpux: Create dummy milli.a archives for binutils
  and ld testsuites [v2]'
headline: 'hppa64-hpux: Create dummy milli.a archives for binutils and ld testsuites
  [v2]'
tldr: Discussion of linker failures on hppa64-hpux related to .text section merging
  during relocatable links.
stakes: Addresses linker issues on hppa64-hpux, potentially impacting software builds
  for this platform.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Addresses test failures by modifying linker behavior.
- Potential impact on long branch stub support needs consideration.
- Modifying the linker script may have broader implications for linking on hppa64-hpux.
primer_expert: The `hppa64elf_after_parse` function in `bfd/elfxx-hppa.c` adds `.text`
  using `lang_add_unique` when `bfd_link_relocatable` is true, preventing section
  merging.  This logic, intended for stub support, causes test failures. The discussion
  suggests modifying the linker script to control `.text` merging, possibly with `UNIQUE`
  or `NOUNIQUE` keywords, influencing linker behavior for relocatable objects.
primer_general: The linker combines compiled object files into a single executable
  or library.  Linker scripts control how sections from these object files are arranged
  in the final output.  This discussion focuses on the HP-UX operating system on the
  HPPA64 architecture and a problem in how the linker handles the merging of `.text`
  sections (which contain executable code) when creating relocatable objects, which
  are intermediate object files that can be linked into other programs or libraries.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

This discussion thread concerns linker failures on the hppa64-hpux platform. The failures appear to stem from how the linker merges .text sections during relocatable links, particularly when preparing for improved stub support for long branches. The suggestion is to modify the default linker script to prevent merging .text sections for incremental links, possibly through `UNIQUE` and `NOUNIQUE` output section keywords.
