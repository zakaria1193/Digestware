---
project: glibc
subsystem: fwd
patch_id: null
tags:
- glibc
- s390
- obsolete
- architecture
- removal
discussion_id: 949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
source_type: public_inbox
title: 'Fwd: [PATCH 0/5] Remove s390-linux-gnu (31bit)'
headline: 'Fwd: [PATCH] Remove s390-linux-gnu (31bit)'
tldr: Removal of s390-linux-gnu (31bit) support from glibc has been committed.
stakes: Removes support for a deprecated architecture, simplifying the glibc codebase.
proposer: Stefan Liebler <stli@linux.ibm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes support for s390-linux-gnu (31bit).
- Simplifies the glibc codebase.
- Reduces maintenance overhead.
primer_expert: This change removes the s390-linux-gnu (31-bit) architecture from glibc,
  including related files in `sysdeps/s390/`.  The commit message references the removal
  of compat syscalls in Linux 6.19, which made the 31-bit ABI functionally obsolete.
  This simplifies the build process and reduces maintenance overhead.  Expect changes
  to `sysdeps/s390/*` and associated Makefiles.
primer_general: Glibc is designed to support a wide variety of operating systems and
  architectures.  Over time, some architectures become obsolete or are no longer actively
  maintained.  This commit removes the code specific to the 31-bit version of the
  IBM System z architecture (s390) from glibc, as support for it has been discontinued
  in the Linux kernel. This simplifies the glibc codebase and reduces the maintenance
  burden.
series_id: 'glibc:fwd: [patch ] remove s390-linux-gnu (31bit)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
bugzilla_url: null
date: '2026-04-20'
---

The patch series removing s390-linux-gnu (31bit) support from glibc has been committed. This follows the deprecation of the 31-bit s390 architecture and its removal from the build-many-glibcs.py script. The changes include removing s390-32 specific files, moving files from s390-64 directories upwards, and adjusting common-files.
