---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- security
- ELF
- x86
- heap overflow
discussion_id: 20261015093017.3106937-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/2] x86 ELF output target confusion, one OOB write and one OOB read'
headline: x86 ELF output target confusion, one OOB write and one OOB read
tldr: Two patches fix out-of-bounds read and write vulnerabilities in the linker related
  to x86 ELF output target confusion.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixing output target confusion enhances security but requires careful handling of
  different ELF formats and backend interactions.
- The patches ensure that the linker correctly identifies and uses the appropriate
  hash table, preventing memory corruption.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a two-part patch series to resolve out-of-bounds access issues
    in the linker caused by confusion over x86 ELF output targets.
  quote: 'A linker script can retarget the output BFD with OUTPUT_FORMAT.  The

    x86 emulation hook and ld''s generic ELF hook still run after that, and

    each assumes the link hash table matches the emulation or ELF.  Each

    patch fixes one out of bounds access found this way.'
primer_expert: This is the cover letter for a series of two patches that fix security
  vulnerabilities in the GNU linker (`ld`) related to output target confusion in x86
  ELF builds. When a linker script uses `OUTPUT_FORMAT` to specify a different target
  (e.g., `elf64-bpfle` or `elf64-nfp`), the x86 emulation hook and the generic ELF
  hook can incorrectly assume the link hash table matches their respective backends.
  This leads to out-of-bounds writes (in patch 1) and out-of-bounds reads (in patch
  2), both potentially causing heap buffer overflows. The patches ensure that the
  correct hash table type is identifi…
primer_glossary:
- term: linker script
  definition: A file that contains commands for the linker, specifying how to arrange
    sections, resolve symbols, and define the output file format.
- term: OUTPUT_FORMAT
  definition: A linker script command used to specify the output file format.
- term: x86 emulation hook
  definition: A mechanism within the linker that allows x86-specific logic to be applied
    during the linking process.
- term: generic ELF hook
  definition: A general-purpose hook for handling ELF files in the linker, used when
    specific backend logic is not applicable or available.
- term: AddressSanitizer
  definition: A fast memory error detector for C/C++ that finds use-after-free, heap
    corruption, and buffer overflow bugs.
series_id: binutils:x86 elf output target confusion, one oob write and one oob read
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015093017.3106937-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch series addresses two distinct security vulnerabilities in the GNU linker (`ld`) related to how it handles x86 ELF output targets when a linker script retargets the output format. The first patch fixes an out-of-bounds write that occurs when a non-x86 target ID is used with the x86 ELF backend. The second patch corrects an out-of-bounds read in the generic ELF hook when a linker script specifies an ELF flavor that uses a generic link hash table instead of an ELF-specific one. Both issues could lead to heap buffer overflows and are detected by AddressSanitizer.
