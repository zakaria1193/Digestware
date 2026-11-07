---
project: binutils
subsystem: ld/pe
patch_id: null
tags:
- linker
- PE/COFF
- relocation
discussion_id: 0c9353b9-bb64-4db3-8592-b21b6ea99177@suse.com
source_type: public_inbox
title: '[PATCH 3/3] ld/PE: use in_reloc_p()'
headline: 'ld/PE: use in_reloc_p()'
tldr: Updates the PE linker to use the generic in_reloc_p() function for relocation
  type checking.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Consolidates relocation handling logic, reducing code duplication.
- Requires ensuring `in_reloc_p` implementations are accurate and complete across
  all relevant architectures.
exchanges: []
primer_expert: This patch modifies the PE/COFF linker's BFD backend to use a standardized
  `in_reloc_p()` function for determining whether a relocation type should be processed.
  It aims to eliminate architecture-specific logic within `ld/pe-dll.c` by ensuring
  that the `in_reloc_p()` helper in BFD backends (like `coff-aarch64.c`, `coff-arm.c`,
  `coff-mcore.c`, `coff-x86_64.c`) correctly identifies and filters out non-altering
  relocations (e.g., ABSOLUTE, SECREL, SECTION) across different architectures.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the executable file format
    used by Windows operating systems. Binutils' ld supports this format for Windows
    targets.
- term: relocation
  definition: A modification of a program or its data in the executable or library
    by the linker or loader to resolve symbolic references and make it runnable at
    its final address. Relocation types specify how the address or value should be
    calculated.
- term: in_reloc_p
  definition: A BFD helper function that determines if a given relocation type should
    be considered for processing, typically by checking if it modifies the binary's
    content.
- term: ABS/NONE relocation
  definition: Relocation types that do not alter the binary's content, often used
    for metadata or to indicate that no relocation is needed for a symbol.
series_id: 'binutils:ld/pe: use in_reloc_p()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0c9353b9-bb64-4db3-8592-b21b6ea99177@suse.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch updates the PE linker to utilize the in_reloc_p() function, which is intended to consolidate relocation type checking logic. The goal is to remove custom relocation type handling for section, section relative, image base relative, and ABS/NONE relocations by ensuring these types are correctly identified by the generic function across various architectures.
