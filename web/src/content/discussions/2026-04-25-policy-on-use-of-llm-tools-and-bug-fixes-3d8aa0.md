---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- llm
- ai
- policy
- code review
discussion_id: 45953524-39c8-4046-a805-698e3c8b243e@netcologne.de
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Policy on use of LLM tools and bug fixes
tldr: The discussion continues on the policy for using LLMs in GCC development, focusing
  on appropriate use cases and code review processes.
proposer: Richard Biener
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Using LLMs may increase development speed but introduces risks to code quality and
  maintainability.
- Including prompts in commits may aid code review but can clutter the commit history.
- Limiting LLM use to local changes may reduce risks but restrict potential benefits.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Suggests LLMs could be used for completing partial transitions but not
    for new compiler features.
  quote: I still hope for sensible use of LLMs for GCC, like finishing long neglected
    partial transitions.  I do not think LLMs are ready to implement new compiler
    features.
- author: Eric Botcazou <ebotcazou@libertysurf.fr>
  role: other
  position: Agrees on limiting LLM use to local changes.
  quote: "Yes, that seems to be a safe and sensible middle ground, in other words\
    \ to \nlimit changes to the local \"scope\" so that any mistakes made are also\
    \ local."
- author: Thomas Koenig <tkoenig@netcologne.de>
  role: other
  position: Argues patches with LLM-generated code need special attention from reviewers
    and suggests including the prompts used to generate the code in commits
  quote: 'I think that patches which contain LLM-generated code need to receive

    special care from *reviewers*, as well (to be formalized how?)'
- author: Giacomo Tesio <giacomo@tesio.it>
  role: other
  position: Reports their company's policy of including prompts in commits containing
    LLM output to aid reviewers.
  quote: 'To this aim, our corporate policy mandates inclusion of prompts in

    commits containing LLM output (together with tool name and version).


    Over time, this helped a lot developers here to build an effective

    insight about the issues that might pass unnoticed.'
- author: Thomas Koenig <tkoenig@netcologne.de>
  role: other
  position: Expresses concern about cluttering commits and the relevance of prompts
    in the long run.
  quote: 'That may be a good thing, or not.  Cluttering up commits is one concern

    that I have. Also, for r'
- author: Eric Botcazou <ebotcazou@libertysurf.fr>
  role: other
  position: Argues that prompts should not replace detailed descriptions of the changes
    in the commit log.
  quote: "That certainly should not preempt the need to provide a description, detailed\
    \ \nfor complex changes if need be, of the change in the commit log, written for\
    \ \nhuman beings, instead of only a prompt jargon that will become obsolete in\
    \ a \nfew months."
primer_expert: The GCC project is discussing a formal policy on the use of Large Language
  Models (LLMs) in development. The discussion involves concerns about code quality,
  maintainability, and code review processes for LLM-generated code. This is a follow-up
  to the creation of the AI Policy Working Group.
primer_general: GCC is the GNU Compiler Collection, a set of tools used to compile
  source code. The increasing use of AI-powered tools (specifically Large Language
  Models) in software development raises questions about code quality and maintainability.
  The GCC community is discussing a policy to address these concerns, focusing on
  appropriate use cases for LLMs and the code review process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/7D76F825-E65A-4218-9CFF-27CDE39211DF@gmail.com
bugzilla_url: null
date: '2026-04-25'
---

The discussion continues regarding a policy for using LLM tools for bug fixes in GCC. Richard Biener suggests that LLMs may be useful for finishing neglected transitions, but are not ready to implement new compiler features. Eric Botcazou agrees, suggesting limiting changes to the local scope. Giacomo Tesio mentions their corporate policy of including prompts in commits containing LLM output to aid code review.
