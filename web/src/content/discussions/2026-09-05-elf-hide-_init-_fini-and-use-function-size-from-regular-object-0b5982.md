---
project: binutils
subsystem: elf
patch_id: null
tags:
- elf
- linker
- symbols
- initialization
discussion_id: CAMe9rOqvG-YGh_9vN0M5De+2gZJiuZPtsFZAN9Hv7GbqC43rOw@mail.gmail.com
source_type: public_inbox
title: '[PATCH v2] elf: Hide _init/_fini and use function size from regular object'
headline: 'elf: Hide _init/_fini and use function size from regular object'
tldr: H.J. Lu proposes hiding _init/_fini symbols and using function sizes from regular
  objects to improve linker behavior with ELF objects.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Hiding linker-generated symbols vs. potential ambiguity.
- Using regular object sizes vs. dynamic object sizes for function size calculation.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submits v2 of a patch to hide _init/_fini symbols and use regular object
    function sizes, detailing changes to the linker's ELF handling and testsuite.
  quote: '1. Hide _init and _fini, when they are used to define DT_INIT and DT_FINI,

    to avoid confusing static linker and run-time linker with ELF objects with

    exported _init and _fini.

    2. Use function size defined in regular object since function from dynamic

    object is independent from function defined in regular object.'
primer_expert: This patch addresses issues in the ELF linker (ld) related to symbol
  resolution and size calculation for initialization functions. It proposes to hide
  the linker-generated _init and _fini symbols when they are used to define the DT_INIT
  and DT_FINI dynamic tags. Additionally, it ensures that the linker uses the size
  of functions defined in regular object files rather than those from dynamic objects,
  resolving a discrepancy that could affect linker behavior.
primer_glossary:
- term: _init
  definition: A special symbol in ELF executables and shared objects, typically used
    to initialize a shared library when it is loaded.
- term: _fini
  definition: A special symbol in ELF executables and shared objects, used to perform
    cleanup operations when a shared library is unloaded.
- term: DT_INIT
  definition: A dynamic tag in the ELF header that specifies the address of the initialization
    function for a shared object.
- term: DT_FINI
  definition: A dynamic tag in the ELF header that specifies the address of the termination
    function for a shared object.
- term: ELF objects
  definition: Executable and Linkable Format files, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: static linker
  definition: A program that combines several object files into a single executable
    file or another object file. It processes code and data from object files and
    resolves symbols.
- term: run-time linker
  definition: A program that is part of the operating system and resolves dynamic
    library references when an executable is run. Also known as a dynamic linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqvG-YGh_9vN0M5De+2gZJiuZPtsFZAN9Hv7GbqC43rOw@mail.gmail.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

H.J. Lu submits version 2 of a patch that aims to improve ELF object handling in the static linker. The changes involve hiding the _init and _fini symbols when they define DT_INIT and DT_FINI to prevent confusion, and using function sizes from regular objects instead of dynamic ones for better accuracy. Changes in v2 include replacing .nops with .space and adjusting testsuite configurations.
