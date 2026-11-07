---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- binutils
- performance
- pe
- build-id
discussion_id: 20261106203339.272-4-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] ld: Read the output in chunks when computing the PE build-id'
headline: 'ld: Read output in chunks when computing PE build-id'
tldr: Linker patch improves build-id computation performance for PE files by reading
  output in chunks.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Optimizes PE build-id computation by reading the output file in chunks
    instead of byte-by-byte.
  quote: 'pecoff_checksum_contents read the output file back one byte at a time,

    seeking before every byte and passing each byte to the hash function

    separately.  For a 235 MB executable this took about 15% of the link

    time.


    Read the file using a 64 KB heap buffer.  If its allocation fails, fall

    back to a 64-byte buffer on the stack.'
primer_expert: This patch addresses a performance bottleneck in the GNU linker's (`ld`)
  calculation of the PE file build-id. The function `pecoff_checksum_contents` was
  inefficiently reading the entire output file byte-by-byte, causing significant overhead.
  The proposed solution reads the file in larger chunks (64KB heap buffer, with a
  64-byte stack fallback) to speed up this process, especially for large executables.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into executables or other binary formats.
- term: PE file
  definition: Portable Executable, the file format used for executables, DLLs, and
    object files in Windows.
- term: build-id
  definition: A unique identifier for a build of an executable or library, used for
    debugging and identifying specific versions of binaries.
- term: checksum
  definition: A value computed from a block of data for the purpose of detecting errors.
    In this context, it's used as part of the build-id calculation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261106203339.272-4-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch optimizes the performance of the GNU linker's (`ld`) build-id computation for PE files. Previously, `pecoff_checksum_contents` read the output file byte-by-byte, which was inefficient for large files (e.g., 15% of link time for a 235 MB executable). The change introduces reading the file in 64 KB chunks using a heap buffer, with a fallback to a 64-byte stack buffer if heap allocation fails, significantly reducing the overhead.
