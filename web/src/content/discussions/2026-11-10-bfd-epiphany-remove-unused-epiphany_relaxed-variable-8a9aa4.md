---
project: binutils
subsystem: bfd/epiphany
patch_id: null
tags:
- cleanup
- bfd
- epiphany
- compiler warnings
discussion_id: 2e9ee958-6fe1-4c7d-836f-c3d5a12e0c0a@efficios.com
source_type: public_inbox
title: 'Re: [PATCH] bfd/epiphany: remove unused epiphany_relaxed variable'
headline: 'bfd/epiphany: remove unused epiphany_relaxed variable'
tldr: Removes an unused variable `epiphany_relaxed` from the BFD epiphany backend
  after it was identified as unused and flagged by a compiler warning.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability.
- Addresses compiler warnings.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the `epiphany_relaxed` variable because it is set but
    unused, causing compiler warnings.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-epiphany.c:45:13:\
    \ error: variable 'epiphany_relaxed' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since the epiphany port was added in commit\ncfb8c0921c8a\
    \ (2011-10-25).  Remove it."
- author: Alan Modra
  role: reviewer
  position: Agrees with the removal of the unused variable.
  quote: OK.
- author: Simon Marchi
  role: proposer
  position: Confirms the patch has been applied.
  quote: null
primer_expert: This is a cleanup patch for the BFD backend supporting the Epiphany
  architecture. It removes a global variable, `epiphany_relaxed`, from `bfd/elf32-epiphany.c`
  that has been syntactically present but functionally unused since the initial introduction
  of the Epiphany port. A recent compiler (Clang) with stricter warning flags (`-Werror=unused-but-set-global`)
  flagged this variable, prompting its removal to maintain code hygiene.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to abstract over various object file formats (like ELF, a.out, COFF).
- term: Epiphany
  definition: A VLIW (Very Long Instruction Word) processor architecture, often used
    in embedded systems and accelerators.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: unused-but-set-global
  definition: A compiler warning indicating that a global variable has been assigned
    a value but is never subsequently read or used.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2e9ee958-6fe1-4c7d-836f-c3d5a12e0c0a@efficios.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch removes the `epiphany_relaxed` variable from the BFD epiphany backend code. The variable was identified as being set but never used, triggering a compiler warning with `-Werror=unused-but-set-global`. It has been unused since the epiphany port was initially added to binutils in 2011.
