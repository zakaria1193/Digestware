---
project: glibc
subsystem: misc
patch_id: null
tags:
- build system
- makefile
- lint
- maintenance
discussion_id: xnwly54br7.fsf@greed.delorie.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] misc: fix lint-makefiles failures'
headline: 'misc: Fix lint-makefiles failures'
tldr: A patch fixes lint-makefiles failures by reordering entries and changing an
  assignment operator. One change is questioned.
stakes: Ensures build system consistency and avoids potential build errors. The '='
  to '+=' change in malloc/Makefile could have unintended consequences.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The patch is mostly approved, but one change is flagged for further
  review, indicating a neutral but cautious sentiment.
technical_tradeoffs:
- Reordering entries improves readability and consistency.
- Modifying assignment operators can have unintended consequences if not carefully
  reviewed.
- Adding comments clarifies the purpose and structure of the Makefile.
series_id: 'glibc:misc: fix lint-makefiles failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/xnwly54br7.fsf@greed.delorie.com
bugzilla_url: null
date: '2026-04-17'
---

This patch addresses lint-makefiles failures by reordering entries and adding comments. One change converts an assignment operator '=' to '+=', which is questioned, as it modifies a macro defined in both aarch64/ and generic/ Makefiles.
