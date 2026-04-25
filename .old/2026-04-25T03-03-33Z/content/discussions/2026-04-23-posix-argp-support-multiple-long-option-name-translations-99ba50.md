---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- argp
- getopt_long
- internationalization
- translations
discussion_id: 450db6bd8f93d16aa277d771bfebd4118baf3df8.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 9/9] posix, argp: Support multiple long option name translations'
headline: 'posix, argp: Support multiple long option name translations'
tldr: Enables multiple space-separated translations for a single command-line option,
  enhancing internationalization flexibility.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increases code complexity due to handling multiple translations.
- May introduce performance overhead in argument parsing due to additional comparisons.
- Requires updating PO files to include space-separated lists of translations.
- Potential for increased memory usage due to storing multiple translations.
exchanges: []
primer_expert: This patch modifies `argp` and `getopt_long` to support multiple long
  option name translations.  It extends the translation mechanism to allow space-separated
  lists of translations for a single option.  This change impacts argument parsing,
  collision detection, and help message generation within `argp` and `posix/getopt.c`,
  requiring updates to data structures and algorithms in those components.  The use
  of `\004` as a separator hints at reliance on existing gettext infrastructure.
primer_general: Command-line programs often support options (like `--verbose`) that
  users can specify to control the program's behavior. For internationalization, these
  option names need to be translated into other languages.  This patch enhances the
  translation mechanism in glibc, the standard C library, to allow a single option
  to have multiple valid translations. This is useful when a concept has multiple
  equivalent translations or when different English options have the same functionality
  in the program.
series_id: 'glibc:posix, argp: support multiple long option name translations'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/450db6bd8f93d16aa277d771bfebd4118baf3df8.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch allows translators to provide multiple alternative translations for a single command-line option, separated by spaces. This addresses scenarios where a concept may have multiple valid translations in another language, or where different option names have the same behavior (e.g., `--eval` and `--execute`). The patch modifies argument matching, collision detection, and help/usage message generation to accommodate multiple translations.
