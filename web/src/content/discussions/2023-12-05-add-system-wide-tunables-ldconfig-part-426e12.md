---
project: glibc
subsystem: glibc
patch_id: null
tags:
- tunables
- configuration
- ldconfig
- performance
- security
discussion_id: 983f232f353ad400cb4f8498934e21672009fd32.1776449736.git.dj@redhat.com
source_type: public_inbox
title: '[PATCH v7 1/4] Add system-wide tunables: ldconfig part'
headline: 'Add system-wide tunables: ldconfig part'
tldr: This patch adds support for system-wide GLIBC tunables via /etc/tunables.conf,
  controlling overridability with prefixes like !, +, and -.
stakes: Allows system administrators to configure glibc behavior, potentially impacting
  performance, security, and functionality of all applications.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: stalled
sentiment_score: 5
sentiment_rationale: This is a complex feature with many potential implications, so
  a neutral score is appropriate in the absence of further discussion.
series_id: 'glibc:add system-wide tunables: ldconfig part'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/983f232f353ad400cb4f8498934e21672009fd32.1776449736.git.dj@redhat.com
bugzilla_url: null
date: '2023-12-05'
---

This patch introduces system-wide tunables for GLIBC, read from /etc/tunables.conf.  Each line defines a tunable with an optional prefix controlling overridability by the GLIBC_TUNABLES environment variable. The tunable cache format includes a filter for limiting application and stores a pre-parsed value and ID for load-time performance.
