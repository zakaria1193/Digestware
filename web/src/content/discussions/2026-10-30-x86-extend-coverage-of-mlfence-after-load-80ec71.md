---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- security
- mitigation
discussion_id: 56d2ad7a-e47d-49c4-8735-99b3181180c1@suse.com
source_type: public_inbox
title: '[PATCH v2 1/3] x86: extend coverage of -mlfence-after-load'
headline: 'x86: extend coverage of -mlfence-after-load'
tldr: Expands the set of instructions that trigger -mlfence-after-load to include
  more loads that affect EFLAGS or subsequent memory accesses.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enhances security by providing broader coverage for speculative execution mitigations.
- May introduce a performance overhead due to more frequent `LFENCE` insertions.
exchanges: []
primer_expert: This patch modifies the `load_insn_p` function in `tc-i386.c` to include
  a wider range of instructions that should trigger an `LFENCE` insertion when `-mlfence-after-load`
  is enabled. It adds specific handling for instructions that read from memory and
  potentially affect EFLAGS or subsequent memory operations, such as LLDT, VERR/VERW,
  BT variants, SHLD/SHRD, ARPL, CMPXCHG, and certain VMX instructions.
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
- term: memory operand
  definition: An operand in an instruction that refers to a location in memory.
- term: VMX
  definition: Virtual Machine Extensions, a set of Intel processor features for supporting
    virtualization.
series_id: 'binutils:x86: extend coverage of -mlfence-after-load'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/56d2ad7a-e47d-49c4-8735-99b3181180c1@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch extends the coverage of the `-mlfence-after-load` option by identifying and including more x86 instructions that require an `LFENCE` to mitigate speculative execution vulnerabilities. Instructions like LLDT, VERR/VERW, BT variants, SHLD/SHRD, ARPL, CMPXCHG, and VMX instructions are now considered, ensuring broader protection.
