---
project: binutils
subsystem: binutils/ctf
patch_id: null
tags:
- binutils
- ctf
- debugging
- security
commit_hash: d5a65d4c5acf91b6fa4223e930b3efd0fa8f4753
source_type: public_inbox
author: Alan Modra <amodra@gmail.com>
headline: Fix CTF type parsing to prevent SIGSEGV on malformed input.
tldr: CTF type parsing code now validates input sizes against section lengths to prevent
  crashes.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Binutils CTF (Common Type Format) parsing logic. Fixes a `SIGSEGV`
  in `libctf/ctf-open.c` by adding bounds checks for variable byte lengths (`vbytes`)
  against the total type section size in both `init_static_types_internal` and `upgrade_types_v1`.
  Previously, invalid `vbytes` could lead to out-of-bounds reads or writes.
primer_glossary:
- term: CTF
  definition: Common Type Format. A debugging data format used to describe type information,
    often an alternative to DWARF. It is stored within object files.
- term: binutils-gdb
  definition: A project that combines the GNU Binutils (assembler, linker, etc.) and
    the GNU Debugger (GDB).
- term: SIGSEGV
  definition: A signal raised by the operating system when a program attempts to access
    a memory address that it is not allowed to access, typically indicating a segmentation
    fault or crash.
- term: libctf
  definition: The library within binutils-gdb responsible for reading and writing
    CTF debugging information.
- term: Variable-length record
  definition: A data structure within CTF where the size is not fixed but determined
    by a length field or other dynamic means, requiring careful handling to avoid
    buffer overflows.
discussion_id_link: public_inbox:binutils#34342
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260703011610.212BA4BA23D9@sourceware.org
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

This commit addresses a crash (SIGSEGV) in the CTF (Common Type Format) parsing library within binutils-gdb. It adds crucial sanity checks in `init_static_types_internal` and `upgrade_types_v1` to ensure that calculated variable-length record sizes do not exceed the bounds of the type section, thus preventing buffer overflows and crashes with malformed CTF data.
