---
project: gcc
subsystem: libgcc/vxworks
patch_id: null
tags:
- libgcc
- vxworks
- powerpc64
- threading
commit_hash: 3af8760505bedeca17283ca9f7daca8e53b50eb9
source_type: github
author: Alexandre Oliva
headline: VxWorks thread creation API adjusted for correct type conversions.
tldr: VxWorks libgcc now correctly handles type conversions for thread entry points,
  fixing powerpc64 issues.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgcc/config/gthr-vxworks-thread.c` code now correctly adapts
  VxWorks' `taskSpawn` conventions to GCC's pthreads-like `__gthread_create` API.
  The `__task_wrapper` adaptor previously misused function pointer types and C argument
  promotions, causing issues on architectures like powerpc64 where `int` and `void
  *` differ in size. This commit rectifies `ENTRYPTR` and `__task_wrapper` formal
  parameters to use proper interface types and explicit conversions, removing risky
  double-underscore prefixes and fixing the indirection for the entry point pointer.
primer_glossary:
- term: __gthread_create
  definition: An abstraction in libgcc for creating threads, intended to provide a
    consistent interface across different threading backends.
- term: VxWorks
  definition: A real-time operating system (RTOS) widely used in embedded systems.
- term: powerpc64
  definition: A 64-bit variant of the PowerPC architecture, commonly used in servers
    and high-performance computing.
- term: void*
  definition: A generic pointer type in C that can point to any data type. Often used
    for passing arbitrary data between functions.
- term: int
  definition: A fundamental integer data type in C. Its size can vary by architecture,
    but is typically 32 bits on most modern systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3af8760505bedeca17283ca9f7daca8e53b50eb9
date: '2025-12-06'
is_stub: false
stub_reason: ''
---

The libgcc implementation for VxWorks has been updated to better align with its `__gthread_create` API. Previously, a wrapper function incorrectly assumed argument types, leading to type conversion issues, particularly on powerpc64. This change introduces explicit conversions and clarifies internal type declarations to ensure correctness.
