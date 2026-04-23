---
project: gcc
subsystem: gcc
patch_id: null
tags:
- LLM
- legal
- copyright
- patent
- licensing
discussion_id: CAFiYyc2jjsTetykOvkBfhm6A3RbRC+4wM5uqyMxoTXnjGxoz7w@mail.gmail.com
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: GCC ponders LLM-assisted code contributions and copyright.
tldr: Richard Biener discusses the blurry line between derived works and software
  patents when using LLMs for GCC contributions.
stakes: Legal risks around copyright and patent infringement could affect GCC's licensing
  and distribution.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- LLMs may increase developer productivity but introduce legal risks.
- Manual code review can mitigate legal risks but is time-consuming.
- The legal implications of LLM-generated code are uncertain and may require legal
  interpretation.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Poses the question of whether using LLMs could lead to copyright or software
    patent issues due to the copying of "concepts."
  quote: But of course GCC code that compiles is unlikely to be a verbatim copy of
    source code that has incompatible license.  So it's not about verbatim copying
    but instead copying "concepts" which then blurrs the line between derived works
    and even software patents?
primer_expert: This thread concerns legal risks of using LLMs to generate or assist
  in writing GCC code. Specifically, the discussion questions whether using LLMs introduces
  new risks of copyright infringement or patent violations, beyond those already present
  with human-authored code. The core issue is whether an LLM can be said to copy "concepts"
  from existing code, and whether that constitutes a violation of copyright or patent
  law. The discussion does not focus on specific files or passes.
primer_general: This discussion revolves around the legal implications of using AI-powered
  coding assistants (LLMs) in the development of GCC, the GNU Compiler Collection.
  Copyright law protects the expression of ideas, while patent law protects inventions.
  The legal question is whether LLMs, in generating code, might inadvertently copy
  copyrighted code or implement patented inventions without permission.  The fear
  is that using LLMs could expose the GCC project to legal challenges if the generated
  code infringes on existing copyrights or patents.  This could affect the project's
  ability to distribute and license the software freely.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc2jjsTetykOvkBfhm6A3RbRC+4wM5uqyMxoTXnjGxoz7w@mail.gmail.com
bugzilla_url: null
date: '2026-04-21'
---

Richard Biener responds to a discussion about the use of LLMs in GCC contributions, focusing on copyright and software patent concerns. He argues that compiled GCC code is unlikely to be a verbatim copy of copyrighted source code. The discussion pivots to the risk of copying "concepts," blurring the line between derived works and software patents.
