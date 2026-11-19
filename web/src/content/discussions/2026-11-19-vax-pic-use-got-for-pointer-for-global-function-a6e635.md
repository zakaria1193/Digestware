---
project: binutils
subsystem: vax
patch_id: null
tags:
- vax
- pic
- linker
- abi
- optimization
discussion_id: 839774b3-6729-4945-b0bb-3dce0fc9cc19@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX: PIC: Use GOT for pointer for global function'
tldr: Refines VAX PIC support by ensuring global function calls use the GOT for indirect
  access, improving ABI compliance.
proposer: Rin Okuyama <rokuyama.rk@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct ABI compliance for VAX PIC.
- Introduces a new test case to verify the correct behavior.
exchanges:
- author: Jan-Benedict Glaw
  role: proposer
  position: Proposes changes to VAX PIC support to correctly handle global function
    calls via the GOT.
  quote: 'Only calls and jumps may go through the PLT.  Any other

    reference wants the address of the symbol and must use the

    GOT, also for a function: a PLT reference is turned into an

    indirect one through the function''s .got.plt slot, which

    holds the PLT entry until the lazy binding has happened, so

    the same function would have different addresses.'
- author: Rin Okuyama
  role: contributor
  position: Reviews the patch and asks for clarification on the specific changes and
    their implications for VAX PIC.
  quote: "Hi,\n\nOn 2026/11/17 3:52, Jan-Benedict Glaw wrote:\n> Hi,\n>\n> On Sun,\
    \ 2026-11-15 14:18:58 +0100, Jan-Benedict Glaw <jbglaw@lug-owl.de> wrote:\n>>\
    \ diff --git a/gas/config/tc-vax.c b/gas/config/tc-vax.c\n>> index 3d21796..614cc8d\
    \ 100644\n>> --- a/gas/config/tc-vax.c\n>> +++ b/gas/config/tc-vax.c\n>> @@ -399,7\
    \ +399,13 @@ md_estimate_size_before_relax (fragS *fragP, segT segment)\n>>  \
    \ \t          || S_IS_EXT…"
primer_expert: This patch revises the PIC code generation for the VAX architecture,
  specifically within `gas/config/tc-vax.c`, to align with ABI requirements for global
  function calls. Previously, indirect references to functions might have been misclassified,
  potentially leading to incorrect use of the PLT (Procedure Linkage Table) for non-call/jump
  instructions. The change ensures that any reference to a global function's address,
  if not a direct call/jump, is handled via the GOT (Global Offset Table), using its
  `.got.plt` slot, thus maintaining correct runtime addresses irrespective of lazy
  binding.
primer_glossary:
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. Essential for shared libraries.
- term: GOT
  definition: Global Offset Table. A table used in PIC executables and shared libraries
    to store addresses of external symbols or global variables, allowing indirect
    access.
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables to resolve
    external function calls at runtime, especially in the context of PIC and shared
    libraries.
- term: VAX
  definition: A legacy minicomputer instruction set architecture developed by Digital
    Equipment Corporation (DEC).
- term: ABI
  definition: Application Binary Interface. Defines how compiled code for different
    components should interact, including function calling conventions, data structures,
    and system calls.
- term: Lazy Binding
  definition: A runtime linking technique where symbols are resolved only when they
    are first called, improving startup performance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/839774b3-6729-4945-b0bb-3dce0fc9cc19@gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch clarifies the VAX Position-Independent Code (PIC) generation, specifically how global function calls are handled. It refines the logic in `gas/config/tc-vax.c` to ensure that indirect references to global functions, which are not direct calls or jumps, correctly use the Global Offset Table (GOT). This change prevents issues where a PLT reference might lead to an incorrect address due to the indirection through the PLT entry before lazy binding occurs.
