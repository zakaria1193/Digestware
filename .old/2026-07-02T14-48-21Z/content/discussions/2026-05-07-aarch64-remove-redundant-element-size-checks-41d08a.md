---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- redundant check
- code simplification
discussion_id: 9aef2ded-6d70-13d7-6977-201dab2cfa44@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 05/23] aarch64: Remove redundant element size checks'
headline: 'Aarch64: Remove redundant element size checks'
tldr: Simplifies `get_data_pattern` by removing redundant checks on qualifier element
  sizes, assuming prior equality checks suffice.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improved code readability and potentially minor performance improvement by removing
  redundant checks.
- Assumes that equality of qualifiers implies equality of element sizes.
exchanges: []
primer_expert: The patch simplifies `opcodes/aarch64-opc.c::get_data_pattern` by removing
  redundant size checks. Code like `(aarch64_get_qualifier_esize (qualifiers[0]) ==
  aarch64_get_qualifier_esize (qualifiers[1]))` is removed because the qualifiers
  themselves are already checked for equality.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch removes duplicate checks, cleaning up the code.'
series_id: 'binutils:aarch64: remove redundant element size checks'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9aef2ded-6d70-13d7-6977-201dab2cfa44@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes redundant checks for element size equality in the `get_data_pattern` function within `opcodes/aarch64-opc.c`. Because the code already checks that the qualifiers are equal, checking their element sizes is redundant.
