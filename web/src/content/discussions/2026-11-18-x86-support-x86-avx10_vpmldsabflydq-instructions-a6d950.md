---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- gas
- x86
- AVX10
- instruction set
discussion_id: 20261118022559.2489269-1-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH v2] x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
headline: 'x86: Support x86 AVX10_VPMLDSABFLYDQ instructions'
tldr: Binutils gas assembler is updated to support the new AVX10_VPMLDSABFLYDQ instruction.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Adding new instruction support increases assembler complexity but enables use of
  new hardware features.
- Internal mnemonic shortening simplifies code but requires careful management to
  avoid conflicts.
exchanges:
- author: Haochen Jiang <haochen.jiang@intel.com>
  role: proposer
  position: Submits a v2 patch to add support for the AVX10_VPMLDSABFLYDQ instruction
    to gas, noting changes from the previous version.
  quote: "This is the v2 patch for AVX10_VPMLDSABFLYDQ according to review.\n\nChanges\
    \ in v2:\n\n  - Use VPMLDSABFLYDQ for internal usage.\n  - Adjust the appearence\
    \ of AVX10_VPMLDSABFLYDQ near AVX10 option group.\n  - Use singular in NEWS since\
    \ only one inst."
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Approves the patch with a minor suggestion to extend a change from the
    "Changes in v2" list to a specific code block.
  quote: 'Yes with the middle of the "Chnages in v2" above also extended to ...


    > --- a/gas/config/tc-i386.c

    > +++ b/gas/config/tc-i386.c

    > @@ -1273,6 +1273,8 @@ static const

    diff (truncated):'
primer_expert: This patch introduces support for the AVX10_VPMLDSABFLYDQ instruction
  into the GNU Assembler (gas). This instruction is part of Intel's AVX10 extension
  set. The changes involve updating opcode tables, configuration files (`tc-i386.c`),
  documentation (`c-i386.texi`), and adding new test cases to the test suite. A shorter
  internal mnemonic `VPMLDSABFLYDQ` is used. The patch is a revision addressing feedback
  from a prior review.
primer_glossary:
- term: AVX10
  definition: A set of advanced vector extensions for Intel processors, designed to
    provide enhanced performance for vectorized computations.
- term: VPMLDSABFLYDQ
  definition: A specific instruction within the AVX10 instruction set, likely performing
    a masked-load operation with fused multiply-add functionality.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    translating assembly language code into machine code.
- term: ISE063
  definition: Likely an Intel document identifier or specification number related
    to instruction set extensions.
- term: opcode
  definition: Operation code. The part of a machine language instruction that specifies
    the operation to be performed.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261118022559.2489269-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch adds support for the AVX10_VPMLDSABFLYDQ instruction to the GNU Assembler (gas). The patch includes updates to the assembler's configuration, documentation, and test suite. A shorter internal name, VPMLDSABFLYDQ, is used for convenience. This is a v2 patch addressing previous review feedback.
