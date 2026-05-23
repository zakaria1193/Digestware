---
project: binutils
subsystem: alpha
patch_id: null
tags:
- binutils
- ld
- alpha
- elf
- tls
discussion_id: CAMe9rOo6ZP-TvzATQswWfYU6Ca9ynrA2ELr=09cEEOWu+LssmA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] alpha: Handle local weak undefined symbol value separately'
headline: 'Alpha: Handle local weak undefined symbol value separately'
tldr: The Alpha backend now handles TLS relocations against local weak undefined symbols
  separately, since their value is always 0.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- This change may introduce subtle ABI compatibility issues if not handled carefully.
- The added complexity in relocation logic could potentially introduce new bugs.
- The performance impact of the change is likely minimal, but should be measured.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes handling TLS relocations against local weak undefined symbols
    separately in the Alpha architecture, as their value is always 0.
  quote: 'Since local weak undefined symbol value is always 0, handle TLS

    relocations against local weak undefined symbols separately.'
primer_expert: This patch addresses a specific relocation scenario in the Alpha architecture's
  ELF implementation within binutils.  Local weak undefined symbols are symbols that
  are not defined in the current object file but may be defined in another. The linker
  needs to handle these symbols specially during relocation. TLS relocations involve
  adjusting addresses for thread-local storage.
primer_general: When creating an executable, the linker combines different pieces
  of code and data.  During this process, it resolves symbols, which are names that
  refer to specific locations in memory.  Sometimes, a symbol might be declared but
  not defined in a particular file (undefined symbol). Weak symbols provide a way
  to resolve conflicts when multiple definitions of the same symbol exist. TLS refers
  to thread-local storage, a mechanism for giving each thread its own private data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOo6ZP-TvzATQswWfYU6Ca9ynrA2ELr=09cEEOWu+LssmA@mail.gmail.com
bugzilla_url: null
date: '2026-05-22'
is_stub: false
---

This patch modifies the binutils elf64-alpha.c file to handle Thread Local Storage (TLS) relocations against local weak undefined symbols separately.  The value of such symbols is always 0.  The patch adds a new function `elf64_alpha_local_undefweak_p` and modifies `elf64_alpha_relocate_section` to implement this change.  Test cases are added to ld/testsuite to verify the new functionality.
