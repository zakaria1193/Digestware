---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- makefile
- build
- lint
- aarch64
discussion_id: 20260420141459.531612-2-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v2 1/2] misc: fix lint-makefiles failures'
headline: 'misc: fix lint-makefiles failures'
tldr: Fixes `lint-makefiles` failures by adding missing dependencies and correcting
  syntax in `sysdeps/aarch64/Makefile` and `sysdeps/generic/Makefile`.
stakes: Ensures proper build process and avoids potential issues arising from Makefile
  errors, affecting all architectures.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved build system reliability and reduced potential for build errors.
- Increased verbosity and potential for merge conflicts due to changes in Makefiles.
- Potential for subtle build behavior changes due to corrected dependencies.
exchanges: []
primer_expert: This patch focuses on resolving Makefile issues detected by `lint-makefiles`
  within glibc's build system.  These errors typically involve incorrect syntax, missing
  dependencies, or other inconsistencies in the Makefiles, which can lead to build
  failures or incorrect compilation. The changes are specific to `sysdeps/aarch64/Makefile`
  and `sysdeps/generic/Makefile`, indicating architecture-specific and generic build
  rules respectively.
primer_general: Makefiles are used to automate the build process of software projects.
  They specify dependencies between files and the commands needed to compile and link
  them. `lint-makefiles` is a script that checks Makefiles for errors and inconsistencies.
  This patch addresses errors found by `lint-makefiles` in glibc, the GNU C Library,
  ensuring a correct and reliable build process.
series_id: 'glibc:misc: fix lint-makefiles failures'
series_role: reply
series_parts:
- title: 'misc: fix lint-makefiles failures'
  url: https://inbox.sourceware.org/libc-alpha/aeXhrdc8BxCy0vsH@arm.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/libc-alpha/20260420141459.531612-2-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses failures reported by the `lint-makefiles` script. It involves adding missing dependencies and fixing syntax errors within the `sysdeps/aarch64/Makefile` and `sysdeps/generic/Makefile` files, contributing to a more robust and reliable build system.
