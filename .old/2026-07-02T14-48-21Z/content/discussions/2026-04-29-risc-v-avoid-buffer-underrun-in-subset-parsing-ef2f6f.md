---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- subset parsing
- buffer underrun
- security
discussion_id: 2f78a893-33c4-4c75-ae0c-4e2d83e3675e@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 15/19] RISC-V: avoid buffer underrun in subset parsing'
headline: 'RISC-V: avoid buffer underrun in subset parsing'
tldr: The patch prevents a potential buffer underrun during RISC-V ISA extension parsing.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: ready
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- None apparent; this is a straightforward security fix.
exchanges:
- author: Jiawei
  role: contributor
  position: Agrees with the patch, which addresses a potential buffer underrun.
  quote: In both instances 'p' can be the first character. Inspecting the character
    immediately ahead of it is then UB.
primer_expert: This patch addresses a buffer underrun in the RISC-V assembler's subset
  parsing logic. Buffer underruns are a type of memory safety vulnerability that can
  lead to crashes or even arbitrary code execution.  The fix ensures that the code
  only accesses valid memory locations.
primer_general: This patch fixes a potential security vulnerability in the RISC-V
  assembler. The vulnerability, called a buffer underrun, could occur when the assembler
  is parsing the list of supported instruction set extensions. By carefully checking
  the boundaries of the data being processed, the patch prevents the assembler from
  accidentally reading data from outside of the allocated memory, thus preventing
  crashes or potential malicious exploitation.
series_id: 'binutils:risc-v: avoid buffer underrun in subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2f78a893-33c4-4c75-ae0c-4e2d83e3675e@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch fixes a potential buffer underrun vulnerability in the RISC-V assembler's ISA extension parsing logic. The code could potentially read before the beginning of the buffer when checking for the 'p' suffix on extension names. The patch adjusts the checks to ensure that the code never attempts to access memory outside of the allocated buffer, resolving the vulnerability.
