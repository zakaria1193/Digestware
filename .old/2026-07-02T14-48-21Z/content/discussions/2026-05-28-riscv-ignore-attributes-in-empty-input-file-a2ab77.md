---
project: binutils
subsystem: riscv
patch_id: null
tags:
- riscv
- linker
- attributes
- elf
- lto
discussion_id: CAMe9rOpM413U8i5oFK=Um4d3ns3+bAyYWf3EAqq7gSMFaXjHhA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] riscv: Ignore attributes in empty input file'
headline: 'riscv: Ignore attributes in empty input file'
tldr: This patch fixes multiple RISC-V linker test failures by ignoring attributes
  in empty input files during attribute merging.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ignoring attributes in empty files might hide genuine errors, but the patch assumes
  that attributes in empty files are generally not meaningful.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes ignoring empty and `.note.gnu.build-id` sections when merging
    attributes to fix multiple RISC-V linker test failures.
  quote: 'Ignore empty and .note.gnu.build-id sections when merging attributes. The
    following linker tests now pass for riscv:


    FAIL: Diagnostics - Wrong magic number mixed with valid CTF sections

    FAIL: --gc-sections with --defsym

    FAIL: --gc-sections with KEEP

    ...'
- author: H.J. Lu
  role: proposer
  position: The patch fixes multiple RISC-V linker test failures.
  quote: 'Ignore empty and .note.gnu.build-id sections when merging attributes. The
    following linker tests now pass for riscv:'
primer_expert: The patch modifies `_bfd_riscv_elf_merge_private_bfd_data` in `elfnn-riscv.c`
  to ignore attributes in empty input files during the attribute merging process.
  This resolves issues where the linker incorrectly detected magic numbers or mishandled
  section garbage collection due to the presence of attributes in empty or `.note.gnu.build-id`
  sections.  The fix is necessary for correct LTO and symbol handling.
primer_general: When linking object files to create an executable, the linker combines
  information from all input files, including attributes that describe various properties
  of the code and data. This patch addresses a problem in the RISC-V linker where
  it was incorrectly processing attributes found in empty input files. By ignoring
  these attributes, the linker can now correctly handle scenarios such as garbage
  collection of unused code sections and link-time optimization, leading to more reliable
  and efficient executables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpM413U8i5oFK=Um4d3ns3+bAyYWf3EAqq7gSMFaXjHhA@mail.gmail.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch addresses multiple failures in the RISC-V linker tests by ignoring attributes found in empty input files when merging attributes.  This change specifically impacts scenarios involving garbage collection of sections (`--gc-sections`), defined symbols (`--defsym`), `KEEP` directives, and LTO (Link-Time Optimization). Ignoring attributes in empty files resolves issues related to incorrect magic number detection and improves the linker's ability to handle various scenarios, ultimately fixing PR ld/34185.
