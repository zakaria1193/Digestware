---
project: glibc
subsystem: fwd
patch_id: null
tags:
- glibc
- s390
- architecture
- deprecation
- removal
discussion_id: 949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
source_type: public_inbox
title: 'Fwd: [PATCH 0/5] Remove s390-linux-gnu (31bit)'
headline: 'Fwd: Remove s390-linux-gnu (31bit)'
tldr: Removes the s390-linux-gnu (31bit) configuration from glibc, as Linux 6.19 dropped
  support for compat syscalls on s390x.
stakes: This change simplifies the glibc codebase by removing support for a deprecated
  architecture.  General developers may be affected if they still target this architecture.
proposer: Stefan Liebler <stli@linux.ibm.com>
consensus: Proposed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced maintenance burden by removing support for a deprecated architecture.
- Potential breakage for users still relying on the s390-linux-gnu (31bit) architecture.
- Simplified codebase and build process.
exchanges:
- author: Stefan Liebler <stli@linux.ibm.com>
  role: proposer
  position: Proposes removing the s390-linux-gnu (31bit) configuration from glibc
    due to the removal of compat syscalls support in Linux 6.19.
  quote: This series now removes s390 (31bit) by removing the s390-32 files, moving
    files from s390-64 directories upwards and adjusting common-files.
primer_expert: This series removes the s390-linux-gnu (31bit) configuration.  The
  removal involves changes to the build system, header files, and source code.  The
  s390-32 architecture was deprecated in glibc 2.43 due to the removal of compat syscalls
  in Linux 6.19.  This change simplifies the glibc codebase by removing support for
  a deprecated architecture.
primer_general: glibc is the GNU C Library, providing standard functions needed by
  programs on Linux systems. This includes functions for system calls, memory allocation,
  file I/O, and string manipulation.  This patch series removes support for a specific,
  older architecture (s390-linux-gnu, 31bit) that is no longer supported by the Linux
  kernel.  This means that glibc will no longer be built for this architecture, and
  programs compiled for it will no longer run correctly.  For developers, this mostly
  means one less platform to worry about; those still targeting it will need to find
  alternatives or use older glibc versions.
series_id: 'glibc:fwd: [patch ] remove s390-linux-gnu (31bit)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/949f1598-3584-45ad-86b0-046b3b8d3191@linux.ibm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch series removes the s390-linux-gnu (31bit) configuration from glibc.  This involves removing s390-32 specific files, moving files from s390-64 directories, and adjusting common files.  The series also adds a preconfigure check that fails with an error message if someone tries to configure for s390 (31bit).
