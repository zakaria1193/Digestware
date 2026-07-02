---
project: binutils
subsystem: include
patch_id: null
tags:
- documentation
- AMDGPU
- ELF
- header file
discussion_id: 20260507194615.943267-5-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH v2 4/4] include: add reference URLs in elf/amdgpu.h'
headline: 'include: Add reference URLs in elf/amdgpu.h'
tldr: Adds URLs to elf/amdgpu.h to clarify the source of AMDGPU ELF header constants.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increased size of the header file due to the addition of URLs (although this is
  negligible).
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Proposes adding reference URLs to the AMDGPU header file to clarify the
    source of the constants.
  quote: During review, a question was "where are those numbers that you are adding
    defined". Add some URLs pointing to the source of truth for those numbers.
primer_expert: This patch enhances the `elf/amdgpu.h` header with URLs pointing to
  the AMDGPU documentation.  This header defines AMDGPU-specific ELF constants used
  by binutils components like `readelf` to interpret AMDGPU code objects.
primer_general: This patch improves the documentation of AMDGPU-specific definitions
  within the binutils source code.  Specifically, it adds URLs to the `elf/amdgpu.h`
  header file, which defines constants related to the structure of AMDGPU ELF files.
  By providing direct links to the relevant AMDGPU documentation, this change makes
  the code easier to understand and maintain.
series_id: 'binutils:include: add reference urls in elf/amdgpu.h'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260507194615.943267-5-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

This patch adds reference URLs to the `elf/amdgpu.h` header file, which defines constants related to AMDGPU ELF headers.  The URLs point to the AMDGPU documentation, clarifying the origin and meaning of these constants. This improves code maintainability and makes it easier for developers to understand the AMDGPU-specific ELF structures.
