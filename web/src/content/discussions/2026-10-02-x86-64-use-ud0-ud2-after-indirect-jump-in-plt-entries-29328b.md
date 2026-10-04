---
project: binutils
subsystem: x86-64
patch_id: null
tags:
- x86-64
- binutils
- speculation
- optimization
- PLT
discussion_id: CAKSQd8UDfv+umXcmkb-a0d3COGYkn+bizrkqWqfW42FqcDMahQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] x86-64: Use UD0/UD2 after indirect jump in PLT entries'
headline: 'x86-64: Use UD0/UD2 after indirect jump in PLT entries'
tldr: Discussion on using UD0/UD2 versus LFENCE/INT3 as speculation barriers after
  indirect jumps in PLT entries.
proposer: H.J. Lu <h.lu@intel.com>
consensus: Under Review
outcome: under_review
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Using UD0/UD2 might be less performant or less secure if they don't act as true
  speculation barriers.
- Using LFENCE or INT3 might introduce performance overhead if they are not strictly
  necessary for all indirect jumps.
- Correctly identifying indirect jumps that benefit from speculation barriers is crucial.
exchanges:
- author: Christian Ludloff <ludloff@gmail.com>
  role: other
  position: Contests the use of UD0/UD2 as speculation barriers, citing Intel's SDM
    which recommends LFENCE or INT3 for indirect branches.
  quote: 'The SDM recommends to follow indirect CALL with LFENCE

    and indirect JMP with either LFENCE or INT3.


    The short answer is "exceptions are not speculation barriers, unless

    explicitly listed as such... and most of them are not listed".


    The long answer is "see https://www.sandpile.org/x86/coherent.htm

    for more" – in this case here, you can skip the bottom half that does

    cover the store buffer and WC…'
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: 'Questions how other exceptions would serve as barriers if #UD does not
    always suffice.'
  quote: 'Yet then, if #UD doesn''t always suffice, how would any other exception

    do (including #BP or, if we also considered ICEBP here, #DB)?'
- author: H.J. Lu <h.lu@intel.com>
  role: proposer
  position: Initially proposed replacing NOP with UD0/UD2 after indirect branches
    in PLT entries based on Intel's optimization guide.
  quote: null
primer_expert: This discussion concerns the appropriate instruction to use as a speculation
  barrier after indirect jumps within Procedure Linkage Table (PLT) entries on x86-64.
  The original patch proposed using UD0/UD2 based on an Intel optimization guide.
  However, concerns were raised that these instructions may not reliably prevent speculative
  execution. The core of the debate is whether UD0/UD2 are sufficient, or if LFENCE
  or INT3, as recommended by Intel's System Programming Guide, are necessary for robust
  speculation control.
primer_glossary:
- term: x86-64
  definition: The 64-bit extension of the x86 instruction set architecture, commonly
    used in modern desktop and server processors.
- term: UD0/UD2
  definition: Undefined instruction exceptions on x86 processors. UD0 is a general
    undefined instruction, while UD2 is specifically designated for use by software
    to indicate an invalid operation.
- term: indirect jump
  definition: A control flow instruction that determines the target address of the
    jump at runtime, typically by reading it from a register or memory location.
- term: PLT
  definition: Procedure Linkage Table, a small section of code used in dynamically
    linked executables to resolve external function calls at runtime.
- term: speculation barrier
  definition: An instruction or mechanism that prevents the processor from speculatively
    executing instructions beyond a certain point, ensuring that out-of-order execution
    does not lead to incorrect state changes or data leaks.
- term: Intel SDM
  definition: Intel Software Developer's Manual, a comprehensive set of documentation
    detailing the architecture and programming of Intel processors.
- term: LFENCE
  definition: A fence instruction that prevents speculative execution of memory loads,
    but not stores or branch instructions, that occur after it.
- term: INT3
  definition: An instruction that generates a breakpoint exception (#BP), often used
    by debuggers. It can also serve as a form of speculation barrier.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8UDfv+umXcmkb-a0d3COGYkn+bizrkqWqfW42FqcDMahQ@mail.gmail.com
bugzilla_url: null
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

This thread discusses the effectiveness of using UD0/UD2 instructions as speculation barriers following indirect jumps in PLT entries, as proposed in a related patch. Christian Ludloff argues that UD0/UD2 are not guaranteed speculation barriers according to Intel's SDM, which recommends LFENCE or INT3 instead. The participants debate the nuances of CPU speculation and exception handling as barriers.
