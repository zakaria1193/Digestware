---
project: glibc
subsystem: elf
patch_id: null
tags:
- thp
- arm
- elf
- kabi
- mmap
discussion_id: CAMe9rOpuLjOmaFDiXVf+LOx54H5Nss95RBziKk91LyceH4Dibg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v5] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP segment load with madvise enabled THP'
tldr: ARM32 kABI limitations cause THP tests to fail, likely due to `MAP_FIXED` and
  address restrictions.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Supporting THP requires careful consideration of architecture-specific memory layout
  and kernel restrictions.
- Using `MAP_FIXED` can lead to compatibility issues on platforms with limited address
  spaces.
- Enabling THP may expose underlying kernel limitations.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Identifies ARM32 kABI limitations as the cause of THP test failures, specifically
    related to `MAP_FIXED` and address restrictions.
  quote: 'It seems to be a limitation of arm32 kABI. The strace of elf/tst-thp-1-static
    shows that execve failed to load the binary: ... The ARM defines a arch_mmap_check
    hook'
- author: '"H.J. Lu" <hjl.tools@gmail.com>'
  role: other
  position: Acknowledges and incorporates Adhemerval's analysis into the patch.
  quote: null
primer_expert: This thread discusses THP support in glibc's ELF loader, specifically
  the interaction with `madvise` and the kernel's memory mapping (`mmap`) system calls.
  The issue arises on ARM32 due to stricter address space limitations enforced by
  `arch_mmap_check`.  Toolchain devs need to be aware of these architecture-specific
  constraints.
primer_general: This discussion concerns Transparent Huge Pages (THP), a memory management
  feature intended to improve performance, and how glibc, the standard C library,
  utilizes them when loading programs. Specifically, it focuses on the ELF loader,
  which is responsible for mapping program segments into memory. The problem arises
  on ARM32 systems, where kernel restrictions prevent the correct loading of THP-enabled
  programs due to address space limitations.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e76adca7-8325-4a0a-bfe1-ec6250d10c5c@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

Adhemerval Zanella Netto identifies that THP tests are failing on ARM due to limitations in the arm32 kABI. The failures appear to be related to the use of `MAP_FIXED` and address restrictions within the kernel's `arch_mmap_check` hook. The `execve` system call fails with an invalid argument error when loading the binary.
