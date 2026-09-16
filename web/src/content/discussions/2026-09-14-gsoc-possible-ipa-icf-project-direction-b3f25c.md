---
project: gcc
subsystem: gsoc
patch_id: null
tags:
- gcc
- gsoc
- ipa
- icf
- optimization
discussion_id: 51s2p0n4-99ns-30s7-0o93-ss4os0n0r1so@fhfr.qr
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction'
tldr: GSoC student explores IPA-ICF with separate function bodies, finding issues
  with inlining and non-null promises.
proposer: Rohith Kapelli <kapellirohith@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Potential for code size reduction through improved ICF.
- Risk of incorrect code generation if separate bodies or inlining are handled improperly.
- Complexity in managing function visibility and linkage across compilation units.
exchanges:
- author: Rohith Kapelli <kapellirohith@gmail.com>
  role: proposer
  position: Reports findings from experiments with separate function bodies for IPA-ICF,
    highlighting incorrect code generation for PR119006 when leaders are inlined and
    issues with non-null promises for PR123227.
  quote: For PR119006, the current merge is safe when the leader's out-of-line body
    is not inlined, but inlining the leader into the other caller produces the wrong
    code. Defining the two structs in the opposite order swaps the leader and makes
    the failure disappear. I also emulated your model by making both functions always_inline,
    putting them in an anonymous namespace so the originals get inlined into…
- author: Richard Biener <rguenther@suse.de>
  role: reviewer
  position: Acknowledged the findings and noted the specifics of PR119006.
  quote: "On Tue, 15 Sep 2026, Rohith Kapelli wrote:\n\n> Hi Richard,\n>\n> I looked\
    \ into the separate-body idea using reduced testcases for \n> PR119006 and PR123227,\
    \ using trunk from 3 September, before the PR119006 \n> and PR123227 fixes.\n\
    >\n> For PR119006, the current merge is safe when the leader's out-of-line \n\
    > body is not inlined, but inlining the leader into the other caller \n> produces\
    \ the wrong code. D…"
primer_expert: This GSoC project explores a new direction for GCC's Identical Code
  Folding (ICF) pass, specifically focusing on how it interacts with Interprocedural
  Analysis (IPA). The student is testing a "separate-body" approach, where function
  definitions might be placed in distinct compilation units or sections, and examining
  its impact on ICF's ability to merge identical code. The discussion details issues
  encountered with specific PRs (119006, 123227) related to inlining, non-null pointer
  promises, and the interaction with GNU extern inline semantics.
primer_glossary:
- term: IPA
  definition: Interprocedural Analysis, a compiler analysis technique that examines
    function calls and data flow across entire program execution, not just within
    a single function.
- term: ICF
  definition: Identical Code Folding, a compiler optimization pass that identifies
    and merges identical functions or code blocks to reduce executable size.
- term: GSoC
  definition: Google Summer of Code, an annual program where Google funds student
    contributions to open-source projects.
- term: PR
  definition: Problem Report, a bug report filed in a project's issue tracking system.
- term: non-null promise
  definition: An assumption or guarantee made by code that a pointer will not be null,
    which can be exploited by optimizations but may lead to issues if violated.
- term: extern inline
  definition: A C language specifier that affects how functions defined with `inline`
    are treated, particularly concerning linkage and visibility across translation
    units.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260914192200.56210-1-kapellirohith@gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

A GSoC student is investigating a project direction for IPA-ICF (Interprocedural Analysis - Identical Code Folding), focusing on the use of separate function bodies. Initial experiments with test cases for PR119006 and PR123227 reveal issues related to incorrect code generation when function bodies are inlined and problems with non-null promises. The student also observed differences in behavior with GNU extern inline and plans further investigation into IPA-cloning and ICF's handling of losing bodies.
