---
project: binutils
subsystem: mach-o
patch_id: null
tags:
- mach-o
- security
- vulnerability
- parser
- bfd
discussion_id: CAMqZ70YNLz8JBLzSXKCogEBnCGnxwu56B44vDy6W0V+gXB4TBg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v3] mach-o: fix out-of-bounds read in bfd_mach_o_read_prebound_dylib'
headline: 'mach-o: fix out-of-bounds read in bfd_mach_o_read_prebound_dylib'
tldr: Fixes an out-of-bounds read vulnerability in Mach-O binary parsing.
proposer: Venkateswara Reddy <venkatchallaceh@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 7
technical_tradeoffs:
- Fixes a critical out-of-bounds read vulnerability by removing unsafe pointer arithmetic.
- Maintains consistency with other Mach-O readers by not adding explicit checks for
  semantic garbage output from overlapping data, which could be added as a separate
  enhancement.
exchanges:
- author: Venkateswara Reddy Challa
  role: proposer
  position: Submits v3 of a fix for an out-of-bounds read in Mach-O parsing, removing
    pointer arithmetic that caused underflows and ensuring reads stay within validated
    offsets.
  quote: 'On the remaining lower-bound / overlap point: with the pointer arithmetic

    gone, both reads now stay within their validated load-command-relative

    file offsets, so there is no out-of-bounds access left -- only the

    possibility of semantically garbage output if the name offset points into

    the modules bitmap. That overlap case is not checked by the sibling

    readers either, so v3 stays consistent with t…'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the fix for out-of-bounds reads but reiterates concerns about
    potential semantic garbage output due to overlapping data if the name offset is
    not properly validated.
  quote: "From: Venkateswara Reddy Challa <venkatchallaceh@gmail.com>\nDate: Fri,\
    \ 16 Oct 2026 16:40:33 +0530\nSubject: [PATCH v3] mach-o: fix out-of-bounds read\
    \ in\n bfd_mach_o_read_prebound_dylib\n\nbfd_mach_o_read_prebound_dylib() read\
    \ the file-controlled name and\nlinked_modules offsets of an LC_PREBOUND_DYLIB\
    \ load command, checked only\nthat each was not greater than the load command\
    \ length, then derived two…"
primer_expert: This patch addresses a security vulnerability in the Mach-O file parser
  within binutils' BFD library. Specifically, the `bfd_mach_o_read_prebound_dylib`
  function incorrectly calculates memory offsets for `LC_PREBOUND_DYLIB` load commands.
  By subtracting a fixed constant from file offsets without ensuring a lower bound,
  pointer arithmetic could underflow, leading to reads outside the intended buffer.
  The fix removes this unsafe arithmetic. A reviewer notes that while the out-of-bounds
  read is fixed, the potential for semantic garbage output remains if offsets point
  into unrelated data, a scena…
primer_glossary:
- term: mach-o
  definition: Mach Object file format, the standard executable file format used by
    macOS, iOS, and other Apple operating systems. Binutils includes support for parsing
    and manipulating these files.
- term: out-of-bounds read
  definition: A memory access error where a program attempts to read data from a memory
    location outside the boundaries of an allocated buffer. This can lead to crashes
    or security vulnerabilities.
- term: load command
  definition: Structures within a Mach-O file that describe the layout and characteristics
    of the file, such as segments, libraries, and other metadata.
- term: LC_PREBOUND_DYLIB
  definition: A specific Mach-O load command that lists prebound dynamic libraries.
    This command contains information about library names and their offsets within
    the load command structure.
- term: BFD
  definition: Binutils 'Binary File Descriptor' library. It provides a common interface
    for reading and writing various object file formats, including Mach-O.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMqZ70YNLz8JBLzSXKCogEBnCGnxwu56B44vDy6W0V+gXB4TBg@mail.gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch (v3) addresses an out-of-bounds read vulnerability in the `bfd_mach_o_read_prebound_dylib` function when parsing Mach-O binaries. The vulnerability arose from pointer arithmetic with offsets that could underflow, leading to incorrect memory access. The fix removes the problematic pointer arithmetic, ensuring reads stay within validated file offsets. While this resolves the out-of-bounds access, the author notes a remaining possibility of semantically incorrect output if an offset points into the 'modules bitmap,' a condition not explicitly checked by sibling readers. They offer to add a specific check for this overlap if preferred.
