---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- AVX
- ISA
- documentation
- naming
discussion_id: CAKSQd8Uut39mtSBZaSXbuypL911y0EYgG-ucAPFynWo=Uc4RNg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] Support AVX10_V2_AUX instructions'
headline: AVX10 instruction naming and spec version feedback
tldr: Discussion regarding the naming convention for AVX10 auxiliary instructions
  and feedback on the ACE specification version.
proposer: Christian Ludloff <ludloff@gmail.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 6
technical_tradeoffs:
- Debates naming conventions for clarity and consistency in instruction sets.
- Highlights potential issues with specification versioning and documentation accuracy.
exchanges:
- author: Christian Ludloff
  role: proposer
  position: Questions the naming convention for AVX10 auxiliary instructions and notes
    the specification version.
  quote: 'In fact doc version 1.15

    latest ACE spec is 1.16.2

    direct feedback on silent doc releases to the EAG

    also, instead of the AVX10_Vn_AUX insanity, has

    anyone considered AVX10_AUX_Vn for naming?'
- author: Jan Beulich
  role: reviewer
  position: Comments on the ACE specification version and the proposed naming convention,
    noting that the 'Vn' might not imply versioning.
  quote: 'Interesting, especially when at the top of

    https://sourceware.org/resource/ai-compute-extensions-ace-specification/

    is says "June 15, 2026".

    Now that it''s clear that the Vn here isn''t intended to have'
- author: Jiang, Haochen
  role: reviewer
  position: Notes that specification updates might be incomplete and that some comments
    regarding exception types are unaddressed.
  quote: 'I don''t know that has been updated either. It seems to me

    that some of my comments are not addressed. (Here I mean

    the exception type) I will mention that.'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges Haochen Jiang's point about unaddressed comments and notes
    that specific instruction issues (FP8 to FP4 convert modrm) appear fixed.
  quote: 'I don''t know that has been updated either. It seems to me

    that some of my comments are not addressed. (Here I mean

    the exception type) I will mention that.

    It seems to me that FP8 to FP4 convert modrm is fixed, it is a clear

    bug in document'
- author: Jiang, Haochen
  role: reviewer
  position: Reiterates that some comments remain unaddressed and highlights a specific
    instruction bug fix.
  quote: 'It seems to me that FP8 to FP4 convert modrm is fixed, it is a clear

    bug in documentation, while FP8 to FP6 still remaining a

    que'
- author: Christian Ludloff
  role: proposer
  position: Confirms specific instructions ('vcvt', 'vpmovssdb') as outliers and agrees
    that 'aux1' and 'aux2' are poor naming choices.
  quote: 'yep, vcvt{bf,hf}82bf4s and vpmovssdb are the only three "outliers", with
    dst=r/m

    yep, aux1 and aux2 are poor names – classic avx512 names did a little better...

    x86... c''est la vie  :)'
primer_expert: This thread discusses the naming conventions for new AVX10 auxiliary
  instructions and related AI Compute Extensions (ACE) specification details. Christian
  Ludloff questions the `AVX10_Vn_AUX` naming, proposing `AVX10_AUX_Vn` as potentially
  more logical. The participants also noted discrepancies in the ACE specification
  version (1.15 vs. 1.16.2) and discussed specific instruction behaviors like `vcvt`
  and `vpmovssdb`. The conversation highlights the need for clear naming and accurate
  documentation in evolving instruction set extensions.
primer_glossary:
- term: AVX10
  definition: A planned extension to the AVX instruction set architecture, aimed at
    improving AI and compute performance.
- term: ACE
  definition: AI Compute Extensions. A set of proposed extensions to the x86 instruction
    set architecture designed to accelerate artificial intelligence workloads.
- term: EAG
  definition: Ecosystem Advisory Group. A group that provides guidance and feedback
    on technical specifications, likely within the context of processor architecture
    extensions.
- term: vcvt
  definition: A vector instruction likely related to data type conversion within AVX/AVX-512.
- term: vpmovssdb
  definition: A vector instruction likely related to packed move operations with scalar
    doubleword elements, possibly for sparse data.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8Uut39mtSBZaSXbuypL911y0EYgG-ucAPFynWo=Uc4RNg@mail.gmail.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

Christian Ludloff and Jan Beulich discuss the naming convention for new AVX10 auxiliary instructions, with Ludloff suggesting AVX10_AUX_Vn as a potentially clearer alternative to AVX10_Vn_AUX. They also note discrepancies in the version of the ACE (AI Compute Extensions) specification being referenced. The conversation touches on specific instructions like `vcvt` and `vpmovssdb`, and the need for direct feedback to the ACE EAG (Ecosystem Advisory Group) on documentation updates.
