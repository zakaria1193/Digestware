---
project: binutils
subsystem: x86
patch_id: null
tags:
- bugfix
- linker
- x86
discussion_id: CAMe9rOqE8c=qO3Twv=WXN767ngZgcc0Xz+0Y+k+sA=Wxz-EyYA@mail.gmail.com
source_type: public_inbox
title: 'x86: Check if needed dynamic relocation section is created'
headline: 'x86: Check if needed dynamic relocation section is created'
tldr: Fixes binutils to avoid aborting when a needed dynamic relocation section is
  not created.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Addresses a specific failure mode rather than the root cause of bad relocations.
exchanges: []
primer_expert: The x86 ELF linker (`elfxx-x86.c`) has a `_bfd_x86_elf_late_size_sections`
  function that processes relocations. If `elf_link_read_relocs_from_section` encounters
  an error, it aborts, which can lead to a failure in creating the dynamic relocation
  section. This patch adds a check to skip counting dynamic relocations if this section
  is not present, preventing an early abort and ensuring the section can be created.
primer_glossary:
- term: relocation
  definition: The process of updating symbolic references in relocatable object code
    to absolute symbols, typically done by the linker.
- term: dynamic relocation
  definition: Relocations that are resolved at runtime by the dynamic linker, used
    for dynamically linked executables and libraries.
- term: PR ld/34448
  definition: A bug report filed against the GNU ld linker, identified by the number
    34448.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqE8c=qO3Twv=WXN767ngZgcc0Xz+0Y+k+sA=Wxz-EyYA@mail.gmail.com
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

This patch for binutils addresses an issue where the elf_link_read_relocs_from_section function aborts on bad relocations, preventing the creation of needed dynamic relocation sections. It proposes to skip dynamic relocation counting if the section hasn't been created, resolving PR ld/34448.
