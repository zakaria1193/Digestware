---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- risc-v
- loongarch
- pie
- shared libraries
discussion_id: 3f670b99-73b0-4212-9451-3aeafb44d88a@suse.com
source_type: public_inbox
title: 'Re: [PATCH 0/3] ld: shared library and PIE support for riscv*-elf and loongarch*-elf'
headline: UEFI PE linking on bare-metal targets
tldr: Discusses proper linking of PE binaries on bare-metal targets vs. enabling PIE/shared
  lib for UEFI.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enabling PIE/shared lib for bare-metal might be a workaround for UEFI, potentially
  not the cleanest solution.
- Direct PE linking support could be more robust but might require more significant
  changes.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions enabling PIE/shared lib for UEFI on bare-metal, suggests direct
    PE linking support as an alternative.
  quote: 'Afaik a "normal" UEFI application is an ordinary PE executable. What you

    describe looks to be the result of some handcrafting. Imo properly

    supporting the true linking of PE binaries from ELF inputs on the targets

    of interest (like is already possible on x86-64, for example) would be

    the better course of action (if UEFI applications are the sole concern

    here).'
primer_expert: This discussion revolves around the implications of enabling shared
  library and PIE (Position Independent Executable) support for bare-metal targets
  like `riscv*-elf` and `loongarch*-elf`. The core of the debate is whether this enablement,
  motivated by UEFI application development needs, is the most appropriate solution,
  or if a more direct approach to linking PE binaries from ELF inputs, akin to what
  exists for x86-64, would be better.
primer_glossary:
- term: PIE
  definition: Position Independent Executable. An executable program that can be loaded
    and run at any arbitrary memory address without modification. This is crucial
    for security features like Address Space Layout Randomization (ASLR).
- term: UEFI
  definition: Unified Extensible Firmware Interface. A standard that defines the software
    interface between an operating system and platform firmware. It is the successor
    to the BIOS.
- term: ET_DYN
  definition: ELF file type indicating a dynamically linked executable. These are
    often used for shared libraries or position-independent executables.
- term: PE binary
  definition: Portable Executable binary. The standard file format for executables,
    DLLs, and object code in Windows.
series_id: 'binutils:ld: shared library and pie support for riscv*-elf and loongarch*-elf'
series_role: cover
series_parts:
- title: 'ld: shared library and PIE support for riscv*-elf and loongarch*-elf'
  url: https://inbox.sourceware.org/binutils/-w8nVtklFMF5sVUSH64C5tSTBhNeakYCcXlp3ozRPvcdFCgP4rQG0KtIyRHbx3Z1rpZRD-52KlKbfujCpuheVo38-wbyboL47NZar6VU_68=@protonmail.com
  n: 0
  total: 3
url: https://inbox.sourceware.org/binutils/3f670b99-73b0-4212-9451-3aeafb44d88a@suse.com
bugzilla_url: null
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

Jan Beulich questions the approach of enabling shared library and PIE support for `riscv*-elf` and `loongarch*-elf` targets solely for UEFI application development. He suggests that directly supporting the linking of PE binaries from ELF inputs, as done on x86-64, might be a more robust solution if UEFI is the primary concern. This comes as a response to a patch series that aims to enable these features for bare-metal targets.
