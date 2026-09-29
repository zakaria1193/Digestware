---
project: binutils
subsystem: bfd/pe
patch_id: null
tags:
- binutils
- bfd
- pe
- debug
- compression
discussion_id: 20260928090146.4016188-2-tobias.deiminger@linutronix.de
source_type: public_inbox
title: '[PATCH 1/3] bfd/PE: fix debug section compression for pei-*'
headline: 'bfd/PE: fix debug section compression for pei-*'
tldr: Fixes incorrect handling of compressed debug sections in PE image files (pei-*).
proposer: Tobias Deiminger <tobias.deiminger@linutronix.de>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Accurately verifying compressed debug sections requires careful management of size
  fields in the PE header, distinguishing between compressed, uncompressed, and file-on-disk
  sizes.
- Ensuring compatibility with debuggers like GDB necessitates correct implementation
  of decompression logic, especially when dealing with variations in PE section header
  fields.
exchanges:
- author: Tobias Deiminger
  role: proposer
  position: Corrects the handling of compressed debug sections in PE image files (pei-*),
    ensuring successful decompression by using the compressed size for verification.
  quote: "bfd supports compressing debug sections for PE/Coff since a29a8af823af\n\
    (\"ChangeLog bfd\"). It works for pe, but never worked for pei in a full\nround\
    \ trip. For example:\n\n $ x86_64-w64-mingw32-gcc -g -o testprog testprog.c\n\
    \ $ objcopy --compress-debug-sections testprog.exe testprog_z.exe\n $ gdb --batch\
    \ -ex \"break fn\" -ex \"info line fn\" testprog_z.exe\n warning: Can't read data\
    \ for section '.zdebug_inf…"
primer_expert: This patch resolves a longstanding issue in BFD's PE backend where
  debug sections compressed with `--compress-debug-sections` could not be correctly
  decompressed and read for `pei-*` targets. The core problem was in `peicode.h:coff_swap_scnhdr_in`,
  which used `VirtualSize` (uncompressed size) instead of the actual compressed size
  for verification. The fix ensures that the correct compressed size is stored and
  used for decompression, and that `virt_size` is updated to the decompressed size
  only after successful decompression, enabling tools like GDB to read the debug information.
primer_glossary:
- term: PE image files (pei-*)
  definition: A specific variant of the PE (Portable Executable) file format, often
    used for Windows executables and DLLs, with specific characteristics that differ
    from standard PE files.
- term: debug sections
  definition: Sections within an executable file that contain debugging information,
    such as symbol tables, line number information, and DWARF data, used by debuggers.
- term: round trip
  definition: The process of applying an operation (e.g., compression) and then its
    inverse (e.g., decompression), verifying that the data returns to its original
    state.
- term: VirtualSize
  definition: A field in the PE section header that typically represents the size
    of the section in memory after decompression or loading, as opposed to its size
    on disk.
- term: SizeOfRawData
  definition: A field in the PE section header that represents the size of the section
    in the file on disk, usually aligned to a specific boundary.
series_id: 'binutils:bfd/pe: fix debug section compression for pei-*'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260928090146.4016188-2-tobias.deiminger@linutronix.de
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Tobias Deiminger corrects a bug where compressing debug sections for PE image files (`pei-*`) did not work correctly in a full round trip. The issue arose from BFD incorrectly using the uncompressed size (`VirtualSize`) instead of the compressed size for decompression verification. The fix ensures the compressed size is used, and `virt_size` is updated only after successful decompression.
