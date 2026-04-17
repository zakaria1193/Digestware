---
project: gcc
subsystem: gcc
patch_id: null
tags:
- LLM
- policy
- code generation
- testing
- optimization
discussion_id: daadecd3-4c90-4e4c-86d7-dfe92da09355@gmail.com
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Policy on use of LLM tools and bug fixes
tldr: Jeffrey Law agrees with using LLMs for generating test code and identifying
  optimization opportunities by analyzing assembly code.
stakes: This discussion explores the use of LLMs in GCC development, potentially impacting
  code quality, review processes, and developer productivity.
proposer: Jeffrey Law <jeffreyalaw@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The author expresses a positive outlook on using LLMs for specific
  tasks, but also acknowledges their limitations.
technical_tradeoffs:
- LLMs may introduce errors or inconsistencies if not carefully validated.
- Over-reliance on LLMs could reduce developers' understanding of the codebase.
- LLMs may raise copyright concerns if the generated code is not properly attributed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/daadecd3-4c90-4e4c-86d7-dfe92da09355@gmail.com
bugzilla_url: null
date: '2026-04-17'
---

Jeffrey Law agrees with the limited use of LLMs, suggesting they could be helpful for generating Python code for testing and identifying potential optimizations in assembly code. He acknowledges that LLMs can be unreliable but helpful in identifying interesting code for further investigation. He focuses more on the patch's overall sensibility, using LLMs to identify corner cases and smaller details in the review process.
