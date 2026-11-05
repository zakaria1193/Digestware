---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- opcode
discussion_id: 9b41c822-c9df-090b-0cbf-7d650f4b1937@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 13/28] aarch64: Remove multiple opcode table handling'
headline: 'aarch64: Remove multiple opcode table handling'
tldr: Simplifies AArch64 opcode handling by removing support for multiple opcode tables.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes complexity by eliminating support for a feature that is not in active use.
- Simplifies the AArch64 opcode handling logic.
exchanges: []
primer_expert: The patch cleans up `aarch64-gen.c` by removing code related to handling
  multiple opcode tables. Since only a single table is actively used and the existing
  code often hardcodes `aarch64_opcode_table`, this cleanup simplifies the logic and
  removes dead code.
primer_glossary: []
series_id: 'binutils:aarch64: remove multiple opcode table handling'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9b41c822-c9df-090b-0cbf-7d650f4b1937@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch removes the code that provided incomplete support for multiple opcode tables in `aarch64-gen.c`. Currently, only one opcode table is in use, and much of the existing machinery already assumes this. Removing this unnecessary and confusing code simplifies the AArch64 opcode generation logic.
