---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- mirror
- release management
discussion_id: 521a2453-2497-426b-19ba-7c5a55650189@pfeifer.com
source_type: public_inbox
title: 'Re: US mirror sites missing newer versions'
headline: US mirror sites missing newer versions
tldr: GCC release 14.2.0 not available on US mirror, site dropped.
proposer: Gerald Pfeifer <gerald@pfeifer.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Gerald Pfeifer <gerald@pfeifer.com>
  role: proposer
  position: Dropped a mirror site that was not syncing releases since February 2023.
  quote: "This one I dropped after giving it a bit more time:\n  commit a81295a4b193da909614074ac6978edbd7ebdad5\n\
    \    mirrors: Drop mirrors.concertpass.com\n    It has not synced our snapshots\
    \ and releases since February 2023."
primer_expert: This discussion concerns the management of GCC mirror sites. The proposer,
  Gerald Pfeifer, removed mirrors.concertpass.com because it failed to sync new releases,
  specifically GCC 14.2.0, rendering it unreliable for users seeking the latest versions.
  This is a routine maintenance task for core project infrastructure.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/521a2453-2497-426b-19ba-7c5a55650189@pfeifer.com
bugzilla_url: null
date: '2026-08-22'
is_stub: false
stub_reason: ''
---

A user reported that GCC release 14.2.0 was not available on a US mirror site. Gerald Pfeifer confirmed that the problematic mirror, mirrors.concertpass.com, was dropped due to not syncing releases since February 2023. He thanked the reporter for the feedback and encouraged further reports.
