---
project: gcc
subsystem: gcc
patch_id: null
tags:
- RTL
- register allocation
- constraints
- ICE
discussion_id: 183098e4-f9d3-4c67-8155-1ec5367df812@gjlay.de
source_type: public_inbox
title: register_operand in non-strict RTL
headline: Inquiry About register_operand in Non-Strict RTL
tldr: Georg-Johann Lay asks whether a register_operand in non-strict RTL can contain
  a REG_P register that doesn't satisfy the operand's constraint.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This question concerns the validity of register operands in RTL (Register
  Transfer Language) before register allocation. RTL is an intermediate representation
  used by GCC. Non-strict RTL refers to a state where certain constraints might not
  be fully enforced, particularly before register allocation has assigned concrete
  registers. The question concerns the interaction between insn predicates (conditions
  that must be true for an instruction to be valid) and insn constraints (restrictions
  on the type of registers that can be used).
primer_general: This email asks a question about GCC's internal representation of
  code, called RTL (Register Transfer Language). RTL is used by the compiler to represent
  the program's instructions in a way that's easier to optimize. The email concerns
  the rules about what kind of registers can be used in RTL instructions, specifically
  whether a register can be used even if it doesn't perfectly match the requirements
  of the instruction. This is important for ensuring that the compiler generates correct
  code and doesn't crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/183098e4-f9d3-4c67-8155-1ec5367df812@gjlay.de
bugzilla_url: null
date: '2026-05-29'
is_stub: false
---

Georg-Johann Lay is investigating ICEs (internal compiler errors) occurring during register allocation with certain RTL test cases and asks about the validity of register_operand usage in non-strict RTL. Specifically, he questions whether a register_operand can hold a REG_P register that doesn't meet the operand's constraint, assuming the register meets register_operand criteria and the machine mode matches. He believes this is allowed before register allocation, with insn predicates taking precedence over insn constraints, and wants to confirm this understanding.
