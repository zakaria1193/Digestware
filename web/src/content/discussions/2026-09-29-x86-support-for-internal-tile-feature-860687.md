---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- ACE
- AMX
- assembler
discussion_id: 1d2f32c004a7bd4e35c075699dcf88879400b730.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 1/7] x86: support for internal ''TILE'' feature'
headline: 'x86: support for internal ''TILE'' feature'
tldr: Adds an internal 'TILE' pseudo-ISA bit to represent instructions shared by AMX_TILE
  and ACE_V1.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces an internal abstraction ('TILE') to manage shared functionality between
  two ISAs.
- Increases code complexity by adding a new feature flag and its associated logic.
exchanges: []
primer_expert: This patch defines an internal feature flag, `cputile`, in `gas/config/tc-i386.c`
  and associated test cases. This flag groups instructions and register usage common
  to both AMX_TILE and ACE_V1. It is implemented as a pseudo-ISA bit, meaning it's
  not a hardware feature itself but a way for binutils to manage shared functionality.
  The implementation ensures that `cputile` is enabled when either AMX_TILE or ACE_V1
  is enabled, and correctly handles its interaction with other CPU features.
primer_glossary:
- term: pseudo-ISA bit
  definition: An internal flag or bit used by the assembler or compiler to represent
    a set of features or instructions that do not correspond to a single, distinct
    hardware ISA extension. It helps in managing shared functionality.
- term: AMX_TILE
  definition: A subset of the Advanced Matrix Extensions (AMX) instruction set, focused
    on tile-related operations.
- term: ACE V1
  definition: AI Compute Extensions version 1, a new x86 instruction set extension.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: ISA
  definition: Instruction Set Architecture. The set of commands a processor can execute.
series_id: 'binutils:x86: support for internal ''tile'' feature'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/1d2f32c004a7bd4e35c075699dcf88879400b730.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch introduces an internal pseudo-ISA bit named 'TILE' within binutils. This feature represents a shared subset of instructions and registers between AMX_TILE and the upcoming ACE V1 architecture, specifically for tile management operations like LDTILECFG, STTILECFG, TILERELEASE, and TILEZERO.
