---
project: gcc
subsystem: gcc/configure
patch_id: null
tags:
- configuration
- abi
- build-system
commit_hash: e63a04e996e2ab8e78a33eea6425596c780758d7
source_type: github
author: Eric Botcazou
headline: Configure machinery now correctly identifies abi32 targets
tldr: GCC's build configuration now accurately recognizes and sets appropriate flags
  for abi32 targets, addressing previous misclassifications.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `acinclude.m4` and `configure.ac` within the GCC
  build system. `acinclude.m4` defines various Autoconf macros used during GCC's configuration.
  The change ensures the `gcc_GAS_FLAGS` macro correctly sets the `--32` flag for
  the GNU Assembler (GAS) when building for abi32 targets. Similarly, `configure.ac`
  is updated to select the correct 32-bit Thread-Local Storage (TLS) sequence, crucial
  for proper thread-safe variable access on these architectures. This fixes an issue
  where the configure script would sometimes incorrectly assume 64-bit properties
  for abi32 systems.
primer_general: When you compile a program with GCC, the compiler needs to know details
  about the computer architecture it's building for. This includes the application
  binary interface (ABI), which defines how programs interact with the operating system
  and other code. An 'abi32' target refers to systems that use a 32-bit ABI, even
  if the underlying hardware is 64-bit. This commit fixes a bug in GCC's setup process
  where it would sometimes misidentify these abi32 systems as full 64-bit systems.
  This could lead to incorrect settings being used during compilation. The change
  ensures GCC now correctly applies 32-bit specific flags and settings, guaranteeing
  programs are built properly for these specific architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e63a04e996e2ab8e78a33eea6425596c780758d7
date: '2026-06-18'
is_stub: false
---

This change updates GCC's configure script logic to properly identify and handle abi32 targets. Previously, the build machinery would sometimes treat these as 64-bit targets, leading to incorrect compiler settings. The fix specifically ensures that `gcc_GAS_FLAGS` is set to `--32` and that the correct 32-bit TLS sequence is used for abi32 targets, resolving configuration mismatches.
