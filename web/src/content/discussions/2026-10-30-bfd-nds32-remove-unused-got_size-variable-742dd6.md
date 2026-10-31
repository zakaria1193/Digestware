---
project: binutils
subsystem: bfd/nds32
patch_id: null
tags:
- BFD
- NDS32
- compiler warnings
- code cleanup
discussion_id: 20261030150041.1145882-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH] bfd/nds32: remove unused got_size variable'
headline: 'bfd/nds32: remove unused got_size variable'
tldr: Removes an unused 'got_size' variable from the NDS32 BFD backend to resolve
  compiler warnings.
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
  position: Submits a patch to remove the unused 'got_size' variable from the NDS32
    BFD backend. This variable has been unused since 2013 and causes compiler warnings.
    The patch also merges related section handling code.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-nds32.c:154:13:\
    \ error: variable 'got_size' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since it was introduced by commit\n35c081572f32\
    \ (\"Add support for Andes NDS32:\", 2013-12-13).  Remove it,\nalong with the\
    \ comment that describes it.  The branches handling the\n.got and .…"
primer_expert: This patch targets the BFD (Binary File Descriptor) library's NDS32
  backend. It removes a global variable `got_size` from `bfd/elf32-nds32.c` that has
  been unused since commit 35c081572f32 added NDS32 support in 2013. The compiler,
  specifically clang with `-Wunused-but-set-global`, flags this variable. The removal
  simplifies the code and consolidates the handling of sections related to the Global
  Offset Table (`.got`, `.got.plt`) and Procedure Linkage Table (`.plt`) by merging
  logic within the `nds32_elf_late_size_sections` function.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A part of GNU Binutils that provides
    a common interface for reading and writing various object file formats.
- term: NDS32
  definition: A 32-bit processor architecture developed by Andes Technology Corporation,
    often used in embedded systems.
- term: GOT
  definition: Global Offset Table. A table used by position-independent executable
    code to store addresses of external functions and variables, allowing them to
    be resolved at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261030150041.1145882-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch removes the 'got_size' variable from the NDS32 BFD backend, as it has been unused since its introduction in 2013. This resolves compiler warnings related to unused global variables. Additionally, the code that handled the .got and .got.plt sections is merged with the .plt section handling for cleaner code.
