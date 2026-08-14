---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocations
- optimization
discussion_id: 20260813170736.1880481-3-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 2/3] LoongArch: Optimize TC_FORCE_RELOCATION_SUB_LOCAL'
headline: 'LoongArch: Optimize TC_FORCE_RELOCATION_SUB_LOCAL'
tldr: Avoid ADD/SUB relocations by using PC-relative fixups when possible.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reduces ADD/SUB relocations at the potential cost of slightly more complex relocation
  handling logic.
- Improves code generation efficiency by using PC-relative fixups where applicable.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to change fixups to PC-relative to avoid ADD/SUB relocations
    when linker-relaxable instructions are absent between a subtraction symbol and
    PC.
  quote: null
primer_expert: This patch modifies gas/config/tc-loongarch.c to optimize relocation
  generation for LoongArch. It refactors the `loongarch_force_relocation_sub_local`
  logic to conditionally use PC-relative fixups instead of ADD/SUB relocations when
  certain conditions related to linker relaxation and instruction segments are met.
  This change affects how the assembler handles symbolic arithmetic expressions and
  aims to reduce the overhead of specific relocation types.
primer_glossary:
- term: relocation
  definition: Information embedded in an object file that describes how to modify
    symbolic addresses and constants when linking. It tells the linker which parts
    of the code or data need to be adjusted based on the final memory layout.
- term: linker relaxation
  definition: A linker optimization that allows it to substitute shorter, faster instructions
    for longer ones if the target address is known to be close enough. This can involve
    changing instruction opcodes and relocation types.
- term: PC-relative
  definition: A type of address calculation where the offset is relative to the current
    program counter (PC). This is common for position-independent code.
- term: ADD/SUB relocations
  definition: Specific relocation types used by the assembler/linker to represent
    the result of an addition or subtraction between symbols or constants. These can
    sometimes be optimized away.
series_id: 'binutils:loongarch: optimize tc_force_relocation_sub_local'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813170736.1880481-3-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch optimizes relocation handling for LoongArch by changing fixups to be PC-relative when no linker-relaxable instructions are present between a subtraction symbol and the program counter. This aims to reduce the emission of ADD/SUB relocations, improving code generation efficiency.
