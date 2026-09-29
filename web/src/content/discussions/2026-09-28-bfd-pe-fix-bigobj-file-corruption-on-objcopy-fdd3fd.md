---
project: binutils
subsystem: bfd/pe
patch_id: null
tags:
- binutils
- bfd
- pe
- objcopy
- corruption
discussion_id: 20260928090146.4016188-3-tobias.deiminger@linutronix.de
source_type: public_inbox
title: '[PATCH 2/3] bfd/PE: fix bigobj file corruption on objcopy'
headline: 'bfd/PE: fix bigobj file corruption on objcopy'
tldr: Fixes corruption in PE bigobj files created by objcopy.
proposer: Tobias Deiminger <tobias.deiminger@linutronix.de>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Correcting `pe-bigobj` file corruption necessitates accepting minor information
  loss regarding flags and start addresses, as the format fundamentally cannot represent
  this data.
- Ensuring `_bfd_aoutsz` is zero and `EXEC_P` is unset prevents invalid output but
  requires careful handling to avoid breaking other PE-related functionalities.
exchanges:
- author: Tobias Deiminger
  role: proposer
  position: Fixes PE bigobj file corruption issues in objcopy by correcting handling
    of optional headers and section sizes.
  quote: "Converting any linked executable to pe-bigobj-* silently produced\ncorrupted\
    \ section headers. For example:\n\n $ gcc -g -o testprog testprog.c\n $ objcopy\
    \ -I elf64-x86-64 -O pe-bigobj-x86-64 testprog testprog.bigobj\n $ objdump -b\
    \ pe-bigobj-x86-64 -h testprog.bigobj | head\n [...]\n Idx Name          Size\
    \      VMA               LMA               File off  Algn\n   0 ^K^B^B/      \
    \ 00001050  00000000000000…"
primer_expert: This patch corrects a critical bug in BFD's PE backend where `objcopy`
  would silently corrupt `pe-bigobj-*` files. The corruption occurred because the
  format's inability to store an OptionalHeader was not properly enforced, leading
  to incorrect section header offsets due to miscalculated `_bfd_aoutsz` and the presence
  of the `EXEC_P` flag. The fix ensures these fields are correctly set to zero or
  unset, preventing invalid output at the cost of some minor data loss inherent to
  the format's limitations.
primer_glossary:
- term: pe-bigobj-*
  definition: A variant of the PE (Portable Executable) file format that supports
    larger section headers, allowing for executables with more sections than the standard
    PE format.
- term: objcopy
  definition: A utility in GNU Binutils used to copy and translate object files, allowing
    modification of sections and symbols.
- term: section headers
  definition: Metadata within an object file that describes each section, including
    its name, size, virtual address, and file offset.
- term: OptionalHeader
  definition: A component of the PE file format that contains information about the
    file, such as entry point, base address, and sizes of code and data sections.
    Not present in `pe-bigobj` format.
- term: _bfd_aoutsz
  definition: An internal BFD structure field likely related to the size of the a.out
    header, which is incorrectly initialized and used in PE bigobj conversions.
- term: EXEC_P
  definition: A flag or attribute indicating that a file is executable. Its incorrect
    presence in `pe-bigobj` contexts triggers logic that assumes an OptionalHeader.
series_id: 'binutils:bfd/pe: fix bigobj file corruption on objcopy'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260928090146.4016188-3-tobias.deiminger@linutronix.de
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Tobias Deiminger addresses a bug where converting to `pe-bigobj-*` formats using `objcopy` silently corrupted section headers. The issue stemmed from incorrect handling of `f_opthdr`, `_bfd_aoutsz`, and `EXEC_P` flags, leading to invalid gaps in the file. The fix ensures `_bfd_aoutsz` is zero and `EXEC_P` is unset for bigobj formats, accepting minor information loss for format correctness.
