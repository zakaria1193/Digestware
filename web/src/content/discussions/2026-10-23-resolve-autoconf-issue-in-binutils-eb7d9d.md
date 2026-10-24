---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- autoconf
- configure
- regression
- aarch64
discussion_id: 20261023163025.4765-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH] Resolve autoconf issue in binutils'
headline: Resolve autoconf issue in binutils
tldr: Fixes a configuration regression in binutils for aarch64 targets by updating
  configure.ac.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: 10
technical_tradeoffs:
- Ensuring the added condition does not negatively impact other targets.
- Verifying that the fix addresses the root cause of the regression and doesn't introduce
  new issues.
exchanges:
- author: Evgeny Karpov
  role: proposer
  position: Submitted a patch to fix a configuration regression in binutils by modifying
    `configure.ac`.
  quote: 'The patch fixes the regression in the configuration in

    2c5ab4463fbfa424e6677549ee6086ed532ac714 by making changes in

    configure.ac.'
- author: Alice Carlotti
  role: maintainer
  position: Reviewed and merged the patch.
  quote: Pushed
primer_expert: This patch addresses a configuration regression in Binutils, specifically
  affecting the build system's handling of `aarch64` targets. A recent commit (2c5ab4463fbfa424e6677549ee6086ed532ac714)
  introduced a problem where the `configure.ac` script incorrectly handled `aarch64-*-mingw*`
  targets. This patch expands the condition to include `aarch64-*-pe*` targets as
  well, ensuring correct configuration for PE (Portable Executable) based Windows
  targets on aarch64.
primer_glossary:
- term: autoconf
  definition: An extensible package of M4 macros that produce shell scripts to automatically
    adapt software package source code to different operating systems and architectures.
- term: configure.ac
  definition: The main input file for Autoconf, which describes how to configure the
    package.
- term: regression
  definition: In software development, a regression is a bug that appears in a new
    version of software after it previously worked correctly.
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: mingw
  definition: Minimalist GNU for Windows, a development environment for creating Windows
    applications using the GNU Compiler Collection.
- term: PE
  definition: Portable Executable, the file format used for executables, object code,
    and DLLs on 32-bit and 64-bit versions of Windows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261023163025.4765-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Evgeny Karpov submits a patch to resolve a regression in binutils' configuration process. The fix modifies `configure.ac` to correctly handle `aarch64-*-pe*` targets in addition to `aarch64-*-mingw*`, addressing an issue introduced by a previous commit. Alice Carlotti confirmed the patch has been pushed.
