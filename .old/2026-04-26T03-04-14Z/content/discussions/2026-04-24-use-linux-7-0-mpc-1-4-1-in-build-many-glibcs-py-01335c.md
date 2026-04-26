---
project: glibc
subsystem: glibc
patch_id: null
tags:
- build
- glibc
- linux
- mpc
- build automation
discussion_id: 50aaf0be-d2e6-267c-be30-34ad10c97df3@redhat.com
source_type: public_inbox
title: Use Linux 7.0, MPC 1.4.1 in build-many-glibcs.py
headline: Use Linux 7.0, MPC 1.4.1 in build-many-glibcs.py
tldr: Updates the build-many-glibcs.py script to use Linux 7.0 and MPC 1.4.1.
proposer: Joseph Myers <josmyers@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Potential build failures or regressions with newer library versions.
- Ensures compatibility with newer Linux kernel and MPC library releases.
exchanges: []
primer_expert: '`build-many-glibcs.py` is a script used for building and testing glibc
  against various versions of its dependencies (kernel headers, GMP, MPFR, MPC). This
  patch updates the script to use newer versions of the Linux kernel headers (7.0)
  and the MPC library (1.4.1).'
primer_general: Glibc, the GNU C Library, relies on other software components like
  the Linux kernel headers and math libraries like GMP, MPFR and MPC. The `build-many-glibcs.py`
  script helps automate the process of building glibc against different versions of
  these dependencies, ensuring compatibility and identifying potential issues. This
  patch updates the script to use newer versions of the Linux kernel headers and the
  MPC library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/50aaf0be-d2e6-267c-be30-34ad10c97df3@redhat.com
bugzilla_url: null
date: '2026-04-24'
---

Joseph Myers proposes updating the `build-many-glibcs.py` script to use Linux kernel version 7.0 and MPC (Multiple Precision Complex) library version 1.4.1. This script is used for building multiple versions of glibc for testing purposes. The change has been tested with host-libraries, compilers, and glibc builds.
