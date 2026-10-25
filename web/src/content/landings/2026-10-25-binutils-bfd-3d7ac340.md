---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
- maintenance
commit_hash: 3d7ac340d6f0dc65d0fa72ff27dc224bb3b4b53e
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for the 2.47 branch.
tldr: The BFD version date is updated to 20261025 for the binutils-gdb/binutils-2_47-branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The BFD library maintains version information in `bfd/version.h`. For
  release branches, a specific date macro `BFD_VERSION_DATE` is used. This commit
  performs an automated update of that date macro for the `2.47-branch` to reflect
  the current day, `20261025`, as part of the release management process.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by GNU Binutils
    and GDB for reading and writing object file formats.
- term: version.h
  definition: A header file that typically contains version information, macros, and
    definitions for a software project.
- term: macro
  definition: A piece of code in a source file that is replaced by a value or sequence
    of code prior to compilation. In C/C++, these are defined using `#define`.
- term: release branch
  definition: A separate line of development in a version control system that is maintained
    for releasing stable versions of software, often with bug fixes applied but without
    introducing new features.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261025000042.507EC4BA2E13@sourceware.org
date: '2026-10-25'
is_stub: true
stub_reason: low_score
---

This commit updates the version date in the `bfd/version.h` file for the `binutils-gdb/binutils-2_47-branch`. The `BFD_VERSION_DATE` macro is changed from `20261024` to `20261025`, reflecting the current date for this release branch.
