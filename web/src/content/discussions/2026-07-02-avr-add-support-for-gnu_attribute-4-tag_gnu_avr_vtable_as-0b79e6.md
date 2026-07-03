---
project: binutils
subsystem: avr
patch_id: null
tags:
- AVR
- binutils
- ELF
- attributes
- virtual tables
discussion_id: 701a37e4-9249-4c5e-abf5-de05c2cc3bec@gjlay.de
source_type: public_inbox
title: '[patch] AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
headline: 'AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
tldr: Adds support for a new ELF attribute to tag AVR object files with virtual table
  address space information.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new ELF attribute, requiring compiler and linker support.
- Enables ABI compatibility checks for vtable placement, potentially at the cost of
  slight complexity in object file interpretation.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Submits a patch to add support for the `.gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)`
    ELF attribute for AVR targets, enabling the tagging of virtual table address spaces.
  quote: null
primer_expert: This patch for binutils' AVR backend introduces a new ELF attribute
  (`Tag_GNU_AVR_VTABLE_AS`) to specify the memory address space for C++ virtual tables.
  This feature is driven by upcoming G++ support for ISO/IEC TR 18037 named address
  spaces, allowing vtables to be placed in non-default memory regions like FLASH to
  save RAM. The attribute provides a mechanism for ABI compatibility by defining values
  that indicate the vtable address space, enabling detection of mismatches between
  object files and ensuring proper linker behavior.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology)
    commonly used in embedded systems.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: GNU attribute
  definition: An extension to the ELF format that allows compilers and linkers to
    convey additional information about the program or its sections.
- term: VTABLE
  definition: Virtual Table, a data structure used by C++ compilers to implement virtual
    function calls. It typically contains pointers to the virtual functions of a class.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/701a37e4-9249-4c5e-abf5-de05c2cc3bec@gjlay.de
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

A patch introduces support for `.gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)` in binutils for AVR targets. This new ELF attribute allows object files to specify where virtual tables are stored (e.g., RAM or different FLASH memory regions). This is crucial for upcoming G++ support for C++ virtual tables in named address spaces, as it enables ABI compatibility checks and prevents RAM wastage on systems where code and data reside in separate memory spaces. The attribute defines various values, including none, RAM, and distinct FLASH memory regions, with a compatibility mechanism for future extensions.
