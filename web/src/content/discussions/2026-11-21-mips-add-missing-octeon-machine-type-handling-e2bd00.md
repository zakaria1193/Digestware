---
project: binutils
subsystem: mips
patch_id: null
tags:
- MIPS
- Octeon
- binutils
- machine-type
- a.out
discussion_id: alpine.DEB.2.21.2611210252440.54328@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [committed] MIPS: Add missing Octeon machine type handling'
headline: 'MIPS: Add missing Octeon machine type handling'
tldr: This commit addresses a follow-up fix for MIPS Octeon machine type handling,
  acknowledging a missed opportunity in a previous commit.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Maintaining compatibility with potentially obsolete a.out format.
- Ensuring correct handling of diverse MIPS processor variants.
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: contributor
  position: Confirms that a.out support is likely obsolete but suggests keeping it
    updated until dropped, and explains the conditions under which the machine type
    handling logic is triggered.
  quote: "Also a.out stuff is probably obsolete (though I'd rather keep it updated\
    \ \nuntil dropped) and the `*_mips_isa_ext_mach' stuff doesn't trigger unless\
    \ \nEF_MIPS_MACH field is clear and AFL_EXT_* in .MIPS.abiflags is not, which\
    \ \ndoesn't normally happen (though obviously you can orchestrate such an ELF\
    \ \nobject; not with standard binutils AFAICT though)."
- author: Andrew Pinski
  role: contributor
  position: Thanks the other author for the follow-up fix, acknowledging he missed
    it previously.
  quote: null
primer_expert: This discussion clarifies an aspect of MIPS machine type handling within
  binutils, specifically concerning Octeon processors and both ELF and older a.out
  object file formats. The comments delve into the nuances of the `*_mips_isa_ext_mach`
  logic, its interaction with the ELF header fields, and the deprecation status of
  a.out.
primer_glossary:
- term: Octeon
  definition: A family of multi-core microprocessors developed by Cavium Networks
    (now Marvell).
- term: BFD
  definition: Binutils Format Description, a library used by binutils to support various
    object file formats.
- term: gold
  definition: An alternative linker for the GNU toolchain, designed to be faster and
    more scalable than the traditional ld linker.
- term: a.out
  definition: A formerly common object file format on Unix-like systems, predating
    ELF.
- term: MIPS
  definition: A family of RISC instruction set architectures.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611210252440.54328@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-21'
is_stub: false
stub_reason: ''
---

This discussion is a reply to a committed patch that added Octeon 3 support to MIPS, specifically addressing machine type handling in BFD and gold, as well as a.out support. The author acknowledges a missed opportunity to include this in the original commit and confirms its necessity.
