---
project: binutils
subsystem: sh
patch_id: null
tags:
- sh
- core dump
- elf
- bfd
- debugging
discussion_id: arxza-w33Q0XNEW_@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] sh: handle Linux core notes in the generic ELF vector'
headline: 'sh: handle Linux core notes in the generic ELF vector'
tldr: Improves SH core file support by prioritizing targets that correctly handle
  core note information.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Prioritizing targets by section count is a heuristic that improves correctness for
  SH core files but might not be universally optimal for all ELF targets.
- The change aims to fix a specific bug rather than refactor the entire target matching
  logic, which could be more complex.
exchanges:
- author: Matt Turner
  role: contributor
  position: 'Explains the problem: Linux SH core files were not correctly parsed due
    to target matching priority, leading to missing register information.'
  quote: 'A Linux sh core file matches elf32-shl, elf32-sh-linux, elf32-shl-nbsd

    and elf32-shl-vxworks with equal priority, and bfd_check_format_matches

    picks the first, elf32-shl. Only the Linux vector handled NT_PRSTATUS

    and NT_PRPSINFO notes, so the core had no .reg section and gdb found no

    registers.'
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a solution to improve target selection for SH ELF core files
    by prioritizing targets with more sections when ambiguity arises.
  quote: 'This patch aims to improve core file support in cases where binutils

    was configured with the target needed to interpret notes not being the

    default target.  In such cases multiple targets may match the object

    file with nothing to choose between them.  As per the PR, elf32-shl,

    elf32-sh-linux, elf32-shl-nbsd and elf32-shl-vxworks all match with

    the same priority,'
primer_expert: This patch modifies `bfd_check_format_matches` for the SH target. Previously,
  when multiple targets (e.g., `elf32-shl`, `elf32-sh-linux`) had equal priority,
  `elf32-shl` was chosen. This is problematic because only `elf32-sh-linux` correctly
  parses NT_PRSTATUS/NT_PRPSINFO notes, essential for GDB register information. The
  change prioritizes targets with more sections to ensure the correct SH Linux core
  file format is selected.
primer_glossary:
- term: core notes
  definition: Sections within a core dump file that contain auxiliary information
    about the process state, such as process status (NT_PRSTATUS) or process information
    (NT_PRPSINFO).
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executable files, shared libraries, and core dumps on many Unix-like systems.
- term: bfd_check_format_matches
  definition: A function within the BFD library responsible for determining which
    target format best matches an input object file when multiple formats could potentially
    apply.
- term: target
  definition: In the context of binutils, a 'target' refers to a specific architecture
    and operating system configuration (e.g., 'sh-linux'). Different targets have
    different ways of structuring object files and interpreting debugging information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/arxza-w33Q0XNEW_@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the SH target's ELF core file handling where the default `elf32-shl` target was chosen over `elf32-sh-linux`, leading to incorrect core file interpretation and missing register information for GDB. The fix modifies `bfd_check_format_matches` to prefer targets with a higher section count when multiple targets match equally, thus prioritizing `elf32-sh-linux` and resolving the issue.
