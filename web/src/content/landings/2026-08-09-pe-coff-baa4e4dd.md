---
project: gcc
subsystem: pe/coff
patch_id: null
tags:
- PE/COFF
- visibility
- linker
- MinGW
- Cygwin
commit_hash: baa4e4ddf800602d818470ef493d3508c4e1e32a
source_type: github
author: Oleg Tolmatcev
headline: 'PE/COFF: Implement visibility attribute via .drectve'
tldr: PE/COFF targets now support the visibility attribute by emitting directives
  to the .drectve section, matching Clang's behavior.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change enables the visibility attribute on PE/COFF targets by
  leveraging the `.drectve` section, similar to Clang's approach. For symbols marked
  `VISIBILITY_HIDDEN` or `VISIBILITY_INTERNAL`, the compiler now emits `-exclude-symbols`
  directives into `.drectve`, rather than just issuing a warning. The GNU linker,
  which processes this section for auto-exporting symbols from DLLs, correctly interprets
  these directives. This ensures that symbols with restricted visibility are not exported,
  providing proper control over the DLL interface.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format. The standard file format
    for executables, object code, and DLLs on 32-bit and 64-bit versions of Windows.
    MinGW and Cygwin use this format on Linux.
- term: visibility attribute
  definition: A C/C++ language extension (supported by GCC and Clang) that allows
    developers to control the visibility of symbols (functions, variables) in shared
    libraries. Common levels are default, hidden, internal, and protected.
- term: .drectve
  definition: A special section in PE/COFF object files used for directives that are
    processed by the linker. Common uses include specifying linker options or exclusion
    directives.
- term: MinGW
  definition: Minimalist GNU for Windows. A development environment for creating Windows
    applications using the GNU Compiler Collection.
- term: Cygwin
  definition: A POSIX-compatible environment for Windows that provides a Linux-like
    interface and tools, including GCC.
- term: auto-export
  definition: A feature of some linkers (like the GNU linker on PE/COFF targets) where
    symbols are automatically exported from a DLL unless explicitly excluded.
- term: VISIBILITY_HIDDEN
  definition: A visibility attribute level that makes a symbol not visible outside
    the shared object where it is defined. It cannot be referenced from other modules.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/baa4e4ddf800602d818470ef493d3508c4e1e32a
date: '2026-08-09'
is_stub: false
stub_reason: ''
---

GCC's PE/COFF targets (MinGW, Cygwin) previously ignored the visibility attribute with a warning. This commit implements support for `VISIBILITY_HIDDEN` and `VISIBILITY_INTERNAL` by emitting `-exclude-symbols` directives into the `.drectve` section. This behavior aligns with Clang and ensures that hidden symbols are correctly excluded from DLL exports, as the GNU linker respects these directives during auto-export processing.
