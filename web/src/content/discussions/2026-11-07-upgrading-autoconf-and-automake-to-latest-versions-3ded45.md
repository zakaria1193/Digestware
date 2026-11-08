---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build system
- autoconf
- automake
- GCC
- binutils
discussion_id: 0618f4af-e2b7-468e-bc5c-d837fc75ac72@app.fastmail.com
source_type: public_inbox
title: Upgrading autoconf and automake
headline: Upgrading autoconf and automake to latest versions
tldr: Proposes upgrading Autoconf and Automake in GCC and Binutils, seeking testing
  advice and confirmation of C99 compliance.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Upgrading build tools can introduce subtle incompatibilities or break cross-compilation
  targets.
- Ensuring C99 compliance after autotools upgrade requires thorough testing across
  all supported platforms.
exchanges:
- author: Pietro Monteiro
  role: proposer
  position: Proposes upgrading Autoconf and Automake, and seeks guidance on testing
    and C99 compliance verification.
  quote: What kind of testing should be done? Are other people able to help here,
    specially for targets that don't use the GNU toolchain?
primer_expert: This proposal involves updating the build system generators Autoconf
  and Automake within the GCC and binutils-gdb codebases. The user has created branches
  with these upgrades and is seeking confirmation that Binutils' C99 requirement is
  maintained, as well as guidance on comprehensive testing strategies, particularly
  for cross-compilation targets.
primer_glossary:
- term: Autoconf
  definition: A tool that automatically configures source code packages to adapt to
    a specific operating system and environment. It generates shell scripts that check
    for system features and dependencies.
- term: Automake
  definition: A tool that helps manage the build process for software packages, generating
    Makefiles from simpler input files.
- term: C99
  definition: An official standard for the C programming language, which introduced
    several new features and improvements over previous versions.
- term: libiberty
  definition: A source code library of C routines used by various GNU programs, including
    GCC and Binutils, providing common utility functions.
- term: GNU toolchain
  definition: A set of programming tools developed by the GNU Project, typically including
    GCC, Binutils, GDB, and the GNU C Library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0618f4af-e2b7-468e-bc5c-d837fc75ac72@app.fastmail.com
bugzilla_url: null
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

Pietro Monteiro proposes upgrading Autoconf and Automake to their latest versions (2.73 and 1.19/1.20 respectively) within the GCC and Binutils projects. Branches with these upgrades are available on the Sourceware forge. The proposer is particularly interested in ensuring that the upgrades do not regress Binutils' requirement for C99 compliance and is seeking advice on necessary testing, especially for non-GNU toolchain targets.
