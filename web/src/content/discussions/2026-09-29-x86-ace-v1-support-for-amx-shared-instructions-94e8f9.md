---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- ACE
- AMX
- tile instructions
discussion_id: f330ab714f3d252cf3971323449f8a4da149b289.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 4/7] x86: ACE V1 support for AMX-shared instructions'
headline: 'x86: ACE V1 support for AMX-shared instructions'
tldr: Enables ACE V1 architecture to reuse existing AMX instructions for tile management,
  row moves, and row converts.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Reuses existing AMX code, simplifying ACE V1 integration.
- Expands the scope of AMX-shared instructions to include ACE V1.
exchanges: []
primer_expert: This change integrates the ACE V1 architecture into binutils by reusing
  existing AMX-related functionality. It updates `gas/config/tc-i386.c` to include
  `ACE_V1` as a supported CPU architecture, and modifies `opcodes/i386-opc.tbl` and
  test suites to ensure that AMX-shared instructions are correctly associated with
  ACE V1. This allows ACE V1 to leverage the groundwork laid for AMX, simplifying
  its implementation.
primer_glossary:
- term: ACE V1
  definition: AI Compute Extensions version 1, a set of x86 instructions designed
    to accelerate AI and machine learning workloads.
- term: AMX
  definition: Advanced Matrix Extensions, an x86 instruction set extension for accelerating
    matrix operations.
- term: TMM registers
  definition: Tile Matrix Multiply registers, used by AMX for matrix operations.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: opcodes
  definition: The part of an instruction that specifies the operation to be performed.
    In binutils, 'opcodes' refers to the component responsible for instruction decoding
    and encoding.
series_id: 'binutils:x86: ace v1 support for amx-shared instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f330ab714f3d252cf3971323449f8a4da149b289.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch enables the ACE V1 architecture and allows it to reuse existing AMX-shared instructions for tile management, row moves, and row converts. It also permits the usage of TMM registers under the ACE_V1 architecture, aligning with the ACE specification.
