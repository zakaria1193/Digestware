---
project: binutils
subsystem: riscv
patch_id: null
tags:
- binutils
- ld
- riscv
- ELF
- relocation
discussion_id: 20261114093829.426976-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 3/6] riscv: relocate IFUNC references from non-alloc sections as
  STT_FUNC'
headline: 'riscv: relocate IFUNC references from non-alloc sections as STT_FUNC'
tldr: Fixes binutils to correctly relocate IFUNC references from non-alloc sections
  on RISC-V.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Modifying relocation logic for non-alloc sections ensures IFUNC symbols are resolved
  correctly, but requires careful testing across various non-alloc section types.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes relocating IFUNC references from non-alloc sections as STT_FUNC
    to fix a bug where relocation scans skip these sections.
  quote: 'A non-alloc section is not loaded and ld.so never processes it, so relocate
    a reference from any non-alloc section, debugging and note sections included,
    as against STT_FUNC: it gets the address of the resolver.'
primer_expert: Similar to the SPARC patch, this addresses `STT_GNU_IFUNC` relocation
  issues in Binutils for the RISC-V architecture. The problem occurs when IFUNC symbols
  are referenced from non-alloc sections, causing `riscv_elf_relocate_section` to
  fail due to skipping these sections. The patch modifies the relocation handler to
  treat these references as `STT_FUNC`, resolving the bug (PR ld/34988) and ensuring
  correct resolution of IFUNC symbols.
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
series_id: 'binutils:riscv: relocate ifunc references from non-alloc sections as stt_func'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261114093829.426976-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

This patch resolves an issue in binutils for RISC-V where IFUNC references from non-allocatable sections like .debug_info were not relocated. The linker's relocation scan skipped these sections, leading to errors. The fix ensures these references are relocated as STT_FUNC, aligning with the behavior for other sections and fixing PR ld/34988.
