---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- RVV
- strcat
- optimization
discussion_id: f0114d80-0d2d-4647-b226-4b2bd5232810@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 09/18] riscv: Add RVV strcat for multiarch and non-multiarch'
headline: 'Riscv: RVV strcat patch approved and pushed.'
tldr: RVV-optimized strcat implementation for RISC-V is approved and committed to
  glibc.
stakes: Improved string concatenation performance on RISC-V architectures with vector
  extensions.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Committed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds RVV-optimized assembly implementation for `strcat`.
- Includes a generic C fallback for systems without RVV support.
- Uses ifuncs to select the optimal implementation at runtime.
primer_expert: This patch implements an RVV-optimized `strcat` for RISC-V, using the
  ifunc mechanism for dynamic dispatch. The relevant files are in `sysdeps/riscv/multiarch/`
  and `sysdeps/riscv/rvv/`. The `strcat.c` file sets up the ifunc resolver, choosing
  between the generic C version (`strcat-generic.c`) and the RVV-optimized assembly
  version (`strcat-vector.S`).
primer_general: The glibc library provides standard C library functions. On RISC-V
  architectures, optimized versions of these functions can be implemented using the
  RVV (RISC-V Vector Extension) for improved performance. Ifuncs (Indirect Functions)
  are used to select the appropriate implementation at runtime based on the CPU's
  capabilities. This patch adds an RVV-optimized `strcat` implementation to glibc.
series_id: 'glibc:riscv: add rvv strcat for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f0114d80-0d2d-4647-b226-4b2bd5232810@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-20'
---

The patch adding RVV-optimized `strcat` for RISC-V, including multiarch support, has been reviewed and approved. The changes include assembly implementations, generic C fallbacks and integration with the ifunc system.  The patch has been pushed to the glibc repository.
