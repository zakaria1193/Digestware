---
project: binutils
subsystem: gprof
patch_id: null
tags:
- gprof
- profiling
- inlining
- debugging
discussion_id: 20260528022134.133959-2-rsaxvc@gmail.com
source_type: public_inbox
title: '[PATCH] gprof: fix disappearing inlined functions'
headline: 'gprof: Fix disappearing inlined functions'
tldr: gprof now includes function names from line/debug symbols, correctly attributing
  CPU cycles to inlined functions.
proposer: Richard Allen <rsaxvc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- May increase the size of the gprof's symbol table.
- Requires access to line/debug symbol information.
exchanges:
- author: Richard Allen <rsaxvc@gmail.com>
  role: proposer
  position: Proposes a patch to load function names from line/debug symbols to fix
    the issue of gprof not showing inlined functions.
  quote: 'Load the function names from line/debug-symbols if available.


    The following test spends most of its CPU cycles mathing the

    long way around in xorshift_reverse(), but prior to this patch

    gprof would show 100% CPU spent in main().'
- author: '"H.J. Lu" <hjl.tools@gmail.com>'
  role: reviewer
  position: States that the full patch was not included in the email.
  quote: null
primer_expert: gprof samples the program counter to determine where time is spent.  Inlined
  functions can be difficult to attribute correctly without line/debug symbol information.  This
  patch modifies corefile.c and gprof.c to load this information, improving the accuracy
  of profiling for inlined functions.
primer_general: gprof is a profiling tool that helps developers understand where their
  programs are spending the most time.  It works by periodically sampling the program's
  execution and recording the function that is currently being executed.  Inlined
  functions, which are inserted directly into the calling function, can be difficult
  for profilers to track accurately, leading to skewed results. This patch aims to
  improve gprof's handling of inlined functions, providing more accurate profiling
  data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260528022134.133959-2-rsaxvc@gmail.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch modifies gprof to load function names from line/debug symbols, ensuring that inlined functions are properly accounted for in profiling results.  Previously, CPU cycles spent in inlined functions might be attributed to the calling function (e.g., main), leading to inaccurate profiling data.  This change provides more precise performance insights by correctly attributing time to inlined functions.
