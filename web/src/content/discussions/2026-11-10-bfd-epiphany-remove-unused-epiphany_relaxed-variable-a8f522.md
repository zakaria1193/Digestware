---
project: binutils
subsystem: bfd/epiphany
patch_id: null
tags:
- epiphany
- bfd
- cleanup
- build
discussion_id: avKilSpeUXbG2Yon@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] bfd/epiphany: remove unused epiphany_relaxed variable'
headline: 'bfd/epiphany: remove unused epiphany_relaxed variable'
tldr: Removes an unused variable 'epiphany_relaxed' from the Epiphany ELF backend.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability and reducing build warnings.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Identified an unused variable causing build warnings and proposed its
    removal.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-epiphany.c:45:13:\
    \ error: variable 'epiphany_relaxed' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since the epiphany port was added in commit\ncfb8c0921c8a\
    \ (2011-10-25).  Remove it."
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Accepted the patch.
  quote: OK.
primer_expert: This patch removes a dead global variable from the Epiphany BFD backend.
  The variable was introduced with the initial support for the Epiphany architecture
  and has not been used since.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to parse and manipulate object files from various architectures and formats.
- term: Epiphany
  definition: A Tensilica configurable processor core, often used in embedded systems.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, shared libraries, and core dumps on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avKilSpeUXbG2Yon@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

A clang build warning highlighted an unused variable 'epiphany_relaxed' in the Epiphany ELF backend, which has been obsolete since 2011. The patch removes this variable to clean up the code.
