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
tldr: This patch series enables `getopt` and `argp` to recognize translated long option
  names, updating NEWS file entries to resolve trivial conflicts.
stakes: This feature enhances internationalization (i18n) support in command-line
  utilities.  Developers working on multilingual applications may find this useful.  Incorrectly
  implemented i18n can introduce security vulnerabilities.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding translation support increases the complexity of option parsing.
- Checking for collisions in translated option names adds overhead.
- Security considerations are important when enabling translations, especially in
  secure programs.
primer: '`getopt` and `argp` are functions used for parsing command-line options.  Internationalization
  (i18n) is the process of designing and developing applications that can be adapted
  to various languages and regions without engineering changes. The NEWS file in glibc
  tracks significant changes.'
series_id: glibc:support translated long option names in getopt and argp
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/037cb6edf4422216d8666ccf4229a42abee73ce6.camel@planete-kraus.eu
bugzilla_url: null
date: '2026-04-19'
---

This patch series (v21) introduces support for translated long option names in `getopt` and `argp`. The proposer is asking if an updated version should be sent to resolve trivial conflicts in the NEWS file. The core functionality of the patch series still applies and the tests still pass.
