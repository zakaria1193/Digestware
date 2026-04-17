---
project: gcc
subsystem: rfc
patch_id: null
tags:
- optimization
- compiler pass
- code size
- reordering
- x86_64
discussion_id: CAFULd4a1_CR=NGZUU1X+EfuT0=Ge5d_32R4dNHN8S0mVPBe8dg@mail.gmail.com
source_type: public_inbox
title: 'Re: RFC: Another pass_late_combine after pass_reorder_blocks?'
headline: Consider adding another pass_late_combine after pass_reorder_blocks
tldr: Adding another pass_cprop_hardreg after pass_reorder_blocks shows code size
  improvements in x86_64 Linux kernel builds.
stakes: Optimizing compiler passes can improve code size and performance, affecting
  the efficiency of compiled software, especially for large projects like the Linux
  kernel.
proposer: Uros Bizjak <ubizjak@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The email presents empirical data supporting a potential optimization,
  which is generally viewed positively.
technical_tradeoffs:
- Adding compiler passes increases compilation time.
- The code size improvement may be architecture-specific or depend on the input code.
- The benefit of the additional pass needs to be weighed against the cost of maintaining
  another pass in the compiler.
- Consider whether a late combine entry, invoked only when BB reordering duplicates
  paths, would be sufficient.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFULd4ZtVsEMN2xc-9mbDZDEZGrQdJtaqzQW1SRLKSbD+RF63w@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

Uros Bizjak reports that adding an additional pass_cprop_hardreg after pass_reorder_blocks results in code size reductions for x86_64 Linux kernel builds. The results suggest a benefit from performing constant propagation after basic block reordering.
