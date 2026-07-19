---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- testsuite
- ABI
discussion_id: 20260718075339.1022267-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] ld: testsuite: Associate C identifiers with the corresponding assembler
  or linker symbols in a target-independent manner.'
headline: 'ld: testsuite: Associate C identifiers with the corresponding assembler
  or linker symbols in a target-independent manner.'
tldr: Uses `asm` keyword to make C identifier to symbol mapping target-independent
  in linker tests.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves testsuite robustness and portability by explicitly defining symbol names,
  at the cost of slightly more verbose test code.
exchanges: []
primer_expert: This patch refactors the binutils linker testsuite to address target-specific
  symbol mangling, particularly the common convention of prepending an underscore
  to C identifiers. It leverages the `asm` keyword in C to explicitly associate C
  identifiers with their corresponding assembler symbol names, making tests like `merge4a.c`
  and `merge4b.s` (and similar linking scenarios) portable across architectures that
  differ in their symbol naming conventions (e.g., H8 vs. ARM).
primer_glossary:
- term: linker
  definition: A program that combines object code from one or more object files and
    libraries into a single executable file, resolving symbol references between them.
- term: assembler
  definition: A program that translates assembly language code into machine code.
- term: symbol
  definition: A name used to refer to a location in memory or a quantity, such as
    a variable name, function name, or constant.
- term: symbol mangling
  definition: The process of encoding additional information into a symbol's name,
    often to support name decoration for function overloading, namespaces, or C++
    features. For C, it often involves adding a leading underscore for global symbols.
- term: asm keyword
  definition: In C, the `asm` keyword (often used with `__asm__` for GNU extensions)
    allows inline assembly code or, in this context, provides a way to specify the
    assembler name for a variable or function.
- term: COFF
  definition: Common Object File Format, a file format for executable and object code,
    primarily used on Windows systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260718075339.1022267-1-jdx@o2.pl
bugzilla_url: null
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

Jan Dubiec's patch addresses issues in the linker testsuite where target-specific symbol naming conventions (like a leading underscore for C identifiers) cause problems when linking C and assembly code or when symbols are provided on the linker command line. By using the `asm` keyword, C identifiers are associated with their assembler/linker symbols in a manner that is independent of the target architecture, resolving these cross-language and command-line symbol resolution problems.
