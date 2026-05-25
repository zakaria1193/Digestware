---
project: gcc
subsystem: gcc
patch_id: null
tags:
- patch review
- coding style
- commit message
- wiki
discussion_id: CALvbMcBPnQzpmkhA+Cc34grLxvFbhhEwnhpdFfuyfYZHt6oy3A@mail.gmail.com
source_type: public_inbox
title: 'Re: Starting patch review wiki'
headline: Starting patch review wiki
tldr: Andrew Pinski added recommendations to the patch review wiki for new developers
  to use tools for commit message and coding style correctness.
proposer: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Suggests using tools that may have false positives, requiring developers to understand
  and ignore irrelevant warnings.
- Adds an extra step to the development process, which may slow down contributions
  if the tools are cumbersome to use.
exchanges:
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: proposer
  position: Added recommendations to the patch review wiki for new developers to use
    tools for commit message and coding style correctness, especially for email patch
    reviews.
  quote: I added some recommendations on what to recommend for new developers to run
    to get either the commit message correct and/or coding style correct.
primer_expert: The patch review wiki helps new reviewers to get started. The recommendations
  suggest using tools to ensure commit messages and coding styles are correct. The
  ``./contrib/check_GNU_style.py`` script is mentioned as needing improvements.
primer_general: The patch review process ensures code changes are high quality and
  maintainable. This discussion highlights tools to help developers format their code
  and commit messages correctly before submitting them for review. Consistent style
  and clear messages improve code readability and make collaboration easier, and this
  reduces the workload of reviewers and maintainers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CALvbMcBPnQzpmkhA+Cc34grLxvFbhhEwnhpdFfuyfYZHt6oy3A@mail.gmail.com
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

Andrew Pinski added recommendations to the patch review wiki for new developers. These recommendations suggest using tools to ensure commit messages and coding styles are correct, especially for email patch reviews. The wiki also notes that ``./contrib/check_GNU_style.py`` needs improvements, since it flags errors incorrectly in some cases.
