---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- relocation
- got
- code
discussion_id: alpine.DEB.2.21.2608112135560.48788@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: bfin, frv, m68k, vax: got creation in check_relocs'
headline: 'bfin, frv, m68k, vax: got creation in check_relocs'
tldr: Call to create GOT section within `check_relocs` is acceptable due to idempotency.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Maciej W. Rozycki
  role: contributor
  position: States that calls to create GOT section functions are idempotent, thus
    the current placement within `check_relocs` is acceptable.
  quote: "I think the original intent was to call `_bfd_elf_create_got_section' \n\
    only once, at least from here. However calls to this function are \nidempotent,\
    \ so this change seems fine to me."
primer_expert: This discussion resolves a minor point of confusion regarding the placement
  of Global Offset Table (GOT) section creation calls within the `check_relocs` function
  in Binutils' BFD library. The concern was that the GOT might not be created under
  certain conditions (`!dynobj`). The consensus is that since the GOT creation functions
  are idempotent, their repeated or conditional calls do not cause issues, even if
  the original author's intent was different.
primer_glossary:
- term: GOT
  definition: Global Offset Table. A table used by position-independent code (PIC)
    to store addresses of global variables and functions. It allows code to access
    data and functions regardless of its final load address.
- term: check_relocs
  definition: A function within the Binutils BFD library responsible for checking
    relocation entries in an object file.
- term: dynobj
  definition: Dynamic object. Refers to an executable or shared library that is linked
    and loaded at runtime.
- term: idempotent
  definition: An operation is idempotent if applying it multiple times has the same
    effect as applying it once.
- term: BFD
  definition: Binary File Descriptor library. A library provided by GNU binutils that
    provides a generic interface to a wide variety of object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2608112135560.48788@angie.orcam.me.uk
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Alan Modra questioned the correctness of calling GOT section creation functions within a `!dynobj` check in `check_relocs`, as it was not obvious if the GOT section would always be created. Maciej W. Rozycki confirms that while the original intent might have been to call it only once, the functions are idempotent, making the current calls acceptable.
