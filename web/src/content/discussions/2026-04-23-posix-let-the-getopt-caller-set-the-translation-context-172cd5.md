---
project: glibc
subsystem: posix
patch_id: null
tags:
- i18n
- getopt_long
- translation context
- internationalization
discussion_id: 081a71d7a620b3f704bab0c0705ae02f3c582d9f.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 2/9] posix: let the getopt caller set the translation context'
headline: 'posix: let the getopt caller set the translation context'
tldr: Enables the getopt caller to set the translation context for option names, disambiguating
  translations in different program parts.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds a new global variable (or reentrant state field), increasing complexity.
- Requires the caller to manage the translation context.
- Uses a custom function for combining context and option name due to the unavailability
  of `pgettext_expr`.
exchanges: []
primer_expert: The patch modifies `posix/getopt.c` and related files to allow the
  `getopt` caller to set the translation context, using a new `optctxt` variable.
  The patch uses a custom function to combine the context and the long option name,
  since `pgettext_expr` is not yet available.
primer_general: '`getopt_long` parses command-line options, and this patch enhances
  its internationalization (i18n) capabilities.  A translation context allows the
  same word to be translated differently depending on its meaning. By allowing the
  caller to set the translation context, option names can be translated differently
  in different parts of the program, improving accuracy and user experience.'
series_id: 'glibc:posix: let the getopt caller set the translation context'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/081a71d7a620b3f704bab0c0705ae02f3c582d9f.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch allows the caller of `getopt_long` to set the translation context for option names. This is useful because option names can have different translations depending on the context in the program.  The patch introduces a new global variable (or reentrant state field) `optctxt` that can be set by the caller.  If `optctxt` is NULL, no translated option names will be recognized.
