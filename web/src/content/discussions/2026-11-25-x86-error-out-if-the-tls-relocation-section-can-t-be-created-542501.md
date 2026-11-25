---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- TLS
- linker
- ELF
discussion_id: 20261125001752.1115235-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: '[PATCH 1/2] x86: Error out if the TLS relocation section can''t be created'
headline: 'x86: Error out if the TLS relocation section can''t be created'
tldr: Fixes x86 linker to report an error when TLS relocation sections cannot be created.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Makes the linker less tolerant of certain configuration errors by turning a silent
  failure into a fatal one.
- Addresses a specific bug found during testing of newer standards and compiler versions.
exchanges: []
primer_expert: In `_bfd_x86_elf_link_setup_gnu_properties`, a prior return of `false`
  on failure to create/align TLS relocation sections (`.rel.tls` or `.rela.tls`) masked
  the issue. This resulted in `htab->rel_tls_desc` remaining `NULL`, skipping necessary
  PLT, `.eh_frame`, and `.sframe` setup. This patch replaces the `return false` with
  `info->callbacks->fatal`, ensuring that the linker terminates with an error, similar
  to other section creation failures in the same function.
primer_glossary:
- term: TLS
  definition: Thread-Local Storage, a mechanism that allows each thread in a multithreaded
    program to have its own copy of a variable.
- term: Relocation section
  definition: A section in an object file or executable that contains information
    about how addresses in the code or data need to be adjusted (relocated) after
    linking.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries used on many Unix-like systems.
- term: GNU properties
  definition: Refers to specific extensions or conventions used by GNU tools, such
    as GNU properties in ELF sections for linker-specific behavior.
- term: PLT
  definition: Procedure Linkage Table, a table used in ELF executables to resolve
    indirect function calls, typically to functions in shared libraries.
series_id: 'binutils:x86: error out if the tls relocation section can''t be created'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125001752.1115235-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the x86 linker where the failure to create or align TLS relocation sections (.rel.tls/.rela.tls) did not result in an error diagnostic. Previously, a false return value masked these failures, causing subsequent TLS-related setup to be skipped. The change ensures that such failures are now reported as fatal errors, preventing silent misconfigurations and improving build robustness, especially with newer C standards and GCC versions.
