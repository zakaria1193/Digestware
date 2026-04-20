---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- i18n
- getopt
- argp
- internationalization
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: This patch series allows `getopt` and `argp` to support translated long option
  names, enhancing internationalization.
stakes: This feature can improve the usability of programs in different languages
  by allowing option names to be displayed in the user's native language. Impacts
  internationalization efforts in glibc.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch series has been iterated on over multiple versions,
  with the author addressing concerns and incorporating feedback.
technical_tradeoffs:
- Adds complexity to `getopt` and `argp`.
- Potential for collisions in option names when translations are enabled.
- Performance impact of checking for collisions and performing translations (though
  this is likely small).
primer: The GNU C Library (`glibc`) provides the system call wrappers and other low-level
  facilities necessary for application programs. `getopt` and `argp` are functions
  used for parsing command-line options. Internationalization (i18n) is the process
  of designing software so that it can be adapted to various languages and regions
  without engineering changes. This often involves translating user-visible strings.
  The proposal aims to integrate i18n more deeply into command-line option parsing.
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

This patch series enables `getopt_long` to match translated option names, allowing the caller to set the translation context and choose the text domain for translation. It also updates the documentation for `argp` to reflect the translated names in `--help` and `--usage`. The series addresses potential collisions in `getopt_long` and excludes secure programs from using option name translations.
