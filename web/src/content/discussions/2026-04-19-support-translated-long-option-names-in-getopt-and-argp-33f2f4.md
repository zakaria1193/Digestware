---
project: glibc
subsystem: glibc
patch_id: null
tags:
- getopt
- argp
- i18n
- internationalization
- translation
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: This patch series adds support for translated long option names in getopt and
  argp, with minor conflicts in the NEWS file.
stakes: This feature enhances internationalization, allowing programs to present command-line
  options in the user's native language.  It could introduce complications in option
  parsing and collision detection.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The author indicates that the patches still apply and tests pass,
  suggesting a positive outlook, despite minor conflicts.
technical_tradeoffs:
- Adds complexity to option parsing logic.
- Requires careful handling of option name collisions, especially with translated
  names.
- Introduces new APIs for setting the translation context and textdomain.
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

This patch series introduces support for translated long option names in `getopt` and `argp`. The author notes minor conflicts in the NEWS file due to recent glibc updates.  The core functionality remains applicable and the tests pass. The series allows translating option names, setting a translation context, and choosing a textdomain. It also includes collision checks and a validation script.
