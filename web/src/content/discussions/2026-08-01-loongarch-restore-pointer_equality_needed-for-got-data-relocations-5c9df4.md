---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- relocations
- got
- linker
discussion_id: 6a024beec3770ba7f563e1fc1632d41a44fa9264.camel@xry111.site
source_type: public_inbox
title: 'Re: [Patch] LoongArch: Restore pointer_equality_needed for GOT data relocations'
headline: 'LoongArch: Restore pointer_equality_needed for GOT data relocations'
tldr: Developer questions the rationale for restoring `pointer_equality_needed` for
  GOT data relocations, arguing it's irrelevant for data symbols.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Balancing the fix for PR 29655 (function pointer equality in PIE) with the correct
  handling of data symbol access via GOT.
- Determining the correct usage of `pointer_equality_needed` for different symbol
  types (function vs. data).
- Ensuring ABI compatibility and runtime stability across various linking scenarios
  (static, dynamic, PIE).
exchanges:
- author: Xi Ruoyao <xry111@xry111.site>
  role: proposer
  position: Questions the reasoning behind restoring `pointer_equality_needed` for
    GOT data relocations, stating it's unrelated to data symbols and suggests the
    problem might be more systemic.
  quote: 'This does not make sense to me.  Global data symbols are accessed via

    R_LARCH_GOT_PC_HI20 everywhere, not only the CRT startup code.  Thus if

    accessing data symbols with R_LARCH_GOT_PC_HI20 is broken we''d have a

    much more wide-spreading breakage.


    Pointer equality matters because

    if you end up comparing the address of the PLT stub and the address of

    the real function you''d break pointer equality.…'
primer_expert: This discussion revolves around a disagreement concerning the handling
  of `pointer_equality_needed` for LoongArch GOT relocations in binutils. A previous
  commit removed this flag for GOT relocations to fix PR 29655 (function pointer equality
  in PIE). However, this caused issues with data symbols accessed via GOT relocations
  in static executables. The poster argues that `pointer_equality_needed` is irrelevant
  for data symbols and questions the proposed fix of selectively re-enabling it.
primer_glossary:
- term: pointer_equality_needed
  definition: A flag used in relocation processing that indicates whether comparing
    addresses of PLT stubs and actual function symbols could lead to incorrect results,
    particularly in PIE executables.
- term: GOT
  definition: Global Offset Table, a table used in position-independent code to store
    addresses of global variables and functions, allowing them to be accessed indirectly.
- term: relocations
  definition: Information in an object file that describes how to modify parts of
    the code or data when linking, such as resolving symbol addresses.
- term: PIE
  definition: Position-Independent Executable, an executable that can be loaded at
    any memory address.
- term: PLT stub
  definition: A small piece of code in the Procedure Linkage Table that acts as an
    intermediary to resolve and jump to a dynamically linked function.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/6a024beec3770ba7f563e1fc1632d41a44fa9264.camel@xry111.site
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

Xi Ruoyao expresses skepticism regarding a proposed patch to restore `pointer_equality_needed` for LoongArch GOT data relocations. He argues that this flag is relevant only for function symbols to ensure pointer equality between PLT stubs and actual functions, and has no bearing on data symbols, suggesting the observed breakage for data symbols implies a more widespread issue than the patch addresses.
