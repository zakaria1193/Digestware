---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- pe
- tls
- windows
discussion_id: 66edde04-610a-42f8-a584-9a3b413c349e@126.com
source_type: public_inbox
title: '[PATCH] Write alignment of `.tls` into `_tls_used.Characteristics`'
headline: Write alignment of `.tls` into `_tls_used.Characteristics`
tldr: Updates binutils to correctly encode TLS variable alignment in PE executables.
proposer: LIU Hao <lh_mouse@126.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct TLS alignment for modern Windows systems.
- Improves compatibility with compilers like Clang and MSVC.
- The change is backward compatible as older systems ignore the alignment field.
exchanges:
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Submits a patch to correctly write the alignment of `.tls` sections into
    the `_tls_used.Characteristics` field of the PE executable's TLS directory.
  quote: "Since Windows 8.1 SDK, Microsoft have replaced\n`IMAGE_TLS_DIRECTORY{32,64}::Characteristics`\
    \ with\n\n    union {\n      DWORD Characteristics;\n      struct {\n        DWORD\
    \ Reserved0 : 20;\n        DWORD Alignment : 4;\n        DWORD Reserved1 : 8;\n\
    \      };\n    };\n\nWhen a user defines an over-aligned thread-local variable\
    \ like\n\n    alignas(128) thread_local int overaligned = 42;\n\nthe alignment\
    \ of TLS t…"
primer_expert: This patch modifies binutils' BFD library, specifically the PE (Portable
  Executable) object file format generation code (`bfd/peXXigen.c`). It addresses
  how the alignment of Thread Local Storage (TLS) variables is recorded in the PE
  header. Modern Windows systems (since Win 8.1 SDK) use a specific bitfield within
  the `Characteristics` member of the `IMAGE_TLS_DIRECTORY` to specify TLS data alignment.
  This patch ensures that binutils correctly writes this alignment value when over-aligned
  TLS variables are used, aligning with compilers like Clang and MSVC.
primer_glossary:
- term: TLS
  definition: Thread Local Storage. A mechanism that allows variables to have unique
    instances for each thread of execution within a process.
- term: PE
  definition: Portable Executable. The file format used for executables, DLLs, and
    object files on Windows operating systems.
- term: BFD
  definition: Binary File Descriptor library, a part of binutils that provides a common
    interface for reading and writing various executable binary file formats.
- term: Characteristics
  definition: A field in various PE structures (like section headers or the TLS directory)
    that contains flags describing the properties or attributes of the associated
    entity.
- term: alignas
  definition: A C++ keyword used to specify the alignment of a variable or type.
- term: over-aligned
  definition: A variable or data structure that requires an alignment greater than
    the default alignment typically provided for its type.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/66edde04-610a-42f8-a584-9a3b413c349e@126.com
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

This patch updates binutils' BFD library to correctly handle the alignment of Thread Local Storage (TLS) variables in Windows PE executables. Since the Windows 8.1 SDK, the `Characteristics` field in the TLS directory has a dedicated subfield for `Alignment`. This patch ensures that when a user defines an over-aligned thread-local variable (e.g., using `alignas`), its alignment is correctly encoded in the `_tls_used.Alignment` field, matching the behavior of Clang and MSVC. This allows the system to allocate TLS storage with the proper alignment.
