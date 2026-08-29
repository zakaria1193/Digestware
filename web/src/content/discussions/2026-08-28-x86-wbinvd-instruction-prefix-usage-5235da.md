---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- binutils
- assembly
- CPU cache
discussion_id: CAKSQd8V-m4oi-JhyxH3Y4KsLhf_CNFaVqbyJbNdd237FspndGA@mail.gmail.com
source_type: public_inbox
title: x86 WBINVD prefix allocations
headline: x86 WBINVD instruction prefix usage
tldr: Discussion on the correct allocation and usage of prefixes for the x86 WBINVD
  instruction, especially with new 'skip hints'.
proposer: Christian Ludloff <ludloff@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ensures assembler/linker support for evolving x86 instruction prefixes.
- Avoids potential conflicts with new, actively used cache control hints.
exchanges:
- author: Christian Ludloff
  role: proposer
  position: Raises concerns about the allocation and usage of prefixes for the x86
    WBINVD instruction, particularly new 'skip hints'.
  quote: 'If the use of x86 prefixes on WBINVD is not

    of your concern, you can stop reading.

    -------------------- 8< -------------------

    I was asked to relay this to binutils/LKML.

    The new hints are in active use by a corporate entity other than Intel/AMD; therefore
    they shouldn''t be redefined.

    0x67 = no CODE hint => skip L0i/L1i cache

    0x66 = no DATA hint => skip L0d/L1d cache

    0xF3 = no INVD hint => skip i…'
primer_expert: This discussion concerns the x86 architecture's `WBINVD` instruction
  and the interpretation of its prefixes. Historically, `WBINVD` (opcode `0x0F, 0x09`)
  invalidates caches. The `WBNOINVD` variant (with `0xF3` prefix) skips invalidations.
  New prefixes are being introduced (e.g., `0x67`, `0x66`, `0xF2`, and segment register
  prefixes `0x26`, `0x2E`, etc.) that provide finer-grained control over which caches
  (code, data, LLC) are affected or allow implementation-specific behaviors. These
  prefixes are reportedly in active use, prompting a discussion on ensuring the assembler
  (`as`) and linker (`l…
primer_glossary:
- term: WBINVD
  definition: An x86 instruction that writes back and invalidates the processor's
    on-chip caches.
- term: Prefix bytes
  definition: In x86 assembly, bytes that precede an instruction opcode to modify
    its behavior, such as segment overrides, LOCK, or operation size.
- term: CPUID flag
  definition: A flag returned by the CPUID instruction, used to query processor information,
    including supported features and capabilities.
- term: LLC
  definition: Last-Level Cache. The cache closest to the processor cores that is shared
    among them, typically L3 cache.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8V-m4oi-JhyxH3Y4KsLhf_CNFaVqbyJbNdd237FspndGA@mail.gmail.com
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

Christian Ludloff brings attention to the usage of prefixes with the x86 WBINVD instruction, noting that new 'skip hints' (0x67, 0x66, 0xF3, 0xF2, and implementation-specific prefixes) are in active use by a corporate entity. The discussion clarifies that these prefixes modify the cache behavior of WBINVD without introducing new CPUID flags. The goal is to ensure binutils correctly handles these prefixes as they are being adopted.
