---
project: gcc
subsystem: tree-ssa-structalias.cc
patch_id: null
tags:
- gcc
- ipa
- pta
- pointer-analysis
- optimization
discussion_id: aqlSE223tVjyInUY@localhost.localdomain
source_type: public_inbox
title: 'Re: tree-ssa-structalias.cc: Why do we iterate over fields of a global varinfo'
headline: 'tree-ssa-structalias.cc: Why do we iterate over fields of a global varinfo'
tldr: Question about redundant loops in IPA PTA code for shadow variables.
proposer: Filip Kastl <fkastl@suse.cz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Potential for code simplification by removing redundant loops.
- Ensuring correctness of pointer analysis for aggregate types.
exchanges:
- author: Filip Kastl <fkastl@suse.cz>
  role: proposer
  position: Asks why a second loop over `vi_next()` is needed in `ipa_pta_execute()`
    for processing fields of global aggregate variables, questioning if fields are
    not already marked `is_global_var=true`.
  quote: null
- author: Richard Biener <rguenther@suse.de>
  role: reviewer
  position: Provided context by asking a question on Sep 1.
  quote: "On Tue, 1 Sep 2026, Filip Kastl wrote:\n\n> Hi.\n> \n> (by aggregates, I\
    \ will mean C structs and arrays and similar constructs that\n> aggregate data\
    \ from other languages that GCC compiles)\n> \n> The first question:\n> -------------------\n\
    > \n> I'm trying to understand the IPA PTA code related to shadow vars.  In the\
    \ code\n> snippet from tree-ssa-structalias.cc:ipa_pta_execute() below, why do\
    \ we need\n> th…"
primer_expert: This discussion touches on GCC's Intermediate Representation (IR) and
  Pointer Analysis (PTA) within the Interprocedural Analysis (IPA) framework. Specifically,
  it questions the logic in `tree-ssa-structalias.cc` regarding `varinfo_t` processing
  for shadow variables, which represent local variables in a callee that might be
  aliased by parameters. The core issue is whether the current traversal correctly
  identifies and processes fields of global aggregates, potentially avoiding redundant
  work.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aqlSE223tVjyInUY@localhost.localdomain
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

Filip Kastl is seeking clarification on a specific loop within GCC's IPA PTA code, related to shadow variables. He questions the necessity of iterating over fields of a global varinfo, suspecting it might be redundant if those fields are already marked as global. This investigation aims to optimize or clarify the handling of aggregate variables and their fields in pointer analysis.
