---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- code review
discussion_id: 765271a2-72d6-4b23-9b1d-2d1656f74f10@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: Resubmits a patch for LoongArch relocation range detection, opting for a non-common
  implementation as per review feedback.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Resubmits a patch for LoongArch relocation range detection, preferring
    a specific implementation over a common one as advised by a reviewer.
  quote: Reuse this patch, since Alan does not recommend using the common implementation.
- author: Harshit Kumar <harshit.kumar@intel.com>
  role: reviewer
  position: Acknowledges the resubmission and confirms that adding the relocation
    name to the error message is a good idea, which will be addressed in a future
    revision.
  quote: Thanks. Naming the relocation makes sense. The message is currently the one
    i386 and x86-64 already print, so I kept the wording the same; I'll add the name
    in the next revision of the series.
primer_expert: This is a follow-up discussion on a patch series for LoongArch's relocation
  handling. The proposer is resubmitting a patch based on feedback that a generic
  implementation was not desired. The discussion also confirms that error messages
  will be enhanced to include relocation names, a suggestion made by the reviewer.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/765271a2-72d6-4b23-9b1d-2d1656f74f10@loongson.cn
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This email resubmits a patch for LoongArch relocation range detection. The proposer is reusing an existing patch because a reviewer recommended against using a common implementation. The discussion also touches upon adding relocation names to error messages, with the reviewer agreeing to incorporate this in a future revision.
