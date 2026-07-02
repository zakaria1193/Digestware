---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- code review
- coding standards
- C89
discussion_id: 49c4da734915ec2bdf9af17e243330e035b66ad1.camel@xry111.site
source_type: public_inbox
title: 'Re: [PATCH v2] LoongArch: Fix relaxation alignment with ld -r (PR 33236)'
headline: 'LoongArch: Fix relaxation alignment with ld -r (PR 33236)'
tldr: A reviewer requests the removal of draft remnants and C++ style comments from
  a Binutils patch for LoongArch linker relaxation alignment.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Xi Ruoyao
  role: reviewer
  position: Requests removal of commented-out draft code and C++ style comments from
    the patch, citing adherence to Binutils' C89 coding standards.
  quote: Again, remove them. A patch shouldn't contain such a draft remnant unless
    it's an RFC. And IIRC binutils code base is still C89 where C++-style comment
    is not allowed.
primer_expert: This review comment concerns a patch for the Binutils linker (`ld`)
  focusing on LoongArch relaxation alignment. The core issue of the review is code
  style and adherence to the project's standards. Specifically, it points out the
  presence of C++-style comments (`//`) and commented-out draft code within a codebase
  that adheres to C89. This highlights a common issue in open-source contributions
  where contributors might inadvertently violate established coding conventions for
  a given project, which, in this case, would generally be defined for `bfd/elfnn-loongarch.c`
  or similar LoongArch-specific…
primer_general: This is a comment during a code review for a bug fix in the linker,
  a program that combines different parts of a compiled program, specifically for
  computers using the LoongArch chip. The person reviewing the code noticed that the
  proposed fix still contained some leftover draft code that was commented out, and
  used a style of comments (starting with `//`) that is generally used in C++ programming.
  However, the Binutils project, which this code belongs to, uses an older standard
  of C (C89) where those types of comments aren't allowed. The reviewer is asking
  the original developer to clean up these stylistic issues so the code properly follows
  the project's rules before it can be included.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/49c4da734915ec2bdf9af17e243330e035b66ad1.camel@xry111.site
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This message is a review comment on a patch for Binutils' LoongArch linker, specifically addressing relaxation alignment with `ld -r`. The reviewer, Xi Ruoyao, points out that the patch contains commented-out draft code and C++ style comments, which are not allowed in the Binutils codebase given its C89 standard. The review suggests cleaning up these stylistic issues before the patch can be accepted. This emphasizes code quality and adherence to project-specific coding standards.
