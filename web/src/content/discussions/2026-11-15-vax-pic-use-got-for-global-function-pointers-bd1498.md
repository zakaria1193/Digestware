---
project: binutils
subsystem: vax
patch_id: null
tags:
- binutils
- vax
- pic
- linker
- got
discussion_id: avmxQky25wVi-ug_@lug-owl.de
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX PIC: Use GOT for global function pointers'
tldr: Patch modifies VAX PIC to use GOT for global function pointers instead of PLT,
  fixing Bug 32941.
proposer: Jan-Benedict Glaw <jbglaw@lug-owl.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Using GOT for global function pointers may simplify address calculation compared
  to PLT indirections, but requires careful management of GOT entries.
- The change impacts how function calls are resolved in PIC code, potentially affecting
  performance or ABI compatibility if not handled correctly.
exchanges:
- author: Rin Okuyama
  role: proposer
  position: Submitted a patch to use GOT instead of PLT for global function pointers
    in VAX PIC, fixing Bug 32941.
  quote: 'Subject: [PATCH] VAX: PIC: Use GOT for pointer for global function


    in same file, instead of PLT


    This fixes the problem reported as Bug 32941: https://sourceware.org/bugzilla/show_bug.cgi?id=32941'
- author: Jan-Benedict Glaw
  role: reviewer
  position: Intends to commit the fix, including Rin Okuyama's patch and an added
    test case.
  quote: 'I intend to commit the following patch, containing your fix and adding a
    testcase for it:'
primer_expert: This discussion concerns a fix for Position-Independent Code (PIC)
  generation on the VAX architecture within the GNU assembler. The core issue, Bug
  32941, is resolved by changing how global function calls are handled. Instead of
  always using the PLT (Procedure Linkage Table), the code now defaults to using the
  GOT (Global Offset Table) for function pointers. This is because indirect function
  calls through the PLT can introduce an extra indirection via the `.got.plt` slot,
  which holds the PLT entry, potentially leading to different effective addresses
  compared to a direct GOT lookup for the fu…
primer_glossary:
- term: Position-Independent Code (PIC)
  definition: Code that can run correctly regardless of where it is loaded in memory,
    crucial for shared libraries.
- term: VAX
  definition: A 32-bit complex instruction set computer (CISC) architecture developed
    by Digital Equipment Corporation (DEC).
- term: GOT
  definition: Global Offset Table. A data structure used in executable files and shared
    libraries to provide an indirection layer for global variables and functions,
    allowing them to be accessed at a fixed offset from the program counter, which
    is essential for PIC.
- term: PLT
  definition: Procedure Linkage Table. A table used in executable files and shared
    libraries to resolve indirect function calls, typically used for calls to functions
    in other shared libraries.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avmxQky25wVi-ug_@lug-owl.de
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This patch revises the VAX PIC (Position-Independent Code) generation to use the Global Offset Table (GOT) for pointers to global functions, rather than the Procedure Linkage Table (PLT). This change addresses Bug 32941, which likely involved incorrect function resolution or addressing in PIC code on VAX. The provided code snippet modifies `gas/config/tc-vax.c` to adjust relocation type selection for function calls and jumps.
