---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- getopt
- argp
- i18n
- internationalization
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: The patch series adds support for translated long option names in `getopt` and
  `argp`, with minor NEWS file conflicts needing resolution.
stakes: Enhances internationalization (i18n) support.  Developers creating command-line
  tools should care if they want to provide localized option names to users.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to `getopt` and `argp` implementations.
- Requires managing translations and potential collisions between translated option
  names.
- Enhances user experience for non-English speakers.
exchanges:
- author: Vivien Kraus <vivien@planete-kraus.eu>
  role: proposer
  position: Provides an update on the patch series, mentioning minor NEWS file conflicts
    and confirming that the core functionality still works.
  quote: As new features are added to the glibc, some trivial conflicts happen in
    the NEWS file.  Should I send an updated version ?
primer_expert: This series touches `getopt_long` and `argp`, which parse command-line
  arguments. The core change involves enabling the matching of translated option names,
  which necessitates checks for collisions and considerations for secure programs
  where translations might be undesirable. The NEWS file documents user-visible changes.
primer_general: '`getopt` and `argp` are functions in glibc that help programs process
  command-line options given by the user. This patch series extends these functions
  to support displaying option names in different languages. This is useful for making
  programs more accessible to users who don''t speak English. The discussion indicates
  that the patches are mostly ready, with minor issues needing to be addressed.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

This is a status update on a patch series that aims to add support for translated long option names in `getopt` and `argp`. The author notes minor conflicts in the NEWS file due to new features being added to glibc. The core functionality of the patch series remains intact and tests continue to pass.
