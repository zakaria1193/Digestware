---
project: binutils
subsystem: binutils
patch_id: null
tags:
- aarch64
- elf
- linker
- tls
- bugfix
discussion_id: akTVYb32aOjEDV8W@squeak.grove.modra.org
source_type: public_inbox
title: PR 34165 aarch64 assertion fail and segv
headline: PR 34165 aarch64 assertion fail and segv
tldr: Fixes an assertion failure and segfault in aarch64 ELF linking related to weak
  undefined TLS symbols.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a crash by relaxing an assertion, potentially masking underlying issues with
  weak undefined TLS symbol handling.
- Aligns AArch64 behavior with x86 for specific TLS symbol scenarios.
exchanges:
- author: Alan Modra
  role: proposer
  position: Applies a fix for PR34165, addressing a segfault and assertion failure
    in aarch64 ELF linking related to weak undefined TLS symbols.
  quote: 'I''m going to apply this as a fix for pr34165.  It fixes the segv and

    results in a zero .got entry for the weak undefined tls syms, the same

    as x86.


    It seems to me that weak undefined and tls don''t work together very

    well, as the address of such a sym includes the thread pointer.  So

    I don''t think there is a reliable machine independent way to test

    whether the sym is defined.'
primer_expert: This patch addresses a segfault and assertion failure in the AArch64
  ELF linker backend of binutils. The problem occurs when weak, undefined TLS symbols
  are encountered. The linker was asserting that the TLS section (`tls_sec`) must
  be non-NULL, but in cases involving weak undefined TLS symbols, `tls_sec` can legitimately
  be NULL. This patch changes the behavior from an assertion to returning 0, which
  correctly handles these symbols and produces a zero `.got` entry, aligning behavior
  with the x86 backend.
primer_glossary:
- term: TLS
  definition: Thread-Local Storage, a mechanism that allows variables to have different
    values for each thread in a multi-threaded program.
- term: weak undefined symbol
  definition: A symbol that is declared but not defined, and has weak linkage. This
    means a definition may be provided elsewhere, but if not, the program can still
    link and potentially run, often with default or zero values.
- term: AArch64
  definition: The 64-bit execution state of the ARM architecture.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: segfault
  definition: A segmentation fault, an error that occurs when a program accesses a
    memory location that it's not allowed to access.
- term: .got
  definition: Global Offset Table, a section in ELF executables and dynamic libraries
    used to store pointers to dynamically resolved external function or variable references.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akTVYb32aOjEDV8W@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch resolves an assertion failure and subsequent segmentation fault in binutils' AArch64 ELF linker. The issue arises when weak undefined TLS symbols are used, as their addresses are tied to the thread pointer. The fix modifies the `dtpoff_base` and `tpoff_base` functions to return 0 instead of asserting that `tls_sec` is non-NULL, thus preventing the crash and resulting in a zero `.got` entry for these symbols, consistent with x86 behavior.
