---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- assembler
- mach-o
- i386-darwin
discussion_id: ahQX5TBTuLWWgw_n@squeak.grove.modra.org
source_type: public_inbox
title: macho gas support
headline: Fixes for Mach-O assembler on i386-darwin proposed
tldr: Alan Modra proposes a patch series to fix issues in the Mach-O assembler for
  i386-darwin, the last remaining Mach-O target supported by gas.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The last patch may have correctness issues related to ignoring subsections when
  processing debug info.
- Not reducing symbols results in a large number of symbols, some with weird internal
  gas names.
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes a patch series to fix issues in the Mach-O assembler for the
    i386-darwin target, noting uncertainty about the last patch's correctness.
  quote: 'ix86-darwin is the only remaining macho target supported by gas.  I''m

    not sure how much it is used nowadays, and judging by the number of

    x86 tests and mach-o tests that fail, it seems no one is actively

    maintaining the code.  So it''s quite possible this series of patches I

    made fixing some issues was wasted time.'
- author: Iain Sandoe
  role: reviewer
  position: Offers to test the patch series.
  quote: 'I will try to look at and test this - over the next week or two - is

    there a branch somewhere I can checkout?'
- author: Alan Modra
  role: contributor
  position: Provides a branch for Iain to checkout the patches.
  quote: 'Thanks!  I hadn''t put them on a branch, but they are now on

    binutils-gdb users/amodra/macho.'
primer_expert: This series addresses issues in the Mach-O backend of gas, the GNU
  assembler, specifically for the i386-darwin target. The patches fix regressions
  and problems related to symbol reduction and DWARF generation.  Mach-O is the file
  format used by macOS, and this support is in gas to assemble code for older macOS
  systems.
primer_general: The GNU Assembler (gas) translates human-readable assembly code into
  machine code that a computer can execute.  This discussion concerns the Mach-O format,
  which is used by macOS operating systems. The patches aim to fix issues in the assembler's
  support for generating Mach-O binaries for older i386-based macOS systems, ensuring
  correct code generation and debugging information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahQX5TBTuLWWgw_n@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

Alan Modra is submitting a patch series to address issues in the Mach-O assembler specifically for the i386-darwin target. This target is the only remaining Mach-O target supported by gas. The changes fix testsuite regressions caused by commit cc28c46227cd and other problems related to symbol reduction and DWARF generation. Iain Sandoe has offered to test the patches.
