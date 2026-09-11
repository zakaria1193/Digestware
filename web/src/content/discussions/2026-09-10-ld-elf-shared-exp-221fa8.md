---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- ELF
- shared libraries
- testsuite
- C++
discussion_id: aqJtJk7OOFFe31cR@squeak.grove.modra.org
source_type: public_inbox
title: ld-elf shared.exp
headline: ld-elf shared.exp
tldr: Fixes ld-elf shared.exp test to correctly handle C++ compiler availability and
  a specific test case.
proposer: Alan Modra
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Improves the robustness and accuracy of the linker test suite.
- Ensures C++ specific tests do not fail due to the absence of a C++ cross-compiler.
- Corrects specific linkage behavior tests related to dynamic library handling.
exchanges:
- author: Alan Modra
  role: proposer
  position: Submits a patch to fix the `ld-elf/shared.exp` test suite, improving its
    handling of C++ tests and a specific shared library test.
  quote: Don't "return" when no CXX, disabling numerous later non-c++ tests. Enable
    "Run with libdl3b.so" too.
- author: Alan Modra
  role: proposer
  position: Provides a follow-up correction, noting that a compiler not defaulting
    to `--as-needed` caused a previous issue and adding `-Wl,--no-as-needed` to the
    `dl3b` test.
  quote: 'I happened to test with a compiler that didn''t default to passing

    --as-needed to ld.'
primer_expert: 'This submission modifies a test script (`shared.exp`) within the `ld-elf`
  test suite for binutils. The script is responsible for testing the linker''s behavior
  with ELF shared libraries. The changes address two main points: first, ensuring
  that C++ specific test cases are conditionally executed only if a C++ compiler is
  available for the target, preventing false negatives; second, correcting and re-enabling
  a test case related to `libdl3b.so` and its linkage behavior, particularly concerning
  the `--as-needed` linker flag.'
primer_glossary:
- term: linker
  definition: A program that combines object files and libraries into an executable
    program, resolving external references between them.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: shared library
  definition: A library whose code can be shared by multiple programs at runtime,
    loaded dynamically by the operating system.
- term: test suite
  definition: A collection of tests designed to verify the correct functionality of
    a software component or program.
- term: CXX_FOR_TARGET
  definition: A variable likely representing the C++ compiler executable used for
    cross-compilation targets within the build system.
- term: --as-needed
  definition: A linker flag that tells the linker to include a library only if it
    is actually needed by the objects being linked.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqJtJk7OOFFe31cR@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch corrects the `ld-elf/shared.exp` test script. It ensures that C++ specific tests are only run when a C++ compiler for the target is available, preventing unnecessary failures. Additionally, it enables a commented-out test for `libdl3b.so` and corrects its expected output, while also deleting an obsolete output file.
