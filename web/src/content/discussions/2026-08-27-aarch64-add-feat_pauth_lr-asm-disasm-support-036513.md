---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- assembler
- disassembler
- architecture
discussion_id: 20260827151014.9719-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH 0/7] aarch64: Add FEAT_PAuth_LR asm/disasm support'
headline: 'aarch64: Add FEAT_PAuth_LR asm/disasm support'
tldr: Adds assembler and disassembler support for AArch64's FEAT_PAuth_LR feature,
  including new instructions and a feature option.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Splitting generated files into separate commits aids review of manual changes but
  necessitates a final squashing step.
- Using internal assembler fixups for PC-relative addressing simplifies object file
  format but requires more complex assembler logic.
exchanges: []
primer_expert: This is the cover letter for a series of 7 patches that add support
  for the AArch64 FEAT_PAuth_LR extension to binutils' assembler (gas) and disassembler
  (objdump). FEAT_PAuth_LR enhances security by allowing the Link Register (LR) to
  be signed or authenticated using the Stack Pointer (SP) and Program Counter (PC)
  as diversifiers. The series introduces a new feature flag `+pauth-lr` (which implies
  `+pauth`), new instruction mnemonics for various forms of PAuth_LR (register operands,
  immediate PC-relative operands), and integrates these into the opcode tables and
  parsing logic. The series uses…
primer_glossary:
- term: FEAT_PAuth_LR
  definition: A specific AArch64 hardware feature extension for Pointer Authentication
    of the Link Register. It enhances security by protecting the LR register from
    corruption.
- term: Link Register (LR)
  definition: In ARM architectures, the LR register stores the return address for
    function calls. Protecting it is crucial for preventing control-flow hijacking
    attacks.
- term: Pointer Authentication (PAuth)
  definition: A security feature that uses cryptographic techniques to generate and
    verify pointers, making it harder for attackers to forge or corrupt pointers.
- term: diversifiers
  definition: Values used in conjunction with cryptographic operations (like pointer
    authentication) to create unique keys or context for each operation, enhancing
    security.
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language code into machine code.
- term: objdump
  definition: A utility that displays information from object files, including disassembly
    of machine code. It is part of binutils.
- term: internal fixup
  definition: A process within the assembler where it resolves addresses or offsets
    that depend on the final code layout, often without emitting explicit relocation
    information to the object file.
series_id: 'binutils:aarch64: add feat_pauth_lr asm/disasm support'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827151014.9719-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch series introduces assembler and disassembler support for the AArch64 FEAT_PAuth_LR (Pointer Authentication for Link Register) extension. The series adds a new `+pauth-lr` feature option that depends on `+pauth`, and incorporates new instruction mnemonics for pointer authentication of the LR register, including register and immediate PC-relative forms. The immediate PC-relative operand is handled as an internal gas fixup. The series is structured with intermediate commits for generated files to ease review of manual changes, with plans to squash them before upstream submission.
