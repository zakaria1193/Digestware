---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- performance
- memory management
- pdb
discussion_id: 20261106203339.272-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] bfd: Grow in-memory BFD buffers geometrically'
headline: 'bfd: Grow in-memory BFD buffers geometrically'
tldr: BFD library patch improves performance by using geometric growth for in-memory
  buffers.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased memory overhead due to larger buffer capacities, though this is generally
  acceptable for performance gains.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Introduces geometric buffer growth for in-memory BFDs to avoid quadratic
    reallocations and improve performance.
  quote: 'memory_bwrite and memory_bseek grew the buffer in 128-byte steps, so

    building a large in-memory BFD out of many small writes reallocated and

    copied the whole buffer repeatedly.  This made writing PDB streams

    quadratic: linking a 235 MB executable with --pdb spent more than half

    of its time in realloc.'
primer_expert: This patch modifies the BFD library's memory buffer management. Previously,
  `memory_bwrite` and `memory_bseek` grew buffers in fixed 128-byte increments, leading
  to quadratic complexity (O(n^2)) for many small writes, as seen when generating
  PDB streams. The solution implements a geometric growth strategy (e.g., doubling
  capacity or growing by 1/8th) to amortize reallocation costs, improving performance
  for large in-memory buffer operations. It also includes fallbacks for exact allocation
  if geometric growth fails.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a GNU library used for accessing and
    manipulating various executable binary file formats.
- term: in-memory BFD
  definition: A Binary File Descriptor object that is created and manipulated entirely
    in RAM, rather than being backed by a file on disk.
- term: reallocation
  definition: The process of moving a block of memory to a new, larger location when
    the current memory block is no longer sufficient to hold the data.
- term: quadratic complexity
  definition: A type of computational complexity where the runtime or space required
    grows proportionally to the square of the input size (O(n^2)). This is generally
    considered inefficient.
- term: PDB
  definition: Program Database, a file format used by Microsoft Visual C++ for storing
    debugging and project information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261106203339.272-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch optimizes the BFD library's handling of in-memory buffers by changing their growth strategy from a fixed 128-byte increment to a geometric progression (growing by one-eighth of capacity, with a minimum of 128 bytes). This significantly reduces the number of reallocations and copies required when building large in-memory BFDs, which was previously a quadratic performance bottleneck, especially when writing PDB streams. The change improves performance for operations like linking large executables with PDB support.
