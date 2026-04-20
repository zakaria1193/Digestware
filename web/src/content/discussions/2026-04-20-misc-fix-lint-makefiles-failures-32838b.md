---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- makefile
- build system
- linting
- aarch64
discussion_id: 20260420141459.531612-2-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v2 1/2] misc: fix lint-makefiles failures'
headline: 'Misc: Fix lint-makefiles failures.'
tldr: Fixes issues reported by lint-makefiles in the aarch64 and generic Makefiles.
stakes: Ensures consistent and correct Makefile syntax, improving build reliability
  and maintainability.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Corrects Makefile syntax, improving maintainability.
- Ensures proper build dependencies and flag propagation.
- No functional changes to the compiled code.
primer_expert: This patch addresses `lint-makefiles` errors in `sysdeps/aarch64/Makefile`
  and `sysdeps/generic/Makefile`. The fixes involve proper Makefile syntax, particularly
  in how variables are defined and used, especially within conditional blocks (`ifeq`).
  This ensures correct build dependencies and flag propagation.
primer_general: Makefiles automate the build process in software projects. They specify
  dependencies between files and the commands needed to compile and link them. Linting
  tools like `lint-makefiles` check Makefiles for errors and inconsistencies. This
  patch corrects such errors in the glibc build system, contributing to a more robust
  and reliable build process.
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

This patch resolves failures reported by the `lint-makefiles` script in the aarch64 and generic Makefiles. It involves correcting the syntax and structure of the Makefiles, specifically related to variable assignments and conditional logic.
