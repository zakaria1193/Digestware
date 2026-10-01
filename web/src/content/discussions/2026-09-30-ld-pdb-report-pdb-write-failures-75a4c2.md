---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- debugging
- error handling
- bugfix
discussion_id: 20260930193657.733-10-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Report failures to write the PDB file'
headline: 'ld/pdb: Report PDB write failures'
tldr: Ensures linker reports errors when writing PDB files, preventing silent failures.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This change in the PDB writing functionality of binutils' linker (ld)
  addresses a silent failure mode. PDB streams are flushed and written upon closing
  the file handle (`bfd_close`). If `bfd_close` encountered an error (e.g., disk full,
  I/O error), the return value was ignored. This meant that `ld` would exit successfully
  even if the PDB file was incomplete or corrupted. The patch now checks `bfd_close`'s
  return value and emits an error message via `einfo` if it fails.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or shared library.
- term: bfd_close
  definition: A function in the BFD library that closes a binary file descriptor,
    flushing any pending writes.
- term: einfo
  definition: A logging function used within binutils to print informational messages.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-10-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch modifies the linker's PDB writing process to check the return value of `bfd_close`. Previously, errors during the closing and writing of PDB streams were ignored, leading to truncated files and successful exits. The change adds a warning message when `bfd_close` fails, ensuring that write errors are reported to the user.
