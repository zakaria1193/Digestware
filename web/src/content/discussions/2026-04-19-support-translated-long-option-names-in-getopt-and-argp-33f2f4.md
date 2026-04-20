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
tldr: A patch series supporting translated long option names in `getopt` and `argp`
  is still applicable despite minor conflicts in the NEWS file.
stakes: Improves internationalization (i18n) support for command-line tools by allowing
  translated option names.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in argument parsing.
- Potential for collisions between translated option names.
- Security considerations when translations are enabled in secure programs.
primer_expert: This series modifies `getopt` and `argp` to support translated long
  option names, enabling i18n of command-line interfaces. Patches touch `posix/getopt.c`,
  `argp/argp-parse.c`, and related headers. Key considerations include collision detection
  for translated option names within `getopt_long` and preventing translations in
  secure contexts (`__libc_enable_secure`). The goal is to allow users to specify
  long options in their native language.
primer_general: '`getopt` and `argp` are functions in glibc that help programs parse
  command-line arguments.  Long options are arguments that start with two hyphens
  (e.g., `--help`).  Internationalization (i18n) is the process of adapting software
  to different languages and regions.  This patch series aims to improve i18n support
  by allowing programs to translate long option names into different languages, so
  users can use command-line options in their native language. This involves changes
  to argument parsing and help message generation.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

Vivien Kraus confirms that a patch series supporting translated long option names in `getopt` and `argp` remains applicable despite trivial conflicts in the NEWS file. The series allows `getopt_long` to match translated option names, lets the caller set the translation context and textdomain, documents translated names in `--help` and `--usage`, and checks for collisions in `getopt_long`.
