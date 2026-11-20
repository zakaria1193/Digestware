---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- elf
- security
- bugfix
discussion_id: tencent_4FB8640D27208A894298C8C5B81022FA7905@qq.com
source_type: public_inbox
title: '[PATCH] bfd: Validate common symbol alignment before bfd_log2 to avoid UB
  [PR binutils/34996]'
headline: 'bfd: Validate common symbol alignment before bfd_log2'
tldr: Fixes undefined behavior in bfd by validating common symbol alignment before
  log2 calculation.
proposer: Haolin Xue <762233433@qq.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds a small performance overhead due to the new validation checks.
exchanges:
- author: Haolin Xue <762233433@qq.com>
  role: proposer
  position: Adds validation guards to elf_link_add_object_symbols to prevent undefined
    behavior caused by malformed common symbols.
  quote: 'A malformed ELF object with a common symbol whose st_value is not a

    power of two (e.g., 0xffffff000000ffff) causes bfd_log2 to return 64,

    which then triggers undefined behavior at the 1 << alignment_power

    shift (elflink.c:10992).'
primer_expert: This change addresses an undefined behavior in the BFD library's ELF
  linking logic. Specifically, it validates the `st_value` of common symbols before
  passing it to `bfd_log2`. The `st_value` is used to determine alignment, and non-power-of-two
  values can lead to `bfd_log2` returning 64, causing a shift overflow in `elf_link_add_object_symbols`.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils to parse and manipulate object files.
- term: ELF
  definition: Executable and Linkable Format, a common standard for object file formats
    on Unix-like systems.
- term: st_value
  definition: A field in the ELF symbol table entry that, for common symbols, indicates
    the symbol's alignment requirement.
- term: undefined behavior
  definition: Program behavior that results from an error, such as memory corruption
    or an invalid operation, for which the C and C++ standards impose no requirements.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/tencent_4FB8640D27208A894298C8C5B81022FA7905@qq.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch adds validation guards to the bfd_log2 function call in elf_link_add_object_symbols. It prevents undefined behavior that occurs when a malformed ELF object has a common symbol whose st_value is not a power of two. The fix rejects invalid st_value values and ensures proper error handling and memory cleanup.
