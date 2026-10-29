---
project: binutils
subsystem: binutils
patch_id: null
tags:
- cleanup
- dead code
- elf
discussion_id: auJ2yCpvnXwWfOD6@squeak.grove.modra.org
source_type: public_inbox
title: Remove moxie, msp and mt check_relocs
headline: Remove unused check_relocs functions for moxie, msp, and mt
tldr: Removes no-op `check_relocs` functions for moxie, msp, and mt ELF backends as
  they perform no useful work.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The `elf_backend_check_relocs` hook is intended for backends to perform
  validation on relocation entries before linking. For the moxie, msp430, and mt targets,
  these functions were either empty stubs or conditionally defined such that they
  never executed their logic. This patch removes these now-dead functions, cleaning
  up the BFD ELF backend implementation.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a low-level interface used by binutils
    for manipulating object files.
- term: ELF backend
  definition: A module within BFD that handles the specifics of the ELF object file
    format for a particular target architecture.
- term: check_relocs
  definition: A function within an ELF backend responsible for verifying the validity
    of relocation entries in an object file during the linking process.
- term: relocation entries
  definition: Data within an object file that specifies how to modify addresses in
    code or data when the object is linked, especially for position-independent code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ2yCpvnXwWfOD6@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch removes the `check_relocs` functions from the moxie, msp430, and mt ELF backends within BFD. These functions were found to do nothing and were not defined by the backend, making them redundant. Their removal simplifies the codebase by eliminating dead code.
