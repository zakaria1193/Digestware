---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- ld
- x86
- ELF
- relocation
discussion_id: 20261114093829.426976-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 1/6] x86: relocate IFUNC references from non-alloc sections as STT_FUNC'
headline: 'x86: relocate IFUNC references from non-alloc sections as STT_FUNC'
tldr: Fixes binutils to correctly relocate IFUNC references from non-alloc sections
  on x86.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves the robustness of the linker for x86 architectures by correctly handling
  IFUNC references in non-alloc sections, especially relevant for debugging information.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes relocating IFUNC references from non-alloc sections as STT_FUNC
    to fix a bug where relocation scans skip these sections.
  quote: 'A non-alloc section is not loaded and ld.so never processes it, so relocate
    a reference from any non-alloc section, debugging and note sections included,
    as against STT_FUNC: it gets the address of the resolver.'
primer_expert: This patch series applies to the x86 (both 32-bit i386 and 64-bit x86_64)
  architectures in Binutils. It resolves a bug (PR ld/34988) where `STT_GNU_IFUNC`
  symbols referenced from non-allocatable sections (like `.debug_info`) are not properly
  relocated by `elf_i386_relocate_section` and `elf_x86_64_relocate_section`. The
  linker skips these sections, leading to relocation failures. The fix ensures these
  references are handled as `STT_FUNC`, pointing to the IFUNC resolver.
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
series_id: 'binutils:x86: relocate ifunc references from non-alloc sections as stt_func'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261114093829.426976-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in binutils for x86 architectures (i386 and x86_64) where IFUNC references from non-allocatable sections are not correctly relocated. The relocation scan skips these sections, causing the linker to abort or misinterpret references, especially from debug sections. The fix treats these references as STT_FUNC, resolving the problem reported in PR ld/34988 and demonstrated with a GCC example.
