---
project: gcc
subsystem: gsoc
patch_id: null
tags:
- gcc
- gsoc
- ipa
- optimization
discussion_id: CACbdTsrjMc73UBON6pSXyHN0V_QmFgSa9E3WH0VANF847q9QDA@mail.gmail.com
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction'
tldr: Rohith Kapelli proposes a 350-hour GSoC project to improve IPA-ICF's function
  merging logic by addressing limitations in equivalence checks.
proposer: Kapelli Rohith <kapellirohith@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Balancing the thoroughness of ICF equivalence checks against the potential performance
  overhead of more complex analysis.
exchanges:
- author: Kapelli Rohith <kapellirohith@gmail.com>
  role: proposer
  position: Proposes a 350-hour GSoC project to improve IPA-ICF, following up on previous
    patches and identifying limitations in current equivalence checks.
  quote: I'll follow up in the next few days with a more concrete technical plan and
    a few questions for Honza on the parts that need his judgement.
- author: Martin Jambor <mjambor@suse.cz>
  role: reviewer
  position: Acknowledges the proposal and expresses satisfaction with the direction,
    indicating it makes sense for a GSoC project.
  quote: null
primer_expert: This GSoC proposal addresses limitations in GCC's Interprocedural Analysis
  (IPA) framework, specifically within the Invalidate Code Folding (ICF) pass. The
  proposer found that ICF's equivalence checking (sem_function::equals_wpa and func_checker)
  can miss or mishandle information across merged functions, impacting optimizations
  for cases like libstdc++ template instantiations. The proposal seeks to refine these
  checks or explore alternative strategies for robust function merging.
primer_glossary:
- term: IPA-ICF
  definition: Interprocedural Analysis - Invalidate Code Folding. A GCC optimization
    pass that identifies identical functions and merges them to reduce code size and
    improve cache performance.
- term: GSoC
  definition: Google Summer of Code. An annual program that offers student developers
    stipends to contribute to open-source projects.
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
- term: LTO
  definition: Link-Time Optimization. An optimization technique that allows the compiler
    to optimize code across multiple source files during the linking stage.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used by GCC
    to represent code during optimization.
- term: SSA
  definition: Static Single Assignment. An intermediate representation property where
    each variable is assigned a value exactly once.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CACbdTsrjMc73UBON6pSXyHN0V_QmFgSa9E3WH0VANF847q9QDA@mail.gmail.com
bugzilla_url: null
date: '2026-10-25'
is_stub: false
stub_reason: ''
---

Following up on previous work on GCC's Interprocedural constant folding (IPA-ICF), Rohith Kapelli proposes a 350-hour Google Summer of Code project. The project aims to address limitations in ICF's equivalence checks that lead to missed or improperly preserved information when functions are merged, particularly impacting template instantiations in libstdc++.
