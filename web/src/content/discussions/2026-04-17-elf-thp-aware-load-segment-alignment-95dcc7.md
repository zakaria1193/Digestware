---
project: glibc
subsystem: elf
patch_id: null
tags:
- elf
- THP
- performance
- alignment
- iTLB
discussion_id: CAHirt9iQp0cC=kxK9TfeRA9Z-0C+JZDw-YtvuWZJ5sDni-B6DA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v9 0/6] elf: THP-aware load segment alignment'
headline: 'elf: THP-aware load segment alignment'
tldr: This patch series enables THP-aware load segment alignment in glibc, reducing
  iTLB misses and improving performance with madvise THP.
stakes: Enabling THP-aware load segment alignment can significantly improve performance
  by reducing iTLB misses, especially in workloads benefiting from THP.
proposer: WANG Rui <wangrui@loongson.cn>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch series has gone through multiple revisions and shows
  performance improvements, indicating positive interest and progress.
series_id: 'glibc:elf: thp-aware load segment alignment'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAHirt9iQp0cC=kxK9TfeRA9Z-0C+JZDw-YtvuWZJ5sDni-B6DA@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

This patch series implements THP-aware load segment alignment in glibc. Benchmarking a clang build of the Linux kernel on x86_64 with this patch in THP madvise mode shows a reduction in iTLB misses, similar to THP always mode. The latest version includes a new test case and minor formatting fixes.
