---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- build
- linux
- mpc
- dependencies
discussion_id: 50aaf0be-d2e6-267c-be30-34ad10c97df3@redhat.com
source_type: public_inbox
title: Use Linux 7.0, MPC 1.4.1 in build-many-glibcs.py
headline: Use Linux 7.0, MPC 1.4.1 in build-many-glibcs.py
tldr: Updates the Linux kernel version to 7.0 and MPC version to 1.4.1 in the build-many-glibcs.py
  script.
proposer: Joseph Myers <josmyers@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The `build-many-glibcs.py` script is used for regression testing and
  building glibc with various toolchains and kernel headers.  Updating the kernel
  and MPC versions ensures that glibc is tested against the latest versions of these
  dependencies. This change primarily affects the build environment used for glibc
  development and testing.
primer_general: Glibc, the GNU C Library, provides the core functions needed for programs
  to run on Linux systems. Before releasing a new version of glibc, developers need
  to test it with different versions of other software it depends on, like the Linux
  kernel and mathematical libraries.  The `build-many-glibcs.py` script automates
  this testing process by building glibc many times with different combinations of
  these dependencies.  This patch simply updates the script to use newer versions
  of the Linux kernel and the MPC library, ensuring that glibc is tested against the
  latest software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/50aaf0be-d2e6-267c-be30-34ad10c97df3@redhat.com
bugzilla_url: null
date: '2026-04-24'
---

This patch updates the `build-many-glibcs.py` script to use Linux kernel version 7.0 and MPC (Multiple Precision Complex) library version 1.4.1. The script is used for building glibc with various configurations and dependencies.
