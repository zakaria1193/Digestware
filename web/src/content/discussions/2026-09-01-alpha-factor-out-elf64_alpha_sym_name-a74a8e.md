---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- refactoring
- symbol resolution
- diagnostics
discussion_id: 20260901023318.3503991-5-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 04/11] alpha: factor out elf64_alpha_sym_name'
headline: 'alpha: factor out elf64_alpha_sym_name'
tldr: Refactor symbol naming in alpha ELF relocations for better code reuse and clarity.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves code maintainability by reducing duplication.
- Standardizes symbol naming for diagnostics.
exchanges: []
primer_expert: This patch introduces a helper function `elf64_alpha_sym_name` to abstract
  the logic for retrieving a symbol's name used in relocation diagnostics. Previously,
  this logic was duplicated within `elf64_alpha_relocate_section`. The new function
  utilizes `bfd_elf_sym_name`, a common utility across BFD backends, to provide a
  consistent naming convention for both global (using `alpha_elf_link_hash_entry`)
  and local symbols, including better handling for section symbols and symbols with
  unreadable names.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps, commonly used on Unix-like systems.
- term: relocation
  definition: A process performed by the linker to adjust symbolic references (like
    function calls or variable accesses) in object code to their final memory addresses
    in the executable or shared library.
- term: symbol name
  definition: The identifier for a variable, function, or other program entity, used
    by the linker to resolve references.
- term: diagnostic message
  definition: An informational message output by the compiler or linker to report
    errors, warnings, or other relevant details about the code or the linking process.
series_id: 'binutils:alpha: factor out elf64_alpha_sym_name'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-5-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch refactors the alpha ELF linker by factoring out the logic for determining a symbol's name into a new function, `elf64_alpha_sym_name`. This function consolidates how both global and local symbols are named for diagnostic messages. It replaces an open-coded version with a call to `bfd_elf_sym_name`, aligning with practices used by other backends and improving consistency in how section symbols and unreadable symbol names are handled.
