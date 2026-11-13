---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- linker
- dynamic symbols
- GOT
- PLT
discussion_id: 20261112115654.1527835-2-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH] s390: Do not force symbol dynamic unless it is undefined weak'
headline: 's390: Do not force symbol dynamic unless it is undefined weak'
tldr: Fixes an issue where symbols were incorrectly marked as dynamic in s390 linking,
  potentially causing interposition errors and assertion failures.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes assertion failures and prevents unintended symbol interposition by restricting
  symbols marked as dynamic, potentially simplifying symbol resolution at the cost
  of requiring explicit handling for symbols that truly need dynamic behavior.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Proposes a change to s390 linker behavior to only force undefined weak
    symbols to be dynamic.
  quote: 'Linking a PIE with a global symbol whose only GOT reference is in a

    discarded section fails with the assertion ((h->got.offset & 1) != 0) in

    finish_dynamic_symbol. ... Forcing such symbols dynamic is also wrong independent
    of discarded

    sections. ... Align with x86-64 commit 9e9821ddd80c ("x86-64: Force symbol dynamic
    if

    it isn''t undefined weak"), RISC-V commit 9e10fcf71c11 ("RISC-V: Fix the

    asser…'
primer_expert: 'The s390 linker incorrectly marks symbols as dynamic when they have
  GOT/PLT references or dynamic relocations, even if they are not intended to be exported
  or dynamically resolved. This leads to two main problems: 1) Assertion failures
  in `finish_dynamic_symbol` when references are in discarded sections, as the GOT
  entry is prepared but not initialized. 2) Unintended symbol interposition, where
  such symbols can shadow identically named symbols in other shared objects, contrary
  to the developer''s intent. This patch modifies `allocate_dynrelocs` to only mark
  undefined weak symbols as dynamic, a…'
primer_glossary:
- term: GOT
  definition: Global Offset Table. A table used in position-independent code to store
    addresses of global variables and functions, allowing indirect access.
- term: PLT
  definition: Procedure Linkage Table. A table used in position-independent code to
    resolve calls to functions in shared libraries.
- term: PIE
  definition: Position-Independent Executable. An executable program that can be loaded
    and run at any memory address.
- term: dynamic symbol
  definition: A symbol that needs to be resolved at runtime by the dynamic linker.
    This includes symbols used by shared libraries or exported by the executable.
- term: interposition
  definition: The ability for a symbol in one shared object (or executable) to mask
    a symbol of the same name in another shared object. This is usually done for debugging
    or security purposes but can be unintended.
- term: undefined weak symbol
  definition: A symbol that is declared but not defined, and is considered 'weak'.
    Weak symbols have lower precedence than defined symbols and can be overridden
    by defined symbols or other weak symbols.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261112115654.1527835-2-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This patch corrects how the s390 linker handles dynamic symbols. Previously, symbols with GOT or PLT references, or dynamic relocations in non-PIC links, were unnecessarily forced into the dynamic symbol table. This could lead to assertion failures, as seen with discarded sections, and allow unintended symbol interposition. The fix aligns s390 with other targets by only marking undefined weak symbols as dynamic, thus preventing these issues.
