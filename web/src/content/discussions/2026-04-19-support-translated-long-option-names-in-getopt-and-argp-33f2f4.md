---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- getopt
- argp
- i18n
- translation
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: Asks if a new version of the patch series is needed due to NEWS file conflicts,
  but confirms the series still applies and tests pass.
stakes: This feature enhances internationalization (i18n) support, enabling command-line
  tools to display option names in the user's preferred language.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased code complexity to handle translations.
- Potential for collisions between translated option names.
- Requires additional infrastructure for managing translations.
exchanges:
- author: Vivien Kraus <vivien@planete-kraus.eu>
  role: proposer
  position: Asks if a new version is needed due to NEWS conflicts, but confirms the
    patch series still applies and tests pass.
  quote: 'As new features are added to the glibc, some trivial conflicts happen

    in the NEWS file.  Should I send an updated version ?


    Outside of this, the patch series still applies, and the tests still

    pass.'
primer_expert: This patch series adds the ability to translate long option names in
  `getopt` and `argp`. It introduces mechanisms for specifying translations for option
  names, allowing command-line tools to present options in different languages. The
  core issue revolves around how translations are loaded and applied during option
  parsing, and how to handle potential collisions between translated option names.
primer_general: '`getopt` and `argp` are standard C library functions used for parsing
  command-line options. This patch series extends these functions to support translated
  option names, improving internationalization (i18n). Libraries like glibc often
  have a `NEWS` file to document new features to end users; here, the patch has changes
  to that file, and the author is checking if those changes need to be re-aligned
  with the current state of `glibc`''s main development branch.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

The author inquires whether an updated version of the patch series is required due to conflicts in the NEWS file. The author also confirms that the patch series still applies cleanly and that all tests continue to pass successfully.
