---
project: binutils
subsystem: vax
patch_id: null
tags:
- vax
- PIC
- gas
- bug fix
discussion_id: avBUEtDH6fRePqRH@lug-owl.de
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX: PIC: Use GOT for pointer for global function'
tldr: Reviewer confirms patch correctness but questions ticket closure.
proposer: Jan-Benedict Glaw <jbglaw@lug-owl.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Rin Okuyama
  role: proposer
  position: Submitted a patch to use GOT for function pointers in VAX PIC code, fixing
    Bug 32941.
  quote: 'Subject: [PATCH] VAX: PIC: Use GOT for pointer for global function


    in same file, instead of PLT


    This fixes the problem reported as Bug 32941: ...'
- author: Jan-Benedict Glaw
  role: reviewer
  position: Acknowledged the patch's correctness but questioned if the bug ticket
    should be closed, implying further action or confirmation might be needed.
  quote: The patch is correct, but I think I cannot close the ticket?
primer_expert: This discussion revolves around a patch for the VAX architecture's
  assembler (gas) concerning Position-Independent Code (PIC). The change modifies
  how global function calls are handled, specifically by using the Global Offset Table
  (GOT) instead of the Procedure Linkage Table (PLT) for function pointers. This aims
  to resolve a bug (32941) related to incorrect relocation types.
primer_glossary:
- term: VAX
  definition: A line of superminicomputers developed by Digital Equipment Corporation
    (DEC), known for its powerful instruction set architecture.
- term: PIC
  definition: Position-Independent Code is executable code that can run correctly
    regardless of where it is loaded in memory. This is crucial for shared libraries.
- term: GOT
  definition: Global Offset Table. A data structure used in a position-independent
    executable to store addresses of external functions and variables, allowing them
    to be accessed indirectly.
- term: PLT
  definition: Procedure Linkage Table. A table used in position-independent executables
    to resolve the addresses of dynamically linked functions at runtime.
- term: Bug 32941
  definition: A specific issue reported in the binutils bug tracking system, which
    this patch aims to fix.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/avBUEtDH6fRePqRH@lug-owl.de
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

Jan-Benedict Glaw reviewed a patch that uses GOT for function pointers in VAX PIC code, addressing Bug 32941. While agreeing the patch is correct, he expresses uncertainty about closing the associated bug ticket.
