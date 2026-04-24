---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- THP
- arm32
- kABI
- dynamic linker
discussion_id: CAMe9rOpuLjOmaFDiXVf+LOx54H5Nss95RBziKk91LyceH4Dibg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v5] elf: Support THP segment load with madvise enabled THP'
headline: 'elf: Support THP segment load with madvise enabled THP'
tldr: A patch to support THP segment loading with madvise enabled THP in glibc faces
  regressions on arm32 due to kABI limitations.
proposer: H.J. Lu
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Identifies regressions on arm32 kABI when running THP tests, leading to
    binary loading failures.
  quote: "It seems to be a limitation of arm32 kABI. The strace of elf/tst-thp-1-static\
    \ shows that execve failed to load the binary:\n\n  $ strace -f elf/tst-thp-1-static\
    \ --direct\n  execve(\"elf/tst-thp-1-static\", [\"elf/tst-thp-1-static\", \"--direct\"\
    ], 0xbeda8468 /* 31 vars */) = -1 EINVAL (Invalid argument)"
- author: H.J. Lu
  role: proposer
  position: Notes that the THP tests pass on x86 and aarch64, but fail on arm.
  quote: 'The added THP tests pass on x86 and aarch64.  Some of them failed on arm:'
primer_expert: This patch series deals with glibc's dynamic linker and its interaction
  with the kernel's Transparent Huge Page (THP) feature. The goal is to enable THP
  for segments loaded by the dynamic linker when THP is configured to use madvise.
  This requires careful consideration of architecture-specific memory mapping restrictions
  (e.g., arm32 kABI's `arch_mmap_check`).
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that aims to
  improve performance by using larger memory pages (typically 2MB) instead of the
  standard 4KB pages. This optimization requires coordination between the kernel and
  the system's C library (glibc), especially the dynamic linker, to ensure that memory
  segments are properly aligned. The 'madvise' setting allows applications to advise
  the kernel about how to manage memory, including the use of THP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e76adca7-8325-4a0a-bfe1-ec6250d10c5c@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

This patch enables Transparent Huge Page (THP) segment loading when THP is enabled with madvise. Adhemerval Zanella Netto reports that while the added THP tests pass on x86 and aarch64, some tests fail on arm. The failure is attributed to a limitation in the arm32 kABI, where the kernel's `arch_mmap_check` hook prevents loading the binary due to address restrictions.
