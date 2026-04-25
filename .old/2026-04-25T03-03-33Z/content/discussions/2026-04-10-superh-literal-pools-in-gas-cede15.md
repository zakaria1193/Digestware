---
project: binutils
subsystem: binutils
patch_id: null
tags:
- assembler
- gas
- SuperH
- literal pools
- register alias
discussion_id: VI1PR07MB59193FF80EAE69D037E3C4C3BF592@VI1PR07MB5919.eurprd07.prod.outlook.com
source_type: public_inbox
title: 'Re: SuperH literal pools in gas'
headline: SuperH literal pools in gas
tldr: Discussion about implementing literal pools for the SuperH architecture in gas,
  and confirming that 'sp' is an alias for 'r15'.
proposer: Joseph Matthews <jmatt50@outlook.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Implementing literal pools could improve code density and performance on SuperH.
- Requires significant understanding of the gas internals and the SuperH architecture.
- May increase the complexity of the assembler.
exchanges: []
primer_expert: This discussion revolves around adding literal pool support to the
  SuperH backend of the GNU assembler (gas).  Literal pools are regions of memory
  where constant data is stored and accessed by instructions. The SuperH architecture's
  limited instruction set and addressing modes could benefit from this optimization.  The
  discussion also touches on the accuracy of existing documentation regarding register
  aliases.
primer_general: An assembler translates human-readable assembly code into machine
  code.  For some CPU architectures, assemblers use 'literal pools' to store constant
  values that instructions can easily access.  This discussion concerns adding literal
  pool support to the SuperH architecture within the GNU assembler.  The thread also
  clarifies a detail about register names on SuperH, confirming that `sp` (stack pointer)
  is another name for register `r15`.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/VI1PR07MB59193FF80EAE69D037E3C4C3BF592@VI1PR07MB5919.eurprd07.prod.outlook.com
bugzilla_url: null
date: '2026-04-10'
---

Joseph Matthews responds to Oleg about implementing literal pools for the SuperH architecture in gas (the GNU assembler).  Matthews expresses uncertainty about their ability to create such a patch due to unfamiliarity with gas internals and the brittle state of SuperH support.  However, they confirm that 'sp' is indeed an alias for 'r15' and offer to document this in `c-sh.texi`.
