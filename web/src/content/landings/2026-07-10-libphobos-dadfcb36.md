---
project: gcc
subsystem: libphobos
patch_id: null
tags:
- libphobos
- netbsd
- linker
- ELF
commit_hash: dadfcb36d905c619f196106ceea6e0f37831f5be
source_type: github
author: Rainer Orth
headline: 'libphobos: Disable .note.GNU-stack on NetBSD'
tldr: Disables the emission of .note.GNU-stack section on NetBSD to fix linker warnings
  and align with system behavior.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `libdruntime/config/common/threadasm.S` to prevent
  the emission of the `.note.GNU-stack` section on NetBSD. This addresses linker warnings
  from `gld` on NetBSD/amd64, which differ from FreeBSD/OpenBSD in their handling
  of this ELF note. NetBSD does not define `TARGET_ASM_FILE_END`, and the bundled
  GCC does not emit this note, so explicitly including it is unnecessary and introduces
  warnings.
primer_glossary:
- term: .note.GNU-stack
  definition: An ELF section that indicates whether the stack segment is executable.
    This is used by some security mechanisms and loaders, but its presence or absence
    can lead to warnings if not handled consistently across platforms.
- term: libphobos
  definition: The runtime library for the D programming language in GCC. It provides
    essential functionalities like memory management, concurrency, and I/O.
- term: gld
  definition: GNU Linker, the standard linker used by GCC. It combines object files
    and libraries into an executable or library, resolving symbols and applying relocations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dadfcb36d905c619f196106ceea6e0f37831f5be
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This commit disables the generation of the `.note.GNU-stack` section for libphobos on NetBSD to resolve linker warnings about executable stacks. NetBSD's linker (`gld`) warns when this section is missing, but the NetBSD platform does not require or use it, unlike FreeBSD and OpenBSD. The change removes its inclusion from `libdruntime/config/common/threadasm.S` for NetBSD.
