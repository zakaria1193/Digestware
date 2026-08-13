---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gdb
- dwarf
- debugging
- intel
discussion_id: 20260812132805.380163-32-markus.t.metzger@intel.com
source_type: public_inbox
title: '[PATCH v4 31/44] gdb, dwarf, ze: add DW_OP_INTEL_regval_bits'
headline: 'gdb, dwarf, ze: add DW_OP_INTEL_regval_bits'
tldr: Adds support for the new DWARF expression DW_OP_INTEL_regval_bits, which allows
  accessing specific bit ranges within registers.
proposer: Markus Metzger <markus.t.metzger@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Extends DWARF expression capabilities to precisely access bit fields within registers.
- Requires modifications in both binutils (for decoding) and gdb (for evaluation).
exchanges: []
primer_expert: This patch series introduces support for `DW_OP_INTEL_regval_bits`,
  an Intel-proposed extension to the DWARF expression language. It enables debuggers
  to precisely extract bit-fields from registers, which is crucial for debugging hardware-level
  features or specific bitwise manipulations. The changes span binutils' DWARF decoding
  logic and gdb's expression evaluation engine, including a new helper function `read_reg`
  in gdb to handle bitwise extraction from register contents.
primer_glossary:
- term: DW_OP_INTEL_regval_bits
  definition: A proposed Intel extension to DWARF expressions that allows fetching
    a specific range of bits from a register.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about compiled programs, enabling features like source-level debugging.
- term: Expression
  definition: In DWARF, a sequence of operations that calculates a value, often used
    to describe the location or value of a variable or piece of data.
- term: Register
  definition: A small, fast storage location within a CPU that holds data and instructions
    currently being processed.
- term: ZE
  definition: Likely refers to 'Zero Extension' or a related concept within Intel's
    extensions, possibly related to how register bits are handled.
series_id: 'binutils:gdb, dwarf, ze: add dw_op_intel_regval_bits'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260812132805.380163-32-markus.t.metzger@intel.com
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This patch adds support for a new DWARF opcode, `DW_OP_INTEL_regval_bits`, proposed by Intel. This opcode allows debuggers to read specific bit ranges from registers, extending the capabilities of DWARF expressions for more precise debugging information. The implementation involves changes in binutils (for DWARF decoding) and gdb (for expression evaluation), including functions to safely read and copy bit segments from registers.
