---
project: glibc
subsystem: posix
patch_id: null
tags:
- i18n
- getopt_long
- collision detection
- internationalization
discussion_id: 5e2bb861a461cf836105efab8cadf833ad3155b4.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 7/9] posix: check for collisions in getopt_long'
headline: Check for collisions in getopt_long
tldr: Adds a runtime check to detect collisions between translated option names in
  `getopt_long`, improving i18n robustness.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds runtime overhead by looping over option pairs, but mitigated by only running
  the check on the first call to `getopt_long`.
- Introduces a new global variable to track the first call to `getopt_long`.
- Only detects collisions at runtime, not during development or translation.
exchanges: []
primer_expert: This patch adds option-translation collision detection to `posix/getopt.c`.
  It loops over option pairs, which may be costly for programs with many arguments;
  the test only runs during the first call to `getopt_long` to avoid performance issues
  and infinite loops. The patch introduces a non-exported global boolean to track
  the first call.
primer_general: '`getopt_long` is a glibc function used to parse command-line options.  It
  handles both short options (e.g., `-v`) and long options (e.g., `--verbose`).  This
  patch adds a check for collisions in translated option names. Option name translations
  allow programs to be used with non-English option names, but can introduce ambiguity
  if the same translation is used for multiple options. This patch hardens against
  such errors.'
series_id: 'glibc:posix: check for collisions in getopt_long'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/5e2bb861a461cf836105efab8cadf833ad3155b4.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch adds a runtime check to `getopt_long` to detect collisions where a developer introduces a new option name that collides with a translation of another option, or when a translator assigns the same translation to two different options.  When a collision is detected, `getopt_long` returns '?' and prints an error message to stderr. To avoid infinite loops, the check is only run on the first call to `getopt_long`.  This improves robustness of internationalized programs using `getopt_long`.
