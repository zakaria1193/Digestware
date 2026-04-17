---
project: gcc
subsystem: gcc
patch_id: null
tags:
- LLM
- policy
- disclosure
- OpenJDK
- code review
discussion_id: 87zf314j5s.fsf@gnu.org
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Policy on use of LLM tools and bug fixes
tldr: Jose Marchesi supports the OpenJDK policy on AI, stressing the need for serious
  disclosure and careful handling of LLM-generated patches.
stakes: This discussion explores the use of LLMs in GCC development, potentially impacting
  code quality, review processes, and developer productivity.
proposer: Jose E. Marchesi <jemarch@gnu.org>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The author supports a clear and strict policy on LLM use, emphasizing
  the importance of disclosure and careful review.
technical_tradeoffs:
- A strict disclosure policy may deter developers from experimenting with LLMs.
- Without clear guidelines, LLM-generated code may bypass proper review processes.
- Balancing innovation with quality control is essential for successful LLM integration.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/87zf314j5s.fsf@gnu.org
bugzilla_url: null
date: '2026-04-17'
---

Jose Marchesi agrees with the OpenJDK policy on AI use and emphasizes that disclosure should be taken very seriously. He believes that statistically generated patches should not be reviewed in the same way as human-written ones. He also suggests adding a statement to the policy that compliance does not guarantee acceptance of LLM-generated code, reinforcing the need for thorough review.
