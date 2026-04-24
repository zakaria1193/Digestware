---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- forge
- archival
- pull request
- mailing list
discussion_id: c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
source_type: public_inbox
title: 'Archival of forge discussions: rollout status'
headline: Report Status on Forge Discussion Archival Rollout
tldr: Claudio Bantaloukas reports on the status of the rollout for the archival of
  closed pull requests from the GCC forge to the gcc-patches mailing list.
proposer: Claudio Bantaloukas <claudio.bantaloukas@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The GCC forge is a web-based platform for collaborative development.
  Archival involves moving older pull requests to the gcc-patches mailing list for
  long-term storage and reference. This process ensures that discussions and code
  changes are preserved even after a pull request is closed.
primer_general: The GCC project uses a web-based platform, often referred to as a
  forge, for developers to collaborate on code changes.  Pull requests are a way for
  developers to propose changes to the main codebase.  To keep the forge organized,
  closed pull requests are being archived to the gcc-patches mailing list, ensuring
  that valuable discussions and code changes are not lost. This report details the
  progress and any issues encountered during this archival process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
bugzilla_url: null
date: '2026-04-23'
---

Claudio Bantaloukas reports on the rollout status for the archival of closed pull requests from the GCC forge to the gcc-patches mailing list.  The archival has been mostly completed, but there are issues with emails lacking descriptions or commits, and with DKIM signatures, which is causing some emails to be blocked. Mark is throttling outgoing emails to mitigate the DKIM issue.
