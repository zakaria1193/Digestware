---
project: gcc
subsystem: gsoc
patch_id: null
tags:
- gcc
- optimization
- gsoc
- ipa
- icf
discussion_id: 756r086p-2929-s22n-soq6-54p3nn494630@fhfr.qr
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction'
tldr: Discussion on using separate bodies for IPA-ICF as a potential GSoC project.
proposer: Richard Biener <rguenther@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Implementing separate bodies for IPA-ICF could improve optimization accuracy for
  certain cases but might increase compiler complexity and compilation time.
exchanges:
- author: Richard Biener <rguenther@suse.de>
  role: proposer
  position: Suggests that implementing separate bodies at the cgraph level, with one
    body for inlining and another for offline code generation, could be a suitable
    GSoC project and identifies potential mentors.
  quote: 'Yes, that''s what I expected - the separate body case only allows some

    cases of mismatches to prevail.  Implementing separate bodies on

    the cgraph level, one body for inlining, one for offline code generation,

    is another thing that might qualify for a GSoC project.  Honza or Martin

    would be to sign-off on that though, as they are the most natural mentors

    for this.'
- author: Rohith Kapelli
  role: contributor
  position: Reports on testing the separate-body idea with reduced test cases for
    PR119006 and PR123227, detailing observations on code generation when the leader's
    out-of-line body is inlined or not, and how ICF handles losing bodies.
  quote: "Hi Richard,\n\nI looked into the separate-body idea using reduced testcases\
    \ for \nPR119006 and PR123227, using trunk from 3 September, before the PR119006\
    \ \nand PR123227 fixes.\n\nFor PR119006, the current merge is safe when the leader's\
    \ out-of-line \nbody is not inlined, but inlining the leader into the other caller\
    \ \nproduces the wrong code. Defining the two structs in the opposite order \n\
    swaps the lea…"
primer_expert: This discussion concerns the GCC Intermediate Representation (IR) and
  optimization passes, specifically related to Interprocedural Analysis (IPA) and
  Identical Code Folding (ICF). The core issue is handling function bodies that are
  identical but might be emitted separately for inlining versus non-inlining (out-of-line)
  code generation. The potential GSoC project would involve modifying the cgraph level
  to manage these distinct bodies.
primer_glossary:
- term: IPA
  definition: Interprocedural Analysis, a compiler optimization technique that analyzes
    program behavior across function calls to optimize the entire program.
- term: ICF
  definition: Identical Code Folding, an optimization that detects and merges identical
    functions or code sections to reduce code size and improve cache performance.
- term: cgraph
  definition: GCC's internal representation for call graphs, used to model function
    calls and their relationships.
- term: GSoC
  definition: Google Summer of Code, an annual program that offers stipends to students
    who contribute to open-source projects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/756r086p-2929-s22n-soq6-54p3nn494630@fhfr.qr
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

Richard Biener acknowledges Rohith Kapelli's findings regarding IPA-ICF and separate bodies, suggesting the implementation of separate bodies at the cgraph level as a viable GSoC project. He indicates that Honza or Martin would be suitable mentors for such a project.
