---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- gas
- cxx
- abi
- deprecation
commit_hash: 4cdc9a9d93571737476034869dd8caaecb5ca35d
source_type: public_inbox
author: Richard Earnshaw <rearnsha@sourceware.org>
headline: GAS deprecates older C++ ABI vtable directives
tldr: The GAS assembler now marks the legacy `.vtable_entry` and `.vtable_inherit`
  directives as deprecated, warning users of their obsolescence.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This change in `binutils/gas` targets the deprecation of two ELF assembler
  directives: `.vtable_entry` and `.vtable_inherit`. These directives historically
  provided GNU-specific ABI support for C++ vtables, predating the establishment of
  the generic C++ ABI in GCC 3.0. Modern targets often lack the backend support for
  these legacy directives, rendering them obsolete. The deprecation involves adding
  a warning for their use at assembly time, removing their mention from the `as.texi`
  documentation, and updating `NEWS` to indicate their forthcoming removal. This streamlines
  the assembler by remov…'
primer_general: When you write C++ code that uses virtual functions, the compiler
  generates something called a 'virtual table' (vtable) behind the scenes. This table
  helps your program figure out which version of a function to call at runtime. Different
  compilers and different versions of the same compiler can have slightly different
  ways of organizing these vtables, which is part of what's called an 'Application
  Binary Interface' (ABI). This commit from the GNU Assembler (GAS) project is about
  tidying up support for very old C++ ABIs. Specifically, it's marking two special
  instructions (`.vtable_entry` and `.vtable_inherit`) that were used for C++ vtables
  before GCC version 3.0 as outdated. These instructions are no longer relevant in
  modern C++ compilation, and the assembler will now warn you if you use them, indicating
  that they will eventually be removed entirely.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260612093354.2E13B4BA5439@sourceware.org
date: '2026-06-12'
is_stub: false
---

The GNU Assembler (GAS) is deprecating the `.vtable_entry` and `.vtable_inherit` ELF directives. These directives were a GNU extension supporting the C++ ABI used in GCC versions prior to 3.0, which has since been superseded by a generic C++ ABI. The assembler will now issue a warning when these obsolete directives are used, and their documentation has been removed, signaling their eventual removal from the toolchain.
