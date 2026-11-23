---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- error handling
- patch series
discussion_id: 1194bbe2-5c01-408c-8131-ffe04b8a74bc@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: A patch series is being developed to detect relocations out of section range
  for LoongArch, with discussion on improving error messages.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Enhances error reporting for easier debugging.
- Potential for a generic ELF check to handle multiple architectures, reducing target-specific
  code.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: contributor
  position: Requests that the relocation name be added to the error message for better
    diagnostics.
  quote: 'Thanks — please use the existing patch and ignore mine.

    By the way, how about adding the relocation name to the error message?'
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Explains that a generic ELF check in his series covers this issue and
    agrees to add relocation names to the error message in a future revision.
  quote: 'The RFC I posted on Monday does this check for every ELF target where

    the linker reads relocations (elf_link_read_relocs_from_section), so it

    covers the sections check_relocs skips, and runs before relaxation:

    https://inbox.sourceware.org/binutils/20261116184333.3297411-1-harshit7kr@gmail.com/


    LoongArch is 15/17; the howto sizes cover the other relocations:

    https://inbox.sourceware.org/binutils/…'
primer_expert: This thread concerns improvements to binutils' error reporting for
  the LoongArch architecture, specifically detecting relocations that reference addresses
  outside the defined section. The proposer has developed a series of patches that
  enhance this checking mechanism, including a generic ELF-wide check. The discussion
  includes a request to make error messages more informative by including the relocation
  name, a feature the proposer plans to implement.
primer_glossary:
- term: LoongArch
  definition: A 64-bit CPU architecture developed by Loongson Technology.
- term: relocation
  definition: Information in an object file that describes how to modify certain values,
    typically code or data, after linking to allow them to be placed at an absolute
    address.
- term: section
  definition: A segment of an object file or executable that contains related data,
    such as code (.text), initialized data (.data), or uninitialized data (.bss).
- term: linker
  definition: A program that combines various pieces of code and data (from object
    files and libraries) and resolves references between them to create a single executable
    file or library.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/1194bbe2-5c01-408c-8131-ffe04b8a74bc@loongson.cn
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This discussion centers on a patch series for LoongArch in binutils that detects relocations exceeding section boundaries. The proposer, Harshit Kumar, has posted a series of patches, with the 15th patch specifically targeting LoongArch. A contributor, mengqinggang, suggests incorporating the relocation name into the error message for better clarity. Harshit agrees to this enhancement in a subsequent revision, while also pointing to a generic ELF check in his series that might supersede the need for a LoongArch-specific check.
