---
project: binutils
subsystem: binutils
patch_id: null
tags:
- assembler
- gas
- SuperH
- literal pools
- documentation
discussion_id: VI1PR07MB59193FF80EAE69D037E3C4C3BF592@VI1PR07MB5919.eurprd07.prod.outlook.com
source_type: public_inbox
title: 'Re: SuperH literal pools in gas'
headline: SuperH literal pools in gas
tldr: The gas assembler's SuperH support is brittle and the author is not confident
  in their ability to produce a patch.
stakes: Fixing bugs or improving features in assemblers directly impacts developers
  using those assemblers for their projects.
proposer: Joseph Matthews <jmatt50@outlook.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges: []
primer_expert: The gas assembler is part of binutils and handles assembly language
  to object code translation. SuperH is a reduced instruction set (RISC) architecture.
  Literal pools are used to store constant data within the code segment. The c-sh.texi
  file likely contains documentation for the SuperH architecture within gas.
primer_general: The GNU assembler (gas) translates human-readable assembly code into
  machine-executable object code. Assembly language is a low-level programming language
  that directly corresponds to a computer's instruction set.  SuperH is a CPU architecture.  Assemblers
  sometimes use 'literal pools' to manage constant data efficiently.  This discussion
  concerns the quality of SuperH support in gas, and an idea for a patch.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/VI1PR07MB59193FF80EAE69D037E3C4C3BF592@VI1PR07MB5919.eurprd07.prod.outlook.com
bugzilla_url: null
date: '2026-04-10'
---

The SuperH support in the gas assembler is brittle, and the author is not confident in their ability to produce a patch to add literal pools. They do note that `sp` is an alias to `r15` but is undocumented in c-sh.texi, which they can amend.
