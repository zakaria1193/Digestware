---
project: glibc
subsystem: elf/loader
patch_id: null
tags:
  - thp
  - elf
  - gnu-property
  - madvise
  - aarch64
discussion_id: PAWPR08MB89821B4B4ABF7C634BA2DA93832A2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: '[RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: 'RFC: Embed THP preferences in ELF binaries via GNU properties'
tldr: 'Two new GNU ELF property flags let ld.so call madvise(MADV_HUGEPAGE) on read-only
  segments and heap arenas, enabling per-binary THP opt-in without sysadmin changes.'
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
  - 'Segment alignment: read-only PT_LOAD segments must be hugepage-aligned (2 MB on
    most arches) for madvise(MADV_HUGEPAGE) to succeed; misaligned segments silently
    skip promotion.'
  - 'Memory overhead: mapping small read-only segments as huge pages wastes physical
    memory; the opt-in flag avoids this for small binaries but moves the decision to
    link time.'
  - 'Heap compaction cost: GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC can trigger kernel memory
    compaction on allocation-heavy workloads, adding latency spikes that may outweigh
    TLB miss savings.'
  - 'COW splitting: promoting shared read-only pages to huge pages can split copy-on-write
    mappings under fork-heavy workloads, increasing private RSS.'
exchanges:
  - author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
    role: proposer
    position: Proposes two new GNU property bits — GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS
      and GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC — to let a binary declare THP preferences
      at link time, with ld.so honouring them via madvise() at startup.
    quote: null
primer_expert: 'Two new bits under GNU_PROPERTY_1_NEEDED in `.note.gnu.property` —
  `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` and `GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC`
  — direct `ld.so` to call `madvise(MADV_HUGEPAGE)` on read-only PT_LOAD segments and
  heap arenas at startup. Processing plugs into `sysdeps/unix/sysv/linux/dl-prop.h`
  alongside `GNU_PROPERTY_NO_COPY_ON_PROTECTED`. Key non-obvious interaction: in
  `_dl_map_segments`, alignment padding required for hugepage promotion can conflict
  with overlapping PT_LOAD segment assumptions, and on THP=madvise systems the hint is
  silently ignored for misaligned segments.'
primer_general: 'Linux Transparent Huge Pages (THP) improve performance for memory-heavy
  workloads by grouping 4 KB pages into 2 MB pages, reducing TLB pressure. Historically,
  enabling THP required either a system-wide kernel setting (affecting every process)
  or explicit madvise() calls embedded in application source code — neither option is
  practical for third-party or legacy binaries. This RFC proposes encoding THP preferences
  directly in ELF binaries using the .note.gnu.property section, the same standard
  mechanism already used for other binary-level hints (e.g. stack executable flags).
  At program start, ld.so reads these flags and issues madvise(MADV_HUGEPAGE) on the
  relevant memory regions automatically, so applications can opt in at build time without
  source changes and without requiring sysadmin intervention — valuable in containerised
  or shared-host environments.'
primer_glossary:
  - term: GNU_PROPERTY_1_NEEDED
    definition: A feature-flags word in the ELF .note.gnu.property section used by GNU
      toolchain components. Individual bits encode loader or runtime requirements that
      ld.so, the Linux kernel, and gdb inspect at load time.
  - term: .note.gnu.property
    definition: A standardised ELF note section that encodes binary-level capability
      and requirement flags. Toolchain components read it at load time to enable or
      verify features without inspecting source code.
  - term: THP (Transparent Huge Pages)
    definition: A Linux kernel feature that promotes contiguous 4 KB page mappings to
      2 MB (or larger) huge pages to reduce TLB misses and page-table overhead. Controlled
      globally via /sys/kernel/mm/transparent_hugepage/enabled or per-mapping via
      madvise().
  - term: madvise(MADV_HUGEPAGE)
    definition: A Linux syscall hint telling the kernel to prefer promoting a memory
      range to huge pages. In THP=madvise mode, only ranges explicitly marked this way
      are promoted, giving per-mapping control.
  - term: ld.so
    definition: "The ELF dynamic linker/loader (glibc's ld-linux.so). It maps shared
      libraries and the main executable into memory at startup, resolves symbols, applies
      relocations, and processes GNU properties before handing control to the program
      entry point."
  - term: PT_LOAD
    definition: An ELF program header type that instructs ld.so (or the kernel) to map
      a segment from the file into virtual memory. Typical PT_LOAD segments carry .text
      (code) and .rodata (constants).
  - term: ELF (Executable and Linkable Format)
    definition: The standard binary format for executables, shared libraries, and object
      files on Linux and most Unix-like systems. It defines how the linker assembles
      code and data and how the loader maps them into memory at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB89821B4B4ABF7C634BA2DA93832A2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-23'
---

Wilco Dijkstra (ARM) proposes two new GNU ELF property flags —
`GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS` and
`GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC` — that let a binary declare its preference
for Transparent Huge Pages at link time, rather than requiring runtime `madvise()`
calls in application code or system-wide kernel configuration.

When `ld.so` detects `GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS`, it calls
`madvise(MADV_HUGEPAGE)` on all read-only PT_LOAD segments (`.text`, `.rodata`) during
program startup. `GNU_PROPERTY_1_NEEDED_THP_ON_MALLOC` similarly instructs the heap
allocator to prefer huge pages for arena mappings. Both flags are encoded as bits under
the existing `GNU_PROPERTY_1_NEEDED` property word in `.note.gnu.property`, following
the same convention as `GNU_PROPERTY_NO_COPY_ON_PROTECTED`.

The proposal addresses a practical deployment gap: Linux's global `THP=always` mode
benefits code-heavy workloads but wastes memory for others, while `THP=madvise` mode
requires application code to call `madvise()` explicitly — something third-party or
legacy binaries cannot easily do. By embedding the preference in the ELF binary itself,
`ld.so` can honour it transparently in any environment running `THP=madvise` or
`THP=always`, with no source or sysadmin changes required.
