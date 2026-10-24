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
discussion_id: ri6a4o4jxw0.fsf@virgil.suse.cz
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction'
tldr: Review of IPA-ICF merges suggests missed properties, prompting a proposal for
  a GSoC project to inventory and classify ICF properties.
proposer: Martin Jambor <mjambor@suse.cz>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased complexity in ICF if more properties need to be checked.
- Potential for missed optimizations if conservative approaches are always taken.
- Cost of identifying and implementing checks for all relevant properties.
- Balancing the benefit of reduced code size against potential performance impacts
  from incorrect merges or conservative checks.
exchanges:
- author: Rohith Kapelli
  role: proposer
  position: Proposed that a GSoC project could build an inventory of properties ICF
    needs to compare, classifying them as harmless if different, able to be made conservative,
    or blocking merges.
  quote: 'This led me to a possible GSoC project: build a complete inventory of the
    properties ICF needs to compare, including properties it currently misses, and
    classify each one as harmless if it differs, something that can be made conservative,
    or something that must block the merge.'
- author: Martin Jambor
  role: reviewer
  position: Acknowledged the proposal and delays, noting that previous merges of ICF
    improvements had issues with equivalence checks missing properties, impacting
    libstdc++ LTO.
  quote: 'Hello,


    sorry that it took us so long to respond.


    On Mon, Sep 14 2026, Rohith Kapelli wrote:

    > Hello,

    >

    > I''ve been working on GCC for the last few months, with four merged patches
    in RTL simplification (PR125683), AArch64 (PR123951), and IPA-ICF (PR119006 and
    PR123227). I was also granted Write After Approval on September 8, sponsored by
    Richard Biener.

    >

    > While working on PR119006 and PR12322…'
primer_expert: This thread discusses potential improvements to GCC's Identical Code
  Folding (ICF) pass, which aims to merge identical functions to reduce code size.
  The core issue is that ICF's current equivalence checks (sem_function::equals_wpa
  and func_checker) are not robust enough, leading to incorrect merges or missed opportunities.
  The proposal, framed as a GSoC project, is to systematically analyze and classify
  all properties that ICF should consider, ensuring safer and more effective function
  merging, especially relevant for LTO and template instantiation scenarios.
primer_glossary:
- term: IPA
  definition: Interprocedural Analysis, a compiler technique that analyzes the relationships
    and dependencies between different functions in a program.
- term: ICF
  definition: Identical Code Folding, a compiler optimization that merges identical
    functions into a single copy to save space.
- term: GSoC
  definition: Google Summer of Code, a program that offers stipends to students who
    contribute to open-source projects during the summer.
- term: LTO
  definition: Link-Time Optimization, a compiler optimization technique that performs
    optimization across different object files during the linking stage.
- term: libstdc++
  definition: The C++ standard library implementation used by GCC.
- term: template instantiation
  definition: In C++, when a template is used with specific types, the compiler generates
    a concrete version of the class or function; this process is called instantiation.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ri6a4o4jxw0.fsf@virgil.suse.cz
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Martin Jambor acknowledges a delay in response to Rohith Kapelli's proposal regarding Interprocedural Analysis (IPA) and Identical Code Folding (ICF) within GCC. The discussion highlights issues where ICF's equivalence checks miss or mishandle properties, leading to problematic merges, particularly impacting libstdc++ LTO workloads. A potential GSoC project is suggested to systematically inventory ICF's required properties, classify them, and add targeted tests, with a focus on improving merge decisions and preserving information across function merges.
