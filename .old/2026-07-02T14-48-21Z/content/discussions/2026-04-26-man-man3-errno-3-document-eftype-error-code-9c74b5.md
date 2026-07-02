---
project: glibc
subsystem: man/man3/errno.3
patch_id: null
tags:
- documentation
- errno
- EFTYPE
discussion_id: ae4K_5f1g3zgSNkC@devuan
source_type: public_inbox
title: 'Re: [PATCH v2 1/2] man/man3/errno.3: Document EFTYPE error code'
headline: 'man/man3/errno.3: Document EFTYPE error code'
tldr: A patch documents the `EFTYPE` error code in the `errno.3` manual page.
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Under Review
outcome: ready
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alejandro Colomar <alx@kernel.org>
  role: reviewer
  position: Reviews the patch and will wait until glibc adds the error code to `<errno.h>`
    before applying the patch.
  quote: I will wait until glibc adds this error code to their <errno.h> before applying
    the patch.  This means either you should write and send a patch to glibc (if so,
    please CC me), or you should ask them to add it themselves (if you're not comfortable
    writing glibc code).
primer_expert: The `errno` facility is a standard way for POSIX functions to report
  errors.  This patch updates the manual page for `errno` to document a specific error
  code, `EFTYPE` (wrong file type), but the underlying glibc header needs to be updated
  first.
primer_general: When a program encounters an error, it often sets a global variable
  called `errno` to indicate the type of error. This patch updates the manual page
  that describes the possible values of `errno`, specifically documenting the `EFTYPE`
  error code which signifies a wrong file type for the intended operation.
series_id: 'glibc:man/man3/errno.3: document eftype error code'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/ae4K_5f1g3zgSNkC@devuan
bugzilla_url: null
date: '2026-04-26'
---

This patch adds documentation for the `EFTYPE` error code to the `errno.3` manual page.  The reviewer has approved the patch but will wait until glibc adds the `EFTYPE` error code to its `<errno.h>` header file before applying the documentation change. The submitter may need to create a patch to glibc or ask them to add it themselves.
