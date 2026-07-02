---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- elf
- linker
- symbol
- bugfix
commit_hash: 1a5ae95bc1fde4aeb159e4e963118b17e1e730b5
source_type: public_inbox
author: Alan Modra
headline: Fix type confusion in elf64_ia64_hash_copy_indirect
tldr: Corrects type confusion in symbol handling within the ELF linker, preventing
  potential errors when merging object files.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `elflink.c`, functions like `_bfd_elf_add_default_symbol`, `elf_link_add_object_symbols`,
  `_bfd_elf_merge_symbol`, and `_bfd_elf_fix_symbol_flags` were using `get_elf_backend_data(abfd)`
  where `abfd` was the input BFD. This caused problems when the output BFD had different
  properties. The fix changes these calls to `get_elf_backend_data(info->output_bfd)`
  to ensure consistency.  This bug was triggered by PR 34062.
primer_general: When linking object files together, the linker uses the Binary File
  Descriptor (BFD) library to handle different file formats. The BFD library provides
  a common interface for accessing information within these files. This commit fixes
  an issue where the linker was using the wrong BFD data structures when merging symbols,
  which could lead to errors. By using the correct BFD data, the linker can now correctly
  handle symbols from different object files, preventing potential linking problems.
discussion_id_link: public_inbox:binutils#34062
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260501124943.B3A5746A9CC7@sourceware.org
date: '2026-05-01'
---

The ELF linker incorrectly used the input BFD's (Binary File Descriptor) data structures instead of the output BFD's when manipulating hash table symbols. This could lead to type confusion and potential errors during symbol merging, especially in scenarios involving shared libraries or object files with different architectures. The fix ensures that the output BFD's data structures are used consistently, resolving the type confusion and preventing potential issues with symbol handling.
