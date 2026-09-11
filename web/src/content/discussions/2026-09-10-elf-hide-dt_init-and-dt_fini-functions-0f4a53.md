---
project: binutils
subsystem: elf
patch_id: null
tags:
- ELF
- linker
- symbols
- dynamic linking
discussion_id: CAMe9rOqYe=QBuWsWaNESBTn3EN4_p1EvpObHQN2XL57GGQCgyA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] elf: Hide DT_INIT and DT_FINI functions'
headline: 'elf: Hide DT_INIT and DT_FINI functions'
tldr: Hides DT_INIT and DT_FINI functions from the dynamic symbol table to resolve
  linker issues.
proposer: H.J. Lu
consensus: Under Review
outcome: under_review
impact_score: 5
sentiment_score: 5
technical_tradeoffs:
- Hides symbols that might otherwise be useful for introspection or debugging, but
  are not intended for external dynamic linking.
- Addresses a potential for symbol conflicts or misinterpretation by ensuring only
  necessary symbols are exported.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to hide DT_INIT and DT_FINI functions from the dynamic
    symbol table.
  quote: Hide special functions used by linker to define DT_INIT and DT_FINI in executable
    and shared library so that they won't be in dynamic symbol table.
- author: Sam James
  role: reviewer
  position: Acknowledges the patch and its description.
  quote: null
- author: Alan Modra
  role: reviewer
  position: Acknowledges the patch and its description.
  quote: null
- author: Jan Beulich
  role: reviewer
  position: Questions the necessity of the patch, noting that hidden symbols should
    not be in the dynamic symbol table and suggesting it might mask an underlying
    issue.
  quote: 'I still don''t quite understand: In reply to my comment on the original,
    combined patch you said the symbols are hidden. Hidden symbols shouldn''t be making
    it into the dynamic symbol table anyway. IOW - are you papering over an issue
    elsewhere?'
- author: H.J. Lu
  role: proposer
  position: Clarifies that the symbols are hidden within glibc, implying a context-specific
    hiding mechanism.
  quote: I said they are hidden in glibc.
primer_expert: This patch addresses linker behavior for ELF binaries, specifically
  concerning the `DT_INIT` and `DT_FINI` dynamic table entries. These entries point
  to initialization and termination functions. The change aims to prevent symbols
  associated with these functions from being exported to the dynamic symbol table,
  potentially simplifying symbol resolution and preventing conflicts, particularly
  when these symbols are handled differently across libraries (e.g., glibc).
primer_glossary:
- term: DT_INIT
  definition: A dynamic table entry (DT_INIT) in an ELF executable or shared library
    that specifies the address of the initialization function to be called when the
    library is loaded.
- term: DT_FINI
  definition: A dynamic table entry (DT_FINI) in an ELF executable or shared library
    that specifies the address of the termination function to be called when the library
    is unloaded.
- term: dynamic symbol table
  definition: A section in an ELF file (usually .dynsym) that contains symbols necessary
    for dynamic linking, such as imported and exported functions and variables.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program, resolving external references between them.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqYe=QBuWsWaNESBTn3EN4_p1EvpObHQN2XL57GGQCgyA@mail.gmail.com
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch proposes to hide the special functions used by the linker to define DT_INIT and DT_FINI in executables and shared libraries. The goal is to prevent these functions from appearing in the dynamic symbol table, addressing issues related to their handling. The patch includes modifications to `bfd/elflink.c` and adds new test cases in `ld/testsuite/ld-elf`.
