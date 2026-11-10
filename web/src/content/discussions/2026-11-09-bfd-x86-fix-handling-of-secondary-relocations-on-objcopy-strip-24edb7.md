---
project: binutils
subsystem: bfd/x86
patch_id: null
tags:
- binutils
- bfd
- x86
- objcopy
- strip
discussion_id: 20261109-fix-livepatch-v1-0-746e33313147@scaleway.com
source_type: public_inbox
title: '[PATCH 0/2] bfd/x86: Fix handling of secondary relocations on objcopy/strip'
headline: 'bfd/x86: Fix handling of secondary relocations on objcopy/strip'
tldr: Fixes silent corruption of secondary relocations by objcopy and strip, restoring
  expected behavior.
proposer: Antoine Damhet <adamhet@scaleway.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Antoine Damhet <adamhet@scaleway.com>
  role: proposer
  position: Submits a two-part patch series to fix corruptions in secondary relocations
    affecting objcopy and strip utilities.
  quote: As outlined in the bug[1], relocations of '.klp.rela.*' sections would be
    silently corrupted by both strip and objcopy. This series restore the original
    behavior for both regressions.
primer_expert: This patch series targets the BFD (Binary File Descriptor) library
  and its x86-specific ELF backend. It corrects issues with handling secondary relocations
  (likely related to livepatching mechanisms like '.klp.rela.*' sections) when these
  sections are processed by `objcopy` or `strip`. The fix appears to involve ensuring
  correct copying of section metadata, preventing data corruption.
primer_glossary:
- term: relocations
  definition: Information in an object file that describes how to modify memory addresses
    when the code or data is linked or loaded into memory. Secondary relocations might
    refer to relocations that are dependent on other relocations or are part of a
    more complex linking process.
- term: objcopy
  definition: A utility in GNU Binutils that copies and translates object files. It
    can be used to remove or modify sections, change symbol names, etc.
- term: strip
  definition: A utility in GNU Binutils that removes symbols and other information
    from object files to reduce their size.
- term: bfd
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    that provides a device-independent interface to a variety of object file formats.
- term: SHT_SECONDARY_RELOC
  definition: A section type in the ELF file format that indicates secondary relocation
    information, often used in specific linking or patching scenarios.
series_id: 'binutils:bfd/x86: fix handling of secondary relocations on objcopy/strip'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109-fix-livepatch-v1-0-746e33313147@scaleway.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This series addresses a bug where secondary relocations in '.klp.rela.*' sections were silently corrupted by both the strip and objcopy utilities. The proposed patches aim to restore the original, correct behavior for handling these relocations.
