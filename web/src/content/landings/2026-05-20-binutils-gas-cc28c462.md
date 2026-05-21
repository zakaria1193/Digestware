---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- binutils
- gas
- assembler
- bugfix
- equates
commit_hash: cc28c46227cd483c22690ff7be003e48b5283573
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Assembler resolves equates safely in presence of symbol loops
tldr: The assembler now resolves equates safely in the presence of symbol loops by
  using `symbol_equated_to`.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR30308 by resolving equates safely in `tc-i386-intel.c`
  when symbol loops are present. It utilizes `symbol_equated_to` and copies value
  expressions before `i386_intel_simplify` is called. The `in_equate` parameter is
  removed as the fix is applied to all symbols, not just equates. Commit 22f8905d9f38
  reintroduced the issue.
primer_general: The GNU Assembler (GAS) translates assembly language source code into
  machine code.  Equates (using the `.equ` directive, or `=` in Intel syntax) define
  symbolic constants. A symbol loop occurs when a symbol's definition depends on itself,
  either directly or indirectly, leading to infinite recursion during resolution.
  This commit fixes an issue where the assembler would incorrectly resolve equates
  in the presence of such loops, leading to errors or unexpected behavior.
discussion_id_link: public_inbox:binutils#30308
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260520091929.C17D94BB58D1@sourceware.org
date: '2026-05-20'
is_stub: false
---

The assembler incorrectly handled equates in the presence of symbol loops due to premature modification of symbol values. This commit fixes the issue by using `symbol_equated_to` to resolve equates safely, copying value expressions before simplification. This change is applied to all symbols for increased safety.
