---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- fts
- consolidation
- ABI
discussion_id: 5410EB13-EECF-4EB6-B1EB-E452949C3D33@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 1/3] io: Consolidate fts implementation'
headline: 'io: Consolidate fts implementation'
tldr: Consolidates the fts implementation for ABIs where off_t and off64_t are the
  same.
stakes: Simplifies the glibc codebase by reducing redundant implementations.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potential ABI breakage on systems where struct stat differs between 32-bit and 64-bit
  (e.g. MIPS n64).
- Code simplification and reduced maintenance burden for ABIs where off_t and off64_t
  are the same.
exchanges:
- author: Adhemerval Zanella <adhemerval.zanella@linaro.org>
  role: proposer
  position: Acknowledges that the fts ABI involves struct stat and raises concerns
    about MIPS n64 where struct stat and struct stat64 are different and will investigate.
  quote: Right, I will check out if there is any changes for such ABIs. I did run
    io tests on mips n32, but I did not check for n64.
primer_expert: '`fts` (file tree walking) is a set of functions in glibc that provides
  a way to traverse directory hierarchies.  Historically, glibc has maintained separate
  implementations for 32-bit and 64-bit ABIs. This patch aims to consolidate these
  implementations where `off_t` and `off64_t` are equivalent, simplifying the code.
  The concern raised is about ABIs like MIPS n64 where `struct stat` differs between
  32-bit and 64-bit, potentially breaking ABI compatibility.'
primer_general: The `fts` functions in glibc are used to walk file directory trees,
  similar to the `find` command in a shell. Due to historical reasons and different
  data models, glibc has often had separate implementations for 32-bit and 64-bit
  systems. This patch seeks to consolidate the code by using a single implementation
  when the types used for file offsets (`off_t` and `off64_t`) are the same size.
  A potential issue is that the `stat` structure, which provides file metadata, may
  differ between ABIs, leading to compatibility problems.
series_id: 'glibc:io: consolidate fts implementation'
series_role: reply
series_parts:
- title: 'io: Consolidate fts implementation'
  url: https://inbox.sourceware.org/libc-alpha/21167075-d79a-8d99-9d5a-1a7ee189d6c9@redhat.com
  n: 1
  total: 3
url: https://inbox.sourceware.org/libc-alpha/5410EB13-EECF-4EB6-B1EB-E452949C3D33@linaro.org
bugzilla_url: null
date: '2026-04-21'
---

This patch consolidates the `fts` implementation in glibc for ABIs where `off_t` is the same as `off64_t`. It removes wordsize-64 and arch-specific implementations, using `fts64.c` and aliases instead.
