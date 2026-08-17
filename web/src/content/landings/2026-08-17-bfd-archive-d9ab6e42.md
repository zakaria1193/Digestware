---
project: binutils
subsystem: bfd/archive
patch_id: null
tags:
- security
- memory-safety
- archive
- linker
- CVE
commit_hash: d9ab6e42e739fe826b02a5f868586132ea2d893a
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix use-after-free in archive symbol map loader that corrupted linker searches
tldr: Plugs a use-after-free in BFD's archive symbol map code that freed map entries
  prematurely, breaking linker symbol lookups.
impact_score: 9
performance_win: false
breaking_change: false
outcome: committed
primer_expert: BFD's archive symbol map (armap) is the in-memory index `bfd` keeps
  so the linker can resolve symbols from static archives without scanning every member.
  `_bfd_load_armap` populates this index from archive headers, allocating `struct
  orl` entries via objalloc. `_bfd_compute_and_push_armap` orchestrates fallback map
  generation when headers are missing, but its cleanup logic—`bfd_release` from a
  `first_name` marker—was freeing the map right after `_bfd_load_armap` returned.
  The `orl` structure holds per-symbol metadata (file position or member BFD pointer,
  name, namidx) for armap writers; the r…
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, the core abstraction layer in binutils
    that presents a uniform API over object files, executables, archives, and core
    dumps regardless of format (ELF, COFF, XCOFF, etc.).
- term: armap
  definition: Archive symbol map, an index stored at the front of a static library
    (`.a`) that maps global symbols to the archive members that define them, enabling
    the linker to extract only the needed `.o` files without scanning every entry.
- term: _bfd_load_armap
  definition: BFD function that parses an existing armap from an archive's header
    and loads it into the in-memory `struct orl` array for fast linker symbol lookups.
- term: _bfd_compute_and_push_armap
  definition: BFD orchestrator function that either loads an existing armap via `_bfd_load_armap`
    or builds one by iterating archive members, then passes the map to format-specific
    writers.
- term: struct orl
  definition: Archive symbol map entry structure in BFD, holding a symbol name and
    either a file offset or a pointer to the member BFD that defines it. Used internally
    during armap generation and serialization.
- term: objalloc
  definition: BFD's arena allocator for per-BFD temporary data. Memory is freed in
    bulk with `bfd_release` from a checkpoint, which makes it fast but requires careful
    ordering to avoid freeing live data.
- term: use-after-free
  definition: Memory-safety bug where code accesses a pointer after the backing allocation
    has been freed. In this case, armap entries were freed before the linker finished
    symbol resolution, leaving dangling pointers that could crash or corrupt data
    structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260817012240.C8A944BA2E3D@sourceware.org
date: '2026-08-17'
is_stub: false
stub_reason: ''
---

The linker's archive symbol map loader `_bfd_load_armap` was freeing the symbol map entries immediately after creating them, leaving dangling pointers that could crash or misbehave during later symbol resolution. This happened because `_bfd_compute_and_push_armap` called `bfd_release` to free objalloc memory starting from a dummy allocation, inadvertently discarding the just-loaded map. The patch also simplifies `struct orl` by removing the redundant `name` pointer indirection and the `namidx` field, which can be recalculated on demand during armap serialization. This fix was discovered while addressing CVE-2026-19548 and prevents silent corruption of linker symbol tables for mapless archives.
