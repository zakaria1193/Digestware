---
project: glibc
subsystem: misc
patch_id: null
tags:
- Makefile
- lint
- build system
- glibc
- AArch64
discussion_id: 20260420141459.531612-2-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v2 1/2] misc: fix lint-makefiles failures'
headline: Fix lint-makefiles failures
tldr: This patch fixes lint-makefiles failures by updating Makefiles in the sysdeps/aarch64
  and sysdeps/generic directories.
stakes: Ensures consistent and error-free Makefile syntax, crucial for reliable builds
  across different architectures.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The changes are primarily cosmetic and should not affect functionality.
- Incorrect Makefile syntax can lead to build failures or incorrect dependencies.
primer_expert: This patch focuses on Makefile maintenance within glibc's architecture-specific
  (`sysdeps/aarch64`) and generic (`sysdeps/generic`) directories.  It primarily involves
  correcting syntax and dependencies to satisfy the `lint-makefiles` check, ensuring
  proper build system behavior. These changes often involve adding missing object
  files to link lines, or correctly declaring header file dependencies. This layer
  directly affects the build process, but rarely application semantics.
primer_general: Makefiles are configuration files that tell the build system how to
  compile and link a software project.  They specify dependencies between files and
  the commands needed to build them.  `lint-makefiles` is a tool that checks Makefiles
  for syntax errors and inconsistencies. This patch corrects Makefile issues in glibc,
  specifically in the architecture-dependent (`sysdeps/aarch64`) and architecture-independent
  (`sysdeps/generic`) parts, ensuring that the build process functions correctly.
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

This patch addresses `lint-makefiles` failures by correcting Makefile syntax in `sysdeps/aarch64` and `sysdeps/generic`. It involves adding missing dependencies, and using consistent naming conventions. The changes ensure that the Makefiles are correctly formatted and avoid potential build issues.
