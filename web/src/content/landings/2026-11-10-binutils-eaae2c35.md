---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- release
- versioning
commit_hash: eaae2c35a38a1b48b3f5ff058139760eb7504ab7
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for release branch
tldr: Updates the build date in `bfd/version.h` for the gdb-18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit is a straightforward update to the versioning information
  for the `gdb-18-branch`. It modifies `bfd/version.h` to increment the `BFD_VERSION_DATE`
  macro from `20261109` to `20261110`. This change is typically made to reflect the
  current date of a release or development cycle.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by binutils
    to read and write object file formats.
- term: version.h
  definition: A header file containing version information macros for the binutils
    project.
- term: macro
  definition: A piece of code that has been given a name. Before compilation, the
    code is expanded from the macro, and the compiler never sees the macro name. It
    is purely a code-substitution mechanism.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261110000027.B2E434B920C8@sourceware.org
date: '2026-11-10'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to reflect the current date, `20261110`. This is a routine update for the `gdb-18-branch` to ensure the version information is current for release builds.
