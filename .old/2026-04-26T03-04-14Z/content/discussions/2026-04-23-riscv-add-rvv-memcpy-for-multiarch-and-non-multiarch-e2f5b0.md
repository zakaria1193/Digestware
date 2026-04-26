---
project: glibc
subsystem: riscv
patch_id: null
tags:
- riscv
- memcpy
- rvv
- multiarch
- duplicate symbol
discussion_id: b30942de-bb35-4521-91b0-2b8b1f74b625@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 05/18] riscv: Add RVV memcpy for multiarch and non-multiarch'
headline: 'riscv: Add RVV memcpy for multiarch and non-multiarch'
tldr: Fixes a duplicate symbol definition in the RVV memcpy patch for riscv.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Aurelien Jarno
  role: other
  position: Noted that commit 89edb2e8c6a7 already added `__memcpy_generic` to `sysdeps/riscv/multiarch/dl-symbol-redir-ifunc.h`,
    causing a duplication.
  quote: "Thanks. I noticed that due to the commit 89edb2e8c6a7 (\"riscv: Resolve\
    \ \ncalls to memcpy using memcpy-generic in early startup\") already adding\n\
    __memcpy_generic to sysdeps/riscv/multiarch/dl-symbol-redir-ifunc.h,\nthis is\
    \ now duplicated:"
- author: Peter Bergner
  role: proposer
  position: Acknowledged the duplicate and confirmed it will be removed.
  quote: 'Weird.  That is not part of the patch and I''m surprised that applying

    the patch didn''t complain that the context was off.  Thanks for spotting

    this and I''ll remove the duplicate.'
primer_expert: This patch corrects a duplicate definition of `__memcpy_generic` in
  `sysdeps/riscv/multiarch/dl-symbol-redir-ifunc.h`. The duplicate arose due to a
  prior commit.  The patch ensures that the symbol is defined only once to avoid linking
  issues in the RISC-V multiarch implementation.
primer_general: This patch fixes an issue in the RISC-V version of `memcpy`, a fundamental
  function for copying memory. A previous commit introduced a duplicate definition
  of a symbol, which this patch removes to prevent potential linking problems. This
  ensures the `memcpy` function works correctly on RISC-V systems.
series_id: 'glibc:riscv: add rvv memcpy for multiarch and non-multiarch'
series_role: reply
series_parts:
- title: 'riscv: Add RVV memcpy for multiarch and non-multiarch'
  url: https://inbox.sourceware.org/libc-alpha/aemf4A7ao2xmO8pW@aurel32.net
  n: 5
  total: 18
url: https://inbox.sourceware.org/libc-alpha/b30942de-bb35-4521-91b0-2b8b1f74b625@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-23'
---

This patch addresses a duplicate symbol definition (`__memcpy_generic`) in the riscv RVV memcpy implementation. The duplicate was introduced by commit 89edb2e8c6a7, and this patch removes it. This ensures that the symbol is defined only once, preventing potential linking errors.
