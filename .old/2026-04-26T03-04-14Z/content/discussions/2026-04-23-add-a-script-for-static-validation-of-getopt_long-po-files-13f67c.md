---
project: glibc
subsystem: posix
patch_id: null
tags:
- i18n
- getopt_long
- static analysis
- collision detection
- perl
discussion_id: 2955a3592a6b97298fbcd76ba9eb152739e6e363.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 8/9] posix: Add a script for static validation of getopt_long PO
  files'
headline: Add a script for static validation of getopt_long PO files
tldr: Introduces a Perl script to statically check PO files for `getopt_long` option
  name translation collisions, catching i18n bugs early.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Requires Perl to be installed to run the validation script.
- Adds complexity to the build process.
- Only catches errors detectable through static analysis of PO files; runtime issues
  may still occur.
exchanges: []
primer_expert: The patch adds `posix/check-getopt-translations.pl`, a Perl script
  adapted from `mtrace.pl`, for static validation of `getopt_long` PO files. This
  script checks for collisions between option names and translations. The script is
  integrated into the build process via changes to `posix/Makefile`.
primer_general: '`getopt_long` uses gettext PO files for option name translations.
  This patch provides a static analysis tool to scan those PO files for errors _before_
  runtime. Specifically, it checks that no two options share the same translation,
  and that no translation conflicts with an untranslated option name. This prevents
  unexpected program behavior due to i18n configuration.'
series_id: 'glibc:posix: add a script for static validation of getopt_long po files'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/2955a3592a6b97298fbcd76ba9eb152739e6e363.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch introduces a Perl script, `check-getopt-translations.pl`, to statically validate PO files used by `getopt_long`. The script checks for collisions between long option names and their translations, allowing developers to catch errors early in the development process.  This prevents embarrassing the translation team and avoids runtime surprises. The script and associated test cases are added to the glibc build system.
