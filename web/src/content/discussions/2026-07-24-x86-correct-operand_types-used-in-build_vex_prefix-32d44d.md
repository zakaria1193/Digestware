---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- gas
- correctness
- vector-extensions
discussion_id: b8d583cc-7932-4c63-b96c-c60c7fae55b4@suse.com
source_type: public_inbox
title: '[PATCH 2/4] x86: correct operand_types[] used in build_vex_prefix()'
headline: 'x86: correct operand_types[] used in build_vex_prefix()'
tldr: Fixes incorrect operand type access in VEX prefix generation for x86.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Corrects a potential bug by using the appropriate operand type data structure.
- Ensures accurate VEX prefix generation, which is crucial for advanced x86 instructions.
exchanges: []
primer_expert: This patch addresses a correctness issue in `gas/config/tc-i386.c`
  concerning the generation of VEX prefixes on x86. The `build_vex_prefix` function
  was incorrectly accessing `t->operand_types[]`. Due to potential updates to the
  `insn_template` (`t`) earlier in the function, the correct operand types are now
  maintained in the global `i.tm_types[]` structure. This patch ensures `build_vex_prefix`
  uses `i.tm_types[]` for accurate operand type checks, resolving a subtle bug that
  was previously benign.
primer_glossary:
- term: VEX prefix
  definition: Vector Extension prefix, used in x86 instructions to extend functionality,
    particularly for SIMD operations.
- term: operand_types[]
  definition: An array specifying the type of each operand for an instruction.
- term: build_vex_prefix()
  definition: A function within the assembler that constructs the VEX prefix for x86
    instructions.
- term: insn_template
  definition: A structure defining the properties and operands of an assembly instruction.
- term: tc-i386.c
  definition: The C source file containing the configuration and logic for the Intel
    386 (x86) architecture in the GNU assembler (gas).
series_id: 'binutils:x86: correct operand_types[] used in build_vex_prefix()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b8d583cc-7932-4c63-b96c-c60c7fae55b4@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

Jan Beulich's second patch in a series corrects an issue in the `build_vex_prefix` function within `tc-i386.c`. Previously, it might have accessed outdated operand type information. This patch ensures it uses the correct, potentially updated, operand types stored in `i.tm_types[]` rather than directly from the `insn_template`.
