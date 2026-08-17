---
project: binutils
subsystem: avr
patch_id: null
tags:
- avr
- gnu-attribute
- ABI
- vtable
- embedded
discussion_id: d4cb40a0-435c-4688-9088-d782ef9f2226@gjlay.de
source_type: public_inbox
title: 'Re: [patch, ping, pushed] AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
headline: 'AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
tldr: Binutils gains support for a new .gnu_attribute to specify AVR vtable address
  spaces, enabling ABI-aware vtable placement.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Committed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables memory optimization for C++ virtual tables on AVR.
- Introduces ABI awareness for vtable placement.
- Requires parsing and handling a new ELF attribute.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Submitted a patch to support `.gnu_attribute 4` for AVR vtable address
    spaces, enabling ABI-aware placement and preventing wasted RAM. Notes adjustments
    were needed due to generic `.gnu-attribute` handling.
  quote: 'The upcoming support for ISO/IEC TR 18037 "Embedded C" named address spaces
    in G++ would allow to put C++ virtual tables into such an address spaces, see
    https://gcc.gnu.org/PR69549.


    The current address space used for vtables is the generic one, which means that
    RAM is wasted on machines where .rodata is located in RAM.


    The TARGET_ADDR_SPACE_FOR_ARTIFICIAL_RODATA GCC target hook allows to chose…'
primer_expert: This patch adds support for the `Tag_GNU_AVR_VTABLE_AS` attribute in
  the `.gnu-attribute` section for AVR targets. This is crucial for upcoming C++ ABI
  changes in GCC that allow virtual tables to be placed in specialized memory spaces
  (e.g., `__flash`) instead of generic RAM, optimizing memory usage. Binutils now
  needs to parse and store this tag to ensure ABI compatibility.
primer_glossary:
- term: .gnu_attribute
  definition: An ELF section used to store arbitrary metadata about an object file,
    often used by toolchains for target-specific information.
- term: AVR
  definition: A family of microcontrollers from Atmel (now Microchip Technology),
    commonly used in embedded systems.
- term: virtual table
  definition: A data structure used in C++'s implementation of polymorphism. It stores
    pointers to the virtual functions of a class.
- term: ABI
  definition: Application Binary Interface. Defines how low-level code, like compiled
    object files and libraries, interact.
- term: Tag_GNU_AVR_VTABLE_AS
  definition: A specific tag within the .gnu_attribute section for AVR targets, indicating
    the intended address space for virtual tables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/d4cb40a0-435c-4688-9088-d782ef9f2226@gjlay.de
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay's patch adds support for `.gnu_attribute 4` (Tag_GNU_AVR_VTABLE_AS) to binutils. This allows C++ compilers to tag object files with information about where virtual tables should be placed, supporting new address spaces like `__flash` and enabling ABI compatibility checks. The implementation required adjustments to generic `.gnu-attribute` handling.
