---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- ld
- aarch64
- ELF
- relocation
discussion_id: 20261114093829.426976-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 2/6] aarch64: relocate IFUNC references from non-alloc sections
  as STT_FUNC'
headline: 'aarch64: relocate IFUNC references from non-alloc sections as STT_FUNC'
tldr: Fixes binutils to correctly relocate IFUNC references from non-alloc sections
  on AArch64.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correct IFUNC symbol resolution from non-allocatable sections, improving
  linker robustness for architectures like AArch64.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes relocating IFUNC references from non-alloc sections as STT_FUNC
    to fix a bug where relocation scans skip these sections.
  quote: 'A non-alloc section is not loaded and ld.so never processes it, so relocate
    a reference from any non-alloc section, debugging and note sections included,
    as against STT_FUNC: it gets the address of the resolver.'
primer_expert: This patch targets the AArch64 architecture within Binutils, specifically
  addressing `STT_GNU_IFUNC` relocation from non-allocatable sections. The core problem
  lies in `elfNN_aarch64_relocate_section` not handling references in sections like
  `.debug_info` or `.note` that are not loaded at runtime. The patch modifies the
  relocation logic to treat these references as `STT_FUNC`, aligning with the solution
  for other architectures and fixing PR ld/34988.
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
series_id: 'binutils:aarch64: relocate ifunc references from non-alloc sections as
  stt_func'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261114093829.426976-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

This patch series corrects binutils' handling of IFUNC references within non-allocatable sections on AArch64. Previously, the linker would abort or fail to relocate these references, particularly those in debug or note sections, due to skipping non-alloc sections. The changes ensure that such references are treated as STT_FUNC, resolving the issue described in PR ld/34988.
