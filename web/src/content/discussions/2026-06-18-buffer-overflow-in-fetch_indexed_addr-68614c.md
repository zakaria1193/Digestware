---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- dwarf
- buffer overflow
- fuzzing
- binutils
discussion_id: ajOJUf3EcSGggKdi@squeak.grove.modra.org
source_type: public_inbox
title: buffer overflow in fetch_indexed_addr
headline: Buffer overflow in fetch_indexed_addr
tldr: This patch fixes potential integer overflows and buffer overflows in DWARF debugging
  information handling by adding stricter sanity checks.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Adds additional checks, which might have a negligible impact on performance for
  DWARF parsing, but significantly improves security.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a patch to prevent integer overflows and buffer overflows in
    DWARF parsing functions by adding more rigorous sanity checks.
  quote: "oss-fuzz found another case where sanity checks weren't good enough.\n\t\
    * dwarf.c (fetch_indexed_addr): Avoid integer overflow when\n\tsanity checking\
    \ field offset\n\t(fetch_indexed_offset): Similarly. Don't bother with \"too small\"\
    \n\twarning, which will be covered by field offset check. Warn\n\tabout base and\
    \ index rather than possibly overflowed calculation."
primer_expert: Within `binutils/dwarf.c`, `fetch_indexed_addr` and `fetch_indexed_offset`
  are responsible for safely retrieving address and offset values from DWARF sections,
  which describe debugging information. These functions operate on potentially untrusted
  input, where `offset`, `num_bytes`, `idx`, `base_address`, and `offset_size` are
  all `uint64_t`. The core vulnerability stems from insufficient bounds checking when
  calculating `offset + num_bytes` or `idx * offset_size + base_address`, potentially
  leading to integer overflow and subsequent out-of-bounds memory access. The fix
  implements explicit che…
primer_general: This patch fixes a security vulnerability in a part of the binutils
  software called DWARF, which stores debugging information inside compiled programs.
  Debugging information helps developers understand how their code is running. The
  specific problem is a "buffer overflow" that could happen when reading this debugging
  information. Imagine you have a box of fixed size (a buffer) to store numbers. If
  someone tries to put too many numbers into the box, or tries to access a number
  outside the box's boundaries, it can lead to the program crashing or, in worst cases,
  allow malicious code to run. This patch adds stricter checks to make sure that when
  the linker reads debugging information, it never tries to access memory outside
  the designated areas, thus preventing such overflows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajOJUf3EcSGggKdi@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-18'
is_stub: false
---

This proposal addresses a buffer overflow vulnerability identified by oss-fuzz in the DWARF debugging information handling within binutils. Specifically, the `fetch_indexed_addr` and `fetch_indexed_offset` functions in `dwarf.c` lacked sufficient sanity checks. The patch introduces more robust overflow prevention logic, particularly for calculating field offsets, and refines warning messages to be more precise about the source of the error.
