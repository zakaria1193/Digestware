---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- internationalization
- getopt
- argp
- i18n
discussion_id: 037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
source_type: public_inbox
title: 'Re: [PATCH v21 0/9] Support translated long option names in getopt and argp'
headline: Support translated long option names in getopt and argp
tldr: This patch series allows programs to use translated long option names in `getopt`
  and `argp`, enabling internationalization of command-line interfaces.
stakes: Improves internationalization support in glibc, allowing command-line tools
  to be more easily translated into different languages.  This can improve the user
  experience for non-English speakers.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to `getopt` and `argp`.
- Requires checks for collisions between translated option names.
- Introduces security considerations related to translated option names in secure
  programs.
- May require updates to build systems and translation workflows.
primer_expert: '`getopt` and `argp` are glibc functions that parse command-line options.
  This series lets programs define translated aliases for long options. This requires
  careful handling of collisions and security considerations (`__libc_enable_secure`).'
primer_general: '`getopt` and `argp` are standard C library functions for parsing
  command-line options passed to programs. They handle options like `-h` or `--help`.
  This series extends these functions to allow option names to be translated into
  different languages, so a program can understand `--ayuda` as the Spanish equivalent
  of `--help` if the program is running in a Spanish locale.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

This patch series (now at v21) adds support for translated long option names to the `getopt` and `argp` functions in glibc.  The goal is to allow command-line tools to be more easily translated into different languages. The author is checking in to see if a trivial conflict in the NEWS file needs to be resolved before the series can move forward.
