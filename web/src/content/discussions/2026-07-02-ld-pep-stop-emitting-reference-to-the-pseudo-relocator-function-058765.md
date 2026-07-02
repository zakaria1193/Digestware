---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- PE
- linker
- runtime
discussion_id: 20260702143816.23422-1-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH] ld: pep: Stop emitting reference to the pseudo-relocator function'
headline: 'ld: pep: Stop emitting reference to the pseudo-relocator function'
tldr: Patch to stop the PE linker from emitting a reference to the _pei386_runtime_relocator
  function, simplifying Cygwin runtime and preparing for future architectu…
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Removing the reference simplifies the Cygwin runtime by eliminating a dummy stub.
- Maintaining the reference for i386 targets ensures backward compatibility with older
  runtimes.
- Removing the reference entirely for future architectures like aarch64 allows for
  cleaner linker behavior without legacy constraints.
exchanges:
- author: Jon Turney
  role: proposer
  position: Proposes to stop the PE linker from emitting a reference to `_pei386_runtime_relocator`
    to simplify the Cygwin runtime and prepare for future architectures.
  quote: null
primer_expert: This patch targets the PE linker (`ld`) and its handling of runtime
  relocation mechanisms, specifically concerning the `_pei386_runtime_relocator` function.
  Currently, `ld` synthesizes a reference to this function for PE targets. In the
  Cygwin environment, this function is a mere stub, serving only to satisfy the linker's
  reference. The MinGW environment has a functional version, but it's invoked directly.
  This change removes the synthesized reference from `ld` for Cygwin, clarifying the
  runtime's role and preparing for the linker's evolution on architectures beyond
  x86.
primer_glossary:
- term: PE
  definition: Portable Executable, a file format for executables, object code, DLLs
    and others used in 32-bit and 64-bit versions of Windows operating systems.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: Runtime relocator
  definition: A function or mechanism that resolves certain symbolic references or
    adjusts addresses in an executable at runtime, often used in dynamic linking or
    for Position-Independent Code (PIC).
- term: Stub
  definition: A small piece of code that acts as a placeholder or interface, often
    used to satisfy a reference or to forward calls to another function.
- term: CRT
  definition: C Runtime, the startup code for C programs that initializes the execution
    environment before main() is called.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260702143816.23422-1-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

Jon Turney proposes to stop the PE linker (ld) from emitting a reference to the `_pei386_runtime_relocator` function. This function currently exists as a non-functional stub in the Cygwin runtime solely to satisfy this linker-synthesized reference. While the MinGW runtime has actual content for this function, it's already called explicitly at CRT startup. The patch aims to remove the confusing stub from the Cygwin runtime, especially as GCC prepares for future architectures like aarch64 where backwards compatibility concerns are less pressing. For PE+ targets, the reference will no longer be emitted, although it will be retained for i386 targets that might still require it for compatibility with older runtimes.
