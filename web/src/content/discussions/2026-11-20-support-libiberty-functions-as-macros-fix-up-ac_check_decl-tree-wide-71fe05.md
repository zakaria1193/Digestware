---
project: binutils
subsystem: binutils
patch_id: null
tags:
- libiberty
- build system
- autoconf
- portability
discussion_id: 87ik1rle2z.fsf_-_@esperi.org.uk
source_type: public_inbox
title: '[PATCH v2] Support libiberty functions as macros; fix up AC_CHECK_DECL tree-wide'
headline: Support libiberty functions as macros; fix up AC_CHECK_DECL tree-wide
tldr: Refactors libiberty checks to use macros for better encapsulation and cross-project
  consistency.
proposer: Nick Alcock <nix@esperi.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces a new macro-based system for libiberty checks.
- Requires changes to multiple projects that use libiberty.
exchanges:
- author: Nick Alcock <nix@esperi.org.uk>
  role: proposer
  position: Proposes a new approach to handle libiberty function checks using macros
    to improve encapsulation and reduce the need for repeated AC_CHECK_FUNCS calls
    in various projects.
  quote: 'Nick> In 2025, Iain Sandoe added memrchr support to libiberty.h. This requires

    > Nick> a new AC_CHECK_FUNCS of memrchr in every project that transitively

    > Nick> includes it, or builds on non-glibc, non-Linux hosts will fail (observed

    > Nick> on FreeBSD 15).'
- author: Tom Tromey
  role: other
  position: Suggests that libiberty should provide its own config.h-style header with
    namespaced names to improve encapsulation and prevent changes from propagating
    widely.
  quote: 'Not really your issue but this would all be a lot simpler if libiberty

    > made a config.h-style header with its own namespaced names, and then

    > included this and checked these names from the include/ headers.'
primer_expert: This patch series revises how libiberty functions are checked and integrated
  into the build system. Previously, new functions added to libiberty required `AC_CHECK_FUNCS`
  to be added to every project that used libiberty transitively, leading to maintenance
  overhead and potential build failures on non-standard hosts. This proposal aims
  to encapsulate these checks, potentially by using macros or a more centralized mechanism,
  to streamline the process and improve portability.
primer_glossary:
- term: libiberty
  definition: A collection of utility C functions developed by the GNU Project, often
    used by GNU tools when standard C library support is insufficient or unavailable.
- term: AC_CHECK_DECL
  definition: An Autoconf macro used to check for the presence of a function declaration.
- term: AC_CHECK_FUNCS
  definition: An Autoconf macro used to check for the presence of a function implementation.
- term: Autoconf
  definition: A tool used by software developers to create portable build scripts
    for Unix-like systems.
- term: memrchr
  definition: A C standard library function that searches for the last occurrence
    of a character within a given memory region.
- term: Encapsulation
  definition: A programming concept that bundles data and methods operating on that
    data within one unit, restricting access to some of the object's components.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87ik1rle2z.fsf_-_@esperi.org.uk
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch, a second version, addresses the propagation of libiberty changes across projects by introducing a macro-based approach for checking libiberty functions. This aims to simplify the maintenance of AC_CHECK_FUNCS calls and improve encapsulation, preventing issues on non-glibc, non-Linux hosts. The proposed solution has been tested and appears to be compatible with existing build systems.
