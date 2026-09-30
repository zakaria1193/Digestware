---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- ace
- amx
- assembler
- disassembler
discussion_id: b117c00537d1b432398465a95a36320ce935989d.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 6/7] x86: add ACE v1 support for tile move instructions'
headline: 'x86: add ACE v1 support for tile move instructions'
tldr: Adds assembler and disassembler support for ACE v1 tile move instructions (TILEMOVROW,
  TILEMOVCOL).
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Using VexGd instead of VexGdq with W=1 for the 32-bit register selector ensures
  correct encoding and disassembly, avoiding potential misinterpretation of register
  size.
- The changes involve modifications to multiple disassembler header files and the
  main C file, indicating a thorough integration effort.
exchanges: []
primer_expert: This patch adds support for ACE v1 tile move instructions (TILEMOVROW,
  TILEMOVCOL) to binutils. It specifically handles the EVEX encoding, noting that
  the register selector is 32-bit but VexGdq with W=1 defaults to a 64-bit register
  display. The solution uses VexGd to ensure correct assembly and disassembly. Test
  cases for x86-64 ACE v1 are included.
primer_glossary:
- term: ACE v1
  definition: Refers to the first version of the AI Compute Extensions (ACE) specification,
    a set of x86 instructions designed for AI and high-performance computing tasks.
- term: TILEMOVROW
  definition: An x86 instruction that moves data between tiles in a row-wise manner,
    part of the AMX (Advanced Matrix Extensions) instruction set.
- term: TILEMOVCOL
  definition: An x86 instruction that moves data between tiles in a column-wise manner,
    also part of the AMX instruction set.
- term: VEX
  definition: Vector Extensions. A prefix byte used in newer x86 instruction sets
    (like AVX) to extend the instruction set and support wider vector registers.
- term: EVEX
  definition: Enhanced Vector Extensions. A more advanced prefix used in AVX-512 and
    later instruction sets, offering greater flexibility and support for longer vectors.
series_id: 'binutils:x86: add ace v1 support for tile move instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b117c00537d1b432398465a95a36320ce935989d.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch enables assembler and disassembler support for the x86 ACE v1 instructions TILEMOVROW and TILEMOVCOL. It addresses an issue where the register selector is always 32-bit, but using VexGdq with W=1 incorrectly prints a 64-bit register. The fix ensures correct representation by using VexGd instead. The changes are detailed in the AI Compute Extensions (ACE) Specification v1.16.2.
