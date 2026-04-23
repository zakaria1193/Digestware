---
project: gcc
subsystem: gcc
patch_id: null
tags:
- LLM
- copyright
- legal
- policy
discussion_id: CAFiYyc2jjsTetykOvkBfhm6A3RbRC+4wM5uqyMxoTXnjGxoz7w@mail.gmail.com
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Discuss using LLMs for bug fixes and potential copyright issues
tldr: Richard Biener discusses the challenges of using LLMs for code contributions,
  focusing on copyright and patent concerns.
stakes: Incorrectly applied LLM-generated code could expose the project to copyright
  or patent infringement.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- LLMs can accelerate development, but introduce legal risks.
- Manual review of LLM-generated code can mitigate risks, but increases development
  time.
exchanges:
- author: Richard Biener
  role: proposer
  position: Argues that compiled GCC code is unlikely to be a verbatim copy, but copying
    concepts could be an issue for copyright and patents.
  quote: But of course GCC code that compiles is unlikely to be a verbatim copy of
    source code that has incompatible license. So it's not about verbatim copying
    but instead copying "concepts" which then blurrs the line between derived works
    and even software patents?
primer_expert: The discussion revolves around legal implications of using LLMs in
  GCC development. It touches on copyright, derived works, and software patents, relevant
  to GCC's legal standing.
primer_general: This discussion concerns the use of Large Language Models (LLMs) like
  ChatGPT in software development, specifically within the GCC project.  LLMs are
  AI models trained on vast amounts of code and text, capable of generating code snippets,
  suggesting fixes, or even writing entire programs. The core concern is that LLMs
  might inadvertently reproduce copyrighted code or patented algorithms, leading to
  legal issues for the project.  This raises questions about due diligence and the
  potential need for new policies regarding the use of LLMs in open-source projects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc2jjsTetykOvkBfhm6A3RbRC+4wM5uqyMxoTXnjGxoz7w@mail.gmail.com
bugzilla_url: null
date: '2026-04-21'
---

Richard Biener comments on the discussion about using LLMs for bug fixes. He raises concerns about LLMs potentially copying concepts, blurring the lines between derived works and software patents.  The issue is whether using LLMs is sufficient evidence of potential copyright infringement, pending legal precedent.
