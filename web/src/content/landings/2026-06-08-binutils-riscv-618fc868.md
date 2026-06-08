---
project: binutils
subsystem: binutils/riscv
patch_id: null
tags:
- risc-v
- linker
- bugfix
commit_hash: 618fc86830cb51295ff9e177c0c55ebc93e5efc5
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: RISC-V `ld` avoids segmentation fault when linking crti.o
tldr: Binutils `ld` no longer crashes when linking certain RISC-V object files by
  adding a null pointer check.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Binutils commit 413cf36d8e81 changed riscv_parse_add_subset, part of
  the RISC-V ELF object file attribute parser in `bfd/elfxx-riscv.c`, to assume that
  riscv_spec_class `isa_spec` would always be non-null. However, certain object files
  such as `crti.o` — which contains C runtime initialization code — can be linked
  with object attributes that cause `riscv_parse_add_subset` to be called with a null
  `isa_spec` pointer, leading to a segmentation fault. This fix adds a null check
  for `rps->isa_spec` to prevent the dereference of a null pointer, thus stabilizing
  the linker behavior.
primer_general: When you compile code, the compiler generates object files, and then
  a linker combines these object files into an executable program. Part of this linking
  process involves parsing specific attributes within the object files, particularly
  for architecture-specific features like those in RISC-V. Binutils is a collection
  of binary tools, which includes the linker (`ld`). This change addresses a bug in
  the RISC-V-specific part of the linker that handles these object file attributes.
  If a particular object file (like `crti.o`, which is part of the standard C library
  runtime) was missing crucial information about the RISC-V instruction set architecture,
  the linker would crash because it tried to access data through a pointer that was
  unexpectedly empty. The fix simply adds a check to ensure that this pointer isn't
  empty before trying to use it, preventing the crash and making the linker more robust.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260608003813.60C974C900DD@sourceware.org
date: '2026-06-08'
is_stub: false
---

This commit fixes a segmentation fault in the linker (`ld`) when processing RISC-V object files, specifically `crti.o`, which would occur when `riscv_parse_add_subset` was called with a null `isa_spec`. The fix reinstates a null pointer check that was previously removed, preventing the linker from dereferencing a null pointer and crashing. This ensures that users compiling for RISC-V do not encounter unexpected linker crashes.
