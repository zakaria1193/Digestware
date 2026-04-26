---
project: glibc
subsystem: posix
patch_id: null
tags:
- i18n
- getopt_long
- internationalization
- translations
discussion_id: 54fc5096228e57b86e75f5e2fb8e322d5254d431.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 1/9] posix: allow getopt_long to match translated option names'
headline: 'posix: allow getopt_long to match translated option names'
tldr: Extends `getopt_long` to recognize translated long option names, simplifying
  i18n for applications.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the `getopt_long` implementation.
- May introduce performance overhead due to the additional translation matching step.
- Abbreviations will only match the untranslated names.
exchanges: []
primer_expert: The patch modifies `posix/getopt.c` and related files to allow `getopt_long`
  to match translated option names.  A new argument, a translation function pointer,
  is added to `_getopt_internal{_r}`. This allows the function to try matching against
  translated option names if the untranslated names are not found.
primer_general: '`getopt_long` is a standard C library function for parsing command-line
  options. This patch adds the ability for `getopt_long` to recognize translated option
  names, enabling programs to support internationalization (i18n) more easily.  This
  means users can use translated option names in their native language, making the
  program more accessible.'
series_id: 'glibc:posix: allow getopt_long to match translated option names'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/54fc5096228e57b86e75f5e2fb8e322d5254d431.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch modifies `getopt_long` to recognize translated long option names.  Without this change, applications must duplicate option names in the `struct options` array to support translations. This patch simplifies internationalization by allowing `getopt_long` to automatically match translated option names.  The patch adds a translation function pointer to `_getopt_internal{_r}`.
