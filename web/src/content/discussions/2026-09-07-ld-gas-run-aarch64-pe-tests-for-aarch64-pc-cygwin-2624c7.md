---
project: binutils
subsystem: gas
patch_id: null
tags:
- AArch64
- PE
- Cygwin
- testing
- linker
discussion_id: 20260907081941.900753-3-dennis@dennisameling.com
source_type: public_inbox
title: 'ld, gas: run the AArch64 PE tests for aarch64-pc-cygwin'
headline: 'ld, gas: Run AArch64 PE tests for aarch64-pc-cygwin'
tldr: AArch64 PE tests are now enabled for the aarch64-pc-cygwin target, expanding
  test coverage.
proposer: Dennis Ameling <dennis@dennisameling.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increases test coverage for the `aarch64-pc-cygwin` target.
- Ensures existing tests correctly validate PE format features on this target.
- Maintains separation for a specific `ld` test with different behavior on Cygwin.
exchanges:
- author: Dennis Ameling
  role: proposer
  position: Adds the `aarch64-pc-cygwin` target to the gating conditions for various
    AArch64 PE tests in `ld` and `gas`.
  quote: 'Add the target to those gates. This runs existing coverage rather than

    adding new tests: the image base, .secrel32 and .secidx link tests, the

    PDB tests, which this target supports, the gas PE and SEH tests, and the

    CodeView tests, CodeView being a PE debug format that the PDB support

    consumes.'
- author: Alice Carlotti
  role: reviewer
  position: Reviewed the proposed patch, noting the specific exclusion of the `pe-aarch64`
    test in `ld` due to differing image base behavior on Cygwin targets.
  quote: 'pe-aarch64 in ld is deliberately left out. It matches absolute addresses

    and so is specific to the 0x140000000 image base, whereas Cygwin targets

    set move_default_addr_high and default to 0x100400000.'
primer_expert: This patch modifies test suite configuration files (`.exp` files) for
  `gas` and `ld` to include the `aarch64-pc-cygwin` target in the gating conditions
  for several AArch64 PE (Portable Executable) tests. These tests cover aspects like
  image base, section relocations (`.secrel32`, `.secidx`), PDB (Program Database),
  CodeView debug information, and SEH (Structured Exception Handling). The inclusion
  is justified because `aarch64-pc-cygwin` uses the same `aarch64pe` emulation and
  PE object format as other supported PE targets. A specific `ld` test (`pe-aarch64`)
  is intentionally excluded due to C…
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: PE
  definition: Portable Executable, the file format used for executables, DLLs, and
    object files on 32-bit and 64-bit versions of Windows.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: ld
  definition: The GNU linker, part of the GNU Binutils package, responsible for combining
    object files and libraries into an executable or shared library.
- term: aarch64-pc-cygwin
  definition: A target triple specifying the architecture (AArch64), vendor (pc),
    and operating system (Cygwin) for cross-compilation.
- term: PDB
  definition: Program Database, a file format used by Microsoft Visual C++ for storing
    debugging information about an executable or DLL.
- term: CodeView
  definition: A debug information format used by Microsoft compilers, often stored
    within PDB files.
- term: SEH
  definition: Structured Exception Handling, a mechanism for handling runtime errors
    and exceptions in Windows.
series_id: 'binutils:ld, gas: run the aarch64 pe tests for aarch64-pc-cygwin'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260907081941.900753-3-dennis@dennisameling.com
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This patch enables several AArch64 PE (Portable Executable) tests for the `aarch64-pc-cygwin` target. Previously, these tests were skipped because their gating conditions did not include Cygwin. The changes add `aarch64-pc-cygwin` to the relevant test gates, allowing existing tests for image base, `.secrel32`, `.secidx`, PDB, CodeView, and SEH to run. This expands test coverage without introducing new tests, leveraging the existing emulation and object format compatibility.
