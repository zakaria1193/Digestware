---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- gas
- aarch64
- testsuite
- elf
commit_hash: 8fcc4a6bb9ad7f754b74ffa68da34ae826d7d0e6
source_type: public_inbox
author: Alan Modra <amodra@gmail.com>
headline: Fix aarch64-pe tls-debug tests for ELF format
tldr: Adjusts aarch64-pe test suite to check for ELF format instead of aarch64 target,
  resolving assembly failures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Updates gas testsuite/gas/aarch64/tls-debug{,-bad}.d to use `[is_elf_format]`
  instead of `aarch64*-*-*` as the target. This is because these tests use ELF section
  directives, which can fail to assemble on non-ELF targets, and the aarch64-specific
  tests are already covered elsewhere.
primer_glossary:
- term: aarch64-pe
  definition: A target configuration for Binutils targeting the AArch64 architecture,
    producing PE (Portable Executable) object files, commonly used on Windows.
- term: tls-debug
  definition: Tests related to Thread-Local Storage (TLS) and debugging information.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on many Unix-like systems.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260711085055.B9ACC4BA2E15@sourceware.org
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

The TLS debug test suite for the aarch64-pe target was failing due to the use of ELF section directives. This commit modifies the test cases to check for the ELF format in general, rather than specifically targeting aarch64. This ensures the tests run correctly without assembly errors, as the aarch64 target is already covered by separate test suites.
