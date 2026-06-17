---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- optimization
- arm
- thumb-1
- ivopts
discussion_id: CAFiYyc3Uvny=SA4uuXyHzsc3hgyc9MJ9JQajWRZy4jzRPDAAOw@mail.gmail.com
source_type: public_inbox
title: 'Re: IVOPTs incorrectly selects post-increment addressing for Thumb-1'
headline: IVOPTs incorrectly selects post-increment addressing for Thumb-1
tldr: GCC's IVOPTs pass generates suboptimal code for Thumb-1 due to incorrectly applying
  post-increment addressing modes that Thumb-1 does not support.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Ciprian Arbone via Gcc
  role: proposer
  position: Reports that IVOPTs incorrectly selects post-increment addressing modes
    for Thumb-1, leading to suboptimal code generation due to Thumb-1's lack of support
    for negative immediate offsets.
  quote: 'The issue occurs because IVOPTs selects a candidate with the lowest cost
    that has the following structure: ... The pattern "increment r0; store-to [r0,
    #-4]" can never be realized as a post-increment store on Thumb-1, yet IVOPTs assigns
    it a low cost.'
primer_expert: IVOPTs (Induction Variable Optimizations) is a GCC pass that optimizes
  loops by transforming induction variables and memory accesses. This issue pertains
  to its interaction with the ARM Thumb-1 instruction set, specifically regarding
  post-increment addressing modes. The problem arises because `get_address_cost()`
  in `tree-ssa-loop-ivopts.cc` incorrectly assigns low costs to certain address patterns
  that are not directly implementable in Thumb-1 due to its architectural limitations
  (e.g., absence of negative immediate offsets for post-increment stores). This leads
  to the generation of less eff…
primer_general: When a computer program runs a loop (like `for (int i = 0; i < size;
  i++)`), a compiler tries to make that loop as fast as possible. One common optimization
  is to use 'induction variables,' which are variables that change in a predictable
  way in each step of a loop. GCC, the GNU Compiler Collection, has a special part
  called IVOPTs (Induction Variable Optimizations) that tries to make these loops
  more efficient. This report highlights a problem where IVOPTs makes a mistake when
  generating code for ARM processors using the 'Thumb-1' instruction set (often found
  in small, low-power devices like the Cortex-M0+). The compiler is trying to use
  a trick called 'post-increment addressing' where a memory location is accessed and
  then the address is automatically updated. However, Thumb-1 doesn't support some
  variations of this trick (specifically, updating the address with a *negative* offset
  after a write). Despite this, IVOPTs thinks these unsupported tricks are cheap and
  efficient, leading…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc3Uvny=SA4uuXyHzsc3hgyc9MJ9JQajWRZy4jzRPDAAOw@mail.gmail.com
bugzilla_url: null
date: '2026-06-16'
is_stub: false
---

Ciprian Arbone reported that GCC's IVOPTs (Induction Variable Optimizations) pass generates suboptimal code for Thumb-1 (Cortex-M0+) due to incorrect post-increment addressing mode selection. Specifically, IVOPTs assigns a low cost to patterns like "increment r0; store-to [r0, #-4]", even though Thumb-1 does not support negative immediate offsets in its addressing modes. This leads to inefficient code generation despite the recent enablement of LDMIA/STMIA instructions for Thumb-1.
