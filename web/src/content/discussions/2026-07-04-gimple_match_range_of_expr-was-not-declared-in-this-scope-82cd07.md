---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build
- gcc
- pattern matching
discussion_id: CACAb0qfE04Gmy_47ZoaYatE49SmPsjOu-bS1zhYCGfQCYfSqHA@mail.gmail.com
source_type: public_inbox
title: ‘gimple_match_range_of_expr’ was not declared in this scope
headline: ‘gimple_match_range_of_expr’ was not declared in this scope
tldr: Developer introduces a new function in GCC's pattern matching code but forgets
  to declare it, causing a build error.
proposer: Kael Andrew Franco <kaelfandrew@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 7
technical_tradeoffs:
- Missing function declaration leads to build failure, requiring a quick fix.
exchanges:
- author: Kael Andrew Franco <kaelfandrew@gmail.com>
  role: proposer
  position: Reports an 'undeclared identifier' error for 'gimple_match_range_of_expr'
    in gcc/match.pd, stemming from their own recent commit.
  quote: '‘gimple_match_range_of_expr’ was not declared in this scope.

    This is giving me headache, what is the problem since I can''t figure it out?'
- author: Sam James <sam@gentoo.org>
  role: reviewer
  position: Notes the error and quotes the original problem description.
  quote: 'Kael Andrew Franco via Gcc <gcc@gcc.gnu.org> writes:


    >  While working on PR126085, i keep running into this problem:

    >

    > ‘gimple_match_range_of_expr’ was not declared in this scope.'
- author: Kael Andrew Franco <kaelfandrew@gmail.com>
  role: proposer
  position: Confirms their commit caused the problem and states they will upload a
    fix.
  quote: 'That was caused by my commit  r17-1683-g43356828d897ad. Will upload a fix

    after quick bootstrap/test.'
primer_expert: This discussion concerns a build failure in GCC's pattern matching
  infrastructure, specifically within `gcc/match.pd`. The error 'gimple_match_range_of_expr
  was not declared in this scope' indicates that a newly added function or macro in
  the pattern definition file is being used before its declaration, likely due to
  a typo or an incomplete addition.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CACAb0qfE04Gmy_47ZoaYatE49SmPsjOu-bS1zhYCGfQCYfSqHA@mail.gmail.com
bugzilla_url: null
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

Kael Andrew Franco encountered an 'undeclared identifier' error for 'gimple_match_range_of_expr' while working on PR126085. The error stems from a recent change to gcc/match.pd. Franco acknowledged the issue was caused by their own commit and promised to upload a fix after testing.
