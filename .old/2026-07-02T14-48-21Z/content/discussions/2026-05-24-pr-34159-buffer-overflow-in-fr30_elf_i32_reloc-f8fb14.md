---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- buffer overflow
- security
- FR30
- ELF
discussion_id: ahLey0Z28PKBcUca@squeak.grove.modra.org
source_type: public_inbox
title: PR 34159, buffer overflow in fr30_elf_i32_reloc
headline: PR 34159, buffer overflow in fr30_elf_i32_reloc
tldr: This patch fixes a buffer overflow in fr30_elf_i32_reloc and removes a FIXME.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Using bfd_elf_generic_reloc may have performance implications compared to the original
  code.
- The reloc offset sanity check adds a layer of safety against malformed object files.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a fix for a buffer overflow in fr30_elf_i32_reloc and removes
    a FIXME.
  quote: null
primer_expert: This patch modifies ``elf32-fr30.c`` to address a buffer overflow in
  the ``fr30_elf_i20_reloc`` and ``fr30_elf_i32_reloc`` functions. It uses ``bfd_elf_generic_reloc``
  for ``ld -r`` and incorporates a reloc offset sanity check. The code interacts with
  the BFD library for ELF object file manipulation.
primer_general: Binutils is a suite of tools used for manipulating binary files, including
  executables and object code.  A buffer overflow occurs when a program writes data
  beyond the allocated memory buffer, potentially leading to crashes or security vulnerabilities.
  This patch fixes a buffer overflow in the binutils library when processing FR30
  architecture ELF files, making it more robust and secure.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahLey0Z28PKBcUca@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch addresses a buffer overflow vulnerability in the ``fr30_elf_i32_reloc`` function within the binutils library, as reported in PR 34159. It modifies the function to use ``bfd_elf_generic_reloc`` when linking relocatable objects (``ld -r``) and adds a sanity check for the relocation offset. The patch also removes a related FIXME comment.
