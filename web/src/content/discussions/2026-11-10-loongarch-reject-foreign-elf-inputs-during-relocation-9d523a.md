---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- ELF
- relocation
discussion_id: avKiQjqas7trz_13@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] LoongArch: Reject foreign ELF inputs during relocation'
headline: 'LoongArch: Reject foreign ELF inputs during relocation'
tldr: Prevents linking of non-LoongArch ELF files by checking input BFD format before
  relocation processing.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds an explicit check to reject unsupported file formats early in the linking process,
  improving robustness.
exchanges:
- author: zhaozhou
  role: proposer
  position: Submitted a patch to reject non-LoongArch ELF inputs during relocation.
  quote: 'Reject non-LoongArch inputs before processing relocations.


    PR ld/34807'
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Accepted the patch.
  quote: OK.
primer_expert: This change to the LoongArch ELF backend ensures that `loongarch_elf_relocate_section`
  only processes input BFDs that are identified as LoongArch ELF files. It adds an
  explicit check for `is_loongarch_elf` early in the function, returning an error
  if the format is incorrect, thus preventing potential issues with cross-architecture
  linking or malformed object files.
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, shared libraries, and core dumps on Unix-like systems.
- term: relocation
  definition: The process of updating symbolic references in object code to absolute
    or relocatable addresses during linking.
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to parse and manipulate object files from various architectures and formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avKiQjqas7trz_13@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch addresses a bug (PR ld/34807) by ensuring that the linker rejects non-LoongArch ELF inputs before attempting relocation processing. This prevents potential errors or incorrect behavior when mixing object files from different architectures.
