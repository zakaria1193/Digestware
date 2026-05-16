---
project: binutils
subsystem: binutils/aarch64
patch_id: null
tags:
- aarch64
- opcode
- code cleanup
commit_hash: 789ff9d67d1b2077c838a56a67ff8cc15e23c9a2
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: 'AArch64: Remove redundant element size checks.'
tldr: Element size checks are now redundant after qualifier equality check, so remove
  them to simplify code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `get_data_pattern` function in `opcodes/aarch64-opc.c` had redundant
  checks on element sizes after checking for qualifier equality. This commit removes
  the redundant checks.
primer_general: When the binutils are handling AArch64 assembly instructions, they
  need to perform checks to ensure that the operands are valid and compatible. This
  commit simplifies these checks by removing redundant comparisons of element sizes,
  because these comparisons are already covered by other checks. This makes the code
  cleaner and potentially more efficient.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260515140832.4761B40A1F85@sourceware.org
date: '2026-05-15'
is_stub: false
---

This commit removes redundant element size checks in AArch64 opcode processing. Since the code already verifies that qualifiers are equal, comparing their element sizes is unnecessary and this commit simplifies the code by removing the redundant checks.
