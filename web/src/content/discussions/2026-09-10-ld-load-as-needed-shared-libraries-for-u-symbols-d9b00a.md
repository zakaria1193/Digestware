---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- shared libraries
- ELF
- symbols
discussion_id: aqJsk3F6NO4zrsmU@squeak.grove.modra.org
source_type: public_inbox
title: make ld -u symbols load --as-needed shared libraries
headline: 'ld: load --as-needed shared libraries for -u symbols'
tldr: Make linker load --as-needed shared libraries when symbols are explicitly requested
  with -u.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures libraries are linked when symbols are explicitly requested, improving predictability.
- Requires test case adjustments to account for the changed linking behavior.
exchanges: []
primer_expert: This change affects ld.bfd's handling of --as-needed shared libraries.
  When a symbol is listed with `-u symbol_name`, the linker now marks the shared library
  containing that symbol as needed, even if no other code explicitly references it.
  This is achieved by introducing `ldlang_ref` to update `non_ir_ref_regular` and
  related ELF hash table entries, ensuring that libraries are linked when their symbols
  are forced via `-u`.
primer_glossary:
- term: --as-needed
  definition: A linker option that causes shared libraries to be linked in only if
    they are actually used by the program. If a shared library is not needed, it is
    not included in the output.
- term: -u symbol
  definition: A linker option that forces the inclusion of `symbol`, even if it is
    not referenced by any other object. This is useful for dynamically loaded modules
    that export symbols.
- term: common symbol
  definition: A symbol that has been declared but not yet defined. In C, this often
    corresponds to global variables without an initializer. The linker typically allocates
    space for common symbols.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqJsk3F6NO4zrsmU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch modifies the linker to treat command-line specified symbols with -u as explicit needs for --as-needed shared libraries. Previously, such libraries might not have been loaded if no other symbols explicitly required them, potentially leading to unexpected behavior or incorrect test results. The changes ensure consistency with archive library behavior and fix issues in test cases related to common symbol size.
