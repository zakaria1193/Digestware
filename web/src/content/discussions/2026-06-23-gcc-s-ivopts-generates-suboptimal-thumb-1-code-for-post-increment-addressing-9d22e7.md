---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- optimization
- arm-thumb
- code-generation
- performance
discussion_id: CAGKGkux6AsM6WcC0kRzX4BzUcvncCF97+v2fni4mRX4_C3s3ag@mail.gmail.com
source_type: public_inbox
title: 'Re: IVOPTs incorrectly selects post-increment addressing for Thumb-1'
headline: GCC's IVOPTs generates suboptimal Thumb-1 code for post-increment addressing
tldr: GCC's Induction Variable Optimizations (IVOPTs) select suboptimal post-increment
  addressing modes for Thumb-1, leading to inefficient code for simple loops.
proposer: Ciprian Arbone <ciprianarbone@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enabling `LDMIA`/`STMIA` for Thumb-1, while potentially beneficial, has exposed
  issues with IVOPTs' cost model, leading to suboptimal code in certain cases.
- Correcting the IVOPTs cost model for post-increment addressing on Thumb-1 might
  require significant adjustments to ensure global optimality without regressions.
exchanges:
- author: Ciprian Arbone <ciprianarbone@gmail.com>
  role: proposer
  position: Reports that IVOPTs generate suboptimal Thumb-1 code for simple loops
    with post-increment addressing, leading to inefficient sequences after enabling
    `LDMIA`/`STMIA`.
  quote: "The issue occurs because IVOPTs selects a candidate with the lowest cost\
    \ that has the following structure: ... GCC currently generates: ... The issue\
    \ occurs because IVOPTs selects a candidate with the lowest cost that has the\
    \ following structure: \nCandidate xxx:\n  Incr POS: after use 0\n  IV struct: "
primer_expert: GCC's Induction Variable Optimizations (IVOPTs) are a crucial part
  of the optimizer, focused on improving loops, particularly by analyzing and transforming
  induction variables. This discussion highlights an issue within IVOPTs related to
  ARM's Thumb-1 instruction set, specifically concerning post-increment addressing
  modes for load/store multiple instructions (`LDMIA`/`STMIA`). The `ARM_AUTOINC_VALID_FOR_MODE_P`
  hook determines if auto-increment addressing is valid for a given machine mode.
  The problem is that while `LDMIA`/`STMIA` have been enabled, IVOPTs' cost model
  seems to incorrectly fa…
primer_general: 'When a compiler like GCC optimizes a program, it tries to make loops
  run as fast as possible. One technique is called "Induction Variable Optimizations"
  (IVOPTs). This involves looking at how variables change within a loop and making
  them more efficient. This problem describes an issue with GCC''s IVOPTs when compiling
  for older ARM processors (specifically, the Thumb-1 instruction set, often found
  in small microcontrollers like the Cortex-M0+). The compiler is generating inefficient
  code for simple loops that access arrays. Instead of using a more direct way to
  load and store data while automatically updating the memory address (called "post-increment
  addressing"), it''s performing extra steps: loading data, then manually adjusting
  the memory address, and then storing the data. This makes the program larger and
  slower than it should be, costing performance on resource-constrained devices. The
  issue became apparent after a change that allowed the compiler to use a specific
  type of effic…'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAGKGkux6AsM6WcC0kRzX4BzUcvncCF97+v2fni4mRX4_C3s3s3ag@mail.gmail.com
bugzilla_url: null
date: '2026-06-23'
is_stub: false
---

GCC's Induction Variable Optimizations (IVOPTs) are generating suboptimal code for Thumb-1 targets, specifically for simple loops using post-increment addressing. This issue arises because IVOPTs incorrectly select a candidate with the lowest cost, even though this candidate leads to inefficient instruction sequences involving `ldmia`/`stmia` and subsequent address adjustments. The problem became apparent after enabling `LDMIA`/`STMIA` instructions for Thumb-1 by modifying `ARM_AUTOINC_VALID_FOR_MODE_P`.
