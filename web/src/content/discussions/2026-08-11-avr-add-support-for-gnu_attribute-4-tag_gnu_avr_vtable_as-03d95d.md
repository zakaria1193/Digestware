---
project: binutils
subsystem: avr
patch_id: null
tags:
- binutils
- avr
- elf
- attribute
- abi
discussion_id: 8c8b10c8-762b-4845-a2a5-c00167bb89e8@gjlay.de
source_type: public_inbox
title: '[patch, ping] AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
headline: 'AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
tldr: Introduce .gnu_attribute 4 to tag AVR object files with vtable address space
  information, supporting ABI compatibility.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables ABI compatibility for vtable placement by providing a mechanism to tag object
  files.
- Introduces a new ELF attribute, potentially increasing the complexity of ELF parsing
  for tools.
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Proposes adding `.gnu_attribute 4` to Binutils for AVR to tag object files
    with vtable address space information, enabling ABI compatibility.
  quote: "The feature of choice is .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)\nwhich\
    \ would tag an object file with one of the following values:\n\n0 (Val_GNU_AVR_VTABLE_NONE)\
    \ for files that neither define nor access \nvtables.\n1 (Val_GNU_AVR_VTABLE_RAM)\
    \ use the generic address space.\n2 (Val_GNU_AVR_VTABLE_FLASH) use the 16-bit\
    \ address space __flash.\n3 (Val_GNU_AVR_VTABLE_FLASH1) use the 16-bit address\
    \ space __fl…"
primer_expert: This patch introduces support for a new GNU attribute, `Tag_GNU_AVR_VTABLE_AS`,
  to Binutils for the AVR target. This attribute is designed to inform the linker
  and other tools about the address space where C++ virtual tables (vtables) are placed.
  This is important because G++ is gaining the ability to place vtables in non-default
  address spaces (e.g., FLASH) via the `TARGET_ADDR_SPACE_FOR_ARTIFICIAL_RODATA` hook.
  Placing vtables in a different address space constitutes an ABI change. The `Tag_GNU_AVR_VTABLE_AS`
  attribute allows object files to declare their vtable address space, enabling ABI…
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology).
    Binutils provides support for targeting these processors.
- term: .gnu_attribute
  definition: An ELF section used to store arbitrary attributes associated with an
    object file or its contents. These attributes can provide information for tools
    like linkers, debuggers, or compilers.
- term: Tag_GNU_AVR_VTABLE_AS
  definition: A specific GNU attribute tag indicating the address space used for virtual
    tables on AVR targets. Values specify different address spaces like RAM or various
    FLASH segments.
- term: vtable
  definition: Virtual Table. A table used in C++ to implement dynamic dispatch for
    virtual functions. It stores pointers to the virtual functions of a class.
- term: ABI
  definition: Application Binary Interface. Defines how low-level code, such as compiled
    programs, should interact with each other. Changes to ABI can break compatibility
    between different compiled components.
- term: TARGET_ADDR_SPACE_FOR_ARTIFICIAL_RODATA
  definition: A GCC target hook that allows a compiler backend to specify a custom
    address space for read-only data, which can include vtables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8c8b10c8-762b-4845-a2a5-c00167bb89e8@gjlay.de
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay proposes adding support for `.gnu_attribute 4` (Tag_GNU_AVR_VTABLE_AS) to Binutils for the AVR target. This new attribute will tag object files with information about the address space used for C++ virtual tables, a necessary step for upcoming G++ support for placing vtables in custom address spaces. This feature is crucial for detecting ABI violations when vtables are moved from the generic address space to other spaces like FLASH.
