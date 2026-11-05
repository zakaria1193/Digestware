---
project: binutils
subsystem: mips
patch_id: null
tags:
- binutils
- mips
- debugging
- dwarf
- compiler
discussion_id: alpine.DEB.2.21.2610291715230.42255@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH 3 11/16] MIPS: Fix line info in compressed MIPS function'
headline: 'MIPS: Fix line info in compressed MIPS function'
tldr: Patch corrects MIPS line number information for compressed functions, addressing
  an issue with DWARF debug info.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: proposer
  position: Corrects test addresses and clarifies capabilities of the binutils test
    framework, while agreeing with the need to fix MIPS line number debug info for
    compressed functions.
  quote: "The addresses used here do not match those with the tests.  I can see the\
    \ \nfailure though, true."
primer_expert: This discussion concerns the accurate generation of DWARF debugging
  information for MIPS architecture, specifically for functions compiled using MIPS16
  or microMIPS instruction sets, which use compressed instruction encodings. The issue
  is that the `_bfd_mips_elf_find_nearest_line` function, responsible for mapping
  code addresses to source lines, may fail for the entry point of such functions because
  the ISA bit is not set in the address. This prevents debuggers from correctly locating
  source line information for these functions. The discussion involves a correction
  to a previous patch and it…
primer_glossary:
- term: MIPS16
  definition: A 16-bit instruction set extension for the MIPS architecture, designed
    to reduce code size.
- term: microMIPS
  definition: A variant of the MIPS instruction set that uses a mix of 16-bit and
    32-bit instructions, offering a balance between code density and performance.
- term: DWARF
  definition: A standardized debugging data format used by many compilers to store
    information about variables, types, and code structure for debuggers.
- term: addr2line
  definition: A command-line utility that translates object code addresses into line
    numbers and function names, used for debugging.
- term: ISA bit
  definition: Instruction Set Architecture bit. In the context of MIPS compressed
    instructions, this bit in the address might indicate whether the instruction at
    that address is 16-bit (compressed) or 32-bit.
series_id: 'binutils: MIPS: Fix line info in compressed MIPS function'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2610291715230.42255@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

Maciej W. Rozycki points out an issue with a previous patch intended to fix line number information for MIPS compressed functions. While acknowledging the failure seen in addr2line output for specific addresses, Rozycki corrects the addresses used in the test case and clarifies that the binutils test framework does support `addr2line` checks. The original patch aimed to allow the first address of a MIPS16/microMIPS function to correctly retrieve filename/line information without needing the ISA bit set.
