---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- assembler
- instruction set
- review
discussion_id: 87zewjja5c.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH v3 5/6] bpf: add the gotox indirect jump instruction'
headline: 'bpf: add the gotox indirect jump instruction'
tldr: Reviewer confirms 'ja' is a suitable mnemonic for the BPF gotox instruction.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures clear and accurate naming conventions for assembly instructions.
- Addresses potential confusion with existing mnemonics.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Initially questioned the choice of 'ja' for the BPF gotox instruction
    but accepted the explanation regarding its PC-relative displacement handling.
  quote: 'Any reason for not using the existing name `jal'' with a register operand

    rather than introducing `ja''?'
- author: Vineet Gupta
  role: proposer
  position: Explains that 'ja' is suitable because the instruction supports both short
    and long displacements, unlike 'jal'.
  quote: 'currently JA and JAL do PC-relative 16 and 32-bit displacements

    respectively, so a 64-bit abs addr can map to either.'
primer_expert: This is a review comment on the `gotox` instruction patch within the
  BPF instruction series. The discussion focuses on the assembler mnemonic `ja` versus
  `jal`. The key point is that the BPF `ja` instruction supports both short (16-bit)
  and long (32-bit) PC-relative displacements, making it a suitable choice for an
  indirect jump that needs to cover a wide range, whereas `jal` historically implies
  a 'long' jump. This clarification resolves the reviewer's concern.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows programs to be run
    in the Linux kernel without altering kernel source code. It's often used for network
    packet filtering and more general in-kernel computation.
- term: gotox
  definition: A BPF instruction for indirect jumps, used for jump tables, similar
    to `goto` in C.
- term: indirect jump
  definition: A jump instruction where the target address is determined at runtime,
    typically by the value in a register or memory location.
- term: assembler mnemonic
  definition: A symbolic name given to an assembly language instruction, such as 'mov',
    'add', or 'jmp'.
- term: PC-relative displacement
  definition: An offset added to the program counter (PC) to determine the target
    address of a jump or branch instruction.
series_id: 'binutils:bpf: add the gotox indirect jump instruction'
series_role: reply
series_parts:
- title: 'bpf: add the gotox indirect jump instruction'
  url: https://inbox.sourceware.org/binutils/dadd3ee1-f2df-4842-ad75-06109af643f7@linux.dev
  n: 5
  total: 6
- title: 'bpf: add the gotox indirect jump instruction'
  url: https://inbox.sourceware.org/binutils/87cxtfm8zj.fsf@gnu.org
  n: 5
  total: 6
- title: 'bpf: add the gotox indirect jump instruction'
  url: https://inbox.sourceware.org/binutils/20261012081159.2015930-6-vineet.gupta@linux.dev
  n: 5
  total: 6
url: https://inbox.sourceware.org/binutils/87zewjja5c.fsf@gnu.org
bugzilla_url: null
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This discussion revolves around the naming of a new BPF instruction, `gotox`, which provides an indirect jump. The reviewer, Jose E. Marchesi, initially questioned why `ja` was chosen over `jal`. The proposer clarifies that `ja` is appropriate because the instruction handles both short (16-bit) and long (32-bit) PC-relative displacements, unlike `jal` which specifically implies a long jump. The reviewer accepts this explanation.
