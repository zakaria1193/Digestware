---
project: binutils
subsystem: ld/pe
patch_id: null
tags:
- binutils
- ld
- linker
- pe
- compiler warnings
discussion_id: 20261019193231.1708375-18-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 17/18] ld/pe: only define target-specific variables when needed'
headline: 'ld/pe: only define target-specific variables when needed'
tldr: Reduces unused global variable warnings in ld/pe by conditionally defining variables
  based on target.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Reduces compiler warnings and improves code clarity.
- Maintains functionality for the targets where these variables are relevant.
- Minimal to no performance impact.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to conditionally define target-specific variables in ld/pe
    to resolve unused variable compiler warnings.
  quote: "Building ld with a recent clang fails with:\n\n    ei386pe.c:122:12: error:\
    \ variable 'support_old_code' set but not used [-Werror,-Wunused-but-set-global]\n\
    \    ei386pe.c:123:15: error: variable 'thumb_entry_symbol' set but not used [-Werror,-Wunused-but-set-global]\n\
    \    ei386pe_posix.c:124:40: error: variable 'image_base_statement' set but not\
    \ used [-Werror,-Wunused-but-set-global]\n\nThe same happens…"
primer_expert: This patch cleans up linker code for the PE object file format. It
  targets unused global variables that trigger `[-Wunused-but-set-global]` warnings
  from Clang. The variables `support_old_code` and `thumb_entry_symbol` are ARM-specific,
  while `image_base_statement` relates to DLL support. By wrapping their definitions
  within `#if` directives tied to `TARGET_IS_armpe`, `TARGET_IS_arm_wince_pe`, and
  `DLL_SUPPORT` respectively, the linker code becomes cleaner and avoids spurious
  warnings for non-applicable targets.
primer_glossary:
- term: PE
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows. It is also used by the linker
    for some embedded targets.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: linker
  definition: A program that combines various pieces of code and data (from object
    files and libraries) into a single executable file.
- term: global variable
  definition: A variable declared outside of any function, accessible from any part
    of the program.
- term: ARM PE targets
  definition: Targets that use the Portable Executable (PE) file format, commonly
    associated with Windows, but also used for certain embedded systems, and specifically
    here, for ARM architectures.
series_id: 'binutils:ld/pe: only define target-specific variables when needed'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-18-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch addresses compiler warnings about unused global variables in the PE (Portable Executable) object file format handling within the linker (`ld`). Specifically, `support_old_code` and `thumb_entry_symbol` are only relevant for ARM PE targets and are now conditionally defined. Similarly, `image_base_statement` is now only defined when `DLL_SUPPORT` is enabled. This change cleans up the codebase and resolves `[-Wunused-but-set-global]` errors reported by Clang.
