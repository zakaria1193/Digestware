---
project: binutils
subsystem: gas
patch_id: null
tags:
- BPF
- gas
- assembler
- testing
- control flow
discussion_id: 87o6e7syqp.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH v4 3/4] gas: bpf: test `gotol'' in a compound conditional'
headline: 'BPF gas: Test `gotol` in compound conditional jumps'
tldr: BPF gas now includes a test case for `gotol` within compound conditional jumps,
  ensuring correct parsing and assembly.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures correct assembly of `gotol` within compound conditional jumps.
- Adds test coverage for a previously untested scenario.
- Validates the effectiveness of the `%t` specifier in distinguishing similar mnemonics.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Approves the patch for the master branch, acknowledging its importance
    in testing the `gotol` instruction within compound conditional jumps.
  quote: 'OK for master.

    Thanks!'
- author: Vineet Gupta
  role: proposer
  position: Introduces a test for the `gotol` instruction within compound conditional
    jumps in the BPF assembler.
  quote: 'Add a test for the compound forms, so the reordering alternative does not

    look equivalent to %t.  Verified that it fails when %t is replaced by the

    reordering: no diagnostic, and each of its three lines silently encoded as

    a conditional jump with a relocation against `l''.'
primer_expert: This patch introduces a new test suite (`jump-gotol-cond-pseudoc.*`)
  for the BPF gas assembler to specifically exercise the `gotol` instruction within
  compound conditional jumps. The context is that a previous fix only addressed standalone
  `gotol` by reordering opcodes, but compound conditional jumps use a different `goto`
  form. This test verifies that the `%t` token boundary specifier correctly distinguishes
  `gotol` from `goto` in these complex cases, preventing silent misassemblies and
  incorrect relocations that would occur if opcode reordering were the sole fix.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to safely execute code in the Linux kernel, often used for networking and tracing.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: gotol
  definition: A BPF assembler instruction, likely a variant of 'goto' with a specific
    operand format or target type.
- term: compound conditional jump
  definition: A control flow instruction in assembly that combines a conditional check
    with a jump, potentially involving multiple conditions or complex operand processing.
- term: Relocation
  definition: A process performed by the linker to adjust memory addresses in machine
    code after assembly, typically to resolve references to symbols or labels defined
    elsewhere.
series_id: 'binutils:gas: bpf: test `gotol'' in a compound conditional'
series_role: reply
series_parts:
- title: 'gas: bpf: test `gotol'' in a compound conditional'
  url: https://inbox.sourceware.org/binutils/20260908062940.2734221-4-vineet.gupta@linux.dev
  n: 3
  total: 4
- title: 'gas: bpf: test `gotol'' in a compound conditional'
  url: https://inbox.sourceware.org/binutils/20260907091102.2595057-5-vineet.gupta@linux.dev
  n: 4
  total: 5
url: https://inbox.sourceware.org/binutils/87o6e7syqp.fsf@gnu.org
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch adds a new test case to the BPF assembler's test suite to specifically cover the `gotol` instruction when used within compound conditional jumps. The existing fix for `gotol` only addressed standalone instances; compound conditional jumps embed a `goto%w%d16` form, making them susceptible to misassembly without this dedicated test. The new test verifies that the assembler correctly handles these scenarios, preventing silent failures and incorrect relocations.
