---
project: glibc
subsystem: manual
patch_id: null
tags:
- glibc
- manual
- aprintf
- asprintf
- documentation
discussion_id: 7ad3070944954bca1b727e8d2423805d9bbd3533.1776882798.git.alx@kernel.org
source_type: public_inbox
title: '[PATCH 2/3] manual/: Prefer aprintf(3) over asprintf(3)'
headline: 'manual/: Prefer aprintf(3) over asprintf(3)'
tldr: This patch updates the glibc manual to recommend `aprintf(3)` over `asprintf(3)`
  where possible.
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Encourages the use of `aprintf` for simpler and safer string formatting.
- Relies on a glibc-specific extension, potentially reducing portability in the short
  term, but anticipating future standardization.
exchanges: []
primer_expert: This patch modifies the glibc manual to recommend `aprintf` over `asprintf`.
  `aprintf` is a glibc extension that allocates a string using `malloc` to fit the
  formatted output, similar to `asprintf`, but it returns the allocated string directly,
  avoiding the need to pass in a pointer to a pointer.  This change reflects a preference
  for a safer and simpler API, with the expectation of future standardization.
primer_general: '`asprintf` and `aprintf` are functions in the glibc library that
  dynamically allocate memory to store the result of a formatted string.  They are
  similar to `sprintf`, but instead of requiring a pre-allocated buffer, they allocate
  the buffer automatically.  `aprintf` is a simpler and safer alternative to `asprintf`,
  as it directly returns the allocated string, reducing the risk of memory leaks or
  errors. This patch updates the glibc manual to encourage developers to use `aprintf`
  where available.'
series_id: 'glibc:manual/: prefer aprintf(3) over asprintf(3)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/7ad3070944954bca1b727e8d2423805d9bbd3533.1776882798.git.alx@kernel.org
bugzilla_url: null
date: '2026-04-22'
---

This patch modifies the glibc manual to recommend the use of `aprintf(3)` over `asprintf(3)`. `aprintf` is considered a better API due to its simplicity, safety, and reduced error potential. The C Committee is considering standardizing `aprintf`, suggesting it will become more portable in the future. The patch updates examples and documentation to reflect the preference for `aprintf`.
