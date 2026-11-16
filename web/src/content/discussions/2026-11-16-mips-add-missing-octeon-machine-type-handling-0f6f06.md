---
project: binutils
subsystem: mips
patch_id: null
tags:
- binutils
- mips
- linker
- bfd
- commit
discussion_id: CA+=Sn1nUQeg3Ln4hZLrY=gpowvQS2=bEW0jRV7cFMwBs9tHGbw@mail.gmail.com
source_type: public_inbox
title: 'Re: [committed] MIPS: Add missing Octeon machine type handling'
headline: 'MIPS: Add missing Octeon machine type handling'
tldr: Commit adds missing Octeon machine type handling to BFD and gold for MIPS.
proposer: Andrew Pinski <pinskia@gmail.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Maciej W. Rozycki
  role: proposer
  position: Committed a change to add missing Octeon machine type handling for MIPS
    in BFD and gold, including a.out support.
  quote: 'Complement commit 2c62985659da ("MIPS: Add Octeon 3 support") and add missing
    AFL_EXT_OCTEON3 to machine type conversion in BFD and gold. Also add missing Octeon
    types to a.out support.'
- author: Andrew Pinski
  role: reviewer
  position: Acknowledged the commit, expressing regret for missing it earlier and
    thanking the author.
  quote: Thanks for doing this. Sorry I had missed it back then.
primer_expert: This commit addresses missing support for specific MIPS Octeon processor
  variants (Octeon3) within binutils. It updates the BFD library's machine type handling
  and the gold linker's MIPS backend to recognize and correctly process these machine
  types, including their representation in a.out object files. This ensures that binutils
  can correctly assemble and link code targeting these specific MIPS architectures.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a backend for GNU Binutils that provides
    a common interface to various object file formats.
- term: gold
  definition: The GNU linker, designed as a faster, more modern replacement for the
    traditional ld linker.
- term: MIPS
  definition: Microprocessor without Interlocked Pipeline Stages, a RISC instruction
    set architecture.
- term: Octeon
  definition: A family of MIPS-based microprocessors designed by Cavium (now Marvell)
    for networking and embedded applications.
- term: a.out
  definition: A.out (Assembler Output) is an older executable file format, largely
    superseded by ELF, but still supported by some toolchains.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+=Sn1nUQeg3Ln4hZLrY=gpowvQS2=bEW0jRV7cFMwBs9tHGbw@mail.gmail.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This commit adds missing handling for Octeon machine types (AFL_EXT_OCTEON3) to the BFD library and the gold linker. It complements a previous commit that added Octeon 3 support. The changes update machine type conversions in BFD and gold, and also add missing Octeon types to a.out support, ensuring broader compatibility for MIPS Octeon processors.
