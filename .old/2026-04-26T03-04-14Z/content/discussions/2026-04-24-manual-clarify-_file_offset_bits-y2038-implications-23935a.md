---
project: glibc
subsystem: manual
patch_id: null
tags:
- glibc
- manual
- Y2038
- _FILE_OFFSET_BITS
- _TIME_BITS
discussion_id: CAEHDMjzdGJ1+46B+gpYDw8VDvfe_0CyMzxOt+Xv3gxDy1k0tiA@mail.gmail.com
source_type: public_inbox
title: '[PATCH v2] manual: clarify _FILE_OFFSET_BITS Y2038 implications [BZ #34095]'
headline: 'Manual: clarify _FILE_OFFSET_BITS Y2038 implications'
tldr: Shamil Abdulaev clarifies in the glibc manual that _TIME_BITS=64 requires _FILE_OFFSET_BITS=64
  for Y2038 safety.
proposer: Shamil Abdulaev <ashamil435@gmail.com>
consensus: Proposed
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Clarifies the manual, improving understandability.
- No code changes, only documentation.
exchanges:
- author: Shamil Abdulaev <ashamil435@gmail.com>
  role: proposer
  position: Clarifies the relationship between  _FILE_OFFSET_BITS and Y2038, documenting
    the transitive dependency between _TIME_BITS and _FILE_OFFSET_BITS.
  quote: 'Clarify that _TIME_BITS=64 (needed for Y2038 safety) requires

    _FILE_OFFSET_BITS=64, so when systems migrate to 64-bit time_t by

    default, _FILE_OFFSET_BITS will also need to default to 64, even for

    applications that do not handle large files.'
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: reviewer
  position: Reviewed the patch.
  quote: null
primer_expert: This patch clarifies the interaction between _FILE_OFFSET_BITS and
  _TIME_BITS, both of which control ABI details, in glibc's manual.  Specifically,
  the Y2038 transition requires a 64-bit time_t, which in turn requires a 64-bit file
  offset.  This affects the default value of _FILE_OFFSET_BITS and potentially impacts
  applications even if they do not use large files.
primer_general: This patch updates the glibc manual to explain how the Y2038 problem
  affects file handling. The Y2038 problem is that 32-bit systems will have issues
  representing times after January 19, 2038.  Glibc, the GNU C Library, uses the `time_t`
  datatype to represent time, and the `_FILE_OFFSET_BITS` macro to specify the number
  of bits to use for file offsets. To fix the Y2038 problem, `time_t` needs to be
  64-bits which requires `_FILE_OFFSET_BITS` to also be 64-bits.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAEHDMjzdGJ1+46B+gpYDw8VDvfe_0CyMzxOt+Xv3gxDy1k0tiA@mail.gmail.com
bugzilla_url: null
date: '2026-04-24'
---

Shamil Abdulaev clarifies in the glibc manual that _TIME_BITS=64 (needed for Y2038 safety) requires _FILE_OFFSET_BITS=64. This means that when systems migrate to 64-bit time_t by default, _FILE_OFFSET_BITS will also need to default to 64, even for applications that do not handle large files. The patch addresses confusion noted in bug report #34095.
