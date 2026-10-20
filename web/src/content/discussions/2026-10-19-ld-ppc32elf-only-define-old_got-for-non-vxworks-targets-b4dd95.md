---
project: binutils
subsystem: ld/ppc32elf
patch_id: null
tags:
- binutils
- ld
- linker
- ppc32elf
- VxWorks
discussion_id: 20261019193231.1708375-19-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 18/18] ld/ppc32elf: only define old_got for non-VxWorks targets'
headline: 'ld/ppc32elf: only define old_got for non-VxWorks targets'
tldr: Fixes unused variable warnings in ld/ppc32elf by making `old_got` conditional
  on non-VxWorks targets.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Eliminates unused variable warnings.
- Improves code clarity by restricting variable scope.
- No functional change for supported targets.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to make the `old_got` variable conditional on non-VxWorks
    targets in ld/ppc32elf to fix unused variable warnings.
  quote: "Building ld with a recent clang fails with:\n\n    eelf32ppcvxworks.c:68:12:\
    \ error: variable 'old_got' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nold_got is only read in ppc_after_check_relocs, which is not generated for VxWorks."
primer_expert: This patch addresses unused variable warnings in the PowerPC 32-bit
  ELF linker configuration, specifically within `ld/emultempl/ppc32elf.em`. The variable
  `old_got` is related to the `--sdata-got` linker option, which controls the placement
  of the Global Offset Table (GOT). This functionality is not applicable to VxWorks
  targets. The change conditionally defines `old_got` and handles `OPTION_OLD_GOT`
  only when the target is not VxWorks, thereby resolving Clang's `[-Wunused-but-set-global]`
  warnings.
primer_glossary:
- term: ld/ppc32elf
  definition: The linker configuration for PowerPC 32-bit targets using the ELF object
    file format.
- term: VxWorks
  definition: A real-time operating system (RTOS) often used in embedded systems.
    The linker needs specific configurations for different operating systems.
- term: Global Offset Table (GOT)
  definition: A data structure used in executable and shared object code on many platforms
    that enables dynamic linking by holding addresses of external symbols and functions.
    The placement and handling of the GOT can vary between targets and link-time options.
- term: linker script
  definition: A file that contains directives for the linker, specifying how to arrange
    code and data sections in the final executable or library, and how to resolve
    symbols.
series_id: 'binutils:ld/ppc32elf: only define old_got for non-vxworks targets'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-19-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch resolves compiler warnings about an unused global variable `old_got` in the `ld/ppc32elf` linker script. The variable and its associated option handling (`OPTION_OLD_GOT`) are only relevant for non-VxWorks targets. The patch moves the definition of `old_got` and the parsing of `--sdata-got` (which sets it) into existing conditional blocks that exclude VxWorks. This change prevents the unused variable warnings reported by Clang.
