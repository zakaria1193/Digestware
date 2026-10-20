---
project: binutils
subsystem: bfd/epiphany
patch_id: null
tags:
- cleanup
- compiler-warnings
discussion_id: 20261019193231.1708375-2-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 01/18] bfd/epiphany: remove unused epiphany_relaxed variable'
headline: 'bfd/epiphany: remove unused epiphany_relaxed variable'
tldr: Removes an unused variable from bfd/elf32-epiphany.c to fix compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability.
exchanges: []
primer_expert: The BFD library's Epiphany backend uses a static boolean variable `epiphany_relaxed`.
  This change removes that variable as it is never actually used after being conditionally
  set, resolving compiler warnings about unused variables. The `relax_section` function's
  logic is simplified accordingly.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor. A library within binutils that provides a common
    interface for reading and writing various binary object file formats.
- term: Epiphany
  definition: A family of microprocessors developed by Adapteva.
- term: unused-but-set-global
  definition: A compiler warning indicating a global variable that has been assigned
    a value but is never subsequently read. This often suggests dead code.
series_id: 'binutils:bfd/epiphany: remove unused epiphany_relaxed variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-2-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch removes the unused `epiphany_relaxed` variable from `bfd/elf32-epiphany.c`. The variable has been unused since the Epiphany port was added in 2011, and its removal addresses clang compiler warnings about unused variables.
