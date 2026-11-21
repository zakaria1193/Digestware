---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- binutils
- Zstandard
- compression
- security
discussion_id: loopr.27.7vxctjzywslg@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] readelf: reject incomplete Zstandard decompression'
headline: 'readelf: reject incomplete Zstandard decompression'
tldr: Fix readelf to reject Zstandard-compressed sections where the decompressed size
  does not match the declared size, preventing the display of uninitialized data.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves robustness by validating decompressed data size.
- May reject slightly malformed files that were previously partially processed.
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Submits a patch to `readelf` to reject Zstandard-compressed sections if
    the decompressed output size does not match the declared uncompressed size, preventing
    the display of uninitialized data.
  quote: Reject the result when the number of decompressed bytes does not match the
    declared uncompressed size.
primer_expert: The `uncompress_section_contents` function in `readelf` handles Zstandard
  decompression. Previously, it only checked `ZSTD_isError()` and not the returned
  decompressed size against the `uncompressed_size` specified in the ELF compression
  header. This could lead to reading uninitialized memory if the actual decompressed
  data was smaller than expected. This patch adds a check for `ret != uncompressed_size`.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: Zstandard
  definition: A fast lossless compression algorithm.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps.
- term: AddressSanitizer
  definition: A memory error detector for C/C++ that finds use-after-free, buffer
    overflows, and use-after-return.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.27.7vxctjzywslg@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in `readelf` where Zstandard-compressed sections could be accepted even if the decompression process returned fewer bytes than declared in the ELF header. This led to `readelf` printing uninitialized heap contents from the unwritten tail of the buffer. The fix ensures that the number of decompressed bytes must match the declared uncompressed size.
