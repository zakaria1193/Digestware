---
project: glibc
subsystem: misc
patch_id: null
tags:
- build
- makefile
- lint
discussion_id: aeXhrdc8BxCy0vsH@arm.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] misc: fix lint-makefiles failures'
headline: 'Misc: Fix lint-makefiles failures'
tldr: This patch addresses lint-makefile failures in the glibc build process.
stakes: Ensuring clean builds and consistent Makefiles is important for maintainability
  and avoiding unexpected build failures.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The discussion is focused on resolving a specific issue with
  clear feedback.
technical_tradeoffs:
- Potential for subtle build regressions if Makefile changes are not carefully reviewed.
- Balancing code style improvements with the need to maintain compatibility and avoid
  unexpected behavior.
series_id: 'glibc:misc: fix lint-makefiles failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXhrdc8BxCy0vsH@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes issues reported by lint-makefiles in the glibc build system. A developer questioned a change from '=' to '+=' in a Makefile assignment, and the author plans to double-check and possibly revert it to avoid introducing unintended side effects. The author will address other minor issues as well.
