---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- avx10
- instruction
- new-feature
discussion_id: SJ5PPF77D28E3C2FDF299316DCE2B0D1EE3EC7C2@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH 1/7] x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
headline: 'x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
tldr: Adds support for the new AVX10_VPMLDSABFLYDQ instruction on x86 architectures.
proposer: Jiang, Haochen
consensus: Under Review
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces new instruction support, expanding assembler capabilities.
- Requires careful handling of patch series numbering and organization.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Questions if the patch was misnumbered as '1/7' since no subsequent patches
    or cover letter were found.
  quote: "> From: Jan Beulich <jbeulich@suse.com>\n> Sent: Monday, November 16, 2026\
    \ 4:17 PM\n> \n> On 16.11.2026 08:54, Haochen Jiang wrote:\n> > There are several\
    \ new ISAs disclosed last week. In ISE063, the only new\n> > ISA is AVX10_VPMLDSABFLYDQ.\n\
    > \n> Just a basic question up front: Was this patch perhaps tagged 1/7 by mistake?\n\
    > I don't see any patches 2..7 here, nor a cover letter."
- author: Haochen Jiang
  role: proposer
  position: Clarifies that the patch numbering was a mistake, as the series was initially
    planned as a single submission and later split, but the numbering was not fully
    updated.
  quote: 'It is a mistake. I initially want to send all new ISA patches in one patch
    series. So

    I generated them all together. But then realized it might be too much for a single

    patch series. So eventually I split them into four different threads. But I forgot

    to change the subject for this one.'
primer_expert: This patch adds support for the AVX10_VPMLDSABFLYDQ instruction to
  binutils. This instruction is part of a new ISA extension, AVX10.3, which is being
  progressively added. The series aims to incorporate several new instructions disclosed
  in recent specifications.
primer_glossary:
- term: AVX10_VPMLDSABFLYDQ
  definition: A specific instruction within the AVX-10 instruction set, related to
    packed data operations.
- term: ISA
  definition: Instruction Set Architecture; the set of commands a CPU can execute.
- term: AVX10
  definition: An extension to the x86 instruction set architecture that provides advanced
    vector operations, building upon AVX-2 and AVX-512.
series_id: 'binutils:x86: support x86 avx10_vpmldsabflydq instructions'
series_role: reply
series_parts:
- title: 'x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
  url: https://inbox.sourceware.org/binutils/7b7d04d8-a41e-4392-be5c-592efe164972@suse.com
  n: 1
  total: 7
- title: 'x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
  url: https://inbox.sourceware.org/binutils/20261116075403.1809267-1-haochen.jiang@intel.com
  n: 1
  total: 7
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C2FDF299316DCE2B0D1EE3EC7C2@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch introduces support for the AVX10_VPMLDSABFLYDQ instruction, a new ISA disclosed recently. The proposer initially intended to include this in a larger series but split them into multiple threads. This patch series aims to incorporate new instruction set extensions into the assembler and disassembler.
