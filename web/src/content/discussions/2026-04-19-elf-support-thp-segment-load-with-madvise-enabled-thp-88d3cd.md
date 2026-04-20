---
project: glibc
subsystem: elf
patch_id: null
tags:
- THP
- madvise
- ELF
- memory management
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'elf: Support THP segment load with madvise enabled THP'
tldr: This patch enables Transparent Huge Page (THP) support for segments loaded with
  madvise in glibc, fixing issues with both dynamic and static executables.
stakes: Enables THP for a wider range of configurations, potentially improving performance
  for applications using large memory regions.  Fixes bugs for both dynamic and static
  executables.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch addresses a known bug and has undergone several revisions,
  suggesting a positive reception.
technical_tradeoffs:
- Adds complexity to the ELF loader.
- Requires coordination with the kernel's THP settings.
primer: THP is a kernel feature that makes the system use larger memory pages (typically
  2MB) instead of the standard 4KB pages. This can reduce TLB pressure and improve
  performance for applications that work with large memory regions.  The ELF loader
  is responsible for mapping program segments into memory.  `madvise` is a system
  call that allows a program to advise the kernel about how it intends to use a region
  of memory, which can influence virtual memory management.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

This patch updates glibc to support THP segment loading when THP is enabled with madvise. It involves changes to segment alignment during object loading and calls to `madvise` with `MADV_HUGEPAGE` on THP-eligible segments.  The patch includes tests to verify correct mapping address alignment. This is version 4 of the patch with some updates based on the previous versions.
