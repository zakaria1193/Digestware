---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- amx
- instruction-set
discussion_id: a43e419bf715044a6d1213f5e8c879437d3b2bc2.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 3/7] x86: templatize AMX_INT8 TDPB* instructions'
headline: 'x86: templatize AMX_INT8 TDPB* instructions'
tldr: Simplifies x86 assembler support for AMX_INT8 TDPB* instructions using a template.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Templatizing instructions reduces code size and improves maintainability but requires
  careful management of the template to ensure correctness for all instances.
- The use of a template for TDPB* instructions facilitates future extensions and reuse
  by other instruction families.
exchanges: []
primer_expert: This patch refactors the `opcodes/i386-opc.tbl` to use a template macro
  `<tdpb>` for the x86 AMX_INT8 TDPB* instructions (TDPBUUD, TDPBUSD, TDPBSSD, TDPBSUD).
  This templating approach consolidates the opcode definitions, making them more maintainable
  and allowing for potential reuse by other related instruction families like TOP4B*.
  The changes reduce redundancy in the instruction table.
primer_glossary:
- term: AMX_INT8
  definition: Refers to instructions within the Advanced Matrix Extensions (AMX) instruction
    set that operate on 8-bit integer data types.
- term: TDPB*
  definition: A family of x86 instructions related to tile data processing, likely
    involving byte-level operations within the AMX context.
- term: templatize
  definition: In programming, to create a template or a generalized form of code that
    can be instantiated multiple times with different parameters. In this context,
    it means using a macro or a pattern to define similar instructions concisely.
- term: iterator
  definition: A programming construct that allows traversal through a sequence of
    data items. In this context, it refers to a mechanism within the opcode table
    processing that can be reused for different instruction definitions.
series_id: 'binutils:x86: templatize amx_int8 tdpb* instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a43e419bf715044a6d1213f5e8c879437d3b2bc2.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch simplifies the assembly and disassembly definitions for the x86 AMX_INT8 TDPB* instructions by using a template. The `TDPBUUD`, `TDPBUSD`, `TDPBSSD`, and `TDPBSUD` instructions can now be represented more concisely using a `<tdpb>` macro, improving maintainability and reducing code duplication. This change also allows for reuse of the iterator by other instruction sets.
