---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- forge
- archival
- pull request
discussion_id: c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
source_type: public_inbox
title: 'Archival of forge discussions: rollout status'
headline: Forge Discussions Archival Rollout Status
tldr: The rollout of pull request archival to the gcc-patches mailing list is mostly
  complete, with some issues around missing descriptions and DKIM signatures.
proposer: Claudio Bantaloukas <claudio.bantaloukas@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The GCC forge is a web-based platform for collaborative software development.  Archiving
  pull requests to the mailing list provides a long-term record of discussions and
  decisions.
primer_general: The GCC project uses a forge, which is a web-based tool, to manage
  contributions.  To keep a historical record, closed pull requests (a request to
  merge code) are being archived to the gcc-patches mailing list. This email discusses
  the status of that archival process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
bugzilla_url: null
date: '2026-04-23'
---

Claudio Bantaloukas reports on the status of the rollout for archiving closed pull requests from the GCC forge to the gcc-patches mailing list. The bot did not send PRs that had been opened, but no one engaged with. Issues remain around PRs lacking descriptions, commits, and DKIM signatures, as well as patches related to libstdc++ all going to the gcc-patches mailing list.
