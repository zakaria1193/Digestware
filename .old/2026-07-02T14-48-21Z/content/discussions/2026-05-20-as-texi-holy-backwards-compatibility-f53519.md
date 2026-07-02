---
project: binutils
subsystem: as.texi
patch_id: null
tags:
- assembler
- gas
- .abort
- documentation
- backwards compatibility
discussion_id: DINU01U6ME10.CNRMXWXNQ284@gmail.com
source_type: public_inbox
title: '[PATCH] as.texi: Holy backwards compatibility'
headline: 'as.texi: Holy backwards compatibility'
tldr: The patch removes a notice in as.texi that .abort will one day not be supported,
  arguing it's a widely used feature.
proposer: 3bd <3bd3bdr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The binutils assembler (gas) provides the `.abort` directive to halt
  assembly immediately. Documentation for gas is in `gas/doc/as.texi`.  This patch
  removes a warning that `.abort` may be removed in the future.
primer_general: The GNU Assembler (gas) is a tool that translates assembly language
  into machine code.  Assembly language is a low-level programming language that is
  specific to a particular computer architecture.  The `.abort` directive is a command
  in assembly language that stops the assembly process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/DINU01U6ME10.CNRMXWXNQ284@gmail.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

A patch is proposed to remove a notice in the binutils assembler documentation (as.texi) stating that the `.abort` directive will one day not be supported. The patch author argues that `.abort` has been around for over 26 years and is now a widely used feature that many tools depend on.
