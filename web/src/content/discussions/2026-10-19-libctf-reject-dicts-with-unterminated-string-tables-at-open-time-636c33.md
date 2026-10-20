---
project: binutils
subsystem: libctf
patch_id: null
tags:
- binutils
- libctf
- security
- vulnerability
- heap overflow
discussion_id: CA+DP1eroEnnJ-jDKcfnSNSS2UKE1yEop3zG-JBUpznnU5Mq-BA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] libctf: reject dicts with unterminated string tables at open time'
headline: 'libctf: reject dicts with unterminated string tables at open time'
tldr: Fixes a heap out-of-bounds read vulnerability in libctf when processing malformed
  CTF string tables.
proposer: Ilias <iliasaberkane2908@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Improved security by preventing heap OOB reads.
- Slight performance overhead due to added termination checks.
- Increased robustness against malformed input.
exchanges:
- author: Ilias <iliasaberkane2908@gmail.com>
  role: proposer
  position: Submits a patch to fix a heap out-of-bounds read vulnerability in libctf
    caused by unterminated string tables, adding a regression test.
  quote: 'ctf_bufopen() passes the (attacker-controlled when reading crafted object
    files) CTF string table to ctf_str_create_atoms(), which walks it with strlen()
    and strdup()s every string it finds. Nothing validated that the table is NUL-terminated
    within cth_strlen bytes, so a strtab whose final string runs off the end of the
    section made the atoms-table init read past the end of the dict buffer: a hea…'
primer_expert: The vulnerability lies in `libctf/ctf-open.c` within `ctf_bufopen`.
  When parsing CTF data, specifically string tables (`.strtab` or the internal CTF
  string table), the code relies on `strlen` to find string boundaries. If a string
  extends beyond the section's bounds and the final string is not NULL-terminated
  within those bounds, `strlen` can read past the allocated buffer. `ctf_str_create_atoms`
  then copies these potentially corrupted strings. This patch adds explicit checks
  for the NUL terminator within the expected string table length before processing,
  preventing the heap OOB read.
primer_glossary:
- term: libctf
  definition: A library within binutils that provides support for the Common Type
    Format (CTF) debugging information, used by DTrace and other dynamic tracing frameworks.
- term: CTF
  definition: Common Type Format, a lightweight debugging and tracing data format
    used to describe type information, often embedded in object files.
- term: string table
  definition: In object files and executable formats, a section containing strings,
    typically symbol names or debugging information strings. In ELF, this is often
    `.strtab`.
- term: heap out-of-bounds read
  definition: A memory safety vulnerability where a program reads data from an adjacent
    memory location on the heap that it is not supposed to access. This can lead to
    information disclosure or crashes.
- term: NUL-terminated
  definition: A string that is terminated by a null character (\0). This is a common
    convention in C and many file formats for marking the end of a string.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+DP1eroEnnJ-jDKcfnSNSS2UKE1yEop3zG-JBUpznnU5Mq-BA@mail.gmail.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch addresses a security vulnerability in libctf where malformed CTF string tables, potentially controlled by an attacker, could lead to a heap out-of-bounds read. The issue arises because the code uses `strlen` and `strdup` without validating that the string table is properly NULL-terminated within its declared length. This patch adds checks to ensure both CTF and external string tables are correctly terminated before processing, preventing the out-of-bounds read and introducing a new regression test for this condition.
