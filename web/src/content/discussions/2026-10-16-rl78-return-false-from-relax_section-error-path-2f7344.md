---
project: binutils
subsystem: rl78
patch_id: null
tags:
- linker
- relaxation
- rl78
- error handling
discussion_id: 20261016123644.1429854-7-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 6/8] rl78: return false from relax_section error path'
headline: 'rl78: return false from relax_section error path'
tldr: Fix rl78 ELF relaxation to return false on error, preventing OOM/IO failures
  from succeeding silently.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures proper error propagation, preventing silent failures.
- Minimal code change with clear benefit for robustness.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Corrects `rl78_elf_relax_section` to return false on error, preventing
    silent success of OOM/IO failures.
  quote: 'In rl78_elf_relax_section, the error_return: block previously returned

    true, causing OOM and I/O failures during section reading to silently

    succeed and proceed with corrupt state.  Correct error_return: to return

    false.'
primer_expert: This patch modifies the `rl78_elf_relax_section` function within `bfd/elf32-rl78.c`.
  The function handles linker relaxation for the RL78 architecture. The fix ensures
  that error conditions, such as memory allocation failures or I/O errors during section
  processing, correctly return a failure status (false) instead of a success status
  (true), thus preventing the linker from continuing with an invalid internal state.
primer_glossary: []
series_id: 'binutils:rl78: return false from relax_section error path'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-7-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch corrects an error path in the rl78 ELF relaxation function (`rl78_elf_relax_section`). Previously, it incorrectly returned true on out-of-memory or I/O failures. This change ensures it returns false, preventing the linker from proceeding with corrupted state after such errors.
