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
discussion_id: CACbdTspmnH_YtCy=OVpT35rRd6PX3CkWcMN_+8H0KkHR5pBeFw@mail.gmail.com
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction discussion.'
tldr: Follow-up on a GSoC project discussion regarding IPA-ICF, with a ping and reference
  to an open PR for a related issue.
proposer: Kapelli Rohith <kapellirohith@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Kapelli Rohith
  role: proposer
  position: Pings for a response on the GSoC project direction and highlights a related
    issue with a submitted patch.
  quote: 'Ping.


    On Sun, 20 Sep 2026 at 8:54 PM Rohith Kapelli <kapellirohith@gmail.com>

    wrote:


    > Hi Richard,

    >

    > Thanks, that makes sense. I''ll continue looking into the cgraph/IPA body

    > handling and the separate-body direction while working out the scope.'
primer_expert: This thread concerns the direction of a GSoC project focused on compiler
  optimizations, specifically within GCC's Interprocedural Analysis (IPA) framework
  and its interaction with Interprocedural Constant Folding (ICF). The discussion
  touches on how function bodies are handled in the cgraph pass and a specific bug
  (PR127509) where alias declarations might bypass IPA optimizations intended for
  direct calls.
primer_glossary:
- term: IPA
  definition: Interprocedural Analysis. Compiler analysis that examines relationships
    between different functions in a program, rather than analyzing each function
    in isolation. This allows for more global optimizations.
- term: ICF
  definition: Interprocedural Constant Folding. A compiler optimization technique
    where constant expressions are evaluated during interprocedural analysis, potentially
    simplifying code across function calls.
- term: GSoC
  definition: Google Summer of Code. A global program where Google funds open-source
    contributions by students during the summer.
- term: cgraph
  definition: A GCC internal representation or pass related to call graphs, used for
    interprocedural analysis and optimization.
- term: PR
  definition: Problem Report. A bug report filed in a project's issue tracking system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CACbdTspmnH_YtCy=OVpT35rRd6PX3CkWcMN_+8H0KkHR5pBeFw@mail.gmail.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This message is a follow-up ping on a previous discussion about a Google Summer of Code (GSoS) project related to Interprocedural Analysis (IPA) and Inter-procedural Constant Folding (ICF). The author refers to earlier comments about cgraph/IPA body handling and a separate-body direction, and also highlights a related issue (PR127509) concerning optimizations for calls through aliases of noipa functions, for which a patch has been submitted.
