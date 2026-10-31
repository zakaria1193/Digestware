---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- optimization
- security
discussion_id: f981e7b1-a333-4e84-89c0-b2d8107dcd41@suse.com
source_type: public_inbox
title: '[PATCH v2 2/3] x86: limit coverage of -mlfence-after-load'
headline: 'x86: limit coverage of -mlfence-after-load'
tldr: Refines the -mlfence-after-load option by excluding instructions that do not
  affect EFLAGS or subsequent memory accesses.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reduces unnecessary `LFENCE` insertions, potentially improving performance.
- Narrows the scope of the security mitigation, relying on other mechanisms for instructions
  not covered.
exchanges: []
primer_expert: This patch adjusts the `load_insn_p` function in `tc-i386.c` which
  determines whether an instruction warrants an `LFENCE` insertion due to the `-mlfence-after-load`
  option. It removes several instructions (POP, NOT, certain shifts/rotates, LIDT,
  INVPCID) from the set that trigger `LFENCE`, as they do not modify EFLAGS or affect
  subsequent memory operations in a way that necessitates this mitigation.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures (ISAs) for CPUs, commonly
    used in personal computers and servers.
- term: -mlfence-after-load
  definition: An assembler option that controls the insertion of an LFENCE (load fence)
    instruction after certain load operations.
- term: LFENCE
  definition: A processor instruction that orders memory loads, preventing subsequent
    loads from being reordered before it.
- term: EFLAGS
  definition: A special register in x86 architecture that stores status flags and
    control bits, modified by many instructions.
- term: instruction
  definition: A command that a CPU can execute.
series_id: 'binutils:x86: limit coverage of -mlfence-after-load'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f981e7b1-a333-4e84-89c0-b2d8107dcd41@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch refines the `-mlfence-after-load` option by excluding several x86 instructions that were previously covered but do not impact EFLAGS or subsequent memory accesses. Instructions like POP with memory operands, NOT, certain shift/rotate operations, LIDT, and INVPCID are now excluded from triggering an `LFENCE` insertion.
