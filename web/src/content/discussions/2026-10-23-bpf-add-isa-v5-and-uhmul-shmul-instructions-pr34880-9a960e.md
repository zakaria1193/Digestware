---
project: binutils
subsystem: bpf
patch_id: null
tags:
- binutils
- gas
- bpf
- isa
- instructions
discussion_id: 20261023193350.93134-1-david.faust@oss.qualcomm.com
source_type: public_inbox
title: '[PATCH] bpf: add ISA v5 and uhmul,shmul instructions [PR34880]'
headline: 'bpf: add ISA v5 and uhmul,shmul instructions [PR34880]'
tldr: Adds support for BPF ISA version 5 and its new UHMUL/SHMUL instructions to the
  GNU Assembler.
proposer: David Faust <david.faust@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Updating the default ISA might affect existing code if new instructions are implicitly
  used or if default behavior changes.
- The new instructions' encoding relies on a field previously unused or used differently,
  requiring careful validation.
- Ensuring backward compatibility for older BPF versions if needed.
exchanges:
- author: David Faust
  role: proposer
  position: Submitted a patch to add support for BPF ISA version 5 and the new UHMUL/SHMUL
    instructions, updating the assembler and disassembler defaults.
  quote: 'This patch adds ISA v5 and support for the new instructions.


    As is custom for BPF, the default ISA selected by the assembler and

    disassembler is updated to the latest, now v5.'
- author: Jose E. Marchesi
  role: reviewer
  position: Reviewed the patch, specifically noting a detail in the opcodes/bpf-opc.c
    diff regarding the encoding of new instructions.
  quote: "Hi Faust.\n\n> diff --git a/opcodes/bpf-opc.c b/opcodes/bpf-opc.c\n> index\
    \ 05503c338ad..e59081e5664 100644\n> --- a/opcodes/bpf-opc.c\n> +++ b/opcodes/bpf-opc.c\n\
    > @@ -41,6 +41,14 @@ const struct bpf_opcode bpf_opcodes[] =\n>     BPF_V1, BPF_CODE,\
    \ BPF_CLASS_ALU64|BPF_CODE_SUB|BPF_SRC_X}, \n>    {BPF_INSN_SUBI, \"sub%W%dr ,\
    \ %i32\", \"%dr -= %i32\", \n>     BPF_V1, BPF_CODE, BPF_CLASS_ALU64|BPF_CODE_SUB|BPF_SRC…"
- author: Vineet Gupta
  role: contributor
  position: Suggested CC'ing Alexei and Yonghong on the patch.
  quote: +CC Alexei and Yonghong
- author: David Faust
  role: proposer
  position: Responded to Jose's comment and provided the full diff context again.
  quote: "On 10/23/26 1:29 PM, Jose E. Marchesi wrote:\n> \n> Hi Faust.\n> \n>> diff\
    \ --git a/opcodes/bpf-opc.c b/opcodes/bpf-opc.c\n>> index 05503c338ad..e59081e5664\
    \ 100644\n>> --- a/opcodes/bpf-opc.c\n>> +++ b/opcodes/bpf-opc.c\n>> @@ -41,6\
    \ +41,14 @@ const struct bpf_opcode bpf_opcodes[] =\n>>     BPF_V1, BPF_CODE,\
    \ BPF_CLASS_ALU64|BPF_CODE_SUB|BPF_SRC_X},\n>>    {BPF_INSN_SUBI, \"sub%W%dr ,\
    \ %i32\", \"%dr -= %i32\",\n>>…"
primer_expert: This patch adds support for the newly introduced BPF ISA version 5
  to GNU Binutils, specifically the assembler (gas) and disassembler. ISA v5 includes
  two new 64-bit multiply instructions, UHMUL and SHMUL, which are encoded as variants
  of the ALU64 MUL instruction by utilizing the offset16 field. The patch updates
  the assembler's configuration, opcode definitions, and documentation to reflect
  these changes, and sets BPF_V5 as the new default ISA.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, an in-kernel virtual machine and programming
    interface commonly used for network packet processing and system tracing.
- term: ISA
  definition: Instruction Set Architecture, defines the set of instructions that a
    processor can understand and execute.
- term: UHMUL
  definition: Unsigned High-half Multiply, a BPF instruction that performs a 64-bit
    multiplication and returns the most significant 64 bits of the result.
- term: SHMUL
  definition: Signed High-half Multiply, a BPF instruction that performs a signed
    64-bit multiplication and returns the most significant 64 bits of the result.
- term: ALU64
  definition: Arithmetic Logic Unit operating on 64-bit operands, a common component
    in modern processors and instruction sets like BPF.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    translating assembly language into machine code.
- term: PR34880
  definition: Patch Request number 34880, a unique identifier for a bug report or
    feature request in the binutils issue tracker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261023193350.93134-1-david.faust@oss.qualcomm.com
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

David Faust submits a patch to binutils to add support for BPF ISA version 5, which introduces two new instructions: UHMUL (unsigned high-half 64-bit multiply) and SHMUL (signed high-half 64-bit multiply). These instructions are encoded as variants of the ALU64 MUL instruction. The patch updates the assembler and disassembler to default to ISA v5 and includes necessary changes to opcode definitions and documentation.
