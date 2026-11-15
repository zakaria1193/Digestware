---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler
- intermediate representation
- plugin
- SSA
discussion_id: 5b16063082b16c2e4c3e2e52bec5485f636177d4.camel@starynkevitch.net
source_type: public_inbox
title: How to dump data from intermediate stages of gcc compilation?
headline: How to dump data from intermediate stages of gcc compilation?
tldr: Developer seeks to inspect GCC's intermediate representation before RTL generation
  for custom CPU targeting.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Using GCC plugins requires understanding GCC's internal APIs, which can change between
  releases.
- Accessing SSA directly provides more high-level information than RTL but requires
  understanding SSA transformations.
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Suggests using GCC plugins and the SSA representation to dump intermediate
    compilation data before RTL generation. Recommends looking into CompCert for further
    insights.
  quote: Practically, I would recommend first writing a GCC plugin ... Your plugin
    would work on the SSA representation.
primer_expert: This query concerns accessing GCC's internal representation, specifically
  the high-level SSA (Static Single Assignment) form before it's lowered to RTL (Register
  Transfer Language). The user wants to inspect this data, likely for a new backend
  or analysis, and is asking for methods beyond RTL dumping.
primer_glossary:
- term: GCC plugin
  definition: A dynamically loadable module that can hook into GCC's compilation process
    to add new passes, diagnostics, or inspect internal representations.
- term: SSA representation
  definition: Static Single Assignment form is an intermediate representation used
    in compilers where every variable is assigned exactly once. It simplifies many
    optimizations and analyses.
- term: RTL
  definition: Register Transfer Language is an intermediate representation in GCC
    that is closer to machine code than SSA, describing operations on registers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/5b16063082b16c2e4c3e2e52bec5485f636177d4.camel@starynkevitch.net
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

Basile Starynkevitch suggests using GCC plugins to access the SSA representation before RTL generation. This approach is intended to help a developer modify GCC to target a custom CPU by allowing inspection and potential dumping of the intermediate compilation stages. The advice points towards GCC plugins and the SSA representation as the primary means to achieve this.
