---
project: binutils
subsystem: bfd/m32c
patch_id: null
tags:
- cleanup
- compiler-warnings
discussion_id: 20261019193231.1708375-3-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 02/18] bfd/m32c: remove unused bytes_saved variable'
headline: 'bfd/m32c: remove unused bytes_saved variable'
tldr: Removes an unused variable from bfd/elf32-m32c.c to fix compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes dead code, improving maintainability.
exchanges: []
primer_expert: The binutils BFD library contains target-specific code for various
  object file formats. This patch cleans up unused code in the m32c target backend,
  specifically removing a variable that was declared but never utilized, which avoids
  compiler warnings related to unused variables.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor. A library within binutils that provides a common
    interface for reading and writing various binary object file formats.
- term: m32c
  definition: A family of microcontrollers from Renesas Electronics.
- term: unused-but-set-variable
  definition: A compiler warning indicating a variable that has been assigned a value
    but is never subsequently read. This often suggests dead code.
series_id: 'binutils:bfd/m32c: remove unused bytes_saved variable'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-3-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch removes the unused `bytes_saved` variable from `bfd/elf32-m32c.c`. A recent clang compiler version started flagging this variable as unused, leading to a build error. The variable has been present but unused since 2006.
