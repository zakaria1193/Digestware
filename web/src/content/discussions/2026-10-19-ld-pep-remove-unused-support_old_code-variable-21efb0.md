---
project: binutils
subsystem: ld/pep
patch_id: null
tags:
- binutils
- ld
- linker
- pep
- compiler warnings
discussion_id: 20261019193231.1708375-17-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 16/18] ld/pep: remove unused support_old_code variable'
headline: 'ld/pep: remove unused support_old_code variable'
tldr: Removes an unused variable `support_old_code` from ld/pep, resolving compiler
  warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes unused code, reducing clutter and avoiding compiler warnings.
- Maintains existing functionality by keeping the `--support-old-code` option accepted.
- No impact on correctness or performance for active targets.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to remove an unused `support_old_code` variable from ld/pep,
    resolving Clang warnings.
  quote: "Building ld with a recent clang fails with:\n\n    ei386pep.c:131:12: error:\
    \ variable 'support_old_code' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe same happens for the other emulations generated from pep.em."
primer_expert: This patch targets the PE (Portable Executable) template file `ld/emultempl/pep.em`,
  used for generating linker configurations for PE targets. The variable `support_old_code`
  was copied from `pe.em` but is only relevant for ARM PE targets, not the x86-focused
  targets typically handled by `pep.em`. Its presence leads to `[-Wunused-but-set-global]`
  warnings from Clang. The patch removes the variable and its associated option handler,
  cleaning up the unused code.
primer_glossary:
- term: PE
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows. It is also used by the linker
    for some embedded targets.
- term: ld/pep
  definition: The linker configuration template for PE (Portable Executable) object
    files, likely an extension or variant of the standard PE handling in binutils.
- term: ARM PE targets
  definition: Targets that use the Portable Executable (PE) file format, commonly
    associated with Windows, but also used for certain embedded systems, and specifically
    here, for ARM architectures.
- term: linker template
  definition: A generic file used by the linker to generate specific configurations
    for different target architectures or operating systems. Changes to the template
    are propagated to all generated configurations.
series_id: 'binutils:ld/pep: remove unused support_old_code variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-17-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch removes the `support_old_code` variable from the PE object file format handling in the linker (`ld/pep`). This variable was inherited from `pe.em` but is only used for ARM PE targets, which `pep.em` does not handle. Consequently, it triggers an unused variable warning when building with Clang. The patch removes the variable declaration and its handling while retaining the `--support-old-code` option's acceptance for compatibility. This cleans up the codebase and resolves compiler warnings.
