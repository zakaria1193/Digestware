---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- binutils
- ld
- linker
- performance
- pe
discussion_id: 6099364a-9972-46ef-936e-83ce696eeb36@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld: Read the output in chunks when computing the PE build-id'
headline: 'ld: Improve PE build-id computation efficiency'
tldr: The linker now reads PE files in chunks for build-id computation, improving
  performance.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves link time performance by optimizing build-id computation at the cost of
  slightly more complex I/O handling.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Submitted a patch to optimize PE build-id computation by reading files
    in chunks.
  quote: "pecoff_checksum_contents read the output file back one byte at a time,\n\
    seeking before every byte and passing each byte to the hash function\nseparately.\
    \  For a 235 MB executable this took about 15% of the link\ntime.\n\nRead the\
    \ file using a 64 KB heap buffer.  If its allocation fails,\nfall back to a 64-byte\
    \ buffer on the stack.\n\nld/\n\t* emultempl/pe.em (pecoff_checksum_contents):\
    \ Read the file in\n\tch…"
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Approved the proposed change.
  quote: Okay.
primer_expert: The `pecoff_checksum_contents` function within `binutils/ld` is responsible
  for computing the build-id for PE (Portable Executable) files. The original implementation
  processed the file byte-by-byte, involving frequent I/O operations and seeks, which
  proved to be a bottleneck, consuming up to 15% of link time for large files. This
  patch optimizes this by introducing buffered I/O using a heap-allocated buffer,
  with a stack-based fallback for robustness. This change affects the `emultempl/pe.em`
  and `emultempl/pep.em` files.
primer_glossary:
- term: PE
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows operating systems. Binutils
    supports generating and manipulating PE files.
- term: build-id
  definition: A unique identifier embedded in an executable or library that helps
    in matching the binary to its debugging information. It's often generated from
    the file's content.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: emultempl
  definition: A directory within binutils that contains template files for different
    executable formats (like PE, COFF, ELF), allowing the linker to be configured
    for various targets.
- term: checksum
  definition: A value computed from a block of data to detect errors. In this context,
    it's part of the build-id generation process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/6099364a-9972-46ef-936e-83ce696eeb36@suse.com
bugzilla_url: null
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

This patch improves the efficiency of the `pecoff_checksum_contents` function in the linker (`ld`) when computing the PE build-id. Previously, it read the file byte-by-byte, which was slow for large executables. The change implements reading the file using a 64KB buffer, falling back to a stack-allocated 64-byte buffer if memory allocation fails. This optimization significantly reduces the time spent on build-id computation.
