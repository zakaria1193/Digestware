---
project: glibc
subsystem: posix
patch_id: null
tags:
- glibc
- getopt_long
- internationalization
- translations
- PO files
discussion_id: 2955a3592a6b97298fbcd76ba9eb152739e6e363.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 8/9] posix: Add a script for static validation of getopt_long PO
  files'
headline: 'posix: Add a script for static validation of getopt_long PO files'
tldr: Introduces a Perl script to statically check PO files for collisions between
  getopt_long option names and translations.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds a new dependency on Perl.
- Increases the complexity of the build process.
- May require updates to the script as the `getopt_long` interface evolves.
- Provides a valuable tool for ensuring translation consistency and correctness.
exchanges: []
primer_expert: This patch adds a Perl script (`posix/check-getopt-translations.pl`)
  to perform static analysis of PO files used with `getopt_long`. The script checks
  for potential translation collisions, where the same translation is used for multiple
  options or an option name is also used as a translation. The script leverages existing
  glibc infrastructure and is integrated into the build process via `posix/Makefile`.
  The addition of `posix/tst-check-getopt-translations.sh` provides a test case for
  the script itself.
primer_general: PO files are used to store translations for software programs. The
  `getopt_long` function in glibc uses translations to provide localized command-line
  options.  This patch introduces a script that automatically checks the PO files
  used for `getopt_long` to ensure that there are no conflicting translations. Conflicting
  translations can cause a program to behave unpredictably, so this script helps to
  catch these problems early in the development process.
series_id: 'glibc:posix: add a script for static validation of getopt_long po files'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/2955a3592a6b97298fbcd76ba9eb152739e6e363.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch introduces `check-getopt-translations.pl`, a Perl script designed to validate PO files used for translating `getopt_long` option names. The script identifies collisions where a translation is used for multiple options or when an option name is also used as a translation. This allows developers to catch translation errors early and prevent issues in localized builds of glibc.
