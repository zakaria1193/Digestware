---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compatibility
- ABI
- compiler
- linking
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: using GNU libc 2.27
tldr: User reports issues using glibc 2.27 with a modern compiler and seeks help resolving
  `__isoc23_strtol` dependency errors.
stakes: This discussion highlights compatibility issues between older glibc versions
  and newer compilers, which can affect software builds and testing.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using an older glibc version may limit access to newer features and security fixes.
- Using `--sysroot` can increase build complexity and may require careful management
  of dependencies.
exchanges:
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: proposer
  position: Reports issues using glibc 2.27 with a modern compiler due to missing
    `__isoc23_strtol` and seeks solutions.
  quote: Is there any hope to use GNU libc 2.27 with modern compilers?
- author: Vincent Lefevre <vincent@vinc17.net>
  role: contributor
  position: Suggests that the user might have to configure GMP and MPFR with `--sysroot=$ROOT`
    in CFLAGS.
  quote: null
- author: Arsen Arsenović <aarsenovic@baylibre.com>
  role: contributor
  position: Suggests using `-save-temps` to find the source of include paths.
  quote: null
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: proposer
  position: Reports no '.i' or '.ii' files are generated when using `-save-temps`.
  quote: null
- author: Arsen Arsenović <aarsenovic@baylibre.com>
  role: contributor
  position: Repeats the suggestion to use `-save-temps`.
  quote: null
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: proposer
  position: Indicates that the issue was resolved by using `--sysroot` and manually
    fixing hardcoded include paths.
  quote: null
primer_expert: This issue arises when using a newer compiler (gcc 15.2.0) with an
  older glibc (2.27). The `__isoc23_strtol` symbol is part of a later glibc ABI, and
  linking against libraries compiled with the newer ABI fails.  The suggested solution
  involves using `--sysroot` to isolate the build environment and ensure consistent
  header/library versions. Toolchain experts will recognize this as a common issue
  when mixing toolchains, but a general dev may not.
primer_general: Glibc (GNU C Library) provides standard functions for C programs.
  Different versions of glibc have different ABIs (Application Binary Interfaces),
  which define how programs interact with the library. When compiling programs, it's
  important to use a glibc version that's compatible with the compiler and other libraries
  being used. This discussion highlights a problem where a program compiled with a
  newer compiler is trying to link against an older glibc, resulting in missing symbols.
  The solution involves ensuring that the compiler and glibc are compatible, often
  by using a `sysroot` to isolate the build environment.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

A user is attempting to use glibc 2.27 with a recent version of GCC and the CORE-MATH test suite, encountering issues due to missing `__isoc23_strtol` references. They have tried various compilation flags and configurations but continue to face linking errors, and seeks advice on resolving these compatibility problems.
