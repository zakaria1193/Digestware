---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- elf
- comdat
- assembler
- linker
discussion_id: 20260727110447.3174-1-kirill@korins.ky
source_type: public_inbox
title: '[PATCH] gas: Avoid section symbols as group signatures'
headline: 'gas: Avoid section symbols as group signatures'
tldr: Fixes gas to not reuse section symbols as COMDAT group signatures, preventing
  invalid object files.
proposer: '"Kirill A. Korinsky" <kirill@korins.ky>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 10
technical_tradeoffs:
- Ensures correct object file generation by disallowing section symbols as group signatures.
- Improves compliance with ELF specifications regarding COMDAT groups.
exchanges:
- author: Kirill A. Korinsky <kirill@korins.ky>
  role: proposer
  position: Submits a patch to prevent gas from using section symbols as COMDAT group
    signatures, explaining that this leads to invalid object files and the need for
    distinct named symbols.
  quote: 'When a COMDAT group signature matches its section name, symbol_find_exact
    finds the existing section symbol. GAS then reuses this unnamed STT_SECTION symbol
    as the group signature, although the signature requires a distinct named symbol.


    Reject section symbols when selecting an existing signature; GAS then creates
    the usual named local STT_NOTYPE symbol.'
- author: Kirill A. Korinsky <kirill@korins.ky>
  role: proposer
  position: Provides context on the issue, noting its discovery during an LLVM toolchain
    port and upstream attempts to address it, including an LLD workaround that was
    rejected. The issue was also observed when building GCC on OpenBSD/sparc64.
  quote: 'This issue was discovered during the OpenBSD/sparc64 LLVM toolchain port
    and the attempt to upstream its LLVM changes: https://github.com/llvm/llvm-project/pull/207609


    An LLD workaround for these objects was rejected upstream: https://github.com/llvm/llvm-project/pull/209841'
primer_expert: This patch modifies the gas assembler's ELF object file emission logic.
  Specifically, it corrects how COMDAT group signatures are handled. When a COMDAT
  group's signature symbol matches an existing section symbol (e.g., `.text` for a
  `.text` section), `symbol_find_exact` would find the section symbol. The assembler
  then incorrectly re-uses this unnamed section symbol as the group signature, violating
  the requirement for a distinct, named symbol. The fix ensures that such section
  symbols are rejected, and a proper named symbol is created.
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the GNU Binutils suite that translates
    assembly language code into machine code.
- term: COMDAT group
  definition: A grouping mechanism in object files for selecting a single version
    of a group of related symbols or sections among potential duplicates. Often used
    for function or data definitions that might appear in multiple object files.
- term: signature
  definition: In the context of COMDAT groups, a unique identifier that determines
    which group 'wins' when multiple object files define the same group.
- term: STT_SECTION symbol
  definition: A symbol table entry of type STT_SECTION, which refers to a specific
    section in the object file. These are typically unnamed.
- term: STT_NOTYPE symbol
  definition: A symbol table entry of type STT_NOTYPE, which indicates that the symbol
    has no defined type. These can be local or global.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on many Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260727110447.3174-1-kirill@korins.ky
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the GNU Assembler (gas) where it incorrectly reuses unnamed STT_SECTION symbols as COMDAT group signatures. This behavior results in invalid object files, particularly when the signature matches the section name. The fix ensures that gas rejects section symbols for signature matching and creates a distinct named symbol instead. The problem was discovered during an LLVM toolchain port to OpenBSD/sparc64.
