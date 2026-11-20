---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- avx10
- instruction set
- assembler
discussion_id: SJ5PPF77D28E3C25BF7B9705A333DE3A380EC792@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH v2] x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
headline: 'x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
tldr: Adds support for the AVX10_VPMLDSABFLYDQ instruction to the x86 assembler.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds a new instruction to the assembler, increasing its complexity slightly. No
  significant performance tradeoffs are introduced.
exchanges:
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: proposer
  position: Submits a v2 patch to add support for AVX10_VPMLDSABFLYDQ, incorporating
    review feedback.
  quote: This is the v2 patch for AVX10_VPMLDSABFLYDQ according to review.
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Approves the patch with a minor suggestion to extend a comment.
  quote: Yes with the middle of the "Chnages in v2" above also extended to ... this.
primer_expert: This patch adds a new instruction, `AVX10_VPMLDSABFLYDQ`, to the x86
  assembler's configuration in `gas/config/tc-i386.c`. It's categorized under the
  AVX10 vector instruction group. The change is primarily an addition to the instruction
  set supported by the assembler, requiring updates to the `cpu_arch` array.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures for computer processors, commonly
    used in PCs and servers.
- term: AVX10
  definition: A set of advanced vector extensions for x86 processors, designed to
    improve performance in floating-point and SIMD operations.
- term: VPMLDSABFLYDQ
  definition: A specific AVX-512 instruction related to packed data manipulation.
- term: assembler
  definition: A program that translates assembly language into machine code.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C25BF7B9705A333DE3A380EC792@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch introduces support for the AVX10_VPMLDSABFLYDQ instruction in the x86 assembler configuration. It adjusts the instruction's placement within the AVX10 option group and uses the singular form in NEWS, as it's a single instruction addition. The change is a minor update to the assembler's instruction set.
