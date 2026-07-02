---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- refactor
- linker
- type safety
commit_hash: 0a6aadacb2e9a2695c82635dd8b2f7fccf537adf
source_type: public_inbox
author: Alan Modra
headline: BFD's implib symbol filtering now uses `size_t` for counts.
tldr: Binutils BFD now uses `size_t` for symbol counts in import library filtering
  functions, improving type safety and consistency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in BFD addresses type consistency in functions related
  to import library symbol filtering, specifically updating parameter and return types
  from `unsigned int` to `size_t` for symbol counts within the `elf_backend_filter_implib_symbols`
  interface and its implementations (e.g., in `elf32-arm.c`). The function `_bfd_elf_filter_global_symbols`
  (which was linker-only and resided in `elf.c`) has been renamed to `_bfd_elf_filter_implib_symbols`
  to better reflect its purpose and has its fallback definition explicitly placed.
  This ensures larger symbol counts can be handled without overfl…
primer_general: When you compile a program that uses an external library, the linker
  in Binutils needs to create an 'import library' that tells your program where to
  find the functions it needs. This process involves filtering a list of symbols (names
  of functions and variables) from the main executable. This commit updates how Binutils
  counts these symbols internally. It switches from using a general 'unsigned integer'
  to a specific type called `size_t`. This change is important because `size_t` is
  designed to hold sizes or counts, especially large ones, ensuring that the linker
  can correctly handle very large programs with many symbols without encountering
  internal errors due to number overflows.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260606013929.AB36E4BA543C@sourceware.org
date: '2026-06-06'
is_stub: false
---

This commit refactors the `filter_implib_symbols` implementations within Binutils BFD to consistently use `size_t` for symbol counts, replacing previous uses of `unsigned int`. This change improves type safety by aligning the count types with standard practice for sizes and counts. The commit also renames `_bfd_elf_filter_global_symbols` to `_bfd_elf_filter_implib_symbols` and moves its fallback definition for clarity, enhancing internal consistency for import library generation.
