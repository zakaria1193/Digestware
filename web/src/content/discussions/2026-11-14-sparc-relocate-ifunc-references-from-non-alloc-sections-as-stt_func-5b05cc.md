---
project: binutils
subsystem: sparc
patch_id: null
tags:
- binutils
- ld
- sparc
- ELF
- relocation
discussion_id: 20261114093829.426976-5-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 4/6] sparc: relocate IFUNC references from non-alloc sections as
  STT_FUNC'
headline: 'sparc: relocate IFUNC references from non-alloc sections as STT_FUNC'
tldr: Fixes binutils to correctly relocate IFUNC references from non-alloc sections
  on SPARC.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Treating IFUNC references from non-alloc sections as STT_FUNC simplifies relocation
  handling but might abstract away some nuances of IFUNC resolution specific to these
  sections.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes relocating IFUNC references from non-alloc sections as STT_FUNC
    to fix a bug where relocation scans skip these sections.
  quote: 'A non-alloc section is not loaded and ld.so never processes it, so relocate
    a reference from any non-alloc section, debugging and note sections included,
    as against STT_FUNC: it gets the address of the resolver.'
primer_expert: This patch series tackles the relocation of `STT_GNU_IFUNC` symbols
  in Binutils' linker (`ld`). The issue arises when these symbols are referenced from
  sections that are not allocated in memory at runtime (e.g., debug sections). The
  linker's relocation logic, specifically in `_bfd_sparc_elf_relocate_section`, incorrectly
  skips these non-alloc sections, leading to failures when resolving IFUNC references.
  The proposed solution modifies the relocation logic to treat these references as
  `STT_FUNC`, ensuring they are resolved correctly to the IFUNC resolver's address.
primer_glossary:
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format used for Indirect Functions, allowing
    dynamic selection of function implementations at runtime.
- term: non-alloc section
  definition: A section in an ELF object file that is not loaded into memory when
    the program is executed. Examples include debugging information sections.
- term: relocation
  definition: The process by which a linker or dynamic loader resolves symbolic references
    and updates addresses in an object file or executable to their final locations
    in memory.
- term: STT_FUNC
  definition: A symbol type in the ELF format representing a function.
- term: PR ld/34988
  definition: A bug report filed against the GNU linker (ld) concerning the handling
    of IFUNC references in non-alloc sections.
series_id: 'binutils:sparc: relocate ifunc references from non-alloc sections as stt_func'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261114093829.426976-5-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where binutils on SPARC fails to relocate IFUNC references originating from non-allocatable sections like .debug_info. Previously, the relocation scan skipped these sections, causing relocation failures or aborts. The fix ensures that references from any non-alloc section are now treated as STT_FUNC, resolving PR ld/34988.
