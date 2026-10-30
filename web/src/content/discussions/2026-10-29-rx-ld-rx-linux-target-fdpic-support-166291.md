---
project: binutils
subsystem: rx
patch_id: null
tags:
- binutils
- rx
- ld
- fdpic
- linker script
discussion_id: 20261029120303.1987315-4-yoshinori.sato@nifty.com
source_type: public_inbox
title: 'RX: ld rx-linux target FDPIC support'
headline: 'RX: ld rx-linux target FDPIC support'
tldr: Adds FDPIC support to the RX linker script for the rx-linux target, defining
  necessary sections.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Modifies linker script behavior, which can be sensitive and may require thorough
  testing across different build configurations.
- Introduces new sections and configurations specific to FDPIC, adding to the overall
  complexity of the linker's support for the RX target.
exchanges: []
primer_expert: This patch updates the linker script (`emulparams/elf32rx_linux.sh`)
  for the RX target on Linux to support FDPIC. It defines new linker script sections
  such as `.got`, `.rela.got.funcdesc`, and `.rofixup` which are essential for FDPIC
  code generation. It also configures constants like `MAXPAGESIZE` and `COMMONPAGESIZE`
  and enables the generation of shared library and PIE scripts, all crucial for enabling
  FDPIC linkage.
primer_glossary:
- term: RX
  definition: A family of 32-bit microcontrollers developed by Renesas Electronics.
- term: ld
  definition: The GNU linker, part of the GNU Binutils package. It combines object
    files and libraries to create an executable file or a shared library.
- term: FDPIC
  definition: Fully Distributable Position-Independent Code. A system for generating
    position-independent code that can be loaded and executed at any memory address
    without modification, including support for shared libraries and position-independent
    data sections.
- term: rx-linux
  definition: A target triplet indicating the RX architecture combined with the Linux
    operating system.
- term: Linker Script
  definition: A file that provides instructions to the linker on how to arrange sections
    from input object files into the output executable or library. It defines memory
    layouts, section placement, and other structural aspects.
- term: GOT
  definition: Global Offset Table. A data structure used in position-independent code
    (PIC) to store addresses of dynamically resolved external functions and global
    variables.
- term: PIE
  definition: Position-Independent Executable. An executable file that can be loaded
    and run at any memory address, similar to position-independent code used for shared
    libraries.
series_id: 'binutils:rx: ld rx-linux target fdpic support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029120303.1987315-4-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch modifies the linker script `elf32rx_linux.sh` to add support for FDPIC (Fully Distributable Position-Independent Code) on the RX architecture for the Linux target. It introduces new linker script sections for GOT, `.rela.got.funcdesc`, and `.rofixup`, and adjusts parameters like `MAXPAGESIZE` and `COMMONPAGESIZE` to accommodate FDPIC requirements.
