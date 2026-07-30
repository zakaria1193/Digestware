---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- aarch64
- disassembler
- debugging
- rfc
discussion_id: b966f89a-d3c9-1116-da51-867d2e7f144c@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: RFC: AArch64 Disassembler: Annotate undefined instructions'
headline: 'AArch64 Disassembler: Annotate undefined instructions'
tldr: Discussion questions the recent commit of an AArch64 disassembler feature that
  annotates undefined instructions, citing potential misinterpretations and limita…
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Providing more informative disassembly vs. potential for misinterpretation.
- Handling of undefined instructions and their addresses.
- Distinguishing between instruction encodings and arbitrary data.
exchanges:
- author: Alice Carlotti
  role: contributor
  position: Questions a recently committed feature that annotates undefined AArch64
    instructions, stating it appears to have been accepted despite issues with address
    handling, symbol support, and potential misinterpretations of data vs. instructions.
  quote: "The issues I see with it are that it:\n- Conflates 32-but values with 64-bit\
    \ address, with the full address displayed as:\n    411030:       0040065c   \
    \     .inst   0x0040065c ; [func1]\n    411034:       00000000        udf    \
    \ #0\n- Only supports symbols at addresses between 0 and 2^32-1\n- Only supports\
    \ 60% of the addresses in that range, since 40% of values are\n  recognised as\
    \ instructions.\n- Inte…"
primer_expert: This discussion revolves around a new feature in the AArch64 disassembler
  that attempts to provide more context for undefined instructions by annotating them
  with symbol information. The core issue is whether the implementation correctly
  resolves addresses and sufficiently distinguishes between actual executable code
  and arbitrary data that might coincidentally resemble instruction encodings, especially
  within the constraints of the AArch64 architecture.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, successor to AArch32.
- term: Disassembler
  definition: A tool that translates machine code (binary instructions) back into
    human-readable assembly language.
- term: Undefined Instruction
  definition: An instruction that is not recognized by the processor's instruction
    set, often resulting in an exception or specific behavior.
- term: .inst
  definition: An assembler directive that inserts raw machine code bytes into the
    output.
- term: Symbol
  definition: A name given to a location in the code or data, such as a function name
    or a variable name, used by the linker and debugger.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/b966f89a-d3c9-1116-da51-867d2e7f144c@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

Alice Carlotti expresses concern that a recently committed feature in the AArch64 disassembler, which annotates undefined instructions, was accepted despite perceived issues. She argues it conflates 32-bit values with 64-bit addresses, has limited symbol address support, and may misinterpret instruction contents as data, questioning the value of the annotations.
