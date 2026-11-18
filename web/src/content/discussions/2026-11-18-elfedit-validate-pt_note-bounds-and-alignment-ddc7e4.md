---
project: binutils
subsystem: elfedit
patch_id: null
tags:
- binutils
- elfedit
- security
- ELF
- validation
discussion_id: CAO9RCZXnWU2z4_-Uh4v0tFHGAyGyX4R7ra7H3oX5XwRET2UT8Q@mail.gmail.com
source_type: public_inbox
title: '[PATCH] elfedit: validate PT_NOTE bounds and alignment'
headline: 'elfedit: validate PT_NOTE bounds and alignment'
tldr: A patch for `elfedit` adds validation for PT_NOTE segment bounds and alignment
  to prevent crashes and security issues when processing crafted binaries.
proposer: mustafa <mustafa@medios.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Increased validation logic complexity vs. improved security and robustness against
  malformed ELF files.
- Slight performance overhead from bounds checking vs. preventing critical crashes
  and vulnerabilities.
exchanges:
- author: mustafa <mustafa@medios.digiscrypt.com>
  role: proposer
  position: Submits a patch to `elfedit.c` that adds validation for PT_NOTE segment
    bounds and alignment, fixing potential crashes and security vulnerabilities.
  quote: 'update_gnu_property maps the whole file read/write and then walks every

    PT_NOTE segment, editing the GNU property notes in place.  The

    program header table is checked against the file size, but the PT_NOTE

    segments themselves are not: p_offset and p_filesz are used as they

    are to compute "map + p_offset", so a note segment that points outside

    the file makes elfedit read and write past the end of…'
primer_expert: This patch addresses security and robustness issues in `elfedit`, specifically
  within the `update_gnu_property` function. The function maps the ELF file and modifies
  GNU property notes in place. The vulnerability lies in not validating the bounds
  of PT_NOTE segments before accessing them. A malicious binary could provide `p_offset`
  and `p_filesz` values that point outside the mapped file, leading to a SIGSEGV or
  arbitrary memory writes. The patch also corrects alignment validation (`p_align`)
  to prevent division-by-zero and ensures power-of-two alignment, and refines the
  `datasz` bounds check…
primer_glossary:
- term: elfedit
  definition: A tool within binutils for editing ELF (Executable and Linkable Format)
    files.
- term: PT_NOTE
  definition: A segment type in an ELF file that contains arbitrary data, often used
    for versioning, OS-specific information, or custom metadata like GNU properties.
- term: p_offset
  definition: A field in an ELF Program Header table entry that specifies the offset
    from the beginning of the file to the first byte of the segment.
- term: p_filesz
  definition: A field in an ELF Program Header table entry that specifies the size
    in bytes of the segment in the file.
- term: p_align
  definition: A field in an ELF Program Header table entry that specifies the alignment
    requirement of the segment.
- term: SIGSEGV
  definition: A signal sent to a process when it attempts to access a memory location
    that it's not allowed to access, typically indicating a segmentation fault.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAO9RCZXnWU2z4_-Uh4v0tFHGAyGyX4R7ra7H3oX5XwRET2UT8Q@mail.gmail.com
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch enhances `elfedit`'s `update_gnu_property` function by adding crucial validation for Program Header table entries of type PT_NOTE. It checks that the `p_offset` and `p_filesz` values keep the note segment within the file's boundaries, preventing potential SIGSEGV crashes or memory corruption from crafted binaries. Additionally, it normalizes and validates the `p_align` field to avoid division-by-zero errors and invalid alignments, and corrects a bounds-checking logic error.
