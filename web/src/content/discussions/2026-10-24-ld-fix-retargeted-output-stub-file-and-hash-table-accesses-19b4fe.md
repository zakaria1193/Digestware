---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- aix
- avr
- m68hc11
- vxworks
discussion_id: 20261024152218.2649262-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/2] ld: fix retargeted-output stub-file and hash-table accesses'
headline: 'ld: fix retargeted-output stub-file and hash-table accesses'
tldr: Addresses crashes in AIX, AVR, and M68HC11 linker emulations when output formats
  are retargeted using linker scripts.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes multiple crashes across different linker emulations.
- Improves robustness when linker scripts retarget output formats.
- Adds defensive checks to prevent null pointer dereferences and out-of-bounds reads.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes a series of patches to fix crashes in AIX, AVR, M68HC11, and
    VxWorks linker emulations related to retargeted output formats, addressing issues
    with stub files and hash table accesses.
  quote: A linker script can retarget the output BFD with OUTPUT_FORMAT. The AVR,
    m68hc1x and VxWorks emulation hooks run after that and assume the output backend
    created a stub file or an ELF link hash table. The generic elf32-gen/elf64-gen
    backends do neither, so the hooks either dereference a NULL stub_file or read
    past a generic hash table.
primer_expert: 'This cover letter introduces a series of patches addressing a common
  issue in linker emulations: the incorrect assumption that specific structures (stub
  files, ELF hash tables) exist after the output format has been retargeted by a linker
  script. For example, generic ELF backends might not create stub files that are expected
  by AVR or M68HC11 emulations, or they might use a generic hash table where an `elf_link_hash_table`
  is expected by VxWorks emulation. The patches add defensive checks for these conditions,
  preventing crashes and ensuring predictable behavior.'
primer_glossary:
- term: OUTPUT_FORMAT
  definition: A linker script command used to specify the output file format.
- term: stub file
  definition: A placeholder file used by the linker for specific linking operations,
    especially in certain emulations or when dealing with dynamic linking.
- term: link hash table
  definition: A data structure used by the linker to store and quickly access symbol
    information.
- term: AVR
  definition: A family of microcontrollers manufactured by Atmel.
- term: M68HC11
  definition: A microcontroller from Motorola's M68HC11 family.
- term: AIX
  definition: Advanced Interactive eXecutive, a Unix operating system developed by
    IBM.
- term: VxWorks
  definition: A real-time operating system (RTOS) commonly used in embedded systems.
series_id: 'binutils:ld: fix retargeted-output stub-file and hash-table accesses'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024152218.2649262-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This series of patches fixes crashes in several linker emulations (AIX, AVR, M68HC11, VxWorks) that occur when a linker script uses `OUTPUT_FORMAT` to retarget the output to a different format, such as a generic ELF. These retargetings can lead to scenarios where required stub files are not created or link hash tables are of a generic type, causing subsequent accesses to be out-of-bounds reads or NULL pointer dereferences. The patches add checks to ensure stub files exist or that hash tables are of the expected type before access, preventing crashes.
