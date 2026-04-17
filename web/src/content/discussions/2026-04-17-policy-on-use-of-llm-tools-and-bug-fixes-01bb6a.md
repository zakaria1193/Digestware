---
project: gcc
subsystem: gcc
patch_id: null
tags:
- LLM
- policy
- disclosure
- copyright
- DCO
discussion_id: xnzf314hyu.fsf@greed.delorie.com
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Policy on use of LLM tools and bug fixes
tldr: DJ Delorie emphasizes the need for disclosure when using AI for code generation
  due to copyright implications.
stakes: This discussion explores the use of LLMs in GCC development, potentially impacting
  code quality, review processes, and developer productivity.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The author expresses concern about the copyright implications
  of LLM-generated code and emphasizes the need for disclosure.
technical_tradeoffs:
- Requiring disclosure may discourage developers from using LLMs for code generation.
- Failing to disclose LLM usage may lead to copyright infringement issues.
- A clear policy is needed to balance innovation with legal compliance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/xnzf314hyu.fsf@greed.delorie.com
bugzilla_url: null
date: '2026-04-17'
---

DJ Delorie highlights the importance of disclosing the use of AI in code generation due to copyright implications and the DCO's implied authorship. He clarifies that using AI for understanding, ideas, reviews, and testing is not an issue, but code-generating uses raise copyright questions. He supports disclosure even for mechanically generated patches from scripts, emphasizing caution due to GCC's visibility.
