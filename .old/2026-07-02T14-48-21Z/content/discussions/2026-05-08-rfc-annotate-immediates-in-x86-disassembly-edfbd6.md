---
project: binutils
subsystem: binutils
patch_id: null
tags:
- disassembly
- x86
- objdump
- testsuite
discussion_id: 977be117-100c-4a9a-8368-0bd8409e88b9@suse.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Jan reports a testsuite failure due to a missing global variable when running
  with RUNTESTFLAGS=x86-64.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding annotations increases the size of the disassembly output.
- The testsuite failure may indicate platform-specific issues.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Reports a testsuite failure due to a missing global variable when running
    with RUNTESTFLAGS=x86-64.
  quote: 'For me the use of the global "exe" in test_objdump_M_annotate is a problem
    when running the testsuite with RUNTESTFLAGS=x86-64: ERROR: can''t read "exe":
    no such variable'
primer_expert: This is a response to a patch series that adds annotations to immediates
  (constants) in x86 disassembly.  The goal is to improve the readability of disassembled
  code by providing additional context for these values, such as symbol names or calculated
  offsets. The problem lies in tcl testsuite code.
primer_general: When disassembling machine code, immediate values (constants) are
  often displayed as raw numbers. This patch series enhances the disassembly output
  by annotating these immediate values with additional information, such as the symbols
  they represent or their calculated offsets, which makes the disassembled code easier
  to understand. The problem lies in tcl testsuite code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/977be117-100c-4a9a-8368-0bd8409e88b9@suse.com
bugzilla_url: null
date: '2026-05-08'
---

Jan Beulich reports a failure in the binutils testsuite when running the 'annotate immediates in x86 disassembly' patch with `RUNTESTFLAGS=x86-64`. The test fails due to a missing global variable "exe". He notes that he doesn't know how to address this issue.
