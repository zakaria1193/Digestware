---
project: binutils
subsystem: binutils
patch_id: null
tags:
- compiler
- ubsan
- disassembler
- tilepro
- tilegx
discussion_id: auJ2FsEJXYZ2MCyb@squeak.grove.modra.org
source_type: public_inbox
title: Undefined shift in print_insn_tilepro
headline: Fix undefined shift in tilepro/tilegx disassemblers
tldr: Changes integer operand values to unsigned to prevent undefined shift behavior.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The `print_insn_tilepro` and `print_insn_tilegx` functions, part of
  the opcodes library, disassemble instructions for the TilePro and TileGX processors.
  The `tilepro_decoded_instruction` and `tilegx_decoded_instruction` structures store
  operand values in `operand_values` fields. If these fields were signed integers
  (`int` or `long long`), and the most significant bit was set, a left shift operation
  on such a value is undefined behavior in C. This can lead to compiler warnings (like
  UBSan's signed integer overflow) or unexpected runtime behavior. By changing `operand_values`
  to `unsigned int`,…
primer_glossary:
- term: undefined behavior
  definition: Behavior that results from an implementation of a C/C++ program that
    depends on the platform, compiler, or other factors, and is not specified by the
    C/C++ language standards. It can lead to crashes, incorrect results, or security
    vulnerabilities.
- term: UBSan
  definition: Undefined Behavior Sanitizer. A runtime checker that detects various
    kinds of undefined behavior in C/C++ code.
- term: disassembler
  definition: A program that translates machine code (binary instructions) back into
    a human-readable assembly language format.
- term: operand
  definition: A value or variable on which an instruction operates.
- term: tilepro
  definition: A family of DSP processors from Tilera Corporation.
- term: tilegx
  definition: A family of multi-core processors from Tilera Corporation, successors
    to TilePro.
- term: signed integer
  definition: An integer data type that can represent positive and negative values,
    as well as zero. The most significant bit is typically used to indicate the sign.
- term: unsigned integer
  definition: An integer data type that can represent only non-negative values. All
    bits are used to represent the magnitude of the number.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ2FsEJXYZ2MCyb@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch prevents undefined shift behavior in the tilepro and tilegx disassemblers by changing the type of `operand_values` from `int` to `unsigned int`. This addresses a potential UBSan error when the top bit of a signed integer operand is set, which would lead to an undefined left shift. The change aligns the types with how values are stored and makes the code safer.
