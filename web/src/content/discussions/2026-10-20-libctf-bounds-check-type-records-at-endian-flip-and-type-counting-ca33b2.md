---
project: binutils
subsystem: libctf
patch_id: null
tags:
- binutils
- libctf
- CTF
- security
- buffer overflow
discussion_id: CA+DP1erWmq0wDshtMZtYifj0a8UjHOTS8ZUN+qH9yiZHaZK30Q@mail.gmail.com
source_type: public_inbox
title: '[PATCH] libctf: bounds-check type records at endian flip and type counting'
headline: 'Libctf: Bounds-check type records at endian flip and type counting'
tldr: Fixes heap buffer overflows and data corruption in libctf when processing malformed
  or foreign-endian CTF type data.
proposer: Ilias <iliasaberkane2908@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Slight performance overhead due to additional bounds checks, though necessary for
  security.
- Requires careful validation of record sizes and offsets to avoid introducing new
  bugs.
exchanges:
- author: Ilias <iliasaberkane2908@gmail.com>
  role: proposer
  position: Submits a patch to add bounds checks to libctf's type record processing
    functions, preventing heap overflows and data corruption when handling malformed
    or foreign-endian CTF data.
  quote: 'opening a foreign-endian CTF dict whose type section contains a record

    whose variable-length data runs past the end of the section (attacker

    controls kind and vlen) makes flip_types() swap up to vlen * elem

    bytes past the malloc''d buffer (heap OOB read-modify-write), before

    init_static_types() ever runs.'
primer_expert: This patch addresses heap buffer overflows in `libctf`'s handling of
  CTF data, particularly when dealing with foreign-endian dictionaries or malformed
  type records. The vulnerability lies in `flip_types()` and related functions trusting
  record metadata (like `kind` and `vlen`) without verifying that the entire record,
  including its variable-length data, fits within the allocated type section buffer.
  This can lead to OOB writes when swapping bytes across endianness. The fixes ensure
  that `get_ctt_size_*()` correctly identifies large-form records before accessing
  `lsize` fields, and that `init_…
primer_glossary:
- term: libctf
  definition: A library for reading and writing Compact Type Format (CTF) data, used
    for debugging information.
- term: CTF
  definition: Compact Type Format, a debugging data format designed to be more compact
    than DWARF.
- term: heap buffer overflow
  definition: A vulnerability where a program writes data beyond the boundaries of
    an allocated buffer on the heap, potentially corrupting adjacent memory or executing
    malicious code.
- term: endianness
  definition: The order in which bytes of a multi-byte data word are stored in computer
    memory. Little-endian stores the least significant byte first, while big-endian
    stores the most significant byte first.
- term: ASan
  definition: AddressSanitizer, a fast memory error detector for C/C++. It finds issues
    like buffer overflows and use-after-free.
- term: OOB
  definition: Out-of-Bounds. Refers to memory accesses that read or write outside
    the allocated bounds of a buffer.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+DP1erWmq0wDshtMZtYifj0a8UjHOTS8ZUN+qH9yiZHaZK30Q@mail.gmail.com
bugzilla_url: null
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This patch addresses security vulnerabilities in `libctf` related to processing Compact Type Format (CTF) data. Specifically, when a foreign-endian CTF dictionary contains type records with malformed variable-length data that extends beyond the allocated section, `flip_types()` can perform heap out-of-bounds read-modify-write operations. Additionally, truncated record tails can cause out-of-bounds reads during type flipping and counting. The patch adds bounds checks to `get_ctt_size_*()`, `init_static_types_internal()`, and `flip_types()` to ensure records are only processed if they fit within the section, preventing these overflows. A regression test is included.
