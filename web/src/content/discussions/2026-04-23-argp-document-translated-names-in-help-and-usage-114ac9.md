---
project: glibc
subsystem: argp
patch_id: null
tags:
- argp
- i18n
- help
- usage
- internationalization
discussion_id: f7ee811c6f1995dc399a48388241ceffb79a23dd.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 3/9] argp: document translated names in --help and --usage'
headline: 'argp: document translated names in --help and --usage'
tldr: Displays translated option names in `argp`'s --help and --usage messages, with
  the original name in parentheses.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Uses dynamic memory allocation, which could fail and prevent the translated option
  name from being displayed.
- Requires a fixed translation context, limiting flexibility.
- Increases the size of the `--help` and `--usage` output.
exchanges: []
primer_expert: This patch modifies `argp/argp-help.c` to include translated option
  names in the `--help` and `--usage` output. The untranslated name is displayed in
  parentheses.  The implementation uses dynamic memory allocation and a fixed translation
  context.
primer_general: '`argp` is a glibc library for parsing command-line arguments. This
  patch improves the usability of programs using translated option names by displaying
  both the translated and untranslated names in the `--help` and `--usage` messages.
  This helps users understand which translated option corresponds to the original
  option name used in scripts or documentation.'
series_id: 'glibc:argp: document translated names in --help and --usage'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f7ee811c6f1995dc399a48388241ceffb79a23dd.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch enhances the `argp` library to display translated option names in the `--help` and `--usage` output. The translated name is shown as the main option name, with the original, untranslated name displayed in parentheses. This allows users to easily identify the corresponding option in scripts or documentation that use the untranslated names. The help message processing uses dynamic memory allocation, and a fixed translation context ensures consistent translation.
