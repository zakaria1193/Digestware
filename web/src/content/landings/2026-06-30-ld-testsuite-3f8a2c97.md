---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- ld
- testsuite
- pe coff
- linker
commit_hash: 3f8a2c9722b1dcb5525ce3943c5c3f98404ace67
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'ld/testsuite: Add comprehensive PE COFF weak external tests'
tldr: Adds extensive test cases for PE COFF weak external symbol behavior in the linker
  test suite.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces extensive test cases for PE COFF weak external
  symbols within the `ld/testsuite`. The tests, based on work by Martin Storsjo, cover
  a matrix of weak/strong symbol interactions, including archive handling and various
  fallback definitions. New test procedures like `weak_ext_test` and `weak_ext_archive_test`
  are added, along with numerous supporting C source files, to thoroughly validate
  the linker's behavior with weak externals across different PE COFF scenarios.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: testsuite
  definition: A collection of programs and scripts used to verify the correctness
    of a software project. In this context, it tests the functionality of the linker.
- term: PE COFF
  definition: Portable Executable Common Object File Format. The file format used
    for executables, object code, and DLLs on 32-bit and 64-bit versions of Windows.
- term: weak external symbol
  definition: A symbol that has a 'weak' linkage. If multiple definitions of a weak
    symbol exist, the linker typically uses one of them by a specific rule (e.g.,
    non-weak first, then defined weak). Weak externals allow for optional fallback
    definitions.
- term: archive file
  definition: A file (often with a .a or .lib extension) that contains multiple object
    files bundled together. The linker can extract individual object files from an
    archive to satisfy symbol references.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260630234859.06B444BA2E37@sourceware.org
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

A new set of comprehensive tests for PE COFF weak external symbols has been added to the linker test suite. These tests cover various interactions between weak and strong symbols, including scenarios with archive files, weak declarations with no fallback, and different combinations of weak/defined symbols. The suite aims to ensure robust handling of PE COFF weak externals.
