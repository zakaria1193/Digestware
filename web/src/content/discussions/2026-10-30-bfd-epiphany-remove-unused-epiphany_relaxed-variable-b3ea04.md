---
project: binutils
subsystem: bfd/epiphany
patch_id: null
tags:
- BFD
- Epiphany
- compiler warnings
- code cleanup
discussion_id: 20261030150008.1142901-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH] bfd/epiphany: remove unused epiphany_relaxed variable'
headline: 'bfd/epiphany: remove unused epiphany_relaxed variable'
tldr: Removes an unused 'epiphany_relaxed' variable from the Epiphany BFD backend
  to fix compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes unused code and resolves compiler warnings with no functional impact.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to remove the unused 'epiphany_relaxed' variable from
    the Epiphany BFD backend. This variable has been unused since 2011 and causes
    compiler warnings. The patch also simplifies the `epiphany_elf_relax_section`
    function.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-epiphany.c:45:13:\
    \ error: variable 'epiphany_relaxed' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since the epiphany port was added in commit\ncfb8c0921c8a\
    \ (2011-10-25).  Remove it."
primer_expert: This patch targets the BFD (Binary File Descriptor) library's Epiphany
  backend. It removes a boolean global variable `epiphany_relaxed` from `bfd/elf32-epiphany.c`.
  This variable has been unused since the Epiphany port was initially added in commit
  cfb8c0921c8a in 2011. The compiler, specifically clang with `-Wunused-but-set-global`,
  flags this variable as unused. The patch also streamlines the `epiphany_elf_relax_section`
  function by removing the now-unnecessary assignment to this variable.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A part of GNU Binutils that provides
    a common interface for reading and writing various object file formats.
- term: Epiphany
  definition: A VLIW (Very Long Instruction Word) processor architecture developed
    by Adapteva, often used in low-power parallel processing applications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261030150008.1142901-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch removes the 'epiphany_relaxed' boolean variable from the Epiphany BFD backend, as it has been unused since the port's introduction in 2011. This resolves compiler warnings about unused global variables. The code that previously set this variable is also removed, simplifying the `epiphany_elf_relax_section` function.
