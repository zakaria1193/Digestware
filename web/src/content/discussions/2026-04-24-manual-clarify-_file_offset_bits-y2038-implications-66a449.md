---
project: glibc
subsystem: manual
patch_id: null
tags:
- glibc
- manual
- _FILE_OFFSET_BITS
- Y2038
- _TIME_BITS
discussion_id: fa6c9625-ff0d-484c-af2d-53d85931bac3@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v2] manual: clarify _FILE_OFFSET_BITS Y2038 implications [BZ #34095]'
headline: 'manual: clarify _FILE_OFFSET_BITS Y2038 implications'
tldr: 'The patch clarifies the relationship between _FILE_OFFSET_BITS and Y2038, explicitly
  documenting the transitive dependency: _TIME_BITS=64 requires _FILE_OFFSET…'
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Ready to Land
outcome: ready
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Shamil Abdulaev
  role: proposer
  position: 'Clarifies the relationship between `_FILE_OFFSET_BITS` and Y2038, explicitly
    documenting the transitive dependency: `_TIME_BITS=64` requires `_FILE_OFFSET_BITS=64`.'
  quote: Clarify that _TIME_BITS=64 (needed for Y2038 safety) requires _FILE_OFFSET_BITS=64,
    so when systems migrate to 64-bit time_t by default, _FILE_OFFSET_BITS will also
    need to default to 64, even for applications that do not handle large files.
- author: Adhemerval Zanella Netto
  role: reviewer
  position: Reviewed the patch and gave it a LGTM.
  quote: LGTM, thanks.
primer_expert: This patch updates the glibc manual to clarify the interaction between
  _FILE_OFFSET_BITS and the Y2038 time_t transition. Specifically, it highlights the
  requirement for _FILE_OFFSET_BITS=64 when _TIME_BITS=64 is used for Y2038 compliance.
  This affects the ABI for file access functions.
primer_general: The `_FILE_OFFSET_BITS` macro in glibc controls whether file access
  functions use 32-bit or 64-bit offsets.  The Y2038 problem is a potential issue
  where systems using a 32-bit `time_t` will experience an overflow in 2038. To fix
  this, `time_t` is being updated to 64-bit, which requires `_FILE_OFFSET_BITS` to
  also be 64-bit. This change clarifies the implications of this dependency in the
  glibc manual.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/fa6c9625-ff0d-484c-af2d-53d85931bac3@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch clarifies the documentation for `_FILE_OFFSET_BITS` in relation to the Y2038 problem. It explicitly documents that `_TIME_BITS=64` (required for Y2038 safety) necessitates `_FILE_OFFSET_BITS=64`. This change ensures that when systems migrate to 64-bit `time_t` by default, `_FILE_OFFSET_BITS` will also default to 64, even for applications not handling large files, addressing confusion in bug report #34095.
