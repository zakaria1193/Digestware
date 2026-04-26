---
project: glibc
subsystem: posix
patch_id: null
tags:
- i18n
- getopt_long
- textdomain
- internationalization
discussion_id: f5ce925d786638e616ef665c5f49980958675283.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 4/9] posix: let the getopt caller choose the textdomain for translation'
headline: 'posix: let the getopt caller choose the textdomain for translation'
tldr: Allows the caller of `getopt` to specify the textdomain for option name translations,
  providing more i18n flexibility.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the `getopt_long` API.
- Requires the caller to manage the `opttextdomain` variable.
- All options in a single `getopt_long` call must use the same textdomain.
exchanges: []
primer_expert: The patch modifies `posix/getopt.c` and related files to allow the
  `getopt` caller to specify the textdomain for translations, using a new `opttextdomain`
  variable. All options in the call to `getopt_long` are looked up in the same domain.
  This approach mirrors the existing mechanism for setting the translation context.
primer_general: '`getopt_long` parses command-line options and can translate option
  names for i18n. A textdomain specifies the set of translations to use. This patch
  enables applications to control the textdomain used for option name translations,
  providing more flexibility in managing translations across different parts of an
  application.'
series_id: 'glibc:posix: let the getopt caller choose the textdomain for translation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f5ce925d786638e616ef665c5f49980958675283.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch introduces a mechanism for the caller of `getopt_long` to specify the textdomain used for option name translations. This provides more flexibility for internationalization, allowing applications to use different textdomains for different parts of the program.  A new `opttextdomain` variable is defined, and the caller can set it using `getopt_long_enable_translations`.
