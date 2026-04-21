---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- rvv
- strcat
- optimization
discussion_id: f0114d80-0d2d-4647-b226-4b2bd5232810@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 09/18] riscv: Add RVV strcat for multiarch and non-multiarch'
headline: 'riscv: Add RVV strcat for multiarch and non-multiarch'
tldr: The RVV `strcat` implementation for RISC-V has been reviewed and pushed.
stakes: This enhances performance of `strcat` on RISC-V architectures by leveraging
  vector instructions.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Proposed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased code complexity due to the addition of new files and build rules.
- Potential performance gains on RISC-V processors with RVV support.
- Maintainability overhead of having multiple implementations of the same function.
exchanges:
- author: Peter Bergner <bergner@tenstorrent.com>
  role: proposer
  position: Acknowledges the review and pushes the patch.
  quote: 'LGTM.  Pushed.


    Reviewed-by: Peter Bergner <bergner@tenstorrent.com>'
primer_expert: This patch introduces optimized RISC-V vector (RVV) implementations
  of standard C string functions within glibc. Specifically, it focuses on the `strcat`
  function, providing both generic and vector-optimized versions to leverage RVV capabilities
  when available. This involves creating new files for the implementations and updating
  relevant Makefiles and ifunc lists to enable runtime selection of the appropriate
  version.
primer_general: glibc, the GNU C Library, provides standard functions for C programs.  Optimized
  implementations of these functions can leverage specific hardware features for performance.  This
  patch series adds optimized versions of string functions for RISC-V processors using
  vector instructions (RVV). The `strcat` function appends one string to the end of
  another. ifunc is a glibc mechanism that allows resolving a function call at runtime
  to the most appropriate implementation based on CPU capabilities.
series_id: 'glibc:riscv: add rvv strcat for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f0114d80-0d2d-4647-b226-4b2bd5232810@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-20'
---

This patch adds an RVV implementation of `strcat` for both multiarch and non-multiarch RISC-V systems. The implementation involves creating generic and vector-optimized versions of `strcat`, as well as updating the necessary Makefiles and ifunc lists. The patch has been reviewed and pushed.
