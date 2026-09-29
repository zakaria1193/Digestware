---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- pe
- debug
- compression
discussion_id: 20260928090146.4016188-1-tobias.deiminger@linutronix.de
source_type: public_inbox
title: '[PATCH 0/3] PE compression/corruption fixes with related test case'
headline: PE compression/corruption fixes with related test case
tldr: A series of patches addresses bugs in BFD PE format compression and corruption,
  introducing a test case for debug section round trips.
proposer: Tobias Deiminger <tobias.deiminger@linutronix.de>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- The fix for `pe-bigobj-*` file corruption involves minor information loss (flag,
  start address) to maintain format integrity, which is deemed acceptable over producing
  invalid output.
- Implementing comprehensive debug section compression and decompression testing across
  all PE targets requires careful handling of format variations and potential interdependencies
  between patches.
exchanges:
- author: Tobias Deiminger
  role: proposer
  position: Submits a series of patches fixing BFD PE format issues related to debug
    section compression and file corruption, along with a new test case.
  quote: 'Here are two loosely related bugfixes for BFD PE formats, covered by a

    new test case that verifies a debug symbol compress-decompress round

    trip for all enabled target formats. The test needs both fixes to

    succeed.'
primer_expert: This series addresses two distinct but related bugs within the BFD
  library's handling of the Portable Executable (PE) format, specifically concerning
  compressed debug sections. The first patch corrects the compression of debug sections
  for `pei-*` targets, which previously failed in a round-trip scenario. The second
  patch fixes corruption issues when converting to `pe-bigobj-*` formats using `objcopy`.
  A new test case is included to validate the compress/decompress functionality for
  debug information across various PE targets.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a component of GNU Binutils that
    provides a common interface for reading and writing various executable file formats.
- term: PE format
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows.
- term: debug sections
  definition: Sections within an executable file that contain debugging information,
    such as symbol tables, line number information, and DWARF data, used by debuggers.
- term: compress-decompress round trip
  definition: The process of compressing data, then decompressing it, and verifying
    that the result is identical to the original data.
- term: pei-*
  definition: A target triplet or format specifier within BFD, typically referring
    to PE Image format variations, distinct from standard PE.
- term: pe-bigobj-*
  definition: A specific PE format variant that supports larger object files, often
    used for executables with many sections.
- term: objcopy
  definition: A GNU Binutils utility used to copy and translate object files from
    one format to another, and to modify sections and symbols.
series_id: binutils:pe compression/corruption fixes with related test case
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260928090146.4016188-1-tobias.deiminger@linutronix.de
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Tobias Deiminger proposes a series of three patches to fix issues related to debug section compression and file corruption in the BFD PE format. The series includes fixes for PE debug section compression on `pei-*` targets and for `objcopy` corruption with `pe-bigobj-*`, along with a new test case to verify a debug symbol compress-decompress round trip across all enabled target formats. The test requires both fixes to pass.
