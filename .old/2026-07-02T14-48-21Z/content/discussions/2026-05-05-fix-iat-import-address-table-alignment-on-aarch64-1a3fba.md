---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- aarch64
- iat
- alignment
- pe32+
discussion_id: 20260505083445.4558-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH v3 0/1] Fix IAT (Import Address Table) alignment on AArch64'
headline: Fix IAT (Import Address Table) alignment on AArch64
tldr: This patch aligns the Import Address Table (IAT) to 8 bytes for PE32+ on AArch64
  to prevent relocation issues.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ensures correct memory access and prevents relocation errors on AArch64.
- Adds a small amount of padding to the IAT to enforce alignment.
- No significant performance impact expected.
exchanges:
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Proposes a patch to align the IAT to 8 bytes for PE32+ on AArch64 to fix
    relocation issues.
  quote: 'The IAT should be aligned to 8 bytes in aarch64-w64-mingw32, otherwise,
    it might result in relocation issues.


    When a function is imported from DLL, it generates the following code:


    adrp    x19, __imp_fn

    lodr     x19, [x19, #:lo12:__imp_fn]


    8 byte alignment is required for ldr relocation. Addresses are placed in IAT.'
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: other
  position: Explains that 8-byte alignment is required for ldr relocation.
  quote: null
primer_expert: This patch addresses an alignment issue in the Import Address Table
  (IAT) for PE32+ binaries on AArch64, specifically when targeting the MinGW environment.
  The IAT, used for storing addresses of imported functions, needs to be 8-byte aligned
  to ensure compatibility with `ldr` instructions used for accessing these addresses.
  Lack of alignment can lead to relocation errors, requiring a fix in `dlltool.c`.
primer_general: When a program uses functions from a Dynamic Link Library (DLL), the
  addresses of those functions need to be stored in a table called the Import Address
  Table (IAT).  On AArch64 systems, especially when using the PE32+ binary format
  (common on Windows), the IAT needs to be aligned to a specific memory boundary (8
  bytes in this case). This alignment is required because the instructions used to
  load addresses from the IAT (`ldr`) expect this alignment. If the IAT is not properly
  aligned, the program may crash or behave unpredictably due to incorrect memory access.
series_id: binutils:fix iat (import address table) alignment on aarch64
series_role: cover
series_parts:
- title: Fix IAT (Import Address Table) alignment on AArch64
  url: https://inbox.sourceware.org/binutils/afmmy2XjxoHlhiqx@arm.com
  n: 1
  total: 1
url: https://inbox.sourceware.org/binutils/20260505083445.4558-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-05-05'
---

This patch aligns the Import Address Table (IAT) to 8 bytes for PE32+ binaries on AArch64. This ensures that addresses placed in the IAT are properly aligned for `ldr` (load register) instructions, preventing potential relocation issues. The patch modifies `binutils/dlltool.c` to implement the alignment.
