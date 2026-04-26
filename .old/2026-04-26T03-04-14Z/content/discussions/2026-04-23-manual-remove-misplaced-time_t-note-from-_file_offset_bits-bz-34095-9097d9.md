---
project: glibc
subsystem: manual
patch_id: null
tags:
- documentation
- glibc
- y2038
- time_t
- _file_offset_bits
discussion_id: f34c6264fc798f67a5e0475b3b817b39966861d0.1776982278.git.ashamil435@gmail.com
source_type: public_inbox
title: '[PATCH] manual: remove misplaced time_t note from _FILE_OFFSET_BITS [BZ #34095]'
headline: 'Manual: Remove misplaced time_t note from _FILE_OFFSET_BITS [BZ #34095]'
tldr: Removes a paragraph about time_t and Y2038 from the _FILE_OFFSET_BITS section
  of the glibc manual.
proposer: Shamil Abdulaev <ashamil435@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 5
technical_tradeoffs:
- Improved documentation clarity vs. potential loss of information about the Y2038
  problem.
- Correctly placing information in the manual for better understanding.
exchanges:
- author: Shamil Abdulaev <ashamil435@gmail.com>
  role: proposer
  position: Proposes removing the paragraph, arguing it's misplaced and better suited
    for the _TIME_BITS section.
  quote: 'The paragraph warning that _FILE_OFFSET_BITS''s default may change due

    to time_t Y2038 safety was placed inside the _FILE_OFFSET_BITS

    section, but Y2038 is a concern of _TIME_BITS.  The adjacent _TIME_BITS

    section already documents the Y2038 behaviour, so remove the

    misplaced paragraph rather than merging it in.'
- author: Mark Harris <mark.hsj@gmail.com>
  role: other
  position: Contends that the paragraph is not misplaced because a change to `_TIME_BITS`
    is inevitable as 2038 approaches, and _FILE_OFFSET_BITS depends on it.
  quote: 'This is not misplaced.  It is saying that as the year 2038 approaches,

    a change to _TIME_BITS=64 is inevitable.  However as mentioned later,

    _TIME_BITS'
- author: Shamil Abdulaev <ashamil435@gmail.com>
  role: proposer
  position: 'Thanks Mark Harris for the clarification and asks if BZ #34095 is considered
    invalid.'
  quote: null
- author: Mark Harris <mark.hsj@gmail.com>
  role: other
  position: Suggests the bug report isn't entirely invalid, indicates wording could
    be improved.
  quote: 'I added my reply there.  I don''t think it''s valid except to the extent

    that it indicates that people are confused by the existing wording,

    which may mean that the wording could be improved.'
primer_expert: This patch deals with documentation related to `_FILE_OFFSET_BITS`
  and `_TIME_BITS` macros in glibc. These macros control the size of file offsets
  and the `time_t` type, respectively. The discussion revolves around the placement
  of a warning about the Y2038 problem and its potential impact on `_FILE_OFFSET_BITS`.
primer_general: Glibc uses macros like `_FILE_OFFSET_BITS` and `_TIME_BITS` to define
  the size of data types used for file operations and time representation. The Y2038
  problem is a potential issue where the `time_t` data type, used to store time, could
  overflow in the year 2038. This patch involves clarifying the documentation around
  these macros and the Y2038 problem.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/f34c6264fc798f67a5e0475b3b817b39966861d0.1776982278.git.ashamil435@gmail.com
bugzilla_url: null
date: '2026-04-23'
---

Shamil Abdulaev proposes removing a paragraph from the glibc manual's `_FILE_OFFSET_BITS` section that discusses the potential impact of `time_t` changes related to the Y2038 problem.  The author argues that this information is more relevant to the `_TIME_BITS` section, which already covers Y2038 concerns. However, it depends transitively on _TIME_BITS potentially influencing also _FILE_OFFSET_BITS.
