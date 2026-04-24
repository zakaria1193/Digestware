---
project: gcc
subsystem: gcc
patch_id: null
tags:
- forge
- pull request
- archival
- mailing list
discussion_id: c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
source_type: public_inbox
title: 'Archival of forge discussions: rollout status'
headline: Forge PR archival is mostly complete
tldr: The rollout of pull request archival from the GCC forge to the gcc-patches mailing
  list is mostly complete, with some issues.
proposer: Claudio Bantaloukas <claudio.bantaloukas@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This status report details the archival of closed pull requests from
  the GCC's Forge instance to the gcc-patches mailing list.  The goal is to preserve
  these discussions. Issues include missing descriptions, incorrect timestamps, and
  email delivery problems related to DKIM signatures.
primer_general: This is a report about archiving discussions related to code changes
  in the GCC project. The discussions, which take place on a platform called "forge,"
  are being copied to a mailing list for long-term storage. This ensures that important
  decisions and reasoning behind code changes are not lost. There were some technical
  issues encountered during the process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/c3f1c579-5408-4936-ba45-cacd1d9bb31b@arm.com
bugzilla_url: null
date: '2026-04-23'
---

Claudio Bantaloukas reports on the status of the rollout of pull request archival from the GCC forge to the gcc-patches mailing list. Most closed PRs have been sent, but several issues remain, including PRs lacking descriptions or commits, patches related to libstdc++ not being sent to the appropriate list, incorrect timestamps on some emails, and email delivery issues due to lack of DKIM signatures.
