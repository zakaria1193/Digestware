---
project: glibc
subsystem: glibc
patch_id: null
tags:
- tunables
- filters
- security
- configuration
- application-specific
discussion_id: fd9039a2989834a76986db9d59b8b3e5fe81f595.1776449736.git.dj@redhat.com
source_type: public_inbox
title: '[PATCH v7 4/4] Add system-wide tunables: Filters'
headline: 'Add system-wide tunables: Filters'
tldr: Adds filters to system-wide tunables based on process name and security status
  (AT_SECURE), limiting tunable application to matching processes.
stakes: Enables fine-grained control over tunable application, improving security
  and allowing for application-specific configurations.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: stalled
sentiment_score: 5
sentiment_rationale: This is a complex security-related feature, so a neutral score
  is appropriate in the absence of further discussion.
technical_tradeoffs:
- Enables fine-grained control but increases configuration complexity.
- Filtering based on process name might not be reliable in all cases.
- Adds overhead to tunable application due to filter evaluation.
series_id: 'glibc:add system-wide tunables: filters'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/fd9039a2989834a76986db9d59b8b3e5fe81f595.1776449736.git.dj@redhat.com
bugzilla_url: null
date: '2026-02-11'
---

This patch adds support for filtering tunables based on the process executable path (matching /proc/self/exe or argv[0]) and the AT_SECURE flag.  Tunables defined after a filter line apply only to matching processes. Filters can match either the full path or the basename.  Support for filtering based on the presence or absence of AT_SECURE is also added.
