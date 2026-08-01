---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- linker
- aarch64
- windows
- ABI
discussion_id: 20260731144655.88354-1-evgeny.karpov@arm.com
source_type: public_inbox
title: 'aarch64: mingw: Auto-import implementation'
headline: 'aarch64: mingw: Auto-import implementation'
tldr: Implements auto-import for AArch64 on MinGW/Cygwin by avoiding pseudo-relocations.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Eliminates pseudo-relocations and runtime handling for improved performance and
  simpler code.
- Adds complexity to the linker's handling of dynamic relocations for AArch64 on Windows.
exchanges:
- author: Evgeny Karpov
  role: proposer
  position: Introduces auto-import support for AArch64 on MinGW/Cygwin, avoiding pseudo-relocations
    and runtime handling for certain bit-size relocations.
  quote: v2 implements auto-import support for 12/21/26 bit size relocations without
    needing pseudo relocations and runtime relocations in MinGW/Cygwin, based on feedback
    during upstreaming changes to MinGW.
- author: Evgeny Karpov
  role: proposer
  position: Explains the necessity of auto-import for resolving symbols during dynamic
    linking, particularly for instructions like `adrp` and `add` when the target symbol
    is unknown at compile time.
  quote: "Auto-import is needed to resolve symbols during dynamic linking.\n\nFor\
    \ example,\n\n  adrp\tx0, dyn_v + 2\n  add\tx0, x0, :lo12:dyn_v + 2"
- author: Martin Storsjö
  role: reviewer
  position: Acknowledges the updated patch series and its approach to implementing
    auto-import.
  quote: 'Thank you for reviewing v1!

    v2 implements auto-import support for 12/21/26 bit size relocations without needing
    pseudo relocations and runtime relocations in MinGW/Cygwin, based on feedback
    during upstreaming changes to MinGW.'
- author: Martin Storsjö
  role: reviewer
  position: Confirms understanding of the auto-import mechanism for dynamic symbol
    resolution using `adrp` and `add` instructions.
  quote: "Auto-import is needed to resolve symbols during dynamic linking.\n\nFor\
    \ example,\n\n  adrp\tx0, dyn_v + 2\n  add\tx0, x0, :lo12:dyn_v + 2"
primer_expert: This patch series introduces auto-import for AArch64 targets on MinGW/Cygwin
  platforms. Auto-import is a linker mechanism that automatically resolves symbols
  from dynamic libraries by creating thunks or stubs. Previously, this often involved
  pseudo-relocations or runtime handling. This series aims to implement auto-import
  by directly supporting dynamic relocations for `adrp` and `add` instructions with
  symbol offsets, eliminating the need for those indirect methods for 12/21/26 bit
  relocations. It also includes tests.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: MinGW
  definition: Minimalist GNU for Windows, a development environment for native Microsoft
    Windows applications using the GNU Compiler Collection.
- term: Cygwin
  definition: A Linux-like environment for Windows that provides a POSIX compatibility
    layer.
- term: auto-import
  definition: A linker feature that automatically resolves symbols from dynamic libraries,
    often by generating import thunks or stubs.
- term: relocation
  definition: The process of updating symbolic references in relocatable object code
    to absolute symbols, typically done by the linker.
- term: pseudo relocation
  definition: A relocation entry that doesn't directly correspond to a standard relocation
    type but is used to convey additional information or control linker behavior.
- term: dynamic relocation
  definition: Relocations that are resolved at runtime by the dynamic linker, used
    for dynamically linked executables and libraries.
- term: IAT
  definition: Import Address Table, a table used by Windows executables and DLLs to
    store addresses of imported functions.
series_id: 'binutils:aarch64: mingw: auto-import implementation'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260731144655.88354-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This patch series introduces auto-import support for AArch64 on MinGW/Cygwin, specifically targeting 12/21/26 bit size relocations. It avoids the need for pseudo-relocations and runtime handling by leveraging dynamic relocations for `adrp` instructions with symbol offsets. This change aims to improve linker performance and compatibility with MinGW/Cygwin environments.
