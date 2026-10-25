---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- avr
- m68hc11
- elf
- crash
discussion_id: 20261024152218.2649262-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/2] ld: refuse the link when no stub file was created'
headline: 'ld: refuse the link when no stub file was created'
tldr: Prevents crashes in AVR and M68HC11 emulations by refusing to link when a required
  stub file is not created due to a generic ELF output format.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Prevents crashes in specific emulations when using generic ELF outputs.
- Ensures a clean failure rather than a segmentation fault.
- Relies on `stub_file` being valid for these emulations.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes to refuse the link when `stub_file` is NULL in AVR and M68HC11
    emulations, preventing crashes caused by generic ELF output formats.
  quote: When a linker script uses OUTPUT_FORMAT to select a generic ELF flavour,
    the output BFD reports the ELF flavour but no stub file is created, leaving stub_file
    == NULL. Both the AVR and M68HC emulation hooks then dereference stub_file.
primer_expert: This patch fixes a crash occurring in the AVR and M68HC11 linker emulations
  when a linker script specifies a generic ELF output format (e.g., `OUTPUT_FORMAT("elf32-little")`).
  The generic ELF backends do not create a stub BFD, resulting in `stub_file` being
  NULL. However, the emulation hooks (`avr_elf_after_open_output` and `m68hc11elf_after_open_output`)
  incorrectly assume `stub_file` is always valid and dereference it, leading to a
  crash. The fix ensures these hooks refuse the link if `stub_file` is NULL, and also
  correctly calls `ldelf_after_open_output` earlier in the AVR case.
primer_glossary:
- term: stub file
  definition: A special file used by the linker to handle certain linking scenarios,
    particularly related to dynamic linking or specific target architectures.
- term: AVR
  definition: A family of microcontrollers manufactured by Atmel.
- term: M68HC11
  definition: A microcontroller from Motorola's M68HC11 family.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
series_id: 'binutils:ld: refuse the link when no stub file was created'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024152218.2649262-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch addresses crashes in the AVR and M68HC11 linker emulations that occur when a linker script uses `OUTPUT_FORMAT` to select a generic ELF flavor. In such cases, no stub file is created, but the emulation hooks (e.g., `avr_elf_after_open_output`) attempt to dereference the null `stub_file`. This change makes these hooks refuse the link with a fatal error when `stub_file` is NULL, preventing crashes and ensuring a clean failure message.
