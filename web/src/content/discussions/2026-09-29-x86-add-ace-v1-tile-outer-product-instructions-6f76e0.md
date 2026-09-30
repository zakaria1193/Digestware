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
discussion_id: 521814471f9493bdab4ff0a646bebfcd2e7d8ee9.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 7/7] x86: add ACE V1 tile outer product instructions'
headline: 'x86: add ACE V1 tile outer product instructions'
tldr: Adds assembler and disassembler support for ACE V1 tile outer product instructions.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding support for new instruction sets requires extensive modifications to opcode
  tables and disassembler logic, increasing maintenance overhead.
- The use of EVEX encoding for these instructions necessitates careful handling of
  prefix bytes and register specifiers to ensure correct assembly and disassembly.
exchanges: []
primer_expert: This is the final patch in a series adding ACE v1 support. It specifically
  targets the tile outer product instructions (TOP2BF16PS, TOP4B*, TOP4MX*). The patch
  modifies opcode tables and disassembler logic to correctly parse and format these
  instructions, referencing the ACE v1 Specification. It includes new test cases and
  updates to the `gas/NEWS` file.
primer_glossary:
- term: ACE V1
  definition: Refers to the first version of the AI Compute Extensions (ACE) specification,
    a set of x86 instructions designed for AI and high-performance computing tasks.
- term: tile outer product
  definition: A matrix operation that computes the outer product of two vectors, where
    the vectors are represented as tiles. These instructions are crucial for accelerating
    matrix multiplication and other deep learning workloads.
- term: TOP2BF16PS
  definition: A specific x86 instruction for computing a tile outer product using
    16-bit Brain Floating Point (BF16) precision.
- term: TOP4B*
  definition: A family of x86 instructions for tile outer products, likely operating
    on 4-byte data types.
- term: TOP4MX*
  definition: Another family of x86 instructions for tile outer products, possibly
    involving mixed-precision operands.
series_id: 'binutils:x86: add ace v1 tile outer product instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/521814471f9493bdab4ff0a646bebfcd2e7d8ee9.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch enhances binutils by adding assembler and disassembler support for several x86 ACE V1 tile outer product instructions: TOP2BF16PS, TOP4B*, and TOP4MX*. The changes include updates to the NEWS file, test suites, and various opcode and disassembler-related header files. This brings comprehensive support for these advanced matrix operations to the toolchain.
