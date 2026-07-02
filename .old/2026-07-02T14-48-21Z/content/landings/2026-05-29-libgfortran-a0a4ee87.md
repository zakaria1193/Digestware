---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- windows
- compatibility
- shared memory
commit_hash: a0a4ee875a49c7ffb04e6b7cec709a8cae90d3f8
source_type: github
author: Peter Damianov
headline: 'Libgfortran: Use MapViewOfFileEx instead of MapViewOfFileExNuma in caf_shmem'
tldr: Libgfortran now uses `MapViewOfFileEx` instead of `MapViewOfFileExNuma` for
  shared memory, maintaining Windows XP support.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `shared_memory.c` in libgfortran's `caf/shmem`
  component, replacing `MapViewOfFileExNuma` with `MapViewOfFileEx`. The change is
  specific to Windows and preserves Windows XP support without affecting functionality,
  as `NUMA_NO_PREFERRED_MODE` makes the two functions equivalent in behavior.
primer_general: This commit modifies the Libgfortran library, which provides runtime
  support for Fortran programs compiled with GCC.  Specifically, it changes how shared
  memory is handled on Windows operating systems. The change ensures that the library
  remains compatible with older versions of Windows (like Windows XP) while maintaining
  the same functionality on newer systems. Shared memory allows different parts of
  a program, or different programs, to access the same data in memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0a4ee875a49c7ffb04e6b7cec709a8cae90d3f8
date: '2026-05-29'
is_stub: false
---

Libgfortran now uses `MapViewOfFileEx` in `caf_shmem` instead of `MapViewOfFileExNuma` when mapping shared memory regions on Windows. This change maintains compatibility with Windows XP, as `MapViewOfFileExNuma` is only available on Windows Vista and later. Since the code was passing `NUMA_NO_PREFERRED_MODE`, the behavior is identical, but the older API is used for broader compatibility.
