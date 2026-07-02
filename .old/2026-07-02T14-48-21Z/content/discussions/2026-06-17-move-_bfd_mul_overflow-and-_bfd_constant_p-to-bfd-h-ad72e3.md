---
project: binutils
subsystem: binutils
patch_id: null
tags:
- refactoring
- header-files
- build-system
- binutils
discussion_id: ajMztGlTpwdV1R3a@squeak.grove.modra.org
source_type: public_inbox
title: move _bfd_mul_overflow from libbfd.h to bfd.h
headline: Move _bfd_mul_overflow and _bfd_constant_p to bfd.h
tldr: Moves `_bfd_mul_overflow` and `_bfd_constant_p` from `libbfd.h` to `bfd.h` to
  make them more broadly available without including `libbfd.h`.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes moving utility macros from libbfd.h to bfd.h to improve header
    inclusion hygiene and allow broader use.
  quote: Replace gas_mul_overflow with _bfd_mul_overflow, and don't include libbfd.h
    outside of bfd/.
primer_expert: This patch refactors the Binutils header hierarchy. Specifically, the
  `_bfd_mul_overflow` macro (for checking integer multiplication overflows) and `_bfd_constant_p`
  macro (for compile-time constant detection) are moved from `bfd/libbfd-in.h` to
  `bfd/bfd-in.h`. This enables other Binutils components like `gas` (the assembler)
  and `ld` (the linker) to use these fundamental utility macros by including `bfd.h`,
  rather than the more comprehensive `libbfd.h`, which is intended for BFD library
  internals. This improves modularity and reduces extraneous dependencies. It also
  standardizes the overflow…
primer_general: This change is about reorganizing the internal files (headers) within
  Binutils, a collection of programming tools for creating and manipulating binary
  programs. Think of headers as blueprints that define functions and variables used
  across different parts of the Binutils programs. This patch moves two important
  helper functions, `_bfd_mul_overflow` (which checks if multiplying two numbers would
  cause an error by making the result too large) and `_bfd_constant_p` (which identifies
  if a value is fixed at the time the program is compiled), to a more central, widely
  accessible header file. This way, different Binutils tools like the assembler and
  linker can use these helpers without needing to include a larger, more complex header
  file, making the Binutils code cleaner and more efficient to compile.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajMztGlTpwdV1R3a@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-17'
is_stub: false
---

This patch relocates the `_bfd_mul_overflow` and `_bfd_constant_p` macros from `libbfd.h` to `bfd.h`. This change allows other Binutils components, such as `gas` and `ld`, to use these helper macros without needing to include the heavier `libbfd.h` header. It also updates various files to use the newly exposed `_bfd_mul_overflow` and removes external inclusions of `libbfd.h`.
