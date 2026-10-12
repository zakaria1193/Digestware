---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- assembler
- instruction set
discussion_id: 9d16bd90-0e2c-41d2-b08b-46c374371173@linux.dev
source_type: public_inbox
title: 'Re: [PATCH] bpf: add the addr_space_cast instruction'
headline: 'bpf: add the addr_space_cast instruction'
tldr: Adds the BPF addr_space_cast instruction to gas and includes tests.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds new functionality to the assembler.
- Requires careful handling of instruction encoding and testing across different architectures
  (endianness).
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.com>
  role: proposer
  position: Responds to review feedback, confirms `addr_space_cast` is not tied to
    a specific ISA version and explains why, and states big-endian tests have been
    added.
  quote: "As implemented today it is not tied to the ISA version. Verifier accepts\
    \ \naddr_space_cast for any program that has arena associated with it.\nclang\
    \ behaves the same way. GCC gating it on something would thus be \ndifferent,\
    \ unnecessary and painful for no real gains."
- author: Jose E. Marchesi
  role: reviewer
  position: Reviewed the patch, initially asking for justification for ISA version
    availability and suggesting big-endian tests, which were later added.
  quote: 'I would add at least one test for big-endian, using some of the 0,1 and

    1,0 address space combinations.'
primer_expert: This patch introduces the `addr_space_cast` instruction to `gas` for
  the BPF target, modifying `include/opcode/bpf.h` and potentially `gas/config/tc-bpf.c`.
  The instruction, which is essentially a `mov` with specific encoding for address
  space manipulation (generic `0` and arena `1`), is being added to support BPF arenas.
  The discussion clarifies that this instruction is not ISA-version-specific, mirroring
  `clang`'s behavior.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows programs to be run
    in the Linux kernel without altering kernel source code. It's often used for network
    packet filtering and more general in-kernel computation.
- term: addr_space_cast
  definition: A BPF instruction used to cast between different address spaces, specifically
    generic and arena address spaces.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly language code into machine code.
- term: immediate
  definition: A value that is explicitly written into an instruction, rather than
    being fetched from memory or a register.
- term: ISA
  definition: Instruction Set Architecture, the set of commands a CPU understands.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/9d16bd90-0e2c-41d2-b08b-46c374371173@linux.dev
bugzilla_url: null
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

This patch adds support for the BPF `addr_space_cast` instruction in the GNU Assembler (gas). This instruction is used for casting between generic and arena address spaces. The proposer clarifies that the instruction is available across all ISA versions, aligning with `clang`'s behavior, and has incorporated reviewer feedback by adding big-endian tests.
