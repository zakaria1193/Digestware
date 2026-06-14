---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c-standard
- glibc
- feature-macros
- documentation
- abi
discussion_id: ai1DVieT3gTr4J5S@devuan
source_type: public_inbox
title: _ISOCxx_SOURCE
headline: C Standard library feature test macros need redesign and documentation fixes
tldr: The current design and documentation for C standard library feature test macros
  like `_ISOC23_SOURCE` are inaccurate and lead to confusion, requiring a new app…
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Simpler, clearer macro naming scheme vs. disruption to existing build systems using
  current `_ISOCxx_SOURCE` macros.
- Improved accuracy of feature availability vs. potential for introducing new compatibility
  issues during transition.
exchanges:
- author: Alejandro Colomar <alx@kernel.org>
  role: proposer
  position: Proposes a redesign and documentation fix for C feature test macros, citing
    inaccuracies in how they handle older standard versions, and suggesting a value-based
    approach similar to POSIX.
  quote: A better design of this macro would be to have a single identifier, and use
    a value to specify the version. This is how POSIX does it. We could call it _ISO_C_SOURCE,
    and have a value such as 202311L for requesting C23.
primer_expert: The discussion revolves around ``_ISOCxx_SOURCE`` feature test macros,
  which control the visibility of C standard library features. These macros are typically
  defined by compilers or build systems to indicate the desired C standard version,
  influencing what declarations and definitions are available from system headers.
  The problem lies in the current implementation's interaction with feature availability
  across different C standard versions (e.g., C99 vs. C11) and the potential for misinterpretation
  of what a given ``_ISOCxx_SOURCE`` definition implies for backward compatibility.
  This direct…
primer_general: When you write C code, you often use functions provided by the C Standard
  Library, like `printf` or `malloc`. These functions are declared in header files
  (like `stdio.h` or `stdlib.h`). Over time, the C language evolves with new standards
  (C99, C11, C23, etc.), which sometimes add new features, remove old ones, or change
  how existing ones work. To manage which version of the C Standard Library you're
  targeting, compilers and operating systems (specifically the C library, like glibc)
  use special macros, or 'feature test macros' like `_ISOC11_SOURCE`. Defining these
  macros tells the compiler which standard version's features you want to enable or
  disable. This proposal points out that the current system for these macros is confusing
  and the documentation is wrong about what features are enabled by each macro, leading
  to unexpected behavior and making it harder for developers to write portable code
  across different C standards.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ai1DVieT3gTr4J5S@devuan
bugzilla_url: null
date: '2026-06-13'
is_stub: false
---

Alejandro Colomar proposes a redesign of the `_ISOCxx_SOURCE` feature test macros in glibc, arguing their current documentation is incorrect and the design is suboptimal. The existing macros incorrectly claim to enable older C features, leading to situations where functions are unexpectedly disabled. Colomar suggests a unified macro, `_ISO_C_SOURCE`, with a version-specifying value, mirroring POSIX's approach for clearer and more accurate feature management.
