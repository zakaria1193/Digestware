---
project: binutils
subsystem: bfd/elf
patch_id: null
tags:
- LoongArch
- linker
- bugfix
- relocation
commit_hash: 86afbefb5085cf6188ee0ddd274e45fbf9463a6e
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: LoongArch linker handles ignored undefined symbols better
tldr: LoongArch linker now correctly handles ignored undefined symbols, preventing
  assertions for call relocations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The LoongArch ELF linker's relocation logic is updated to correctly
  handle ignored undefined symbols. When an undefined symbol is marked as 'ignored',
  it's treated as a dynamically resolved symbol. This change prevents a BFD assertion
  that could occur when ` --unresolved-symbols=ignore-all` is used with call relocations,
  ensuring that such symbols are handled gracefully even if they lack a PLT entry.
primer_glossary:
- term: LoongArch
  definition: A family of reduced instruction set computer (RISC) architectures developed
    in China.
- term: BFD
  definition: The Binary File Descriptor library, a low-level interface for handling
    object code and executable files across different formats.
- term: ELF
  definition: The Executable and Linkable Format, a common standard file format for
    object files, executables, and shared libraries on Unix-like systems.
- term: PLT
  definition: The Procedure Linkage Table, a table in an executable or library used
    for dynamic linking, allowing indirect calls to functions.
- term: relocation
  definition: The process of updating symbolic references from their assigned memory
    addresses to their final memory addresses after linking or loading.
- term: undefined symbol
  definition: A symbol that is referenced in one object file but not defined (declared)
    in any object file being linked.
- term: --unresolved-symbols=ignore-all
  definition: A linker option that instructs the linker to ignore all unresolved symbols,
    treating them as dynamically resolved.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261102093559.1112B4B99F74@sourceware.org
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This change modifies the LoongArch ELF linker to correctly handle ignored undefined symbols. Previously, attempting to resolve ignored undefined symbols that failed local resolution could lead to a BFD assertion when a PLT entry was requested. The fix ensures that ignored undefined symbols, especially for call relocations, are treated appropriately, preventing assertion failures.
