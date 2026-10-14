---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- regression
- memory leak
- c++
- atomic operations
discussion_id: CBDAA2D8-D69A-4667-A8CE-7A5B4402F6FB@utexas.edu
source_type: public_inbox
title: GCC 15 and 16 regression causes frame memory leaks
headline: GCC 15 and 16 regression causes frame memory leaks
tldr: A regression in GCC 15 and 16 causes memory leaks in programs compiled with
  the latest versions.
proposer: Gheith, Ahmed <ag@utexas.edu>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Potential performance degradation due to incorrect atomic operation handling.
- Increased memory consumption leading to program instability.
exchanges:
- author: Gheith, Ahmed
  role: proposer
  position: Reports a memory leak in GCC 15 and 16 compared to GCC 14, linking it
    to a change from atomic to non-atomic operations for subtract.
  quote: 'The attached program works as expected when compiled with g++ 14 but reports
    leaks with both g++ 15 and 16.


    Visual inspection of the generated code suggests that it’s related to replace
    an atomic sub in g++ 14 with a non-atomic one in g++ 15.'
- author: Jonathan Wakely
  role: reviewer
  position: Requests the reporter to file a bug report on the official GCC bug tracking
    system.
  quote: Please report this to https://gcc.gnu.org/bugzilla - thanks
- author: Torbjorn SVENSSON
  role: other
  position: Acknowledges Jonathan Wakely's request to report the issue on Bugzilla.
  quote: null
primer_expert: A regression in GCC's C++ frontend for versions 15 and 16 has been
  identified, manifesting as a frame memory leak. The issue appears to be related
  to the optimization of atomic operations, specifically a change from atomic to non-atomic
  subtract operations. This impacts code that uses threading and potentially other
  concurrency primitives.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CBDAA2D8-D69A-4667-A8CE-7A5B4402F6FB@utexas.edu
bugzilla_url: null
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

Ahmed Gheith reports a memory leak occurring in GCC 15 and 16 that is not present in GCC 14. The issue appears to stem from a change in how atomic subtract operations are handled, switching from atomic to non-atomic operations. This regression impacts programs using C++23 features and threading.
