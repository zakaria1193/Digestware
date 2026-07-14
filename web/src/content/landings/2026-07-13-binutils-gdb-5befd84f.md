---
project: binutils
subsystem: binutils/gdb
patch_id: null
tags:
- maintenance
- gdb
- cleanup
commit_hash: 5befd84f46c67ba4b5a7aefb3fae0423eb024935
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Archive GDB ChangeLog files
tldr: Outdated ChangeLog files are moved to an 'archive' directory in GDB.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit archives GDB's ChangeLog files, which have been unmaintained
  since 2021. The files are moved from their respective source directories (e.g.,
  gdb/ChangeLog-YYYY) into a new top-level `archive/` directory, restructuring the
  project's historical logging mechanism. This also entails updating pre-commit hooks
  to no longer ignore these files.
primer_glossary:
- term: ChangeLog
  definition: A file historically used to record changes made to a software project,
    often including dates, authors, and descriptions of modifications.
- term: GDB
  definition: The GNU Debugger, a powerful tool for debugging programs written in
    C, C++, Fortran, and other languages.
- term: git log
  definition: A Git command that displays commit history, showing when and why changes
    were made to a codebase.
- term: pre-commit hooks
  definition: Scripts that automatically run before a commit is made to check for
    code style, formatting, or potential errors, helping to maintain code quality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260713113348.251434BA2E0C@sourceware.org
date: '2026-07-13'
is_stub: true
stub_reason: low_score
---

ChangeLog files, which have not been updated since 2021, are no longer maintained. To declutter the source tree and improve file system operations like searching and refactoring, these files are moved from their original directories into a new top-level 'archive' directory. This change reduces noise for developers who use tools like `git log` for version history.
