---
project: binutils
subsystem: gas
patch_id: null
tags:
- elf
- gas
- debugging
- linker
- symbols
discussion_id: 20260701035918.1453550-1-i@maskray.me
source_type: public_inbox
title: '[PATCH v4] gas: add --reloc-section-sym={all,internal,none} option for ELF'
headline: 'gas: add --reloc-section-sym={all,internal,none} option for ELF'
tldr: Adds a new option to control how GAS converts local symbols referenced by relocations
  to section symbols, aiding debugging and tool compatibility.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Increases flexibility for debugging and tool integration at the cost of slightly
  larger symbol tables when 'none' or 'internal' options are used.
- Adds complexity to the GAS command-line interface.
exchanges:
- author: Fangrui Song
  role: proposer
  position: Proposes adding a new option to control the conversion of local symbols
    in ELF relocations to section symbols, enhancing debugging and tool integration.
  quote: 'When generating relocations for non-ifunc local symbols that satisfies

    several conditions, GAS converts them to reference the section symbol

    (STT_SECTION) instead, folding the original symbol''s offset into the

    addend.  This allows the original local symbol to be omitted from

    .symtab, but the STT_SECTION symbol itself must be present, so the

    conversion saves .symtab entries only when a section has…'
- author: Alan Modra
  role: reviewer
  position: Asks for clarification on the change to `complain_overflow_dont` and expresses
    confidence in the correctness of the patch.
  quote: "Which you now change to complain_overflow_dont?\n\nNot saying the change\
    \ is incorrect (it certainly looks right, \nthanks), because if it was, I have\
    \ confidence that the \ntest-suite would trigger a failure, but that wording is\
    \ \nconfusing."
primer_expert: This patch introduces a command-line option to GAS for fine-grained
  control over how local symbols involved in ELF relocations are handled. By default,
  GAS optimizes symbol table size by converting local symbols referenced by relocations
  into section symbols (STT_SECTION), effectively omitting the original local symbol.
  This change allows users to opt-out of this conversion ('none') or restrict it to
  compiler-internal symbols ('.L' prefixed, 'internal'), which is beneficial for debugging
  and tools that rely on explicit symbol presence.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, the default assembler used by the GNU Compiler Collection
    (GCC).
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: relocation
  definition: A directive that describes how to modify code or data when an object
    file is linked. Relocations typically specify an address and the type of modification
    needed, such as patching in an offset or a symbol address.
- term: local symbol
  definition: A symbol that is local to a compilation unit and not intended to be
    visible or used by other modules. In GAS, these often start with a '.' or '.L'.
- term: STT_SECTION
  definition: A symbol type in the ELF format that represents a section itself, often
    used as a placeholder or for specific section-related operations.
- term: .symtab
  definition: The symbol table section in an ELF file, which contains information
    about all symbols (functions, variables, etc.) defined or referenced in the object
    file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260701035918.1453550-1-i@maskray.me
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch introduces the --reloc-section-sym option to GAS, allowing users to control the conversion of local symbols used in ELF relocations. By default, eligible local symbols are converted to reference section symbols (STT_SECTION), which can reduce .symtab entries. The new option allows this conversion to be limited to compiler-generated locals ('internal') or disabled entirely ('none'), providing greater flexibility for debugging and compatibility with tools that benefit from preserved symbol names.
