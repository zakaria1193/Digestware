---
project: binutils
subsystem: bfd/x86-64
patch_id: null
tags:
- relocation
- x86-64
- COFF
- BFD
discussion_id: 55dfd86f-a92d-4a41-9980-e0c6f4feaa87@suse.com
source_type: public_inbox
title: '[PATCH 1/3] bfd/x86-64: support COFF relocation type R_AMD64_ABS'
headline: 'bfd/x86-64: support COFF relocation type R_AMD64_ABS'
tldr: Adds support for the R_AMD64_ABS relocation type in the x86-64 COFF backend.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables the use of non-altering relocations for x86-64 COFF files.
- Requires other parts of the toolchain (like the linker) to correctly handle this
  new relocation type.
exchanges: []
primer_expert: This patch updates the `bfd/coff-x86_64.c` file to introduce support
  for the COFF relocation type `R_AMD64_ABS`. It defines this type in the `howto_table`
  and ensures that `coff_amd64_reloc_type_lookup` maps `BFD_RELOC_NONE` to `R_AMD64_ABS`.
  The `in_reloc_p` function is also updated to not treat `R_AMD64_ABS` as an altering
  relocation. This aligns the x86-64 COFF backend with the handling of non-altering
  relocations, similar to ELF's `R_X86_64_NONE` and Windows' `IMAGE_REL_AMD64_ABSOLUTE`.
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
- term: R_AMD64_ABS
  definition: A COFF relocation type for x86-64 architecture that represents an absolute
    relocation, meaning it does not modify the binary's content and is similar to
    ELF's R_X86_64_NONE.
- term: BFD
  definition: Binary File Descriptor library, a crucial part of GNU Binutils that
    provides a common interface for reading and writing various object file formats.
series_id: 'binutils:bfd/x86-64: support coff relocation type r_amd64_abs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/55dfd86f-a92d-4a41-9980-e0c6f4feaa87@suse.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch introduces support for the R_AMD64_ABS relocation type within the x86-64 COFF backend of binutils. This type is analogous to ELF's R_X86_64_NONE and is known in the Windows world as IMAGE_REL_AMD64_ABSOLUTE. It is intended to be used for relocations that do not alter the binary content, similar to how R_*_NONE is handled in other contexts.
