---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- ld
- risc-v
- shared-libraries
- pie
discussion_id: jeAeSOc0FC-XFsR2J5imaA5ZNIySqThcvvUHsNxKLy3L9dWW7xf_vp2cyqt6qPLVwnst9J7dnaxSqFvTqJPMBaazkvHUdC3FbdiS-wslOmM=@protonmail.com
source_type: public_inbox
title: '[PATCH 1/3] RISC-V: Enable shared library and PIE support for  riscv*-elf'
headline: 'RISC-V: Enable shared library and PIE support for riscv*-elf'
tldr: Enable shared library and PIE support for RISC-V ELF targets to facilitate UEFI
  application development.
proposer: mintsuki <mintsuki@protonmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enabling PIE/shared library support for riscv*-elf might introduce a small overhead
  for embedded systems that do not require these features, though the patch argues
  the exclusion was arbitrary and not based on any specific technical constraint.
- The change simplifies the toolchain for RISC-V UEFI development, removing a blocker
  for users needing PIE/shared library capabilities.
exchanges:
- author: mintsuki <mintsuki@protonmail.com>
  role: proposer
  position: Proposes enabling shared library and PIE support for riscv*-elf by modifying
    elf32lriscv-defs.sh, citing the need for UEFI application development.
  quote: 'riscv*-elf is the only RISC-V target for which ld refuses -shared and

    -pie.  elf32lriscv-defs.sh has withheld GENERATE_SHLIB_SCRIPT and

    GENERATE_PIE_SCRIPT from it since be1dce26256a ("RISC-V: Disable shared

    library support for embedded elf."), whose commit message is a ChangeLog

    entry and records no reason.  Nothing in the RISC-V backend depends on

    the exclusion, and riscv*-elf does not even set…'
primer_expert: This series modifies `ld/emulparams/elf32lriscv-defs.sh` to unconditionally
  enable `GENERATE_SHLIB_SCRIPT` and `GENERATE_PIE_SCRIPT` for the `riscv*-elf` target.
  The change removes a historical restriction that prevented the generation of scripts
  necessary for building dynamically linked executables (ET_DYN) and Position-Independent
  Executables (PIE). This is crucial for targets like UEFI applications, which are
  ET_DYN images and rely on PIE or `shared -Bsymbolic` for self-relocation.
primer_glossary:
- term: PIE
  definition: Position-Independent Executable. An executable file that can be loaded
    at any address in memory without modification. This is achieved through special
    relocation entries and is crucial for security and flexibility.
- term: ET_DYN
  definition: Executable ELF file type. Indicates a dynamically linked executable
    or a shared object. PIE executables are of this type.
- term: UEFI
  definition: Unified Extensible Firmware Interface. A specification that defines
    the software interface between an operating system and platform firmware. UEFI
    applications are typically loaded and run by the UEFI firmware.
- term: R_RISCV_RELATIVE
  definition: A RISC-V specific relocation type used for position-independent code,
    where the relocation value is determined by adding the image's base address to
    the symbol's offset.
- term: elf32lriscv-defs.sh
  definition: A shell script within Binutils that defines linker emulation parameters
    specific to the 32-bit little-endian RISC-V architecture.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
series_id: 'binutils:risc-v: enable shared library and pie support for riscv*-elf'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/jeAeSOc0FC-XFsR2J5imaA5ZNIySqThcvvUHsNxKLy3L9dWW7xf_vp2cyqt6qPLVwnst9J7dnaxSqFvTqJPMBaazkvHUdC3FbdiS-wslOmM=@protonmail.com
bugzilla_url: null
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

This patch series enables support for shared libraries and Position-Independent Executables (PIE) for RISC-V ELF targets, specifically the riscv*-elf toolchain. Historically, these features were disabled for this target, but the author argues there's no technical dependency and other bare-metal ELF targets support them. The primary motivation is to enable the building of UEFI applications, which require PIE or shared library support.
