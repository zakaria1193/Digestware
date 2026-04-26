---
project: glibc
subsystem: posix
patch_id: null
tags:
- security
- getopt_long
- i18n
- setuid
- setgid
discussion_id: 0f4a0180b879bfd9a05c841af1e425a52296f1c0.1776957778.git.vivien@planete-kraus.eu
source_type: public_inbox
title: '[PATCH v22 5/9] posix: do not allow option name translations for secure programs'
headline: 'posix: do not allow option name translations for secure programs'
tldr: Disables option name translations in `getopt_long` for setuid/setgid/AT_SECURE
  programs, ensuring predictable behavior.
proposer: Vivien Kraus <vivien@planete-kraus.eu>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Disables i18n for secure programs, which may reduce usability in some cases.
- Relies on the `__libc_enable_secure` flag to accurately identify secure programs.
exchanges: []
primer_expert: This patch modifies `posix/getopt.c` to disable option name translations
  when `__libc_enable_secure` is set. This is a security measure to prevent untrusted
  translations from affecting the behavior of privileged binaries.
primer_general: '`getopt_long` is used to parse command-line options. This patch disables
  option name translations in secure programs (setuid/setgid) to ensure predictable
  behavior.  In secure programs, it''s crucial the program behaves exactly as the
  programmer intended.  Translations could mask options or change their meaning, creating
  a security hole.'
series_id: 'glibc:posix: do not allow option name translations for secure programs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/0f4a0180b879bfd9a05c841af1e425a52296f1c0.1776957778.git.vivien@planete-kraus.eu
bugzilla_url: null
date: '2026-04-23'
---

The patch modifies `getopt_long` to disable option name translations for programs running in secure environments (SETUID, SETGID, or AT_SECURE). This ensures that such programs are invoked with the expected option names and prevents unexpected behavior due to potentially malicious translations.
