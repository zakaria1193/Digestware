---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- disassembler
- instruction-encoding
discussion_id: 20260601062446.2367458-1-haochen.jiang@intel.com
source_type: public_inbox
title: 'Re: [PATCH] x86: Support BHI_CTRL instruction'
headline: 'x86: Support BHI_CTRL instruction'
tldr: Discussion continues on the x86 BHI_CTRL instruction support, specifically regarding
  the correct handling of REX.W and REX2.W prefixes.
proposer: Jan Beulich
consensus: Proposed
outcome: under_review
impact_score: 5
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Questions whether REX2.W would have the same effect as REX.W for the BHI_CTRL
    instruction and suggests a test case.
  quote: 'So Size64 is here to have REX.W emitted. The whitepaper isn''t clear about

    APX

    at all, though: Would REX2.W also have the same effect? (Whichever way it

    is,

    this then perhaps also wants covering in the testsuite.)'
- author: Jiang, Haochen
  role: proposer
  position: Clarifies that the encoding is fixed and REX2.W won't have the same effect,
    but welcomes a test case.
  quote: No, it won't. The encoding is fixed. But a testcase is welcomed here to clarify.
- author: Jan Beulich
  role: reviewer
  position: Expresses concern that the disassembler might not reject REX2.W and questions
    the differing behavior of W bits in REX vs. REX2.
  quote: 'But you had a good point here, the current disassembler won''t "reject"
    rex2.w

    (i.e., not taking this back to nop from my understanding) and take it as rex.w.


    This let me further wonder if a user input something like "{rex2} ibhf", should
    we

    accept that?'
- author: Jiang, Haochen
  role: proposer
  position: States that REX2.W should be accepted if it results in the intended encoding,
    but notes that REX2.W does not have the same effect as REX.W.
  quote: 'We should accept it if the resulting encoding does what is intended / written.

    According to Christian''s reply REX2.W doesn''t have the same effect, but I wonder

    if it''s really sensible that way.'
primer_expert: The discussion concerns the x86 instruction `BHI_CTRL` and its encoding
  within binutils. Specifically, it delves into the interaction between the instruction's
  encoding and the REX prefix, particularly `REX.W` vs. `REX2.W`. The `Size64` flag
  in the opcode table is used to ensure `REX.W` is emitted, but there's ambiguity
  about `REX2.W`'s behavior and whether the disassembler should accept constructions
  like `{rex2} ibhf`. This touches on the precise semantics of REX prefixes in modern
  x86 extensions.
primer_glossary:
- term: BHI_CTRL
  definition: An x86 instruction related to Branch History Buffer control.
- term: REX prefix
  definition: An instruction prefix in x86 architecture used to extend the instruction
    set, including enabling 64-bit operands (REX.W).
- term: REX.W
  definition: The W bit in the REX prefix, which signifies a 64-bit operand size.
- term: REX2.W
  definition: An alternative REX prefix encoding that also controls operand size.
- term: disassembler
  definition: A tool that translates machine code back into human-readable assembly
    language.
- term: opcode table
  definition: A data structure used by assemblers and disassemblers to map instruction
    mnemonics and operands to their corresponding machine code.
- term: APX
  definition: Likely refers to AMD's Advanced Performance Extensions or a similar
    microarchitecture extension.
series_id: 20260601062446.2367458-1-haochen.jiang@intel.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/1cf7a0d1-c080-4adc-8c27-f5542a36c2e6@suse.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

This discussion revolves around the correct implementation of the `BHI_CTRL` instruction for x86 in binutils, particularly concerning the encoding and usage of REX prefixes. The initial patch proposed using `Size64` to ensure REX.W is emitted. A key point of debate is whether REX2.W should have the same effect as REX.W for this instruction, as the documentation is unclear. There's a call for a test case to clarify this behavior and ensure the disassembler handles potential ambiguities correctly.
