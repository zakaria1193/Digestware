---
project: binutils
subsystem: bfd/nds32
patch_id: null
tags:
- cleanup
- build
- linker
- nds32
discussion_id: 20261019193231.1708375-4-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 03/18] bfd/nds32: remove unused got_size variable'
headline: 'bfd/nds32: remove unused got_size variable'
tldr: Remove unused `got_size` variable from Andes NDS32 ELF support.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code and simplifies section handling logic.
- Resolves build warnings and cleans up the codebase.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `got_size` variable from `elf32-nds32.c`,
    which causes build errors.
  quote: "Building bfd with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/bfd/elf32-nds32.c:154:13:\
    \ error: variable 'got_size' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe variable has been unused since it was introduced by commit\n35c081572f32\
    \ (\"Add support for Andes NDS32:\", 2013-12-13).  Remove it,\nalong with the\
    \ comment that describes it.  The branches handling the\n.got and .…"
primer_expert: This patch removes an unused variable `got_size` and associated logic
  from `bfd/elf32-nds32.c`. This variable was intended to track the size of Global
  Offset Table (GOT) sections for the Andes NDS32 architecture but has been unused
  since its introduction in 2013. The `nds32_elf_late_size_sections` function, which
  used `got_size`, now has its logic for `.got` and `.got.plt` sections merged with
  the handling for `.plt`, as these sections are not independently managed in this
  context. The change resolves a compiler warning and simplifies the code.
primer_glossary:
- term: Global Offset Table (GOT)
  definition: A table used in position-independent executable (PIE) code to store
    addresses of external functions and variables, allowing them to be resolved at
    runtime.
- term: bfd.h
  definition: Header file for the Binary File Descriptor (BFD) library, which provides
    a common interface to manipulate various executable file formats.
- term: nds32
  definition: A 32-bit instruction set architecture developed by Andes Technology
    Corporation.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
series_id: 'binutils:bfd/nds32: remove unused got_size variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-4-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi is removing the `got_size` variable from the Andes NDS32 ELF support in `bfd/elf32-nds32.c`. This variable has been unused since its introduction in 2013 and causes a build failure with recent Clang versions due to the `-Wunused-but-set-global` warning. The patch also merges sections related to `.got` and `.got.plt` into the `.plt` handling.
