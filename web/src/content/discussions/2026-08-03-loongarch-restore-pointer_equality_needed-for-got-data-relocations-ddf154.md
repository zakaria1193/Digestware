---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- linker
- loongarch
- relocation
- GOT
discussion_id: anBEsrlkwMTUZ1Kl@void-bee.tail05c47.ts.net
source_type: public_inbox
title: 'Re: [Patch] LoongArch: Restore pointer_equality_needed for GOT data relocations'
headline: 'LoongArch: Restore pointer_equality_needed for GOT data relocations'
tldr: Discusses a regression in LoongArch GOT relocations; the proposer acknowledges
  Xi Ruoyao's critique and plans to bisect.
proposer: Yanjun Yang <yangyj.ee@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Reintroducing `pointer_equality_needed` for data symbols to fix static executable
  crashes, potentially reintroducing issues for function pointers if not handled carefully.
- Distinguishing between function and data symbols for correct GOT relocation handling.
exchanges:
- author: Yanjun Yang <yangyj.ee@gmail.com>
  role: proposer
  position: Acknowledges Xi Ruoyao's critique of the proposed fix for LoongArch GOT
    relocations, confirms the regression source commit, and plans to bisect.
  quote: null
- author: Xi Ruoyao
  role: reviewer
  position: Questions the reasoning behind the proposed patch, specifically why `pointer_equality_needed`
    would apply to data symbols and suggests the breakage is more widespread if the
    issue is as described.
  quote: 'This does not make sense to me.  Global data symbols are accessed via

    R_LARCH_GOT_PC_HI20 everywhere, not only the CRT startup code.  Thus if

    accessing data symbols with R_LARCH_GOT_PC_HI20 is broken we''d have a

    much more wide-spreading breakage.


    This again does not make sense to me.  Pointer equality matters because

    if you end up comparing the address of the PLT stub and the address of

    the real…'
primer_expert: This thread concerns a regression in the LoongArch toolchain support
  within GNU Binutils, specifically related to how Global Offset Table (GOT) entries
  are handled for data symbols. A previous commit intended to fix function pointer
  equality issues in PIE executables by removing the `pointer_equality_needed` flag
  for GOT relocations. However, this broke static executables that use data symbols
  accessed via GOT, causing runtime errors. The discussion revolves around correctly
  restoring this flag only for data symbols, addressing reviewer concerns about the
  logic and scope of the fix.
primer_glossary:
- term: LoongArch
  definition: A 64-bit RISC instruction set architecture developed in China, used
    in various processors and systems.
- term: GOT
  definition: Global Offset Table. A special section in ELF executables and shared
    libraries that stores addresses of global variables and functions, allowing for
    position-independent code.
- term: relocation
  definition: A process performed by a linker or loader that adjusts symbolic addresses
    in object code to their final absolute locations in memory. Relocations specify
    how to modify memory references within code or data to point to the correct addresses
    of symbols.
- term: PIE
  definition: Position-Independent Executable. An executable file that can be loaded
    at any memory address. This is often used for security reasons to mitigate certain
    types of attacks.
- term: static executable
  definition: An executable file that includes all necessary library code directly
    within itself, rather than relying on shared libraries linked at runtime. This
    results in larger file sizes but removes runtime dependencies.
- term: pointer equality
  definition: In the context of executables, this likely refers to ensuring that comparing
    function pointers obtained through different means (e.g., direct call vs. GOT
    entry) yields the same result.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/anBEsrlkwMTUZ1Kl@void-bee.tail05c47.ts.net
bugzilla_url: null
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

This email is a reply in a discussion about a regression in LoongArch GOT (Global Offset Table) relocations. The original patch aimed to fix PR 29655 by removing `pointer_equality_needed` for GOT relocations, but this caused runtime segfaults in static executables due to altered GOT layout for data symbols. Xi Ruoyao questioned the logic, particularly concerning data symbols. The author acknowledges the critique, states that commit `7f9d6d6ead5` is the regression source, and plans to bisect further.
