---
project: binutils
subsystem: binutils/configure
patch_id: null
tags:
- configure
- aarch64
- windows
- regression
commit_hash: 31249660c695a9169ca97590a2c325585740c101
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: Fix binutils configuration for aarch64-*-pe*
tldr: Binutils configuration now correctly includes aarch64-*-pe targets for building
  dlltool.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Reverts a change in `configure.ac` that incorrectly excluded `aarch64-*-pe*`
  from the `aarch64-*-mingw*` case statement. This ensures that `dlltool` and related
  tools are correctly configured and built for PE targets on aarch64, addressing a
  regression introduced in a previous commit.
primer_glossary:
- term: autoconf
  definition: A tool that automatically configures source code packages to adapt to
    different operating systems and environments. It generates shell scripts that
    check for necessary system components and set up build configurations.
- term: dlltool
  definition: A utility that creates import libraries for Windows DLLs, used by the
    binutils toolchain when targeting Windows.
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: PE
  definition: Portable Executable, a file format for executables, object code, DLLs,
    and system components used in 32-bit and 64-bit versions of Windows operating
    systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261023172511.7824E4BA2E1C@sourceware.org
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

This commit resolves an autoconf issue by ensuring that the `aarch64-*-pe*` target is included when determining build settings for `dlltool` and other tools. This fixes a regression that prevented these tools from being built for the specified target, ensuring proper test configuration.
