---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- concurrency
- fortran
commit_hash: bcf14085d8270f173ee6f1f4f9ae8352959e5ca1
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: Fix data race on unit stream pointer during concurrent I/O
  operations.'
tldr: Fixes a data race in libgfortran's unit stream pointer handling to ensure thread-safe
  concurrent I/O.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch resolves a race condition in `libgfortran/io/unix.c` involving
  the `gfc_unit`'s `stream` pointer. The `find_file0` function reads this pointer
  with only unit-level locking, while `new_unit`, `set_internal_unit`, and close paths
  modify it with unit mutexes. This allows `find_file0` to observe a stale, NULL,
  or freed `stream` pointer. The fix introduces `file_dev` and `file_ino` members
  to `gfc_unit` and uses new accessor functions (`get_unit_stream`, `unit_file_id_matches`)
  that employ acquire/release semantics for the `stream` pointer. `find_file0` now
  compares the `file_dev`/`file…
primer_glossary:
- term: data race
  definition: A concurrency issue where two or more threads access the same memory
    location, and at least one of the accesses is a write, without proper synchronization,
    leading to unpredictable behavior.
- term: unit stream pointer
  definition: In libgfortran, a pointer within a `gfc_unit` structure that refers
    to the underlying file stream object used for I/O operations.
- term: acquire/release semantics
  definition: Memory ordering guarantees provided by atomic operations. 'Acquire'
    ensures that memory operations preceding the atomic load are visible to other
    threads that perform a 'release' store to the same location. 'Release' ensures
    that memory operations preceding the atomic store become visible to other threads
    performing an 'acquire' load.
- term: mutex
  definition: A mutual exclusion primitive used to protect shared data from being
    accessed by multiple threads simultaneously, ensuring that only one thread can
    hold the mutex (and thus access the data) at a time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bcf14085d8270f173ee6f1f4f9ae8352959e5ca1
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This commit addresses a data race condition in libgfortran's I/O handling that could occur during concurrent operations. Specifically, the `find_file0` function could dereference a stream pointer that was concurrently modified or freed by other I/O operations (like `new_unit`, `set_internal_unit`, or `close`). The fix involves storing file device and inode information separately and using atomic operations (acquire/release semantics) when accessing the stream pointer, ensuring that `find_file0` only compares identifiers and avoids dereferencing potentially invalid pointers.
