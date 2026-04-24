---
project: glibc
subsystem: argp
patch_id: null
tags:
- glibc
- argp
- internationalization
- translations
- security
discussion_id: 53ee606bab9eba01c1e9cd1d1bfc3298518d1ffd.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 6/9] argp: do not display option name translations if __libc_enable_secure'
headline: 'argp: do not display option name translations if __libc_enable_secure'
tldr: Disables the display of translated option names in argp when the `__libc_enable_secure`
  flag is set.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Reduces code complexity by avoiding unnecessary translation lookups.
- May slightly improve performance in secure mode.
- Ensures consistent behavior when translations are disabled.
exchanges: []
primer_expert: This patch modifies `argp/argp-help.c` to prevent the display of option
  name translations when `__libc_enable_secure` is set. The change adds a check for
  `__libc_enable_secure` in `translate_option_name` and returns the original name
  if the flag is enabled. This avoids unnecessary translation lookups and potential
  errors when translations are explicitly disabled.
primer_general: The `argp` library helps programs parse command-line arguments. Programs
  can translate option names (like `--verbose`) into other languages for internationalization.
  This patch disables the display of translated option names when the program is running
  in a secure mode where translations are not used. This simplifies the program's
  behavior and avoids potential issues.
series_id: 'glibc:argp: do not display option name translations if __libc_enable_secure'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/53ee606bab9eba01c1e9cd1d1bfc3298518d1ffd.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch modifies the `argp` library to disable the display of translated option names when the `__libc_enable_secure` flag is enabled.  When `__libc_enable_secure` is set, it indicates that translations are disabled, so this change prevents the library from attempting to display translations that are not available. This simplifies the code and avoids potential issues when running in secure mode.
