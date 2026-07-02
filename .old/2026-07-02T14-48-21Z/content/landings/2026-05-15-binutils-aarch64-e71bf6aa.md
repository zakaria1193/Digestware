---
project: binutils
subsystem: binutils/aarch64
patch_id: null
tags:
- aarch64
- assembler
- bugfix
commit_hash: e71bf6aa5a92ad40a4e0b2980f4c6e2955f86025
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: 'AArch64: Add an assert to inherent_reg_qualifier.'
tldr: The default case in `inherent_reg_qualifier` is unreachable, so replace it with
  an assert.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The AArch64 port's `inherent_reg_qualifier` in `gas/config/tc-aarch64.c`
  determines the operand qualifier for a register. The default case was expected to
  be unreachable. This change replaces the default return with `gas_assert (0)` to
  catch unexpected cases during development.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.
  For AArch64, GAS needs to determine the correct qualifiers for registers based on
  their usage. This commit adds a check to ensure that a specific code path, intended
  to be unreachable, remains so. If this code path is ever executed, the assembler
  will now halt with an assertion, signaling a bug.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260515140857.C4B7F40A1F86@sourceware.org
date: '2026-05-15'
is_stub: false
---

In the AArch64 assembler, the `inherent_reg_qualifier` function determines the operand qualifier associated with a given register. The default case in this function should be unreachable. This commit replaces the default case with an assert to catch unexpected behavior during development.
