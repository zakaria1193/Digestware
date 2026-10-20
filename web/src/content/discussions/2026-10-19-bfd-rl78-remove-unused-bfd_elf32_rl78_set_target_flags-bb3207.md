---
project: binutils
subsystem: bfd/rl78
patch_id: null
tags:
- cleanup
- compiler-warnings
discussion_id: 20261019193231.1708375-5-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 04/18] bfd/rl78: remove unused bfd_elf32_rl78_set_target_flags'
headline: 'bfd/rl78: remove unused bfd_elf32_rl78_set_target_flags'
tldr: Removes an unused function and variable from bfd/elf32-rl78.c to fix compiler
  warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability.
exchanges: []
primer_expert: The BFD library's RL78 backend has a function and a global variable
  intended for setting target flags, specifically related to warning mismatches. This
  change removes them because they have no callers and are unused, cleaning up dead
  code and resolving compiler warnings.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor. A library within binutils that provides a common
    interface for reading and writing various binary object file formats.
- term: RL78
  definition: A family of microcontrollers from Renesas Electronics.
- term: unused-but-set-global
  definition: A compiler warning indicating a global variable that has been assigned
    a value but is never subsequently read. This often suggests dead code.
series_id: 'binutils:bfd/rl78: remove unused bfd_elf32_rl78_set_target_flags'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-5-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch removes the unused `bfd_elf32_rl78_set_target_flags` function and its associated `no_warn_mismatch` variable from `bfd/elf32-rl78.c`. Both have been unused since the RL78 port was added in 2011, and their removal addresses clang compiler warnings.
