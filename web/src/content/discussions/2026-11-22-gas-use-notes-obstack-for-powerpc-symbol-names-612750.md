---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- powerpc
- memory leak
- obstack
discussion_id: loopr.29.6mbps0lhvfsl@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] gas: Use notes obstack for PowerPC symbol names'
headline: 'gas: Use notes obstack for PowerPC symbol names'
tldr: Fixes a memory leak in the PowerPC backend of GNU Assembler by using the notes
  obstack for symbol names.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Changes memory management strategy for PowerPC symbol names.
- Requires verification that the new allocation method is compatible with existing
  gas internals.
exchanges: []
primer_expert: The PowerPC backend for GAS (gas/config/tc-ppc.c) currently leaks memory
  due to `xstrndup` allocations for symbol names in `ppc_frob_symbol()`. These allocated
  buffers are never freed, leading to a leak for each symbol processed. This patch
  rectifies this by using `notes_memdup0()` which allocates memory on the notes obstack.
  This ensures that symbol names are managed and deallocated correctly alongside other
  gas symbol names, preventing the memory leak.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: Obstack
  definition: An object-stack data structure that allows for efficient allocation
    and deallocation of many small objects.
- term: PowerPC
  definition: A RISC instruction set architecture developed by Apple, IBM, and Motorola.
- term: ASan
  definition: AddressSanitizer, a memory error detector for C/C++.
- term: Symbol name
  definition: A human-readable identifier associated with a memory address or a variable
    in a program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.29.6mbps0lhvfsl@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This patch addresses a memory leak in the PowerPC configuration of GAS where allocated symbol names were not being freed. By switching the allocation mechanism from `xstrndup` to `notes_memdup0`, the symbol names are now managed by the notes obstack, ensuring they are cleaned up automatically with the rest of the gas symbol names. This change was tested on the current master branch.
