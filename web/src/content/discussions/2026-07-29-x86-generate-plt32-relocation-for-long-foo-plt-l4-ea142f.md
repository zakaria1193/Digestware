---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- relocation
- linker
- assembler
discussion_id: CAMe9rOpksJFKzyKiH4A-2jP97UBC_vNJ_9PQm+uOq8_v5cwjsQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] x86: Generate PLT32 relocation for ".long foo@PLT - .L4"'
headline: 'x86: Generate PLT32 relocation for ".long foo@PLT - .L4"'
tldr: H.J. Lu confirms the necessity and correctness of generating R_X86_64_PLT32
  for specific directives to resolve PC32 relocations against function symbols.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensuring correct PLT resolution for indirect function calls.
- Handling specific assembler directives that require PLT32 relocation.
- Maintaining compatibility with existing relocation mechanisms.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Confirms that the patch correctly generates the R_X86_64_PLT32 relocation
    for specific directives, enabling the use of PLT entries for PC32 relocation against
    function symbols. This addresses a gas PR.
  quote: Add BFD_RELOC_X86_64_PLT32 and use it to generate R_X86_64_PLT32 for directives
    like ".long foo@PLT - .L4" so that PLT entries are used to resolve PC32 relocation
    against function symbols for such directives.
primer_expert: This discussion pertains to a patch for the x86 architecture in binutils
  that introduces a new relocation type, BFD_RELOC_X86_64_PLT32. The patch's goal
  is to correctly generate the R_X86_64_PLT32 ELF relocation type for specific assembler
  directives, such as ".long foo@PLT - .L4". This is crucial for ensuring that indirect
  function calls via the Procedure Linkage Table (PLT) are resolved properly using
  PC32 relative addressing, particularly in scenarios involving function symbols.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures developed by Intel, widely
    used in personal computers and servers.
- term: relocation
  definition: A process performed by the linker to adjust memory addresses in code
    or data segments of an object file so that they can be correctly loaded and executed
    at a specific memory location.
- term: PLT32
  definition: A specific type of relocation that targets the Procedure Linkage Table
    (PLT) and involves a 32-bit offset, often used for function calls.
- term: R_X86_64_PLT32
  definition: An ELF relocation type for the x86-64 architecture, indicating a PC32-relative
    relocation against a PLT entry.
- term: PC32
  definition: A relocation type that computes a 32-bit offset relative to the current
    Program Counter (PC).
- term: GAS
  definition: GNU Assembler, part of the GNU toolchain responsible for converting
    assembly code into machine code.
- term: BFD
  definition: GNU Binary File Descriptor library, providing a common interface to
    various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpksJFKzyKiH4A-2jP97UBC_vNJ_9PQm+uOq8_v5cwjsQ@mail.gmail.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

In response to Jan Beulich's questions, H.J. Lu clarifies that the patch is necessary for generating the R_X86_64_PLT32 relocation for directives like ".long foo@PLT - .L4". This ensures that PLT entries are used to resolve PC32 relocations against function symbols, addressing a reported gas PR.
