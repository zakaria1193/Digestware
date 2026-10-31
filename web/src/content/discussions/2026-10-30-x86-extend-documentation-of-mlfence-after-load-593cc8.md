---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- documentation
- security
discussion_id: af213db6-d078-4571-962e-df3774ac9edf@suse.com
source_type: public_inbox
title: '[PATCH v2 3/3] x86: extend documentation of -mlfence-after-load'
headline: 'x86: extend documentation of -mlfence-after-load'
tldr: Clarifies the scope of the -mlfence-after-load option in the assembler documentation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves clarity of assembler options.
- No functional code change, only documentation update.
exchanges: []
primer_expert: This change updates the documentation for the `-mlfence-after-load`
  assembler flag. Previously, it was broadly stated to apply after 'load instructions'.
  This update clarifies that it's targeted towards specific loads that might affect
  speculative execution in the context of Spectre/Meltdown (Intel SA-00334) by inserting
  an `LFENCE` instruction, and that not all load instructions are covered.
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
- term: ISA
  definition: Instruction Set Architecture. The set of commands a processor understands.
- term: Intel SA-00334
  definition: A security advisory from Intel related to speculative execution vulnerabilities
    (like Spectre and Meltdown) that led to mitigation techniques like the insertion
    of fences.
series_id: 'binutils:x86: extend documentation of -mlfence-after-load'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/af213db6-d078-4571-962e-df3774ac9edf@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This documentation update clarifies the behavior of the `-mlfence-after-load` option in the x86 assembler. It specifies that the option applies to ISAs affected by Intel SA-00334 and affects load instructions that alter registers used in subsequent memory accesses, rather than all load instructions.
