---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- loongarch
- binutils
- linker
- testsuite
- shared library
commit_hash: e4a4c6963f1a9f6f5a0e5c1deb58e01e7b2acdb9
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'ld: Pin hash style in LoongArch shared library tests'
tldr: LoongArch shared library tests now explicitly set the hash style to 'both'.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The LoongArch ELF linker test suite, specifically tests involving `DT_RELR`
  relocations and shared libraries, requires explicit pinning of the hash style. The
  default hash style for `loongarch*-elf` is `sysv`, while the Linux default is `both`.
  The test expectations were written against the `both` style. This commit modifies
  `relr-data-shared.d`, `relr-discard-shared.d`, and `relr-got-shared.d` to pass `--hash-style=both`.
  This ensures that the symbol indices in the `.dynsym` table, which are compared
  in the tests, are consistent regardless of the target's default hash style.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another library.
- term: LoongArch
  definition: A 64-bit RISC instruction set architecture developed in China.
- term: shared library
  definition: A library that can be loaded and linked at runtime by multiple programs
    simultaneously, reducing memory usage and allowing for easier updates.
- term: hash style
  definition: Refers to the algorithm used by the linker to organize symbols in the
    symbol table. Common styles include 'sysv', 'gnu', and 'both'.
- term: DT_RELR
  definition: A dynamic section tag in ELF files indicating the presence of relocation
    entries in a specific format, often used for Position-Independent Code (PIC).
- term: symbol index
  definition: The position of a symbol within the dynamic symbol table (`.dynsym`)
    of an ELF object file. This index is used in relocation entries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260927022714.855A64BA23C7@sourceware.org
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

Three linker test cases for LoongArch shared libraries (`relr-data-shared.d`, `relr-discard-shared.d`, `relr-got-shared.d`) have been updated to explicitly pass `--hash-style=both`. This ensures consistent test results across different environments, as the default hash style for bare-metal targets (like `loongarch*-elf`) differs from that of Linux (sysv vs. both), affecting symbol indexing in relocation entries. This change is a prerequisite for enabling shared library and PIE support on LoongArch, allowing these tests to pass correctly.
