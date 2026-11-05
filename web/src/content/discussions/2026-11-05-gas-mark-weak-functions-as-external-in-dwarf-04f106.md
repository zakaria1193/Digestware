---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- dwarf
- debugging
- weak-symbols
discussion_id: 20261105034333.4141200-1-luolongjuna@gmail.com
source_type: public_inbox
title: 'gas: Mark weak functions as external in DWARF'
headline: 'gas: Mark weak functions as external in DWARF'
tldr: Patch for gas ensures weak functions are correctly marked as external in DWARF
  debug info, preventing GDB misclassification.
proposer: Longjun Luo <luolongjuna@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The GNU Assembler (GAS) generates DWARF debug information, including
  DIEs (Debug Information Entries) for functions. This patch addresses an issue where
  weak symbols, which have `BSF_GLOBAL` cleared, were not properly marked with the
  `DW_AT_external` attribute in their Subprogram DIEs. This misrepresentation causes
  debuggers (like GDB) to treat them as static (internal) rather than external (visible
  outside the compilation unit), impacting debugging. The change modifies the `dwarf2dbg.c`
  file to consider `S_IS_WEAK` when setting `DW_AT_external`.
primer_glossary:
- term: DWARF
  definition: A standardized debugging data format used by many compilers to store
    information about variables, types, and code structure for debuggers.
- term: GAS
  definition: GNU Assembler, the assembler used by the GCC compiler toolchain.
- term: weak function
  definition: A function for which the linker can choose a definition from multiple
    available ones, typically used for providing default implementations that can
    be overridden.
- term: subprogram DIE
  definition: A Debug Information Entry (DIE) within the DWARF format that describes
    a function or subroutine.
- term: DW_AT_external
  definition: A DWARF attribute within a DIE indicating whether the entity (like a
    function) is visible outside the current compilation unit.
- term: static
  definition: In C, a keyword that limits the scope of a function or variable to the
    current translation unit (source file).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261105034333.4141200-1-luolongjuna@gmail.com
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This patch modifies the GNU Assembler (GAS) to correctly mark weak functions as external in DWARF debug information. Previously, GAS only checked for the `BSF_GLOBAL` flag, which is cleared for weak symbols, causing subprogram DIEs to omit or falsely set the `DW_AT_external` attribute. This led to debuggers like GDB incorrectly classifying weak functions as static. The fix adds a check for `S_IS_WEAK` alongside `S_IS_EXTERNAL` when emitting subprogram DIEs.
