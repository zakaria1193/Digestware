---
project: glibc
subsystem: glibc
patch_id: null
tags:
- i18n
- getopt
- argp
- internationalization
- translations
discussion_id: cover.1776957777.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: Adds support for translated long option names in `getopt` and `argp`, improving
  i18n capabilities in glibc.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch series modifies `posix/getopt.c`, `argp/argp-help.c`, and
  related files to add support for translated long option names. The series introduces
  new functions and variables to manage translation contexts and textdomains. There's
  a new `libc.abilist`, so the series is updated.
primer_general: '`getopt` and `argp` are glibc libraries for parsing command-line
  options. This patch series enhances their internationalization (i18n) capabilities
  by adding support for translated long option names. This allows programs to be used
  more easily in different languages, improving the user experience for non-English
  speakers.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/cover.1776957777.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch series enables support for translated long option names in both `getopt` and `argp`. This allows programs to be more easily internationalized, as users can use translated option names in their native language. The series includes changes to `getopt` to recognize translated option names, as well as changes to `argp` to display translated names in help messages.
