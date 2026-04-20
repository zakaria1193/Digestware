---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- getopt
- argp
- internationalization
- translations
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: The author asks if an updated version of the patch series is needed, due to
  minor NEWS file conflicts.
stakes: This series allows applications to support translated long option names in
  `getopt` and `argp`, improving internationalization.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The author is actively maintaining the patch series, but the
  status is unclear pending feedback on the NEWS conflict.
technical_tradeoffs:
- Requires modifications to `getopt` and `argp` to handle translated option names.
- May introduce potential conflicts if translations are not carefully managed.
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

Vivien Kraus inquires about submitting an updated version of their patch series, version 21, which supports translated long option names in `getopt` and `argp`. The series still applies cleanly and the tests pass, but there are minor conflicts in the NEWS file due to new glibc features. The core functionality remains unchanged.
