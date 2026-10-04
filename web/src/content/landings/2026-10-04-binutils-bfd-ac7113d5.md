---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- coff
- PE
- crash fix
commit_hash: ac7113d5e2452c54c5de3c261f00b157ababbd51
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix segfault in coff-go32-exe PE parsing
tldr: Corrected BFD to properly handle coff-go32-exe files, preventing segfaults and
  incorrect format recognition.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Commit ac7113d5e2452c54c5de3c261f00b157ababbd51 addresses a bug in
  `bfd/format.c` affecting the `coff-go32-exe` format. Previously, `bfd.offset` was
  repurposed, leading to incorrect `bfd_check_format` behavior and a `BFD_ASSERT`
  in `format.c:777`. The fix adds an `origin` field to `struct bfd_preserve` and modifies
  `bfd_preserve_save` and `bfd_preserve_restore` to manage it. This prevents BFD from
  incorrectly matching against parts of the file after the Go32 stub and ensures correct
  format identification, resolving segfaults and ambiguity issues reported by oss-fuzz.
primer_glossary:
- term: coff-go32-exe
  definition: A specific variant of the COFF executable file format used for DOS executables
    running under GO32 extenders.
- term: PE
  definition: Portable Executable, a file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows.
- term: BFD
  definition: The Binary File Descriptor library, a generic interface for handling
    various object file formats.
- term: bfd.offset
  definition: A field within the BFD structure that traditionally represented an offset
    within an archive. Its meaning was changed, leading to misinterpretations for
    certain file formats.
- term: segfault
  definition: A segmentation fault, an error that occurs when a program accesses a
    memory location that it is not allowed to access.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261004021638.788684BA79A1@sourceware.org
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

A crash in `_bfd_pe_print_private_bfd_data_common` when processing coff-go32-exe files has been fixed. Changes in BFD altered the meaning of the `bfd.offset` field, causing misinterpretation of file structure for subsequent target matches. This led to assertions failing and segfaults. The fix introduces `origin` to `struct bfd_preserve` and ensures it's saved and restored correctly, preventing BFD from misidentifying file formats and avoiding the crash.
