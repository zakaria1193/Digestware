---
project: binutils
subsystem: bfd/nds32
patch_id: null
tags:
- nds32
- bfd
- cleanup
- build
discussion_id: avKi01NkA5FRKAEF@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] bfd/nds32: remove unused got_size variable'
headline: 'bfd/nds32: remove unused got_size variable'
tldr: Removes an unused variable 'got_size' from the NDS32 ELF backend.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability and reducing build warnings.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Identified an unused variable causing build warnings and proposed its
    removal.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-nds32.c:154:13:\
    \ error: variable 'got_size' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since it was introduced by commit\n35c081572f32\
    \ (\"Add support for Andes NDS32:\", 2013-12-13).  Remove it,\nalong with the\
    \ comment that describes it.  The branches handling the\n.got and .…"
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Accepted the patch.
  quote: OK.
primer_expert: This patch cleans up the NDS32 ELF backend by removing an unused global
  variable 'got_size' that was identified by static analysis. The variable has been
  dead code since its introduction and its removal simplifies the section handling
  logic.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, shared libraries, and core dumps on Unix-like systems.
- term: NDS32
  definition: Andes NDS32, a 32-bit embedded processor architecture.
- term: .got
  definition: Global Offset Table. A section in ELF object files used for position-independent
    code to access global variables and function addresses.
- term: .got.plt
  definition: Global Offset Table for Procedure Linkage Table. Used in dynamically
    linked executables.
- term: .plt
  definition: Procedure Linkage Table. A section in ELF object files used for dynamically
    linked executables to resolve external function calls.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avKi01NkA5FRKAEF@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

A build warning from clang [-Wunused-but-set-global] identified an unused 'got_size' variable in the NDS32 ELF backend. This variable has been obsolete since 2013. The patch removes it and merges empty .got and .got.plt section handling into the .plt handling.
