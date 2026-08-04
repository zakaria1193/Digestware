---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- binutils
- gas
- xtensa
- relocation
- dwarf
discussion_id: 7e22e4c80ad1779e1a6b57df2b8ef7272146037a.camel@espressif.com
source_type: public_inbox
title: '[PATCH] xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
headline: 'xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
tldr: Introduces a new relocation type for Xtensa to better handle DWARF 5 uleb128
  differences, enabling linker relaxation for functions with debug info.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enables linker relaxation for functions with DWARF 5 debug info, potentially improving
  code size and performance.
- Introduces a new relocation type, increasing complexity in assembler and linker
  code.
- Falls back to `no_transform` for sleb128 and cross-section differences, and reports
  overflow for excessive growth.
exchanges:
- author: Alexey Lapshin <alexey.lapshin@espressif.com>
  role: proposer
  position: Proposes adding R_XTENSA_PDIFF_ULEB128 relocation type to support DWARF
    5 uleb128 differences, enabling linker relaxation for functions with debug info.
  quote: null
primer_expert: This patch targets the Xtensa toolchain support within GNU Binutils
  and GAS. It addresses a limitation in how DWARF 5 debug information uses `uleb128`
  to encode differences between symbol locations and range lists. Previously, the
  assembler had to prevent linker relaxation (`no_transform`) for code containing
  these `uleb128` differences, hindering optimization. This patch introduces a new
  relocation type (`R_XTENSA_PDIFF_ULEB128`) that allows the assembler to pad the
  `uleb128` value and the linker to rewrite it in place after relaxation, effectively
  re-enabling relaxation for such code sectio…
primer_glossary:
- term: DWARF 5
  definition: The fifth version of the DWARF debugging data format standard. It includes
    enhancements for representing debug information more efficiently and expressively.
- term: uleb128
  definition: Unsigned LEB128 (Little Endian Base 128) is a variable-length encoding
    format used for representing unsigned integers. It's compact for small numbers
    but can grow for larger ones.
- term: linker relaxation
  definition: An optimization process performed by the linker where it adjusts machine
    code to use shorter, more efficient instruction forms after the initial object
    code has been generated. This often involves changing absolute addresses or offsets
    to relative ones.
- term: no_transform
  definition: A flag or directive used in object files that tells the linker not to
    attempt any optimizations or modifications (like relaxation) on the associated
    code or data section.
- term: Xtensa
  definition: A configurable processor architecture commonly used in embedded systems.
    Toolchain support for Xtensa involves specific instructions and relocation types.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/7e22e4c80ad1779e1a6b57df2b8ef7272146037a.camel@espressif.com
bugzilla_url: null
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

This patch introduces a new relocation type, R_XTENSA_PDIFF_ULEB128, for the Xtensa architecture to improve the handling of unsigned LEB128 (uleb128) differences in DWARF 5 debug information. Previously, DWARF 5's use of uleb128 for symbol differences forced code containing this debug info to be marked `no_transform`, effectively disabling linker relaxation for nearly every function. The new relocation allows the linker to rewrite the padded uleb128 value in place after relaxation, thus enabling relaxation for functions with DWARF 5 debug info.
