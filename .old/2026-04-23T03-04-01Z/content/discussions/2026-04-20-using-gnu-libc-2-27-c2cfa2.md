---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compiler
- linking
- ABI
- compatibility
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Using GNU libc 2.27
tldr: User faces linking issues when trying to use glibc 2.27 with a modern compiler
  and seeks advice.
stakes: Illustrates the challenges of using older glibc versions with newer toolchains,
  potentially impacting reproducibility and testing of legacy systems.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using an older glibc version might be necessary for testing legacy software, but
  introduces compatibility challenges with newer compilers.
- Using `--sysroot` and similar options can resolve linking issues, but adds complexity
  to the build process.
- Recompiling libraries with specific compiler flags may be required to ensure compatibility,
  but can be time-consuming.
exchanges:
- author: Paul Zimmermann
  role: proposer
  position: Describes the problem of linking against glibc 2.27 with a modern compiler
    and asks for help.
  quote: Is there any hope to use GNU libc 2.27 with modern compilers?
- author: Vincent Lefevre
  role: contributor
  position: Responds to Paul regarding linking issues.
  quote: null
- author: Arsen Arsenović
  role: contributor
  position: Suggests to look at the compiler commands.
  quote: null
- author: Paul Zimmermann
  role: proposer
  position: Tried Arsen's suggestion but failed.
  quote: null
- author: Arsen Arsenović
  role: contributor
  position: Responds to Zimmermann's failure.
  quote: null
- author: Paul Zimmermann
  role: proposer
  position: States that he solved the issue with Vincent's help.
  quote: null
primer_expert: The issue revolves around ABI compatibility between an old glibc (2.27)
  and a modern compiler.  `__isoc23_strtol` is a function introduced in a later glibc
  version. The problem arises because MPFR (Multiple Precision Floating-Point Reliable
  Library) is being linked against the older glibc, while being compiled with a newer
  compiler that expects the newer symbol.  Sysroot is often used for cross-compilation
  setups.
primer_general: The GNU C Library (glibc) is the standard C library for many Unix-like
  systems. It provides essential functions for programs, including memory management,
  file I/O, and string manipulation. Compilers translate human-readable code into
  machine-executable code.  Different versions of glibc and compilers can have different
  ABIs (Application Binary Interfaces), which define how compiled code interacts.
  When using older versions of glibc with newer compilers you may need to configure
  the compiler to use headers and libraries from the older glibc version via --sysroot.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

Paul Zimmermann is encountering issues when trying to use GNU libc 2.27 with a modern compiler (gcc 15.2.0) for testing CORE-MATH. The linker complains about undefined references to `__isoc23_strtol`, even after recompiling GMP and MPFR with `-std=c99`. He seeks advice on how to resolve these linking errors to test math functions with the older glibc version.
