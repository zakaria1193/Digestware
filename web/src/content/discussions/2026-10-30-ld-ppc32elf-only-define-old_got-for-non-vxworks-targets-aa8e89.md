---
project: binutils
subsystem: ld/ppc32elf
patch_id: null
tags:
- linker
- PowerPC
- VxWorks
- compiler warnings
discussion_id: 20261030150202.1147947-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH] ld/ppc32elf: only define old_got for non-VxWorks targets'
headline: 'ld/ppc32elf: only define old_got for non-VxWorks targets'
tldr: Removes unused 'old_got' variable from the ppc32elf linker template for VxWorks
  targets to fix compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Resolves compiler warnings and cleans up code by removing an unused variable for
  a specific target, with no functional change for other targets.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to conditionally define the 'old_got' variable and its
    handling only for non-VxWorks targets in the ppc32elf linker, as it is unused
    and causes compiler warnings on VxWorks.
  quote: "Building ld with a recent clang fails with:\n\n    eelf32ppcvxworks.c:68:12:\
    \ error: variable 'old_got' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nold_got is only read in ppc_after_check_relocs, which is not generated\nfor\
    \ VxWorks.  The --sdata-got option that sets it is not registered for\nVxWorks\
    \ either.  Move the variable and the handling of OPTION_OLD_GOT\ninside the existing\
    \ non-VxWorks c…"
primer_expert: This patch modifies the `ppc32elf.em` linker template, which defines
  behavior for PowerPC 32-bit ELF targets. Specifically, it addresses a static variable
  `old_got` and the `--sdata-got` option. This variable is used in `ppc_after_check_relocs`,
  a function that is not generated for VxWorks targets. The build system's use of
  clang with `-Wunused-but-set-global` flags this unused variable. The change confines
  the `old_got` definition and its option parsing to when the target is not VxWorks,
  resolving the warning.
primer_glossary:
- term: ld/ppc32elf
  definition: Refers to the linker script template for PowerPC 32-bit ELF targets
    within the GNU Binutils project.
- term: VxWorks
  definition: A real-time operating system (RTOS) often used in embedded systems.
- term: old_got
  definition: A variable likely related to the management of the Global Offset Table
    (GOT) in the linker, possibly for compatibility with older conventions.
- term: GOT
  definition: Global Offset Table. A table used by position-independent executable
    code to store addresses of external functions and variables, allowing them to
    be resolved at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261030150202.1147947-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch addresses a compiler warning about an unused global variable, 'old_got', on VxWorks targets. The variable and its associated option handling are only relevant for non-VxWorks targets. The change moves the definition and option parsing of 'old_got' inside the existing conditional that checks for non-VxWorks builds, resolving the warning and cleaning up the code.
