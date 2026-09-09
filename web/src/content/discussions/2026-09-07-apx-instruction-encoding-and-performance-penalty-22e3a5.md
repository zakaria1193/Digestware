---
project: binutils
subsystem: binutils
patch_id: null
tags:
- APX
- x86
- performance
- instruction encoding
discussion_id: SJ5PPF77D28E3C25DC59AE37A1283402ABEECB22@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: APX vs "length changing prefix"
headline: APX instruction encoding and performance penalty
tldr: Intel clarifies that APX EVEX-encoded instructions with operand size prefixes
  may incur performance penalties.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential performance penalties for using operand size prefixes with EVEX encoding.
- Code size may increase if prefixes are used to achieve smaller immediates.
- Requires careful consideration by developers optimizing for APX.
exchanges:
- author: Jiang, Haochen
  role: proposer
  position: Confirms that overriding operand size in APX EVEX-encoded instructions
    can incur a performance penalty if it changes the instruction length.
  quote: 'Yes, it will suffer penalty.


    If you use a "default" OSIZE/ASIZE for a given mode+opcode, then there''s no

    penalty. If you override something which changes overall length, there''s a

    potential penalty.'
- author: Jan Beulich
  role: reviewer
  position: Asked whether APX EVEX-encoded instructions with operand size prefixes
    changing immediate size would suffer performance penalties, similar to legacy
    encodings.
  quote: "What I'm asking is whether e.g.\n\n\t{nf} add 0x777, %cx\n\nis penalized\
    \ over either of\n\n\t{nf} add 0x777, %ecx\n\t{nf} add 0x777, %rcx\n\n(the former\
    \ having imm16, the latter two having imm32). And I assume\nthat like for legacy\
    \ encodings\n\n\t{nf} add 0x77, %cl\n\nis not. (Yet independently the non-ND 8-\
    \ and 16-bit forms then would\nlikely suffer a partial register access penalty.)"
primer_expert: This exchange concerns the performance implications of operand size
  overrides within APX's EVEX encoding. Specifically, it addresses whether changing
  the immediate size via prefixes (e.g., 0x777 to 0x7777) in an EVEX-encoded instruction,
  which may alter the instruction's byte length, incurs a decode penalty on Intel
  CPUs. The response clarifies that such length changes can indeed trigger penalties.
primer_glossary:
- term: APX
  definition: Advanced Performance Extensions, a set of new instructions and features
    for x86 processors aimed at improving performance and efficiency.
- term: EVEX
  definition: A prefix byte used in x86-64 instruction encoding to support extended
    features like AVX-512, allowing for 256-bit and 512-bit vector operations and
    more flexible encoding.
- term: operand size prefix
  definition: An instruction prefix byte (like 0x66) that modifies the default operand
    size (e.g., from 32-bit to 16-bit) for subsequent instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C25DC59AE37A1283402ABEECB22@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This discussion clarifies a performance aspect of Intel's APX (Advanced Performance Extensions) instruction set. A reviewer inquired whether EVEX-encoded instructions, similar to legacy encodings, would suffer performance penalties if operand size prefixes change the immediate size. The response confirms that overriding the default operand size, which changes the overall instruction length, can indeed lead to a penalty.
