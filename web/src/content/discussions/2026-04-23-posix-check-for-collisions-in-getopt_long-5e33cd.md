---
project: glibc
subsystem: posix
patch_id: null
tags:
- glibc
- getopt_long
- internationalization
- translations
- collision detection
discussion_id: 5e2bb861a461cf836105efab8cadf833ad3155b4.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 7/9] posix: check for collisions in getopt_long'
headline: 'posix: check for collisions in getopt_long'
tldr: Adds runtime checks to detect collisions between option names and their translations
  in `getopt_long`.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds runtime overhead, although the checks are performed only once.
- Increases code complexity.
- Requires adding a global or per-state boolean to track initialization status.
- The collision detection logic iterates over all pairs of options, potentially impacting
  performance with many options defined.
exchanges: []
primer_expert: This patch introduces collision detection for translated option names
  in `posix/getopt.c`. It aims to catch cases where option names or translations overlap,
  leading to ambiguous program behavior. The implementation adds a one-time check
  during the first call to `getopt_long`, using a global or per-state boolean to track
  initialization status. This avoids repeated checks and potential infinite loops.
  The changes affect both the reentrant and non-reentrant versions of `getopt_long`.
primer_general: The `getopt_long` function parses command-line options in C programs.
  To support internationalization, option names can be translated into other languages.
  This patch adds a safety mechanism to detect situations where different options
  end up having the same translated name. This can happen due to programmer errors
  or translation mistakes. The patch checks for these 'collisions' and reports them,
  preventing unexpected behavior in the program.
series_id: 'glibc:posix: check for collisions in getopt_long'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/5e2bb861a461cf836105efab8cadf833ad3155b4.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch introduces runtime checks in `getopt_long` to detect collisions between option names and their translations.  Such collisions can arise when developers introduce new options that conflict with existing translations, or when translators assign the same translation to multiple options. The checks are performed only during the first call to `getopt_long` to minimize performance impact, and they output an error message to stderr before returning an error code.
