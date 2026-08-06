---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- relocations
- assembler
- elf
- plt
discussion_id: 73f785be-5b1a-4c45-8b27-2611b242bd6d@suse.com
source_type: public_inbox
title: 'Re: [PATCH] x86: Disallow ".long foo@PLT - .L4" for PLT32 relocation'
headline: 'x86: Disallow ".long foo@PLT - .L4" for PLT32 relocation'
tldr: Binutils' x86 assembler now disallows `.long foo@PLT - .L4` to prevent incorrect
  PLT32 relocations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Disallowing the syntax outright, rather than issuing a warning, might break existing
  code that relies on this behavior, even if it's technically incorrect.
- The decision to reject `.long` for PLT expressions implies that users must explicitly
  use the correct syntax, potentially increasing assembly code complexity.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Clarifies that the x86 assembler now disallows `.long foo@PLT - .L4` for
    PLT32 relocations, explaining the underlying relocation calculation and overflow
    conditions.
  quote: 'L + A - P


    with the usual meaning of


    L - address of PLT entry for the referenced symbol

    A - addend

    P - address of the storage unit being relocated


    Since the result has to be a valid (64-bit) address, sign-extension is necessary,
    and hence the overflow condition has to match that (starting from the 32-bit input
    field).'
- author: Maciej W. Rozycki
  role: reviewer
  position: Seeks clarification on the R_X86_64_PLT32 calculation and the expected
    linker behavior for overflow conditions.
  quote: 'Would you please provide me with the calculation R_X86_64_PLT32 stands for
    and what the calculation required would be for `.long'' should we have an actual
    relocation representing this operation?


    Also what is the linker expected by the psABI to do on an overflow condition?'
- author: H.J. Lu
  role: contributor
  position: Explains that for `.long`, there is no correct relocation type for PLT
    expressions, and R_X86_64_PLT32 is the appropriate type for PLT expressions, while
    R_X86_64_PC32 is for simple PC-relative expressions.
  quote: For .long there simply is no correct relocation type to use for PLT (and,
    fwiw, simple PC-relative) expressions. The correct type to use is R_X86_64_PLT32
    (and R_X86_64_PC32 for the simple PC-rel case).
- author: Maciej W. Rozycki
  role: reviewer
  position: Acknowledges the explanation regarding `.long` and `.slong` and questions
    whether an assembly warning would be appropriate, inquiring about the origin of
    this assembly pattern.
  quote: Ack, understood, although would perhaps an assembly warning be in order?
    Does this case typically come from handwritten assembly or one of compiled origin?
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: States that a warning is not feasible because the problematic assembly
    syntax can originate from both handwritten and compiled code.
  quote: Both, hence imo a warning is out of question.
primer_expert: This patch addresses an ambiguity in x86 assembly syntax related to
  PC-relative relocations involving the PLT. Specifically, it disallows the construct
  `.long symbol@PLT - offset` when generating PLT32 relocations. The core issue is
  that `.long` doesn't have a directly corresponding relocation type for such expressions,
  unlike R_X86_64_PLT32 which correctly handles `L+A-P`. The decision to reject this
  syntax outright, rather than warn, stems from its potential to appear in both hand-written
  assembly and compiler output.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures (ISAs) for microprocessors,
    commonly used in desktop and server computers.
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables to resolve
    dynamic library calls at runtime. It acts as an intermediary between the program
    and the actual library functions.
- term: PLT32 relocation
  definition: A type of relocation specific to the x86-64 architecture that encodes
    a 32-bit offset for accessing the Procedure Linkage Table. It is often used for
    indirect calls to functions in shared libraries.
- term: R_X86_64_PLT32
  definition: An ELF relocation type for the x86-64 architecture. It calculates a
    32-bit PC-relative offset to an entry in the Procedure Linkage Table (PLT).
- term: R_X86_64_PC32
  definition: An ELF relocation type for the x86-64 architecture. It calculates a
    32-bit PC-relative offset to a symbol.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, and shared libraries on Unix-like systems.
- term: psABI
  definition: Processor-specific Application Binary Interface. Defines the low-level
    conventions for how software components interact at the machine code level, including
    function calling conventions, data type representations, and system call interfaces.
- term: addend
  definition: A constant value included in a relocation entry that is added to the
    base address of a symbol to calculate the final address.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/73f785be-5b1a-4c45-8b27-2611b242bd6d@suse.com
bugzilla_url: null
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This change disallows the assembly syntax `.long foo@PLT - .L4` for PLT32 relocations on x86. The discussion clarifies that the correct relocation type for PLT32 is R_X86_64_PLT32, which involves `L + A - P`. While `.long` can be used, it lacks a proper relocation type for PLT expressions, leading to potential issues. The decision is to reject this specific syntax to avoid ambiguity and ensure correct relocation handling, rather than issuing a warning, as it can originate from both hand-written and compiled code.
