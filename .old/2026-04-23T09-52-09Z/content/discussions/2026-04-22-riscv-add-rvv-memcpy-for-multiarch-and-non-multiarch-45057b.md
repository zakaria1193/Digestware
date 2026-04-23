---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- memcpy
- RVV
- optimization
discussion_id: a16bd5f8-d602-417c-8eba-194d3ac40a65@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [EXT] [PATCH v5 05/18] riscv: Add RVV memcpy for multiarch and non-multiarch'
headline: 'Riscv: Add RVV memcpy for multiarch and non-multiarch'
tldr: RVV memcpy implementation for RISC-V is accepted with a suggestion for potential
  future optimization.
stakes: Optimized memcpy implementations are crucial for performance, as memory copying
  is a fundamental operation. RVV (RISC-V Vector extension) allows for significant
  performance improvements on RISC-V processors.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Committed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The current hwprobe implementation might be slightly less efficient than a combined
  call, but is easier to understand and maintain.
- Optimizing memcpy for RVV improves performance on RISC-V systems with vector extensions,
  but adds complexity to the glibc codebase.
exchanges:
- author: Peter Bergner <bergner@tenstorrent.com>
  role: reviewer
  position: Accepts the patch and suggests a potential optimization of combining the
    two hwprobe calls into one for performance improvements, but leaves it for a future
    patch.
  quote: These two hwprobe calls could potentially be combined into one call to hwprobe
    with two keys... ..so I'm accepting the code as is and if someone prefers to combine
    them, then they can submit a patch.
primer_expert: This patch adds a RISC-V Vector extension (RVV) optimized memcpy to
  glibc. `memcpy` is the standard C library function for copying memory. Multiarch
  refers to the ability to select different implementations of a function based on
  CPU capabilities. `hwprobe` is a mechanism for detecting CPU features at runtime.
  The discussion centers on optimizing the feature detection and memcpy implementation
  for RVV-enabled RISC-V systems.
primer_general: Glibc is the standard C library used by most Linux systems, providing
  essential functions for programs to run. `memcpy` is a core function that copies
  blocks of memory. RISC-V is a modern, open-source computer architecture. RVV is
  the "vector extension" for RISC-V, a set of instructions for doing the same operation
  on many pieces of data at once. `hwprobe` is a function that detects the particular
  features of the CPU that's running.  This discussion revolves around adding a fast,
  RVV-specific version of memcpy to glibc, and how best to detect whether the CPU
  supports RVV.
series_id: 'glibc:riscv: add rvv memcpy for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/a16bd5f8-d602-417c-8eba-194d3ac40a65@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-22'
---

A patch adding a RVV (RISC-V Vector extension) implementation of `memcpy` for both multiarch and non-multiarch systems has been reviewed and accepted. The reviewer suggests a potential future optimization: combining two `hwprobe` calls into one, but ultimately accepts the code as is.
