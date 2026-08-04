---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- linker
- x86
- relocation
- ELF
discussion_id: CAMe9rOpTBfSWyDtPphPOqaeazfxBiOUPsFfNB5wKgzEuf9ewFg@mail.gmail.com
source_type: public_inbox
title: '[PATCH] x86: Check if needed dynamic relocation section is created'
headline: 'x86: Check if needed dynamic relocation section is created'
tldr: Fixes an issue in binutils where a needed dynamic relocation section might not
  be created if an earlier relocation fails.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures more relocations are processed by not prematurely aborting on errors, potentially
  revealing other issues but improving robustness.
- Adds a conditional check to maintain correct behavior when the dynamic relocation
  section is indeed not needed or not created.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submits a patch to ensure that the dynamic relocation count is skipped
    only if the needed dynamic relocation section has not been created, preventing
    premature abortion of relocation processing.
  quote: null
primer_expert: This patch for the GNU linker (ld) modifies the x86 ELF backend. Specifically,
  it addresses an issue in `_bfd_x86_elf_late_size_sections` where `elf_link_read_relocs_from_section`
  could abort on an invalid relocation. If this happens, subsequent relocations are
  not processed, and a required dynamic relocation section might not be created. The
  patch adds a check to only skip the dynamic relocation count if the section hasn't
  been created, ensuring more reliable processing of relocations.
primer_glossary:
- term: relocation
  definition: A process performed by a linker or loader that adjusts symbolic addresses
    in object code to their final absolute locations in memory. Relocations specify
    how to modify memory references within code or data to point to the correct addresses
    of symbols.
- term: dynamic relocation
  definition: Relocations that are resolved at runtime by the dynamic linker. These
    are necessary for dynamically linked executables and shared libraries, allowing
    code to be loaded and linked while the program is running.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: BFD
  definition: The Binary File Descriptor library, a part of GNU Binutils. It provides
    a generic interface to read and write various object file formats, including ELF.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpTBfSWyDtPphPOqaeazfxBiOUPsFfNB5wKgzEuf9ewFg@mail.gmail.com
bugzilla_url: null
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the x86 ELF linker where the processing of relocations could be prematurely aborted due to an error. This premature abortion prevents the creation of necessary dynamic relocation sections, which in turn affects subsequent relocations. The fix ensures that the dynamic relocation count is skipped only if the needed section has not yet been created, thus allowing relocations to be processed more robustly.
