---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- tls
- relaxation
discussion_id: 20261005102157.2614702-4-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH v5 3/4] RISC-V: Add elf_link_hash_entry to relax_func args.'
headline: 'RISC-V: Add elf_link_hash_entry to relax_func args.'
tldr: Pass elf_link_hash_entry to relaxation functions for consistent TLS handling.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces an unused parameter in some relaxation functions for now, slightly increasing
  function signature complexity.
exchanges: []
primer_expert: This patch adds an `elf_link_hash_entry` argument to various RISC-V
  relaxation helper functions in `bfd/elfnn-riscv.c`, such as `_bfd_riscv_relax_pc`
  and `_bfd_riscv_relax_section`. While some of these functions do not currently use
  the argument, it's introduced for consistency with other relaxation functions, particularly
  those involved in TLS handling (as seen in related patches). This change prepares
  the relaxation infrastructure to properly access symbol information through the
  hash table during the relocation processing, which is crucial for advanced features
  like TLSDESC.
primer_glossary:
- term: elf_link_hash_entry
  definition: A data structure used by the linker to store information about symbols
    during the linking process, including their type, address, and other attributes.
- term: Relaxation
  definition: A linker optimization process that adjusts addresses and instructions
    after an initial layout to improve code density or fix addressability issues.
- term: TLS
  definition: Thread-Local Storage. A mechanism that provides each thread with its
    own copy of a variable.
- term: Relocation
  definition: Information in an object file that describes how to modify addresses
    and other values when the file is linked with other files or loaded into memory.
series_id: 'binutils:risc-v: add elf_link_hash_entry to relax_func args'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005102157.2614702-4-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch modifies RISC-V relaxation functions in binutils to accept an `elf_link_hash_entry` argument. This change is part of a larger effort to unify TLS handling and ensure that all necessary symbol information is available during the relaxation process. By passing the hash entry, the relaxation functions can correctly process TLS-related relocations, improving the robustness of TLS support.
