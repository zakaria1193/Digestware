---
project: binutils
subsystem: elf
patch_id: null
tags:
- elf
- linker
- symbol
discussion_id: aqSgvUFtjNhIpqC-@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] elf: Hide DT_INIT and DT_FINI functions'
headline: 'elf: Hide DT_INIT and DT_FINI functions'
tldr: Reviewer OK'd patch to hide DT_INIT/DT_FINI functions, agreeing they are special
  and should be hidden by GNU ld.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Automatically hiding `_init` and `_fini` from .dynsym simplifies symbol tables but
  deviates slightly from a strict interpretation of user-supplied symbols.
- This change aligns with common practice and improves the clarity of dynamic linking
  information.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Approved the patch, stating that `_init` and `_fini` are special and it's
    correct for GNU ld to hide them from .dynsym.
  quote: 'I OK''d the patch on the grounds that _init and _fini are sufficiently special
    given the magic connection to DT_INIT and DT_FINI.


    I completely agree with Jan that the ELF spec is silent in this area, and that
    a user supplied _init or _fini ought to be hidden by making them so in the source.
    However, I don''t think it is wrong for GNU ld to force them hidden and remove
    them from .dynsym.'
primer_expert: This patch modifies GNU ld's handling of `_init` and `_fini` symbols,
  which are traditionally associated with the DT_INIT and DT_FINI entries in the ELF
  dynamic section. The change aims to automatically hide these symbols from the dynamic
  symbol table (.dynsym), even though they are user-supplied and not linker-created
  symbols. The rationale hinges on their special nature and established linkage conventions.
primer_glossary:
- term: _init
  definition: A convention for a function that is executed automatically by the dynamic
    linker before any other code in a shared object or executable is run. It is typically
    associated with DT_INIT.
- term: _fini
  definition: A convention for a function that is executed automatically by the dynamic
    linker when a shared object or executable is unloaded. It is typically associated
    with DT_FINI.
- term: DT_INIT
  definition: A dynamic tag in an ELF object that specifies the address of the initialization
    function (`_init`) for a shared library or executable.
- term: DT_FINI
  definition: A dynamic tag in an ELF object that specifies the address of the termination
    function (`_fini`) for a shared library or executable.
- term: ELF dynamic symbol table (.dynsym)
  definition: A section in an ELF file containing symbols that are needed for dynamic
    linking, such as exported functions and global variables in shared libraries.
- term: GNU ld
  definition: The GNU linker, a standard component of the GNU Binutils package responsible
    for combining object files into executables or shared libraries.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqSgvUFtjNhIpqC-@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-12'
is_stub: false
stub_reason: ''
---

This discussion concerns a patch to hide `_init` and `_fini` functions by default in GNU ld, which are associated with DT_INIT and DT_FINI dynamic section entries. While the ELF specification is silent on this exact behavior, the reviewer agrees that these functions are special and that GNU ld correctly handles them by hiding them from the dynamic symbol table (.dynsym).
