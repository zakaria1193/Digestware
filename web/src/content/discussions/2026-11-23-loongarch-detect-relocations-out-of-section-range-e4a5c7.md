---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- error handling
discussion_id: 20261123064059.1917899-1-harshit7kr@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: LoongArch relocation error message will include relocation name in a future
  revision.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improved error messages aid debugging.
- Adding relocation names requires minor code changes.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Agrees to add the relocation name to the error message in a future revision,
    acknowledging its usefulness.
  quote: 'Thanks. Naming the relocation makes sense. The message is currently

    the one i386 and x86-64 already print, so I kept the wording the same; I''ll add
    the name in the next revision of the series.'
- author: mengqinggang <mengqinggang@loongson.cn>
  role: contributor
  position: Thanks Harshit and suggests adding the relocation name to the error message.
  quote: 'Thanks — please use the existing patch and ignore mine.

    By the way, how about adding the relocation name to the error message?'
primer_expert: This discussion concerns error handling in the LoongArch linker (ld)
  within binutils. Specifically, it addresses situations where a relocation entry's
  offset points outside the bounds of its associated section. The patch aims to improve
  diagnostics by making these errors more informative, with a follow-up suggestion
  to include the name of the relocation for easier identification.
primer_glossary:
- term: LoongArch
  definition: A 64-bit CPU architecture developed by Loongson Technology.
- term: relocation
  definition: Information in an object file that describes how to modify certain values,
    typically code or data, after linking to allow them to be placed at an absolute
    address.
- term: section
  definition: A segment of an object file or executable that contains related data,
    such as code (.text), initialized data (.data), or uninitialized data (.bss).
- term: linker
  definition: A program that combines various pieces of code and data (from object
    files and libraries) and resolves references between them to create a single executable
    file or library.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261123064059.1917899-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

Following a suggestion to include the relocation name in error messages, Harshit Kumar agrees to add this detail in a future revision of the patch series. This change addresses the detection of relocations that fall outside the valid range of a section for the LoongArch architecture. The original patch maintained consistency with existing error messages from i386 and x86-64.
