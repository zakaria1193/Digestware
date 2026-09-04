---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- ld
- shared libraries
- pie
- bare-metal
discussion_id: xNxiTDeYjvXtAxtxnW56SEn6-MaCLHOHNy04Rs6UgQyaoaF-psGViNlOU7k5CDWEYzINbfoOSdubntpcx10wld1LQFelo15ZNCOxn2HGcxc=@protonmail.com
source_type: public_inbox
title: '[PATCH 3/3] LoongArch: Enable shared library and PIE support for loongarch*-elf'
headline: 'LoongArch: Enable shared library and PIE for loongarch*-elf'
tldr: Enables shared library and PIE support for LoongArch bare-metal targets.
proposer: mintsuki <mintsuki@protonmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables functionality that was previously disabled, potentially uncovering or introducing
  new issues on bare-metal targets.
- Aligns LoongArch bare-metal capabilities with other ELF targets that support shared
  libraries and PIE.
exchanges:
- author: mintsuki <mintsuki@protonmail.com>
  role: proposer
  position: Enables shared library and PIE support for LoongArch bare-metal targets
    by modifying emulparams.
  quote: 'loongarch*-elf withholds GENERATE_SHLIB_SCRIPT and GENERATE_PIE_SCRIPT,

    so ld refuses -shared and -pie for it.  The exclusion arrived with the

    original LoongArch ld port, copied from the RISC-V emulparams, and no

    reason was recorded for it either.  loongarch*-elf does not set

    EMBEDDED.


    The rationale is the one given for the RISC-V patch in this series; it

    applies here unchanged.'
primer_expert: This patch modifies the linker emulation parameters for LoongArch bare-metal
  targets (`loongarch*-elf`). It removes specific exclusions for `GENERATE_SHLIB_SCRIPT`
  and `GENERATE_PIE_SCRIPT` that were present in the `emulparams` files. These exclusions,
  inherited from RISC-V, prevented the use of `-shared` and `-pie` flags, which are
  now enabled unconditionally. This is motivated by the need to build UEFI applications
  on these targets.
primer_glossary:
- term: LoongArch
  definition: A family of instruction set architectures developed by Loongson Technology
    for China.
- term: loongarch*-elf
  definition: A target triple specifying the LoongArch architecture, generic ELF object
    format, and no operating system (bare-metal).
- term: GENERATE_SHLIB_SCRIPT
  definition: A linker configuration option that controls whether scripts for building
    shared libraries are generated.
- term: GENERATE_PIE_SCRIPT
  definition: A linker configuration option that controls whether scripts for building
    Position Independent Executables are generated.
- term: EMBEDDED
  definition: A configuration flag or target type indicating that the build is for
    an embedded system with specific constraints.
series_id: 'binutils:loongarch: enable shared library and pie support for loongarch*-elf'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/xNxiTDeYjvXtAxtxnW56SEn6-MaCLHOHNy04Rs6UgQyaoaF-psGViNlOU7k5CDWEYzINbfoOSdubntpcx10wld1LQFelo15ZNCOxn2HGcxc=@protonmail.com
bugzilla_url: null
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

This patch enables shared library and PIE (Position Independent Executable) support for `loongarch*-elf` targets by modifying the `emulparams` files. Previously, these features were explicitly disabled for LoongArch bare-metal, a restriction inherited from RISC-V without clear justification. Enabling these features is necessary for building UEFI applications on these platforms and aligns with the capabilities provided to other bare-metal ELF targets.
