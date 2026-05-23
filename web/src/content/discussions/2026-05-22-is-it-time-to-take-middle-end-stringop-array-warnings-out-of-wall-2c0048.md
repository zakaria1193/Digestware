---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- warnings
- middle-end
- diagnostic-paths
- C++
discussion_id: hgGNkR4qROW1AFjKLBH1JQ@gmx.net
source_type: public_inbox
title: 'Re: Is it time to take the middle-end stringop/array warnings out of -Wall?'
headline: Is it time to take middle-end stringop/array warnings out of -Wall?
tldr: Richard suggests that middle-end diagnostics should enable diagnostic-paths
  to show currently visible preconditions in C++.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enabling diagnostic-paths may increase compilation time.
- May require changes to GCC's internal data structures to efficiently track and display
  preconditions.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Suggests that diagnostics should enable diagnostic-paths, especially in
    C++, to show currently visible preconditions and improve the usefulness of middle-end
    warnings.
  quote: Much like that diagnostics that do this should probably enable diagnostic-paths,
    at least for their emitted diagnostics.  Because the path is what shows the currently
    visible preconditions.  Remember that esp. with C++ the set of visible preconditions
    is heavily dependent on inlining decisions.
- author: Matthias Kretz <MatthiasKretz@gmx.net>
  role: other
  position: Acknowledges Richard's reply.
  quote: null
- author: Martin Uecker <muecker@gwdg.de>
  role: other
  position: Acknowledges Richard's reply.
  quote: null
primer_expert: GCC's middle-end performs optimizations and transformations on the
  intermediate representation (IR) of code.  Stringop/array warnings detect potential
  buffer overflows or out-of-bounds accesses during this phase. Diagnostic paths trace
  the flow of data and control in the IR, revealing preconditions that influence optimization
  and warning behavior.
primer_general: Compilers use a multi-stage process to translate human-readable code
  into machine instructions. After parsing and initial conversion, the "middle-end"
  stage optimizes the code. This stage can detect potential errors, such as writing
  beyond the boundaries of an array.  These errors may depend on conditions checked
  earlier in the code; diagnostic paths can help developers understand how those conditions
  affect the warning.
series_id: 6C8E18B9-B946-4358-94A3-2979A435417C@gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/6C8E18B9-B946-4358-94A3-2979A435417C@gmail.com
bugzilla_url: null
date: '2026-05-22'
is_stub: false
---

Richard Biener comments on a previous proposal to categorize certain warnings as `-Wmiddle-end`. He suggests diagnostics should enable diagnostic-paths, to show currently visible preconditions. Biener notes that in C++ the set of visible preconditions depends heavily on inlining decisions, which affects how useful these warnings are.
