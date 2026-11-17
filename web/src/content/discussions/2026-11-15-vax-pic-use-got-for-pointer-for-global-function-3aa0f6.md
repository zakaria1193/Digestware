---
project: binutils
subsystem: vax
patch_id: null
tags:
- binutils
- gas
- VAX
- PIC
- linking
discussion_id: 20250505054546.B078184D31@mail.netbsd.org
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX: PIC: Use GOT for pointer for global function'
tldr: Maintainer intends to commit a patch and add a test case to fix VAX PIC issues
  related to global function pointers, resolving a reported bug.
proposer: Jan-Benedict Glaw <jbglaw@lug-owl.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 9
technical_tradeoffs: []
exchanges:
- author: Rin Okuyama
  role: proposer
  position: Submitted a patch to address a bug in VAX PIC handling of global function
    pointers.
  quote: 'in same file, instead of PLT


    This fixes the problem reported as Bug 32941: https://sourceware.org/bugzilla/show_bug.cgi?id=32941'
- author: Jan-Benedict Glaw
  role: maintainer
  position: Intends to commit the proposed patch after adding a test case, confirming
    it addresses the reported bug.
  quote: 'I intend to commit the following patch, containing your fix and adding a
    testcase for it:'
primer_expert: This patch modifies the VAX gas backend's handling of Position-Independent
  Code (PIC). It changes the relocation type used for indirect global function calls
  from PLT-relative to GOT-relative. This addresses a bug where PLT indirection can
  lead to incorrect function addresses after lazy binding, particularly affecting
  function pointers. The change also refines the logic for when to use PLT vs. GOT
  for indirect branches.
primer_glossary:
- term: VAX
  definition: A discontinued 32-bit computer architecture developed by Digital Equipment
    Corporation (DEC).
- term: PIC
  definition: Position-Independent Code. Code that can run correctly regardless of
    where it is loaded in memory. Essential for shared libraries.
- term: GOT
  definition: Global Offset Table. A table used in PIC code to store addresses of
    global variables and functions, allowing them to be accessed indirectly.
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to resolve function calls to external libraries at runtime.
- term: 'Bugzilla #32941'
  definition: A specific bug report filed on the Sourceware Bugzilla site, detailing
    an issue with VAX PIC global function pointer handling.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avmxQky25wVi-ug_@lug-owl.de
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This discussion centers on a patch for the VAX architecture that modifies how Procedure Call Standard (PCS) or Position-Independent Code (PIC) handles global function pointers. The patch aims to use the Global Offset Table (GOT) instead of the Procedure Linkage Table (PLT) for function pointers to resolve an issue reported in Bugzilla #32941. The maintainer intends to commit this fix along with a new test case.
