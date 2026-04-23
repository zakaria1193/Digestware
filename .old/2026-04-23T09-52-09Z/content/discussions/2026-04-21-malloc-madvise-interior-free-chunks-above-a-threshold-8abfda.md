---
project: glibc
subsystem: malloc
patch_id: null
tags:
- glibc
- malloc
- memory management
- tcache
- madvise
discussion_id: cover.1776760573.git.xavier.roche@algolia.com
source_type: public_inbox
title: '[RFC PATCH 0/1] malloc: madvise interior free chunks above a threshold'
headline: 'Malloc: Madvise interior free chunks above a threshold'
tldr: Call madvise() on large free chunks to release memory back to the kernel, avoiding
  RSS bloat after tcache was introduced.
stakes: Reduces memory footprint in applications with frequent allocations and deallocations,
  potentially improving performance and resource utilization.
proposer: Xavier Roche <xavier.roche@algolia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potential overhead of `madvise()` calls.
- Choice between `MADV_FREE` (lazy release) and `MADV_DONTNEED` (aggressive release).
- Complexity of managing a per-arena counter to limit syscall frequency.
exchanges:
- author: Xavier Roche <xavier.roche@algolia.com>
  role: proposer
  position: Proposes to extend `_int_free_maybe_trim` to `madvise` the page-aligned
    interior of consolidated chunks >= 64 KB, using the caller's original pre-merge
    chunk size as the gate.
  quote: 'Extend _int_free_maybe_trim to madvise the page-aligned interior

    of consolidated chunks >= ATTEMPT_TRIMMING_THRESHOLD (64 KB),

    using the'
primer_expert: Since glibc 2.26, the introduction of tcache means that `free()` no
  longer returns physical pages to the kernel for chunks in the interior of the arena
  heap. This patch proposes to call `madvise()` with `MADV_FREE` or `MADV_DONTNEED`
  on large free chunks within `_int_free_maybe_trim` in `malloc/malloc.c` to release
  memory back to the kernel. This aims to mitigate RSS bloat observed after the introduction
  of tcache. The patch introduces a per-arena counter to avoid excessive syscalls.
primer_general: The GNU C Library's (glibc) malloc implementation manages dynamic
  memory allocation for programs. When memory is no longer needed, it's freed.  However,
  after glibc version 2.26, freed memory isn't always immediately returned to the
  operating system, potentially leading to a larger memory footprint (RSS) than expected.
  This patch proposes a solution to release unused memory back to the OS by using
  the `madvise()` system call, which provides hints to the kernel about how memory
  is being used. By advising the kernel that certain regions are no longer needed,
  the system can reclaim those resources, reducing the application's overall memory
  usage.
series_id: 'glibc:malloc: madvise interior free chunks above a threshold'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/cover.1776760573.git.xavier.roche@algolia.com
bugzilla_url: null
date: '2026-04-21'
---

This patch proposes calling `madvise()` on the interior of large free chunks in the glibc malloc implementation. Since glibc 2.26, `free()` no longer returns physical pages to the kernel for chunks in the interior of an arena heap due to the introduction of tcache. This can lead to increased RSS. The patch aims to address this by releasing unused memory back to the kernel, either lazily or aggressively based on chunk size, similar to what `malloc_trim()` does.
