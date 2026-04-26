---
project: glibc
subsystem: argp
patch_id: null
tags:
- argp
- security
- i18n
- setuid
- setgid
discussion_id: 53ee606bab9eba01c1e9cd1d1bfc3298518d1ffd.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 6/9] argp: do not display option name translations if __libc_enable_secure'
headline: 'argp: do not display option name translations if __libc_enable_secure'
tldr: Disables option name translations in `argp` when `__libc_enable_secure` is set,
  ensuring predictable invocation for setuid/setgid programs.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Disables i18n for secure programs, potentially reducing usability in some contexts.
- Relies on the `__libc_enable_secure` flag to correctly identify secure programs.
exchanges: []
primer_expert: This patch modifies `argp/argp-help.c` to disable option name translations
  when `__libc_enable_secure` is set.  This prevents potentially untrusted translations
  from affecting the behavior of setuid/setgid binaries.
primer_general: '`argp` is a glibc library for parsing command-line arguments. Option
  name translations enable i18n, but can be undesirable for security-sensitive programs.
  The `__libc_enable_secure` flag indicates that the program is running in a secure
  context (e.g., setuid). When set, this patch disables option name translations in
  `argp` to ensure predictable program invocation.'
series_id: 'glibc:argp: do not display option name translations if __libc_enable_secure'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/53ee606bab9eba01c1e9cd1d1bfc3298518d1ffd.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

This patch modifies `argp` to disable the display of translated option names when the `__libc_enable_secure` flag is set.  This flag is used to indicate that the program is running in a secure environment, such as a setuid or setgid program. Disabling translations in secure mode ensures that the program's invocation is predictable and not subject to user-controlled translations, mitigating potential security risks.
