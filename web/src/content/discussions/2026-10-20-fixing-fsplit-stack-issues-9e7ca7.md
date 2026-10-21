---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- -fsplit-stack
- stack overflow
- recursion
- performance
discussion_id: 0a331e73-2125-4586-8d55-a89ba87ffd67@users.sourceforge.net
source_type: public_inbox
title: fixing -fsplit-stack
headline: Fixing -fsplit-stack issues
tldr: Proposes fixes for severe issues in GCC's -fsplit-stack option, aiming to improve
  performance and stability for recursion-heavy code.
proposer: Thomas Neumann <tneumann@users.sourceforge.net>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Potential for increased complexity in signal handling and exception unwinding code
  to achieve performance gains.
- The fixes are currently x86-64 specific, requiring further work for other architectures.
exchanges:
- author: Thomas Neumann <tneumann@users.sourceforge.net>
  role: proposer
  position: 'Identifies and proposes fixes for three main issues in -fsplit-stack:
    high stack switch cost, incorrect signal handler stack computation, and crashes
    during exception unwinding.'
  quote: 'I have prototype fixes for all three (x86-64 only for now). By making

    __morestack re-entrant safe we can avoid signal blocking, bringing stack

    switch cost to about 5ns, which fixes the hot loop problem. The other

    two are largely classical bug fixes.'
- author: Martin Uecker <uecker@tugraz.at>
  role: other
  position: Acknowledges the description of issues with -fsplit-stack.
  quote: null
- author: Ian Lance Taylor <ian@airs.com>
  role: other
  position: Acknowledges the description of issues with -fsplit-stack.
  quote: null
primer_expert: This thread addresses problems in GCC's `-fsplit-stack` compiler option,
  which enables recursive functions to use a dynamically growing stack. The issues
  concern performance (high cost of stack switching due to signal blocking), correctness
  (crashes in signal handlers on AVX-512, and during exception unwinding), and potentially
  `alloca`/VLA usage. The proposer has developed fixes for x86-64 that target `__morestack`
  re-entrancy to reduce overhead.
primer_glossary:
- term: -fsplit-stack
  definition: A GCC compiler option that modifies function prologue/epilogue to handle
    stack overflow dynamically by allocating more stack space when needed. This is
    particularly useful for deeply recursive functions.
- term: AVX-512
  definition: Advanced Vector Extensions 512, an instruction set extension for Intel
    processors that allows for wider vector operations.
- term: re-entrant
  definition: A function that can be interrupted in the middle of its execution, safely
    called again (re-entered) before the previous invocation completes, and then continue
    correctly. This is crucial for signal handlers and multi-threaded environments.
- term: alloca
  definition: A function that allocates memory on the call stack. The memory is automatically
    freed when the calling function returns.
- term: VLA
  definition: Variable Length Array. An array whose size is determined at runtime
    rather than compile time.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/0a331e73-2125-4586-8d55-a89ba87ffd67@users.sourceforge.net
bugzilla_url: null
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

Thomas Neumann proposes to fix critical issues with GCC's -fsplit-stack option that hinder its practical use. The main problems identified are high stack switch overhead (167ns due to signal blocking), incorrect stack computation for signal handlers leading to crashes on AVX-512 systems, and crashes during exception unwinding. Prototype fixes are available for x86-64, aiming to reduce switch costs to around 5ns by making `__morestack` re-entrant safe.
