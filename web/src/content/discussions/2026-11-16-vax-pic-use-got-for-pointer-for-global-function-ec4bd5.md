---
project: binutils
subsystem: vax
patch_id: null
tags:
- binutils
- gas
- vax
- PIC
- GOT
discussion_id: avtQ9VkPT8ZOox87@lug-owl.de
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX: PIC: Use GOT for pointer for global function'
tldr: A VAX assembler patch clarifies that global function pointers in PIC code should
  use the GOT, not the PLT, to avoid issues with lazy binding and differing addr…
proposer: Jan-Benedict Glaw <jbglaw@lug-owl.de>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Using GOT for function pointers ensures stable addresses but might incur a minor
  performance penalty compared to direct PLT calls if the function is called frequently
  before first resolution.
- Ensuring correct PIC behavior by using GOT for non-call/jump function references
  prevents runtime issues related to dynamic address resolution.
exchanges:
- author: Jan-Benedict Glaw <jbglaw@lug-owl.de>
  role: proposer
  position: Submits a patch and accompanying explanation clarifying that global function
    pointers in VAX PIC code should use the GOT, not the PLT, to ensure consistent
    addresses.
  quote: 'Only calls and jumps may go through the PLT.  Any other

    reference wants the address of the symbol and must use the

    GOT, also for a function: a PLT reference is turned into an

    indirect one through the function''s .got.plt slot, which

    holds the PLT entry until the lazy binding has happened, so

    the same function would have different addresses.'
primer_expert: This patch refines the VAX backend's handling of Position Independent
  Code (PIC) concerning global function pointers. Previously, the logic might have
  incorrectly allowed or implicitly used the PLT for non-call/jump references to global
  functions. This change explicitly directs such references to use the GOT. The reasoning
  is that the PLT is designed for indirect calls via a trampoline, and its contents
  are updated during lazy binding. Using the PLT for simply obtaining a function's
  address would result in a dynamic address (pointing to the PLT stub initially, then
  potentially the actual func…
primer_glossary:
- term: VAX
  definition: A defunct computer architecture developed by Digital Equipment Corporation
    (DEC), for which GCC has historical support.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. Essential for shared libraries.
- term: GOT
  definition: Global Offset Table. A data structure used in position-independent code
    to store addresses of global variables and functions.
- term: PLT
  definition: Procedure Linkage Table. A table used in position-independent code to
    resolve external function calls dynamically at runtime.
- term: lazy binding
  definition: A dynamic linking process where external function calls are resolved
    the first time they are invoked, rather than at program startup.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/avtQ9VkPT8ZOox87@lug-owl.de
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch revises the VAX assembler's logic for handling Position Independent Code (PIC) and global function pointers. It clarifies that direct references to global functions (other than calls and jumps) must use the Global Offset Table (GOT) to obtain the function's address. Using the Procedure Linkage Table (PLT) for non-call/jump references would lead to indirect references through a PLT entry, causing the function to have different addresses before and after lazy binding. The patch also introduces a new test case to verify this behavior.
