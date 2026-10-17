---
project: binutils
subsystem: risc-v/bfd
patch_id: null
tags:
- risc-v
- architecture
- specification
- toolchain
- commit
discussion_id: ece93820-a80a-4c25-8a06-23eb943798db@suse.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: correct canonical extension order (again)'
headline: 'RISC-V/bfd: correct canonical extension order (again)'
tldr: Confirmed that a patch to correct RISC-V canonical extension order has been
  committed.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Maintains a correct and standardized order for RISC-V extensions, aiding toolchain
  compatibility.
- Simplifies the canonical ordering logic by removing the 'N' extension while preserving
  dependencies for Z* extensions.
exchanges:
- author: Kito Cheng
  role: contributor
  position: Agreed to drop the 'N' extension from the canonical RISC-V order while
    keeping others for Z* extension ordering, noting that 'P' might be standardized
    soon.
  quote: 'Thanks for the updating, I''ve updated GCC side[1], but forgot update

    binutils sideㄡ


    The main reason to keep J, K, L, P, and T is that these letters are

    still important for determining the canonical order of Z* extensions,

    so I would prefer to keep them. P may land as early as 2027.


    Anyway, OK with dropping N.'
- author: Jan Beulich
  role: maintainer
  position: Confirmed that the patch was committed and that a minor test suite adjustment
    was required.
  quote: 'Committed, yet just to mention: This then also required a small testsuite

    adjustment.'
primer_expert: This is a follow-up confirmation that a patch, likely the one discussed
  in a previous thread, has been applied to binutils' BFD library. The patch corrects
  the canonical ordering of RISC-V architecture extensions. The core of the change
  involved removing the 'N' extension from the set used for canonical ordering, while
  keeping 'J', 'K', 'L', 'P', and 'T' because they influence the ordering of other,
  future extensions (Z* extensions). The decision aligns with ongoing efforts to maintain
  precise and correct support for the evolving RISC-V specification within the toolchain.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles. It is modular and extensible.
- term: canonical order
  definition: A standardized or preferred sequence for listing components, in this
    case, RISC-V architecture extensions. This is important for consistency and for
    defining the behavior of related features.
- term: extension
  definition: In the context of RISC-V, an extension is a set of additional instructions
    that augment the base ISA (e.g., 'M' for integer multiplication/division, 'A'
    for atomic operations, 'F'/'D' for floating-point, 'V' for vector operations).
    They are often denoted by letters appended to the base ISA, like 'RV64IMAFD'.
- term: Z* extensions
  definition: A naming convention in RISC-V for extensions that are not yet standardized
    or are in development. Their ordering can depend on other base extensions.
- term: test suite
  definition: A collection of test cases designed to verify the correctness of a software
    component or system. Binutils includes test suites for various tools and libraries.
- term: BFD
  definition: Binutils 'Binary File Descriptor' library. It provides a common interface
    for reading and writing various object file formats, including support for RISC-V.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ece93820-a80a-4c25-8a06-23eb943798db@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This email confirms the commitment of a patch that corrects the canonical order of RISC-V extensions within the binutils project. The discussion leading to this commit involved the decision to remove the 'N' extension from the canonical order while retaining others like 'J', 'K', 'L', 'P', and 'T' due to their importance in determining the order of Z* extensions and potential future inclusion. A small adjustment to the test suite was also necessary following the patch's application.
