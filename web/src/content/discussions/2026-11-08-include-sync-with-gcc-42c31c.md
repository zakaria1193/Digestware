---
project: binutils
subsystem: include
patch_id: null
tags:
- binutils
- gcc
- include
- synchronization
- headers
discussion_id: 20261108190131.592363-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: '[PATCH] include: sync with GCC'
headline: 'include: sync with GCC'
tldr: Binutils include directory synchronized with GCC, incorporating updates from
  several GCC commits.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 5
technical_tradeoffs:
- Ensuring binutils and GCC use consistent definitions for internal utilities and
  types can prevent subtle build and runtime issues.
- Keeping the include directories synchronized requires ongoing effort and potential
  merge conflicts.
exchanges:
- author: Pietro Monteiro
  role: proposer
  position: Submits a patch to synchronize binutils' include directory with GCC's,
    and later retracts it due to a mailing list address typo, indicating a resend.
  quote: 'I copied from include in the gcc tree all common files, except for

    btf.h. I did some git archeology to get the list of commits the

    changes came from.


    I''m sending the patch rather than just committing to give folks time to test.'
- author: Pietro Monteiro
  role: proposer
  position: Acknowledges a mistake in the original submission (wrong mailing list)
    and states the patch will be resent.
  quote: 'Please disregard, I typo-ed the gdb-patches mailing list address and will
    resend.


    sorry,

    pietro'
primer_expert: This patch updates the common header files in binutils' `include/`
  directory to match those in GCC's `include/` directory. This synchronization ensures
  that binutils uses the same definitions and declarations for various internal functions
  and macros as GCC, which is important for build system consistency and avoiding
  subtle incompatibilities. The updates span across various components and architectures,
  reflecting recent developments in GCC's header files. The author initially sent
  this to the wrong mailing list and intended to resend.
primer_glossary:
- term: libiberty
  definition: A collection of utility routines used by GCC and GNU Binutils, providing
    common functions like string manipulation and memory allocation.
- term: LoongArch
  definition: A RISC-V-like instruction set architecture developed in China.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is modular and
    extensible.
- term: CTF
  definition: Compact Type Format, a debugging data format used to describe type information.
- term: header files
  definition: Files in C/C++ that contain declarations of functions, variables, and
    macros, typically included using the `#include` directive.
series_id: 20261108190131.592363-2-pietro@sociotechnical.xyz
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261108190131.592363-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This patch synchronizes the `include/` directory of binutils with that of GCC. It pulls in changes from multiple GCC commits, including updates to libiberty, macro parameter handling, typo fixes, and architecture-specific code for LoongArch and RISC-V. The author notes that this patch is being sent for testing before direct commitment. A subsequent reply indicates this was a resend due to a typo in the original mailing list address.
