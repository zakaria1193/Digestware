---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- gpl
- ai
- copyright
- licensing
discussion_id: c26266a301c0ce507690aeb36095118970360a95.camel@starynkevitch.net
source_type: public_inbox
title: 'Re: GCC AI Policy Announcement'
headline: GCC AI Policy Announcement
tldr: Developer questions the definition and implications of AI-assisted code for
  GPL-licensed software.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Determining the legal status of AI-generated code under copyright law.
- Balancing the desire to incorporate AI advancements with the obligations of open-source
  licenses.
- Defining clear contribution guidelines for AI-assisted code.
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Questions the definition of AI-assisted code and its implications for
    copyright and the GPL, noting that AI funding is common for GCC development.
  quote: 'What happens if a patch contains a non-trival amount of code that cannot
    be copyrighted because it was assisted by AI?


    Are software projects like refpersys.org (source code below) considered

    as "AI"?


    Are code generators like https://carburetta.com/ considered as AI (they

    do use some clever AI techniques, and could be extended to use even

    better one).


    In some countries (including mine, France)…'
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: reviewer
  position: Acknowledges the question and its relation to a previous announcement
    but does not provide an answer in the snippet.
  quote: null
- author: Sam James <sam@gentoo.org>
  role: other
  position: Acknowledges the question and its relation to a previous announcement
    but does not provide an answer in the snippet.
  quote: null
primer_expert: This thread discusses the implications of AI-generated code on the
  GPL license as applied to GCC. The core issue is how to handle contributions where
  the authorship is partially or wholly machine-generated, and whether such code affects
  the GPL's copyright and distribution terms.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/c26266a301c0ce507690aeb36095118970360a95.camel@starynkevitch.net
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

Basile Starynkevitch raises concerns about the policy on AI-assisted code in GCC, questioning what constitutes AI and how it impacts the GPL. He notes that much GCC code is funded through AI-related calls and asks for clarification on how to handle AI-assisted contributions, referencing past involvement with AI-inspired techniques in GCC.
