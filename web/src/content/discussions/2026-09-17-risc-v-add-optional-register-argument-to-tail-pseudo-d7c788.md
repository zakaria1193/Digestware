---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- tail call
discussion_id: 4da18583-e522-40a3-ab07-9201ad061010@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add optional register argument to tail pseudo'
headline: 'RISC-V: Add optional register argument to tail pseudo'
tldr: Patch adds support for an optional register argument to the RISC-V 'tail' pseudo-instruction
  for software-guarded tail calls.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds flexibility to tail call implementation at the cost of slightly more complex
  assembly syntax.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Submits a patch to add an optional register argument to the RISC-V 'tail'
    pseudo-instruction, enabling software-guarded tail calls.
  quote: "The lpad instruction of Zicfilp is encoded using an auipc hint \nencoding,\
    \ so\nan instrumented binary still runs correctly on a CPU without Zicfilp.  For\n\
    that to work, compilers must be able to emit a software guarded tail call\nusing\
    \ t2 as the scratch register without Zicfilp appearing in the ISA\nstring.\n\n\
    Add `tail <symbol>, <rt>' for that, which expands the same way as\n`jump <symbol>,\
    \ <rt>'."
primer_expert: This patch affects the GNU Assembler (gas) for the RISC-V architecture.
  It adds support for a new operand to the `tail` pseudo-instruction, allowing a register
  to be specified as a scratch register. This is motivated by the Zicfilp extension's
  instruction encoding and the need for backward compatibility, enabling software-guarded
  tail calls that function correctly on older hardware.
primer_glossary:
- term: tail pseudo-instruction
  definition: A directive in assembly language that indicates a tail call, a function
    call that replaces the current stack frame instead of pushing a new one.
- term: Zicfilp
  definition: A RISC-V extension that provides instructions for profile-guided optimization,
    including features that can be leveraged for tail calls.
- term: software-guarded tail call
  definition: A tail call implemented using software instructions to ensure correctness,
    especially when hardware support might be absent or for compatibility reasons.
- term: scratch register
  definition: A general-purpose register used temporarily during computation, often
    for intermediate results or as a parameter for specific instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/4da18583-e522-40a3-ab07-9201ad061010@iscas.ac.cn
bugzilla_url: null
date: '2026-09-17'
is_stub: false
stub_reason: ''
---

This patch introduces support for an optional register argument to the RISC-V 'tail' pseudo-instruction. This addition enables compilers to emit software-guarded tail calls using a scratch register, ensuring correct execution even on CPUs that do not support the Zicfilp extension. The change includes modifications to gas test suites and opcode definitions.
