---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- assembly
- opcode
discussion_id: 2855a581-d751-4a5b-97cd-dc1e47721166@suse.com
source_type: public_inbox
title: '[PATCH v2] x86: introduce <hl> template'
headline: 'x86: introduce <hl> template'
tldr: Introduces a new <hl> template in binutils' i386-opc.tbl to simplify the definition
  of instruction pairs involving high/low byte operations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces redundancy in opcode definitions, improving maintainability.
- Introduces a new abstraction that requires understanding.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes adding a new <hl> template to the i386-opc.tbl to abstract common
    instruction patterns, aiming to reduce code duplication.
  quote: <hl:mov:fp:int:mul:shuf:rep:opsz, h:4:1:8:e5:f3:f2:, l:0:0:0:d5:f2:f3:66>
primer_expert: This patch modifies binutils' opcode table (`i386-opc.tbl`) for x86
  architecture. It introduces a new template `<hl>` to abstract common prefixes and
  opcodes for instruction pairs, such as `PMULHW` and `PMULLW`, which have related
  high/low byte variations. This aims to reduce the boilerplate in defining similar
  instructions, especially with the addition of new instruction extensions.
primer_glossary:
- term: opcodes
  definition: The part of a machine language instruction that specifies the operation
    to be performed.
- term: i386-opc.tbl
  definition: A table file used by binutils to define the opcodes and instruction
    formats for the Intel 386 and compatible architectures.
- term: template
  definition: In this context, a macro-like construct within the opcode table definition
    that allows for reusable definitions of instruction patterns.
- term: x86
  definition: A family of instruction set architectures (ISAs) developed by Intel,
    commonly used in personal computers and servers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2855a581-d751-4a5b-97cd-dc1e47721166@suse.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This patch introduces a new template `<hl:mov:fp:int:mul:shuf:rep:opsz, h:4:1:8:e5:f3:f2:, l:0:0:0:d5:f2:f3:66>` into the binutils opcodes table for x86. The goal is to reduce redundancy in defining instruction pairs that share similar patterns, particularly those involving high and low byte operations. This template aims to cover various instructions like MOV, FP, INT, MUL, SHUF, REP, and OPSZ, streamlining the opcode table maintenance.
