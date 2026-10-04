---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bugfix
- coff
- PE
- segfault
discussion_id: asG27CdAaBmPF3h2@squeak.grove.modra.org
source_type: public_inbox
title: coff-go32-exe segv in _bfd_pe_print_private_bfd_data_common
headline: coff-go32-exe segv in _bfd_pe_print_private_bfd_data_common
tldr: Fixes a segfault in binutils when handling coff-go32-exe files due to incorrect
  offset interpretation.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to fix a segfault in binutils related to handling coff-go32-exe
    files by correctly managing the `bfd.offset` and `origin` fields.
  quote: Commit 4d095f5b5e57 made use of bfd.offset in coff-go32-exe object files,
    changing the field's meaning from "offset in an archive".  This results in some
    confusion in bfd_check_format after an object file has been successfully recognised
    as coff-go32-exe because bfd.offset is then set for any further target matches
    (which means the match is done against that part of the file after the go32 stub).…
primer_expert: This patch addresses a bug in binutils' BFD library concerning the
  interpretation of file offsets for `coff-go32-exe` executables. A recent commit
  changed the meaning of `bfd.offset` from an archive member offset to an internal
  file offset, confusing the format detection logic. The fix involves correctly saving
  and restoring the `origin` field of `struct bfd_preserve` to ensure proper file
  identification, preventing segfaults and incorrect format ambiguities.
primer_glossary:
- term: coff-go32-exe
  definition: A specific executable file format used for 32-bit DOS extenders, often
    associated with DJGPP.
- term: BFD
  definition: The Binary File Descriptor library, a backend for binutils that provides
    a common interface for reading and writing various executable file formats.
- term: segv
  definition: Segmentation fault, a runtime error that occurs when a program accesses
    a memory location that it's not allowed to access.
- term: oss-fuzz
  definition: An open-source fuzzing service that helps projects find bugs in their
    code by automatically generating and testing inputs.
- term: PE
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/asG27CdAaBmPF3h2@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

A segfault in binutils' `_bfd_pe_print_private_bfd_data_common` function, triggered by oss-fuzz, is addressed by this patch. The issue arises from a recent change that repurposed the `bfd.offset` field for coff-go32-exe files, causing confusion in format checking. This change introduces `bfd_preserve_save` and `bfd_preserve_restore` to correctly handle the `origin` field, ensuring that files are accurately recognized as `coff-go32-exe` and not misidentified as other PE variants.
