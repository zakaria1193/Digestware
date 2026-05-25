---
project: binutils
subsystem: mips
patch_id: null
tags:
- binutils
- objcopy
- MIPS
- ELF
- section allocation
discussion_id: ahLelwz89ecd39ec@squeak.grove.modra.org
source_type: public_inbox
title: 'mips: section .note.gnu.build-id can''t be allocated in segment'
headline: 'mips: section .note.gnu.build-id can''t be allocated in segment'
tldr: Fixes an objcopy error on MIPS when .note.gnu.build-id follows SHT_NOBITS sections
  due to file offset tracking.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The patch modifies file offset tracking logic, which could potentially impact performance
  or introduce regressions in other scenarios.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a fix for an objcopy error on MIPS systems related to section
    allocation.
  quote: null
primer_expert: This patch addresses an issue in `bfd/elf.c` within the `assign_file_positions_for_load_sections`
  function. The problem arises when processing ELF files for MIPS targets where a
  `SHT_PROGBITS` section (``.note.gnu.build-id``) immediately follows `SHT_NOBITS`
  sections (``.MIPS.abiflags``, ``.reginfo``). The fix ensures correct file offset
  tracking, resolving the allocation error during `objcopy` operations.
primer_general: The `objcopy` utility is used to copy and translate object files.
  ELF files are a standard format for executables, object code, shared libraries,
  and core dumps.  ELF files are divided into sections, some of which contain code
  or data (``SHT_PROGBITS``) and some of which don't (``SHT_NOBITS``). This patch
  fixes an issue where `objcopy` would fail on MIPS architectures when a section containing
  data immediately followed a section that didn't, which makes the toolchain more
  reliable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahLelwz89ecd39ec@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch resolves an error encountered during ``objcopy`` on MIPS systems. The error occurred when the ``.note.gnu.build-id`` section, which has the type ``SHT_PROGBITS``, immediately followed sections with the type ``SHT_NOBITS`` (e.g., ``.MIPS.abiflags`` and ``.reginfo``). The underlying cause was a bug in file offset tracking within the ``assign_file_positions_for_load_sections`` function.
