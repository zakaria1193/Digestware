---
project: gcc
subsystem: testsuite, aarch64
patch_id: null
tags:
- testsuite
- aarch64
- big-endian
commit_hash: c17b07eace479118410715fd3c18d7cf997511f6
source_type: github
author: Iain Sandoe
headline: AArch64 test suite requires big-endian support.
tldr: AArch64 test suite now correctly gates tests requiring big-endian support.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the GCC testsuite for AArch64 to accurately reflect
  test dependencies on the `-mbig-endian` code generation option. A new target-specific
  check, `aarch64_mbig_endian`, is introduced and used to gate various tests, preventing
  them from running on configurations that do not support big-endian output, even
  if the host system is little-endian.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, widely used in mobile devices and increasingly
    in servers and desktops.
- term: big-endian
  definition: A byte order where the most significant byte is stored at the lowest
    memory address. This is in contrast to little-endian, where the least significant
    byte is stored at the lowest address.
- term: host system
  definition: The computer system on which a program is being compiled or executed.
- term: code generation
  definition: The process of translating an intermediate representation of a program
    into machine code or assembly code for a specific target architecture.
- term: test suite
  definition: A collection of test cases designed to be used to verify and validate
    that a particular software build or component meets its expected requirements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c17b07eace479118410715fd3c18d7cf997511f6
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

Several AArch64 test cases inherently require big-endian code generation capabilities, irrespective of the host system's endianness. This change introduces a target support check for `-mbig-endian`. Tests that need this functionality are now gated by this check, ensuring they only run when big-endian support is available.
