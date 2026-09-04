---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bpf
- assembler
- parsing
- goto
- linker
discussion_id: 4bad5b00-5758-4b73-a49a-aaba5022b5b9@linux.dev
source_type: public_inbox
title: 'Re: [PATCH v2 2/2] PR 34558: bpf: don''t mis-assemble `gotol'' with signed
  offset'
headline: 'BPF assembler: Fix `gotol'' and `goto'' mnemonic parsing'
tldr: Corrects BPF assembler to handle `gotol' and `goto' mnemonics with flexible
  spacing and signed offsets.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reordering the opcode table is a less invasive change than modifying the core parsing
  logic.
- Ensures compatibility with existing BPF assembly syntax, including flexible spacing.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Explains that the `%W` template approach is insufficient due to whitespace
    handling and flexible operand spacing.
  quote: 'Yet another reason the %w approach won''t work.

    Anyways....


    I don''t understand that implication.'
- author: Jose E. Marchesi
  role: reviewer
  position: Proposes reordering the opcodes table as a fix for existing issues with
    `goto` and `gotol` mnemonics.
  quote: 'In any case, wouldn''t simply reordering the opcodes table like below fix

    the existing broken issues without having to add special casing to the

    generic template-based parser?  Something like this passes the new test:'
primer_expert: This exchange delves into the intricacies of the BPF assembler's instruction
  parsing, specifically the `goto` and `gotol` mnemonics. The problem stems from how
  `gas` handles whitespace and parses operands, which affects the flexibility of writing
  BPF assembly. The discussion revolves around fixing PR 34558 by potentially reordering
  the opcode table to ensure correct assembly of these instructions with signed offsets
  and varying spacing.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter. A technology that allows for safe and efficient
    execution of custom code within the Linux kernel, often used for networking and
    security tasks.
- term: PR 34558
  definition: Problem Report number 34558, referring to a specific bug or issue filed
    in the binutils bug tracking system.
- term: mnemonic
  definition: A symbolic name that represents a machine language instruction, used
    in assembly language.
- term: gas
  definition: The GNU Assembler, part of the GNU toolchain, used to translate assembly
    language code into machine code.
series_id: 'binutils:pr 34558: bpf: don''t mis-assemble `gotol'' with signed offset'
series_role: reply
series_parts:
- title: 'PR 34558: bpf: don''t mis-assemble `gotol'' with signed offset'
  url: https://inbox.sourceware.org/binutils/8733vq2vzy.fsf@gnu.org
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/4bad5b00-5758-4b73-a49a-aaba5022b5b9@linux.dev
bugzilla_url: null
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

Vineet Gupta and Jose E. Marchesi discuss the nuances of parsing BPF assembler instructions, specifically the `goto` and `gotol` mnemonics. The conversation clarifies that the assembler must support flexible spacing around operands and signs, and that whitespace handling by `gas` can interfere with this. They explore solutions involving reordering opcode tables to correctly assemble instructions like `gotol` and `goto` with signed offsets, addressing issues highlighted in PR 34558.
