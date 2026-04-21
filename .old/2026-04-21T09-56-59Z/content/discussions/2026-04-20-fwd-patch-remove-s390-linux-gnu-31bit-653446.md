---
project: glibc
subsystem: fwd
patch_id: null
tags:
- glibc
- s390
- architecture
- removal
- deprecation
discussion_id: 949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
source_type: public_inbox
title: 'Fwd: [PATCH 0/5] Remove s390-linux-gnu (31bit)'
headline: 'Fwd: [PATCH ] Remove s390-linux-gnu (31bit)'
tldr: The removal of s390-linux-gnu (31bit) support from glibc has been committed
  due to its deprecation following the removal of compat syscalls in Linux 6.19.
stakes: This change removes support for 31-bit s390 systems, potentially affecting
  users still running on that architecture.
proposer: Stefan Liebler <stli@linux.ibm.com>
consensus: Proposed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced maintenance burden by removing support for a deprecated architecture.
- Potential breakage for users still running 31-bit s390 systems.
- Simplification of the glibc codebase and build system.
exchanges:
- author: Stefan Liebler <stli@linux.ibm.com>
  role: proposer
  position: Announces that the patch series has been committed.
  quote: 'Hi,

    I''ve just committed the series.

    @Adhemerval: Thanks for the review.

    Bye Bye s390 (31bit)'
primer_expert: This patch series removes the s390-linux-gnu (31-bit) architecture
  support from glibc. The removal follows the deprecation of this architecture due
  to the removal of compatibility syscalls in the Linux kernel. The changes involve
  removing specific files, moving files from s390-64 directories and adapting the
  build system.
primer_general: glibc, the GNU C Library, provides the core functions for programs
  running on Linux systems. This patch removes support for a specific architecture,
  s390-linux-gnu (31-bit), because the Linux kernel no longer supports running 31-bit
  programs on s390x (System z) hardware. This involves removing specific files and
  adjusting the build system to reflect the removal of this architecture.
series_id: 'glibc:fwd: [patch ] remove s390-linux-gnu (31bit)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch series removes support for the s390-linux-gnu (31bit) architecture in glibc. This follows the deprecation of the architecture in glibc 2.43 and the removal of compat syscalls for s390x in Linux 6.19. The series involves removing s390-32 specific files, moving files from s390-64 directories upwards, and adjusting common files.
